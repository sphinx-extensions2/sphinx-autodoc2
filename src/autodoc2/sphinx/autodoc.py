"""autodoc directive for sphinx."""

from __future__ import annotations

from contextlib import contextmanager
import typing as t

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxDirective

from autodoc2.sphinx.utils import (
    get_all_analyser,
    get_database,
    load_config,
    nested_parse_generated,
    warn_sphinx,
)
from autodoc2.utils import ItemData, WarningSubtypes

try:
    import tomllib
except ImportError:
    # python < 3.11
    import tomli as tomllib  # type: ignore


class AutodocObject(SphinxDirective):
    """Directive to render a docstring of an object."""

    required_arguments = 1  # the full name
    final_argument_whitespace = False
    has_content = True

    # TODO autogenerate this from the config
    option_spec: t.ClassVar[dict[str, t.Any]] = {
        "literal": directives.flag,  # return the literal render string
        "literal-lexer": directives.unchanged,  # the lexer to use for literal
    }

    def run(self) -> list[nodes.Node]:
        source, line = self.get_source_info()
        # warnings take the docname and line number
        warning_loc = (self.env.docname, line)

        full_name = self.arguments[0]
        autodoc2_db = get_database(self.env)

        if full_name not in autodoc2_db:
            warn_sphinx(
                f"Could not find {full_name}",
                WarningSubtypes.NAME_NOT_FOUND,
                location=warning_loc,
            )
            return []

        # find the parent class/module
        mod_parent = None
        class_parent = None
        for ancestor in autodoc2_db.get_ancestors(full_name, include_self=True):
            if ancestor is None:
                break  # should never happen
            if class_parent is None and ancestor["type"] == "class":
                class_parent = ancestor
            if ancestor["type"] in ("module", "package"):
                mod_parent = ancestor
                break

        if mod_parent is None:
            warn_sphinx(
                f"Could not find parent module {full_name}",
                WarningSubtypes.NAME_NOT_FOUND,
                location=warning_loc,
            )
            return []

        # ensure rebuilds when the source file changes
        file_path = mod_parent.get("file_path")
        if file_path:
            self.env.note_dependency(file_path)

        # load the configuration with overrides
        overrides = {}
        try:
            overrides = tomllib.loads("\n".join(self.content)) if self.content else {}
        except Exception as err:
            warn_sphinx(
                f"Could not parse TOML config: {err}",
                WarningSubtypes.CONFIG_ERROR,
                location=warning_loc,
            )
        config = load_config(self.env.app, overrides=overrides, location=warning_loc)

        # setup warnings
        def _warn_render(msg: str, type_: WarningSubtypes) -> None:
            warn_sphinx(msg, type_, location=warning_loc)

        # create the content from the renderer
        content = list(
            config.render_plugin(
                autodoc2_db,
                config,
                all_resolver=get_all_analyser(self.env),
                warn=_warn_render,
                standalone=True,
            ).render_item(full_name)
        )

        if "literal" in self.options:
            literal = nodes.literal_block(text="\n".join(content))
            self.set_source_info(literal)
            if "literal-lexer" in self.options:
                literal["language"] = self.options["literal-lexer"]
            return [literal]

        with _set_parents(self.env, mod_parent, class_parent):
            base = nested_parse_generated(
                self.state,
                content,
                source,
                line,
                match_titles=True,  # TODO
            )

        return base.children or []


@contextmanager
def _set_parents(
    env: BuildEnvironment, mod: ItemData, klass: ItemData | None
) -> t.Generator[None, None, None]:
    """Ensure we setup the correct parent
    This allows sphinx to properly process the `py` directives.
    """
    current_module = env.ref_context.get("py:module")
    current_class = env.ref_context.get("py:class")
    env.ref_context["py:module"] = mod["full_name"]
    if klass:
        env.ref_context["py:class"] = klass["full_name"]
    try:
        yield
    finally:
        env.ref_context["py:module"] = current_module
        env.ref_context["py:class"] = current_class
