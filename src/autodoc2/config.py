"""The configuration for the extension."""

from __future__ import annotations

from copy import deepcopy
import dataclasses as dc
from importlib import import_module
import re
import typing as t

if t.TYPE_CHECKING:
    from autodoc2.render.base import RendererBase


class ValidationError(Exception):
    """An error validating a config value."""


CONFIG_PREFIX = "autodoc2_"


@dc.dataclass
class PackageConfig:
    """A package-level config item."""

    path: str = dc.field(
        metadata={
            "help": "The path to the package, "
            "relative to the source directory (POSIX format).",
            "sphinx_type": str,
        }
    )
    from_git_clone: tuple[str, str] | None = dc.field(
        default=None,
        metadata={
            "help": "Clone a git (url, branch/tag)/ "
            "If using this option the 'path' will be relative to root of the cloned repository.",
        },
    )
    module: str | None = dc.field(
        default=None,
        metadata={
            "help": "The module to use as the root of the package, "
            "otherwise the file/directory name is used."
        },
    )

    exclude_dirs: list[str] = dc.field(
        default_factory=lambda: ["__pycache__"],
        metadata={
            "help": "Directories to exclude from module analysis (matched by fnmatch).",
        },
    )

    exclude_files: list[str] = dc.field(
        default_factory=list,
        metadata={
            "help": "Files to exclude from module gathering (matched by fnmatch).",
        },
    )

    auto_mode: bool = dc.field(
        default=True,
        metadata={
            "help": "Whether to automatically generate documentation for the package.",
        },
    )

    def as_triple(self) -> t.Iterable[tuple[str, t.Any, dc.Field]]:  # type: ignore[type-arg]
        """Yield triples of (name, value, field)."""
        fields = {f.name: f for f in dc.fields(self.__class__)}
        for name, value in dc.asdict(self).items():
            yield name, value, fields[name]


def _coerce_packages(name: str, item: t.Any) -> list[PackageConfig]:
    """Coerce the packages config option to a set."""
    if not isinstance(item, (list, tuple)):
        raise ValidationError(f"{name} must be a list")
    if len(item) == 0:
        raise ValidationError(f"{name} must not be empty")
    # make sure we don't mutate the original (triggers sphinx total rebuild)
    new = [deepcopy(i) for i in item]
    for i, package in enumerate(new[:]):
        # TODO here we should use the PackageConfig to validate
        if isinstance(package, str):
            new[i] = package = {"path": package}
        if not isinstance(package, dict):
            raise ValidationError(f"{name}[{i}] must be a string or dict")
        if not isinstance(package["path"], str):
            raise ValidationError(f"{name}[{i}]['path'] must be a string")
        if package["path"].startswith("/"):
            raise ValidationError(f"{name}[{i}]['path'] must be relative")
        if "path" not in package:
            raise ValidationError(f"{name}[{i}] must have a 'path' key")
        if "from_git_clone" in package:
            if not isinstance(package["from_git_clone"], (tuple, list)):
                raise ValidationError(
                    f"{name}[{i}]['from_git_clone'] must be a tuple/list"
                )
            if len(package["from_git_clone"]) != 2:
                raise ValidationError(
                    f"{name}[{i}]['from_git_clone'] must be a tuple of length 2"
                )
            for idx in (0, 1):
                if not isinstance(package["from_git_clone"][idx], str):
                    raise ValidationError(
                        f"{name}[{i}]['from_git_clone'][{idx}] must be a string"
                    )
        if "module" in package and not isinstance(package["module"], str):
            raise ValidationError(f"{name}[{i}]['module'] must be a string")
        for key in ("exclude_files", "exclude_dirs"):
            if key in package and (
                not isinstance(package[key], list)
                or not all(isinstance(x, str) for x in package[key])
            ):
                raise ValidationError(f"{name}[{i}][{key!r}] must be a list of strings")
        if "autodoc" in package and not isinstance(package["autodoc"], bool):
            raise ValidationError(f"{name}[{i}]['autodoc'] must be a boolean")

    return [PackageConfig(**p) for p in new]


