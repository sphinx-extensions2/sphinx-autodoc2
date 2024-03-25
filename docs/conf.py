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
    "announcement": "<em>Just released 🎉, feedback welcomed at "
    "<a href='https://github.com/chrisjsewell/sphinx-autodoc2/discussions'>sphinx-autodoc2</a></em>",
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
        "exclude_dirs": [
            "__pycache__",
            # "migrations",
        ],
    },
]
autodoc2_render_plugin_regexes = [(r"autodoc2\.db", "myst")]
autodoc2_replace_annotations = [
    ("re.Pattern", "typing.Pattern"),
]
autodoc2_docstring_parser_regexes = [
    (r"autodoc2\.sphinx\.docstring\._example", "myst"),
]
autodoc2_deprecated_module_regexes = [
    r"aiida\.parsers\.parser",
]
autodoc2_module_all_regexes = [r"aiida\.[^\.]+"]
autodoc2_skip_module_regexes = [
    r"aiida\.[^\.]+\..*",
    r"aiida\.(__main__|calculations|restapi|sphinxext|storage|workflows)",
]
# autodoc2_docstrings = "all"

nitpick_ignore_regex = [
    (r"py:.*", r"typing_extensions.*"),
    (r"py:.*", r"astroid.*"),
    (r"py:.*", r"docutils.*"),
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

import typing as t  # noqa: E402

from autodoc2.config import CONFIG_PREFIX, Config, PackageConfig  # noqa: E402
from docutils import nodes  # noqa: E402
from sphinx.application import Sphinx  # noqa: E402
from sphinx.util.docutils import SphinxDirective  # noqa: E402


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
            # if "category" in field.metadata:
            #     text.append(f"**category**: { field.metadata['category']}")
            #     text.append("")
            type_ = type_to_string(field.metadata.get("doc_type", field.type))
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
        for name, value, field in pkg_config.as_triple():
            text.append(f"``````{{confval}} {CONFIG_PREFIX}packages[{name}]")
            text.append(f'{field.metadata.get("help", "")}')
            text.append("")
            type_ = type_to_string(field.type)
            text.append(f"**type**: {type_}")
            text.append("")
            default_str = value if isinstance(value, str) else repr(value)
            if not default_str:
                pass
            elif len(default_str.splitlines()) < 2:
                text.append(f"**default**: ``{default_str}``")
            else:
                text.append("**default**:")
                text.append("")
                text.append("```")
                text.append(default_str)
                text.append("```")
            text.append("``````")
        self.state.nested_parse(text, self.content_offset, base_node)
        return base_node.children  # type: ignore


def type_to_string(type_: t.Any) -> str:
    """Convert a type to a string."""
    # TODO just keeping it simple for now but can we do this with astroid!?
    if isinstance(type_, tuple):
        return " or ".join(type_to_string(t) for t in type_)
    if type_ is type(None):
        return "``None``"
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
    if "RstRender" in type_string:
        return '``"rst"``'
    return type_string
