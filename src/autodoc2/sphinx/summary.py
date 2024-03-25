"""Directive to generate a summary of listed objects."""

from __future__ import annotations

from typing import Any, ClassVar

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

from autodoc2.sphinx.utils import (
    get_all_analyser,
    get_database,
    load_config,
    nested_parse_generated,
    warn_sphinx,
)
from autodoc2.utils import ItemData, WarningSubtypes


class AutodocSummary(SphinxDirective):
    """Directive to generate a summary of listed objects."""

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: ClassVar[dict[str, Any]] = {
        "renderer": directives.unchanged_required,
    }

    def run(self) -> list[nodes.Node]:
        source, line = self.get_source_info()
        # warnings take the docname and line number
        warning_loc = (self.env.docname, line)

        all_resolver = get_all_analyser(self.env)

        # load the configuration
        overrides = {}
        if "renderer" in self.options:
            overrides = {"render_plugin": self.options["renderer"]}
        config = load_config(self.env.app, overrides=overrides, location=warning_loc)

        db = get_database(self.env)

        objects: list[ItemData] = []
        content_line: str
        aliases: dict[str, str] = {}
        for content_idx, content_line in enumerate(self.content):
            parts = content_line.strip().split(maxsplit=1)
            if len(parts) == 0:
                continue
            full_name = parts[0]
            alias: str | None = None
            if full_name.startswith("~"):
                full_name = full_name[1:]
                alias = full_name.split(".")[-1]
            if len(parts) > 1:
                alias = parts[1]
            if (item := db.get_item(full_name)) is None and (
                resolved_name := all_resolver.get_name(full_name)
            ):
                item = db.get_item(resolved_name)
            if item is not None:
                for ancestor in db.get_ancestors(full_name, include_self=True):
                    if ancestor and "file_path" in ancestor:
                        if file_path := ancestor["file_path"]:
                            self.env.note_dependency(file_path)
                        break
                if alias:
                    aliases[item["full_name"]] = alias
                elif full_name != item["full_name"]:
                    aliases[item["full_name"]] = full_name
                objects.append(item)
            else:
                warn_sphinx(
                    f"Could not find {full_name}",
                    WarningSubtypes.NAME_NOT_FOUND,
                    location=(
                        self.env.docname,
                        line + self.content_offset + 1 + content_idx,
                    ),
                )

        if not objects:
            return []

        # setup warnings
        def _warn_render(msg: str, type_: WarningSubtypes) -> None:
            warn_sphinx(msg, type_, location=warning_loc)

        # TODO it would be ideal to create this as nodes, rather than nested parsing,
        # but for now this is the simplest option
        content = list(
            config.render_plugin(
                db,
                config,
                all_resolver=all_resolver,
                warn=_warn_render,
                standalone=True,
            ).generate_summary(objects, alias=aliases)
        )
        base = nested_parse_generated(self.state, content, source, line)

        return base.children or []