def _validate_replace_list(name: str, item: t.Any) -> list[tuple[str, str]]:
    """Validate that an item is a list of tuples."""
    if not isinstance(item, list) or not all(
        isinstance(x, (list, tuple)) and len(x) == 2 for x in item
    ):
        raise ValidationError(f"{name!r} must be a list of (string, string) tuples")
    return [(str(x[0]), str(x[1])) for x in item]


def _validate_hidden_objects(name: str, item: t.Any) -> set[str]:
    """Validate that the hidden objects config option is a set."""
    if not isinstance(item, (list, tuple, set)) or not all(
        isinstance(x, str) for x in item
    ):
        raise ValidationError(f"{name!r} must be a list of string")
    value = set(item)
    _valid = {"undoc", "dunder", "private", "inherited"}
    if not value.issubset(_valid):
        raise ValidationError(f"{name!r} must be a subset of {_valid}")
    return value


def _validate_regex_list(name: str, item: t.Any) -> list[t.Pattern[str]]:
    """Validate that an item is a list of regexes."""
    if not isinstance(item, list) or not all(isinstance(x, str) for x in item):
        raise ValidationError(f"{name!r} must be a list of string")
    compiled = []
    for i, regex in enumerate(set(item)):
        try:
            compiled.append(re.compile(regex))
        except re.error as exc:
            raise ValidationError(f"{name}[{i}] is not a valid regex: {exc}") from exc
    return compiled


def _validate_list_tuple_regex_str(
    name: str, item: t.Any
) -> list[tuple[t.Pattern[str], str]]:
    """Validate that an item is a list of (regex, str) tuples."""
    if not isinstance(item, list) or not all(
        isinstance(x, (list, tuple)) and len(x) == 2 for x in item
    ):
        raise ValidationError(f"{name!r} must be a list of (string, string) tuples")
    compiled = []
    for i, (regex, replacement) in enumerate(item):
        try:
            compiled.append((re.compile(regex), replacement))
        except re.error as exc:
            raise ValidationError(f"{name}[{i}] is not a valid regex: {exc}") from exc
    return compiled


def _load_renderer(name: str, item: t.Any) -> type[RendererBase]:
    """Load a renderer class."""
    from autodoc2.render.base import RendererBase

    if isinstance(item, type) and issubclass(item, RendererBase):
        return item
    if not isinstance(item, str):
        raise ValidationError(
            f"{name!r} must be a string or subclass of {RendererBase.__qualname__}"
        )
    if item in ("rst", "restructuredtext"):
        from autodoc2.render.rst_ import RstRenderer

        return RstRenderer
    if item in ("markdown", "md", "myst"):
        from autodoc2.render.myst_ import MystRenderer

        return MystRenderer
    try:
        module_path, klass_name = item.rsplit(".", 1)
        mod = import_module(module_path)
        kls = getattr(mod, klass_name)
    except ImportError as exc:
        raise ValidationError(f"{name!r} could not be loaded: {exc}") from exc

    if not isinstance(kls, type) or not issubclass(kls, RendererBase):
        raise ValidationError(
            f"{name!r} must load a subclass of {RendererBase.__qualname__}"
        )
    return kls


def _load_regex_renderers(
    name: str, item: t.Any
) -> list[tuple[t.Pattern[str], type[RendererBase]]]:
    """Load a list of (regex, renderer)."""
    if not isinstance(item, (list, tuple)):
        raise ValidationError(f"{name!r} must be a list or tuple")
    new: list[tuple[t.Pattern[str], type[RendererBase]]] = []
    for i, child in enumerate(item):
        if not (isinstance(child, (list, tuple)) and len(child) == 2):
            raise ValidationError(f"{name}[{i}] must be a list/tuple of length 2")
        try:
            pattern = re.compile(child[0])
        except re.error as exc:
            raise ValidationError(
                f"{name}[{i}][0] is not a valid regex: {exc}"
            ) from exc
        klass = _load_renderer(f"{name}[{i}][1]", child[1])
        new.append((pattern, klass))

    return new


