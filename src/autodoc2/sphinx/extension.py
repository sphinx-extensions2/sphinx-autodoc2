"""The sphinx extension for the package."""

from __future__ import annotations

from contextlib import suppress
import hashlib
from pathlib import Path, PurePosixPath
import shutil
import subprocess
from time import sleep
import typing as t

from sphinx.application import Sphinx

from autodoc2 import __version__
from autodoc2.analysis import analyse_module
from autodoc2.config import CONFIG_PREFIX, Config
from autodoc2.db import UniqueError
from autodoc2.sphinx.autodoc import AutodocObject
from autodoc2.sphinx.docstring import DocstringRenderer
from autodoc2.sphinx.summary import AutodocSummary
from autodoc2.sphinx.utils import (
    LOGGER,
    get_all_analyser,
    get_database,
    load_config,
    warn_sphinx,
)
from autodoc2.utils import WarningSubtypes, yield_modules

try:
    from sphinx.util.display import status_iterator
except ImportError:
    # sphinx <6 compatibility
    from sphinx.util import status_iterator  # type: ignore


def setup(app: Sphinx) -> dict[str, str | bool]:
    """Entry point for sphinx."""
    # create the configuration options
    for name, default, field in Config().as_triple():
        sphinx_type = t.Any
        if "sphinx_type" in field.metadata:
            sphinx_type = field.metadata["sphinx_type"]
            if sphinx_type in (str, int, float, bool, list):
                sphinx_type = (sphinx_type,)
        app.add_config_value(
            f"{CONFIG_PREFIX}{name}",
            field.metadata.get("sphinx_default", default),
            "env",
            types=sphinx_type,  # type: ignore[arg-type]
        )

    # create the main event
    app.connect("builder-inited", run_autodoc)
    app.add_directive("autodoc2-docstring", DocstringRenderer)
    app.add_directive("autodoc2-summary", AutodocSummary)
    app.add_directive("autodoc2-object", AutodocObject)

    # TODO support viewcode, when a package is not installed

    return {
        "version": __version__,
        # TODO allow for parallelization of some form
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def run_autodoc(app: Sphinx) -> None:
    """The primary sphinx call back event for sphinx."""

    config = load_config(app)

    top_level_modules = []
    for i, _ in enumerate(config.packages):
        mod_path = run_autodoc_package(app, config, i)
        if mod_path is not None:
            top_level_modules.append(mod_path)

    # create the index page
    if top_level_modules and config.index_template:
        import jinja2

        content_str = jinja2.Template(config.index_template).render(
            top_level=top_level_modules
        )
        index_path = Path(app.srcdir) / PurePosixPath(config.output_dir) / "index.rst"
        if not (index_path.exists() and index_path.read_text("utf8") == content_str):
            index_path.parent.mkdir(parents=True, exist_ok=True)
            index_path.write_text(content_str, "utf8")


def run_autodoc_package(app: Sphinx, config: Config, pkg_index: int) -> str | None:
    """Run autodoc for a single package.

    :return: The top level module name, relative to the api directory.
    """

    package = config.packages[pkg_index]

    # find all the modules to analyse
    root_path: None | Path = Path(app.srcdir)
    if package.from_git_clone is not None:
        url, ref = package.from_git_clone
        root_path = get_git_clone(app, url, ref, config)
    if root_path is None:
        return None

    path = root_path / PurePosixPath(package.path)
    modules: t.Iterable[tuple[Path, str]]
    if path.is_file():
        root_module = package.module or path.stem
        modules = [(path, root_module)]
    elif path.is_dir():
        root_module = package.module or path.name
        modules = list(
            yield_modules(
                path,
                root_module=root_module,
                exclude_dirs=package.exclude_dirs,
                exclude_files=package.exclude_files,
            )
        )
    else:
        warn_sphinx(f"Package {path} does not exist", WarningSubtypes.MISSING_MODULE)
        return None

    autodoc2_db = get_database(app.env)

    # store mapping of file paths to root modules and their hashes
    # this allows us to check if we need to re-analyse a module
    autodoc2_cache: dict[str, EnvCache]
    if not hasattr(app.env, "autodoc2_cache"):
        app.env.autodoc2_cache = autodoc2_cache = {}  # type: ignore
    else:
        autodoc2_cache = app.env.autodoc2_cache

    # compute the hash of the modules,
    # so we can check if we need to re-analyse them
    hasher = hashlib.sha256()
    for mod_path, _ in sorted(modules):
        hasher.update(mod_path.read_bytes())
    hash_str = hasher.hexdigest()

    if (
        path.as_posix() in autodoc2_cache
        and autodoc2_cache[path.as_posix()]["hash"] == hash_str
        and autodoc2_cache[path.as_posix()]["root_module"] == root_module
    ):
        LOGGER.info(f"[Autodoc2] Using cached analysis {root_module!r}")
        # TODO perhaps to keep the database upd-to-date we also need to detect
        # if something has been removed
    else:
        # clear the current module from the database
        autodoc2_db.remove(root_module, descendants=True)
        get_all_analyser(app.env).clear_cache()
        # analyse the modules and write to the database
        for mod_path, mod_name in status_iterator(
            modules,
            "[Autodoc2] Analysing package...",
            length=len(modules),
            stringify_func=(lambda x: str(x[1])),
        ):
            for data in analyse_module(mod_path, mod_name):
                try:
                    autodoc2_db.add(data)
                except UniqueError:
                    warn_sphinx(
                        f"Duplicate item {data['full_name']} ({data['type']})",
                        WarningSubtypes.DUPLICATE_ITEM,
                    )
        autodoc2_cache[path.as_posix()] = {"hash": hash_str, "root_module": root_module}

    output = Path(app.srcdir) / PurePosixPath(config.output_dir) / root_module

    if not package.auto_mode:
        if output.exists() and output.is_dir():
            shutil.rmtree(output)
        return None

    # find all the package/module, so we know what files to write
    LOGGER.info("[Autodoc2] Determining files to write ...")
    to_write: list[str] = []
    stack = [root_module]
    while stack:
        item = stack.pop()
        to_write.append(item)
        stack.extend(
            [
                mod
                for mod in autodoc2_db.get_children_names(item, {"package", "module"})
                if not any(pat.fullmatch(mod) for pat in config.skip_module_regexes)
            ]
        )

    def _warn_render(msg: str, type_: WarningSubtypes) -> None:
        warn_sphinx(msg, type_)

    # write the files
    output.mkdir(parents=True, exist_ok=True)
    paths = []
    for mod_name in status_iterator(
        to_write,
        "[Autodoc2] Writing modules...",
        length=len(to_write),
        stringify_func=(lambda x: str(x)),
    ):
        render_cls = config.render_plugin
        for pat, cls in config.render_plugin_regexes:
            if pat.fullmatch(mod_name):
                render_cls = cls
                break
        content = "\n".join(
            render_cls(
                autodoc2_db,
                config,
                all_resolver=get_all_analyser(app.env),
                warn=_warn_render,
            ).render_item(mod_name)
        )
        out_path = output / (mod_name + render_cls.EXTENSION)
        paths.append(out_path)
        if not (out_path.exists() and out_path.read_text("utf8") == content):
            # Don't write the file if it hasn't changed
            # this means that sphinx doesn't mark it for rebuild (mtime based)
            out_path.write_text(content, "utf8")

    # clean old files
    for path in output.iterdir():
        if path.is_dir():
            continue
        if path not in paths:
            path.unlink()

    return f"{root_module}/{root_module}"


def get_git_clone(
    app: Sphinx, url: str, branch_tag: str, config: Config
) -> None | Path:
    """Download a git repository to the given folder."""
    # create a sha of the url and branch
    folder = hashlib.sha256(url.encode("utf8") + branch_tag.encode("utf8")).hexdigest()
    path = Path(app.outdir) / "_autodoc2_git_clones" / folder
    if path.exists():
        return path
    LOGGER.info(f"[Autodoc2] Cloning {url}@{branch_tag}")
    path.parent.mkdir(parents=True, exist_ok=True)
    retries = 3
    while retries:
        try:
            subprocess.check_call(
                [
                    "git",
                    "clone",
                    "--single-branch",
                    "--branch",
                    branch_tag,
                    url,
                    str(path),
                ],
                env={"GIT_TERMINAL_PROMPT": "0"},
                stdout=subprocess.DEVNULL,
            )
            break
        except subprocess.CalledProcessError as err:
            LOGGER.info(f"[Autodoc2] retrying clone {url}@{branch_tag} after: {err}")
            if path.exists():
                # remove any partial clone
                with suppress(Exception):
                    shutil.rmtree(path)
            sleep(2)
            retries -= 1
    else:
        warn_sphinx(
            f"Failed to clone {url}@{branch_tag}", WarningSubtypes.GIT_CLONE_FAILED
        )
        return None
    return path


class EnvCache(t.TypedDict):
    """Cache for the environment."""

    hash: str  # the hash of the package files
    root_module: str  # the fully qualified root module name
