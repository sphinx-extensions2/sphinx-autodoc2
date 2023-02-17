"""The configuration for this packages documentation."""
from datetime import date

from autodoc2 import __version__

# -- Project information -----------------------------------------------------

project = "sphinx-autodoc2"
version = __version__
copyright = f"{date.today().year}, Chris Sewell"
author = "Chris Sewell"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "autodoc2",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",  # for aiida
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
myst_enable_extensions = ["fieldlist", "deflist"]

# -- HTML output -------------------------------------------------

html_theme = "furo"
html_title = "sphinx-autodoc2"
# html_logo = "logo.svg"
html_theme_options = {
    "top_of_page_button": "edit",
    "source_repository": "https://github.com/chrisjsewell/sphinx-autodoc2/",
    "source_branch": "main",
    "source_directory": "docs/",
}

# --- Autodoc configuration ------

autodoc2_packages = [
    "../src/autodoc2",
    {
        "path": "aiida",
        "from_git_clone": (
            "https://github.com/aiidateam/aiida-core.git",
            "v2.2.2",
        ),
        "skip_module_regexes": [
            r"aiida\.[^\.]+\..*",
            r"aiida\.(__main__|calculations|restapi|sphinxext|storage|workflows)",
        ],
        "module_all_regexes": [
            r"aiida\.[^\.]+",
        ],
        "deprecated_module_regexes": [
            r"aiida\.parsers\.parser",
        ],
        "exclude_dirs": [
            "__pycache__",
            # "migrations",
        ],
    },
]
autodoc2_render_plugin_regexes = [(r"autodoc2\.db", "myst")]
# autodoc2_sort_names = True

nitpick_ignore_regex = [
    ("py:class", r"re\.Pattern"),
    (r"py:.*", r"typing_extensions.*"),
    (r"py:.*", r"astroid.*"),
    # TODO for some reason in:
    # .. py:function:: format_args(args_info: autodoc2.utils.ARGS_TYPE ...
    # ARGS_TYPE is treated as a class rather than data
    ("py:class", r"autodoc2\.utils\..*_TYPE"),
    # from aiida
    (r"py:.*", r"types\.FunctionType"),
    (
        r"py:.*",
        r"(aiida|circus|click|disk_objectstore|importlib_metadata|kiwipy|plumpy|pgsu|requests).*",
    ),
    (r"py:.*", r"(DaemonException|Manager|PersistenceError)"),
    (r"py:.*", r"QueryBuilder\._get_ormclass"),
]

# --- Additional configuration ----

from dataclasses import fields  # noqa: E402
import typing as t  # noqa: E402

from docutils import nodes  # noqa: E402
from sphinx.application import Sphinx  # noqa: E402
from sphinx.util.docutils import SphinxDirective  # noqa: E402

from autodoc2.config import CONFIG_PREFIX, Config, PackageConfig  # noqa: E402


def setup(app: Sphinx) -> None:
    app.add_object_type(
        "confval",  # directivename
        "confval",  # rolename
        "pair: %s; configuration value",  # indextemplate
    )

    app.add_directive("autodoc2-config", CreateConfigDirective)
    app.add_directive("autodoc2-config-package", CreateConfigPkgDirective)


class CreateConfigDirective(SphinxDirective):
    """Document the configuration options."""

    def run(self) -> t.List[nodes.Node]:
        text = []

        config = Config()
        for name, value, field in config.as_triple():
            text.append(f"``````{{confval}} {CONFIG_PREFIX}{name}")
            text.append(f'{field.metadata.get("help", "")}')
            text.append("")
            if "category" in field.metadata:
                text.append(f"**category**: { field.metadata['category']}")
                text.append("")
            if "sphinx_type" in field.metadata:
                type_ = type_to_string(field.metadata["sphinx_type"])
                text.append(f"**type**: {type_}")
                text.append("")
            default_str = value if isinstance(value, str) else repr(value)
            if len(default_str.splitlines()) == 1:
                text.append(f"**default**: ``{default_str}``")
            else:
                text.append("**default**:")
                text.append("")
                text.append("```")
                text.append(default_str)
                text.append("```")
            text.append("")
            text.append("``````")

        base_node = nodes.Element()
        self.state.nested_parse(text, self.content_offset, base_node)
        return base_node.children  # type: ignore


class CreateConfigPkgDirective(SphinxDirective):
    """Document the package-level configuration options."""

    def run(self) -> t.List[nodes.Node]:
        base_node = nodes.Element()
        text = []
        pkg_config = PackageConfig("")
        config_fields = {f.name: f for f in fields(Config)}
        for name, _, field in pkg_config.as_triple():
            text.append(f"``````{{confval}} {CONFIG_PREFIX}packages[{name}]")
            if name in config_fields:
                text.append("*global override*")
                text.append("")
                text.append(f'{config_fields[name].metadata.get("help", "")}')
            else:
                text.append(f'{field.metadata.get("help", "")}')
            text.append("``````")
        self.state.nested_parse(text, self.content_offset, base_node)
        return base_node.children  # type: ignore


def type_to_string(type_: t.Type[t.Any]) -> str:
    """Convert a type to a string."""
    # TODO just keeping it simple for now but can we do this with astroid!?
    if type_ is str:
        return "``str``"
    if type_ is int:
        return "``int``"
    if type_ is bool:
        return "``bool``"
    if type_ is float:
        return "``float``"
    if type_ is list:
        return "``list``"
    type_string = str(type_)
    if type_string == "typing.Optional[str]":
        return "``str`` or ``None``"
    if "RstRender" in type_string:
        return '``"rst"``'
    return type_string