@dc.dataclass
class Config:
    """The configuration for autoapi."""

    packages: list[PackageConfig] = dc.field(
        default_factory=list,
        metadata={
            "help": (
                "The packages to analyse. "
                "Each item can be a simple string, "
                "pointing to the package path, "
                "relative to the source directory (in POSIX format), "
                "or it can be a dictionary with more fine-grained control "
                "(see {ref}`config:package`))."
            ),
            "sphinx_type": list,
            "sphinx_validate": _coerce_packages,
            "doc_type": "list[str | dict]",
            "category": "required",
        },
    )

    output_dir: str = dc.field(
        default="apidocs",
        metadata={
            "help": (
                "The root output directory for the documentation, "
                "relative to the source directory (in POSIX format)."
            ),
            "sphinx_type": str,
            "category": "render",
        },
    )

    render_plugin: type[RendererBase] = dc.field(
        default_factory=(lambda: _load_renderer("render_plugin", "rst")),
        metadata={
            "help": (
                "The renderer to use for the documentation. "
                "This can be one of `rst` or `md`/`myst`, "
                "to use the built-in renderers, "
                "or a string pointing to a class that inherits from `RendererBase`, "
                "such as `mypackage.mymodule.MyRenderer`."
            ),
            "sphinx_type": str,
            "sphinx_default": "rst",
            "sphinx_validate": _load_renderer,
            "doc_type": "str",
            "category": "render",
        },
    )

    render_plugin_regexes: list[tuple[t.Pattern[str], type[RendererBase]]] = dc.field(
        default_factory=list,
        metadata={
            "help": "A list of (regex, renderer) to use for specific modules",
            "sphinx_type": list,
            "sphinx_validate": _load_regex_renderers,
            "doc_type": "list[tuple[str, str]]",
            "category": "render",
        },
    )

    module_all_regexes: list[t.Pattern[str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "Regexes which match fully qualified module names, "
            "to specify they should use the `__all__` when "
            "determining which children to document",
            "sphinx_type": list,
            "sphinx_validate": _validate_regex_list,
            "doc_type": "list[str]",
            "category": "render",
        },
    )

    skip_module_regexes: list[t.Pattern[str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "Regexes which match fully qualified module/package names, to skip them",
            "sphinx_type": list,
            "sphinx_validate": _validate_regex_list,
            "doc_type": "list[str]",
            "category": "render",
        },
    )

    hidden_objects: set[t.Literal["undoc", "dunder", "private", "inherited"]] = (
        dc.field(
            default_factory=lambda: {"inherited"},
            metadata={
                "help": (
                    "The default hidden items. "
                    "Can contain:\n"
                    "- `undoc`: undocumented objects\n"
                    "- `dunder`: double-underscore methods, e.g. `__str__`\n"
                    "- `private`: single-underscore methods, e.g. `_private`\n"
                    "- `inherited`: inherited class methods\n"
                ),
                "sphinx_type": list,
                "sphinx_validate": _validate_hidden_objects,
                "doc_type": 'list["undoc" | "dunder" | "private" | "inherited"]',
                "category": "render",
            },
        )
    )

    hidden_regexes: list[t.Pattern[str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "Regexes which match against fully qualified names, to mark them as hidden",
            "sphinx_type": list,
            "sphinx_validate": _validate_regex_list,
            "doc_type": "list[str]",
            "category": "render",
        },
    )

    no_index: bool = dc.field(
        default=False,
        metadata={
            "help": "Do not generate a cross-reference index.",
            "sphinx_type": bool,
            "category": "render",
        },
    )

    deprecated_module_regexes: list[t.Pattern[str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "Regexes which match against module names, to mark them as deprecated",
            "sphinx_type": list,
            "sphinx_validate": _validate_regex_list,
            "doc_type": "list[str]",
            "category": "render",
        },
    )

    module_summary: bool = dc.field(
        default=True,
        metadata={
            "help": "Whether to include a per-module summary.",
            "sphinx_type": bool,
            "category": "render",
        },
    )

    docstring_parser_regexes: list[tuple[t.Pattern[str], str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "Match fully qualified names against regexes to use a specific parser. "
            "The parser can be one of 'rst', 'myst', or the fully qualified name of a custom parser class. "
            "The first match is used. ",
            "sphinx_type": list,
            "sphinx_validate": _validate_list_tuple_regex_str,
            "doc_type": "list[tuple[str, str]]",
            "category": "render",
        },
    )

    class_docstring: t.Literal["merge", "both"] = dc.field(
        default="merge",
        metadata={
            "help": (
                "How to handle documenting of classes. "
                "If `merge`, the `__init__` docstring is appended to the class docstring "
                "and the `__init__` method is omitted."
                "If `both`, then the `__init__` method is included separately."
            ),
            "sphinx_type": str,
            "doc_type": '"merge" | "both"',
            "category": "render",
        },
    )

    class_inheritance: bool = dc.field(
        default=True,
        metadata={
            "help": "Whether to document class inheritance.",
            "sphinx_type": bool,
            "category": "render",
        },
    )

    annotations: bool = dc.field(
        default=True,
        metadata={
            "help": "Whether to include annotations.",
            "sphinx_type": bool,
            "category": "render",
        },
    )

    docstrings: t.Literal["all", "direct", "none"] = dc.field(
        default="direct",
        metadata={
            "help": "Which objects to include docstrings for. "
            "'direct' means only from objects that are not inherited.",
            "sphinx_type": str,
            "doc_type": '"all" | "direct"',
            "category": "render",
        },
    )

    sort_names: bool = dc.field(
        default=False,
        metadata={
            "help": "Whether to sort by name, when documenting, otherwise order by source",
            "sphinx_type": bool,
            "category": "render",
        },
    )

    replace_annotations: list[tuple[str, str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "List of (from, to) for annotation replacements",
            "sphinx_type": list,
            "sphinx_validate": _validate_replace_list,
            "category": "render",
        },
    )

    replace_bases: list[tuple[str, str]] = dc.field(
        default_factory=list,
        metadata={
            "help": "List of (from, to) for class base replacements",
            "sphinx_type": list,
            "sphinx_validate": _validate_replace_list,
            "category": "render",
        },
    )

    index_template: str | None = dc.field(
        default=(
            "API Reference\n"
            "=============\n"
            "\n"
            "This page contains auto-generated API reference documentation [#f1]_.\n"
            "\n"
            ".. toctree::\n"
            "   :titlesonly:\n"
            "{% for package in top_level %}\n"
            "   {{ package }}\n"
            "{%- endfor %}\n"
            "\n"
            ".. [#f1] Created with `sphinx-autodoc2 <https://github.com/chrisjsewell/sphinx-autodoc2>`_\n"
            "\n"
        ),
        metadata={
            "help": (
                "The Jinja template for the top-level {output_dir}/index.rst, "
                "or None if no index should be written. "
                "The template will be passed a ``top_level`` variable, "
                "which is a list of top-level package/module names."
            ),
            "sphinx_type": (str, type(None)),
            "category": "render",
        },
    )

    # TODO regexes
    # module_summary: bool | None = None
    # class_inheritance: bool | None = None
    # class_docstring: t.Literal["merge", "both"] | None = None
    # annotations: bool | None = None
    # sort_names: bool | None = None
    # docstrings

    def as_triple(self) -> t.Iterable[tuple[str, t.Any, dc.Field]]:  # type: ignore[type-arg]
        """Yield triples of (name, value, field)."""
        fields = {f.name: f for f in dc.fields(self.__class__)}
        for name, value in dc.asdict(self).items():
            yield name, value, fields[name]
