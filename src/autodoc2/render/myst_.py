"""Renderer for MyST."""

from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


_RE_DELIMS = re.compile(r"(\s*[\[\]\(\),]\s*)")


class MystRenderer(RendererBase):
    """Render the documentation as MyST."""

    EXTENSION = ".md"

    def render_item(self, full_name: str) -> t.Iterable[str]:
        item = self.get_item(full_name)
        if item is None:
            raise ValueError(f"Item {full_name} does not exist")
        type_ = item["type"]
        if type_ == "package":
            yield from self.render_package(item)
        elif type_ == "module":
            yield from self.render_module(item)
        elif type_ == "function":
            yield from self.render_function(item)
        elif type_ == "class":
            yield from self.render_class(item)
        elif type_ == "exception":
            yield from self.render_exception(item)
        elif type_ == "property":
            yield from self.render_property(item)
        elif type_ == "method":
            yield from self.render_method(item)
        elif type_ == "attribute":
            yield from self.render_attribute(item)
        elif type_ == "data":
            yield from self.render_data(item)
        else:
            self.warn(f"Unknown item type {type_!r} for {full_name!r}")

    def generate_summary(
        self, objects: list[ItemData], alias: dict[str, str] | None = None
    ) -> t.Iterable[str]:
        alias = alias or {}
        yield "````{list-table}"
        yield ":class: autosummary longtable"
        yield ":align: left"
        yield ""
        for item in objects:
            full_name = item["full_name"]
            # TODO get signature (for functions, etc), plus sphinx also runs rst.escape
            if full_name in alias:
                yield f"* - {{py:obj}}`{alias[full_name]} <{full_name}>`"
            else:
                yield f"* - {{py:obj}}`{full_name}`"
            if self.show_docstring(item):
                yield f"  - ```{{autodoc2-docstring}} {full_name}"
                if parser_name := self.get_doc_parser(full_name):
                    yield f"    :parser: {parser_name}"
                yield "    :summary:"
                yield "    ```"
            else:
                yield "  -"
        yield "````"

    @staticmethod
    def enclosing_backticks(text: str) -> str:
        """Ensure the enclosing backticks are more than any inner ones."""
        backticks = "```"
        while backticks in text:
            backticks += "`"
        return backticks

    def render_package(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a package."""
        if self.standalone and self.is_hidden(item):
            yield from ["---", "orphan: true", "---", ""]

        full_name = item["full_name"]

        yield f"# {{py:mod}}`{full_name}`"
        yield ""

        yield f"```{{py:module}} {full_name}"
        if self.no_index(item):
            yield ":noindex:"
        if self.is_module_deprecated(item):
            yield ":deprecated:"
        yield from ["```", ""]

        if self.show_docstring(item):
            yield f"```{{autodoc2-docstring}} {item['full_name']}"
            if parser_name := self.get_doc_parser(item["full_name"]):
                yield f":parser: {parser_name}"
            yield ":allowtitles:"
            yield "```"
            yield ""

        visible_subpackages = [
            i["full_name"] for i in self.get_children(item, {"package"})
        ]
        if visible_subpackages:
            yield from [
                "## Subpackages",
                "",
                "```{toctree}",
                ":titlesonly:",
                ":maxdepth: 3",
                "",
            ]
            for name in visible_subpackages:
                yield name
            yield "```"
            yield ""

        visible_submodules = [
            i["full_name"] for i in self.get_children(item, {"module"})
        ]
        if visible_submodules:
            yield from [
                "## Submodules",
                "",
                "```{toctree}",
                ":titlesonly:",
                ":maxdepth: 1",
                "",
            ]
            for name in visible_submodules:
                yield name
            yield "```"
            yield ""

        visible_children = [
            i["full_name"]
            for i in self.get_children(item)
            if i["type"] not in ("package", "module")
        ]
        if not visible_children:
            return

        yield f"## {item['type'].capitalize()} Contents"
        yield ""

        if self.show_module_summary(item):
            for heading, types in [
                ("Classes", {"class"}),
                ("Functions", {"function"}),
                ("Data", {"data"}),
                ("External", {"external"}),
            ]:
                visible_items = list(self.get_children(item, types))
                if visible_items:
                    yield from [f"### {heading}", ""]
                    yield from self.generate_summary(
                        visible_items,
                        alias={
                            i["full_name"]: i["full_name"].split(".")[-1]
                            for i in visible_items
                        },
                    )
                    yield ""

            yield from ["### API", ""]
            for name in visible_children:
                yield from self.render_item(name)

    def render_module(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a module."""
        yield from self.render_package(item)

    def render_function(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a function."""
        short_name = item["full_name"].split(".")[-1]
        show_annotations = self.show_annotations(item)
        sig = f"{short_name}({self.format_args(item['args'], show_annotations)})"
        if show_annotations and item.get("return_annotation"):
            sig += f" -> {self.format_annotation(item['return_annotation'])}"

        yield f"````{{py:function}} {sig}"
        yield f":canonical: {item['full_name']}"
        if self.no_index(item):
            yield ":noindex:"
        # TODO overloads
        if "async" in item.get("properties", []):
            yield ":async:"
            # TODO it would also be good to highlight if singledispatch decorated,
            # or, more broadly speaking, decorated at all
        yield ""
        if self.show_docstring(item):
            yield f"```{{autodoc2-docstring}} {item['full_name']}"
            if parser_name := self.get_doc_parser(item["full_name"]):
                yield f":parser: {parser_name}"
            yield "```"
        yield "````"
        yield ""

    def render_exception(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an exception."""
        yield from self.render_class(item)

    def render_class(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a class."""
        short_name = item["full_name"].split(".")[-1]
        constructor = self.get_item(f"{item['full_name']}.__init__")
        sig = short_name
        if constructor and "args" in constructor:
            args = self.format_args(
                constructor["args"], self.show_annotations(item), ignore_self="self"
            )
            sig += f"({args})"

        # note, here we can cannot yield by line,
        # because we need to look ahead to know the length of the backticks

        lines: list[str] = [f":canonical: {item['full_name']}"]
        if self.no_index(item):
            lines += [":noindex:"]
        lines += [""]

        # TODO overloads

        if item.get("bases") and self.show_class_inheritance(item):
            lines += [
                "Bases: "
                + ", ".join(
                    [self._reformat_cls_base_myst(b) for b in item.get("bases", [])]
                ),
                "",
            ]

        # TODO inheritance diagram

        if self.show_docstring(item):
            lines.append(f"```{{autodoc2-docstring}} {item['full_name']}")
            if parser_name := self.get_doc_parser(item["full_name"]):
                lines.append(f":parser: {parser_name}")
            lines.append("```")
            lines.append("")

            if self.config.class_docstring == "merge":
                init_item = self.get_item(f"{item['full_name']}.__init__")
                if init_item:
                    lines.extend(
                        [
                            "```{rubric} Initialization",
                            "```",
                            "",
                            f"```{{autodoc2-docstring}} {init_item['full_name']}",
                        ]
                    )
                    if parser_name := self.get_doc_parser(init_item["full_name"]):
                        lines.append(f":parser: {parser_name}")
                    lines.extend(["```", ""])

        for child in self.get_children(
            item, {"class", "property", "attribute", "method"}
        ):
            if (
                child["full_name"].endswith(".__init__")
                and self.config.class_docstring == "merge"
            ):
                continue
            for line in self.render_item(child["full_name"]):
                lines.append(line)

        backticks = self.enclosing_backticks("\n".join(lines))
        yield f"{backticks}{{py:{item['type']}}} {sig}"
        for line in lines:
            yield line
        yield backticks
        yield ""

    def render_property(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a property."""
        short_name = item["full_name"].split(".")[-1]
        yield f"````{{py:property}} {short_name}"
        yield f":canonical: {item['full_name']}"
        if self.no_index(item):
            yield ":noindex:"
        for prop in ("abstractmethod", "classmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"
        if item.get("return_annotation"):
            yield f":type: {self.format_annotation(item['return_annotation'])}"

        yield ""
        if self.show_docstring(item):
            yield f"```{{autodoc2-docstring}} {item['full_name']}"
            if parser_name := self.get_doc_parser(item["full_name"]):
                yield f":parser: {parser_name}"
            yield "```"
            yield ""
        yield "````"
        yield ""

    def render_method(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a method."""
        short_name = item["full_name"].split(".")[-1]
        show_annotations = self.show_annotations(item)
        sig = f"{short_name}({self.format_args(item['args'], show_annotations, ignore_self='self')})"
        if show_annotations and item.get("return_annotation"):
            sig += f" -> {self.format_annotation(item['return_annotation'])}"

        yield f"````{{py:method}} {sig}"
        yield f":canonical: {item['full_name']}"
        if self.no_index(item):
            yield ":noindex:"
        # TODO overloads
        # TODO collect final decorated in analysis
        for prop in ("abstractmethod", "async", "classmethod", "final", "staticmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"

        yield ""
        if self.show_docstring(item):
            yield f"```{{autodoc2-docstring}} {item['full_name']}"
            if parser_name := self.get_doc_parser(item["full_name"]):
                yield f":parser: {parser_name}"
            yield "```"
            yield ""
        yield "````"
        yield ""

    def render_attribute(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an attribute."""
        yield from self.render_data(item)

    def render_data(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a data item."""
        short_name = item["full_name"].split(".")[-1]

        yield f"````{{py:{item['type']}}} {short_name}"
        yield f":canonical: {item['full_name']}"
        if self.no_index(item):
            yield ":noindex:"
        for prop in ("abstractmethod", "classmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"
        if item.get("annotation"):
            yield f":type: {self.format_annotation(item['annotation'])}"
        value = item.get("value")
        if isinstance(value, str):
            if len(value.splitlines()) == 1:
                if len(value) > 100:
                    value = value[:100] + "..."
                yield ":value: >"  # use > to ensure its understood as a string
                yield f"   {value!r}"
            else:
                yield ":value: <Multiline-String>"
                # TODO in sphinx-autoapi, they made a code block inside a details/summary HTML
        else:
            value = str(value).replace("\n", " ")
            if len(value) > 100:
                value = value[:100] + "..."
            yield ":value: >"
            yield f"   {value}"

        yield ""
        if self.show_docstring(item):
            yield f"```{{autodoc2-docstring}} {item['full_name']}"
            if parser_name := self.get_doc_parser(item["full_name"]):
                yield f":parser: {parser_name}"
            yield "```"
            yield ""
        yield "````"
        yield ""

    def _reformat_cls_base_myst(self, value: str) -> str:
        """Reformat the base of a class for RST.

        Base annotations can come in the form::

            A[B, C, D]

        which we want to reformat as::

            {py:obj}`A`\\[{py:obj}`B`, {py:obj}`C`, {py:obj}`D`\\]

        """
        result = ""
        for sub_target in _RE_DELIMS.split(value.strip()):
            sub_target = sub_target.strip()
            if _RE_DELIMS.match(sub_target):
                result += f"{sub_target}"
                if sub_target.endswith(","):
                    result += " "
                else:
                    result += "\\"
            elif sub_target:
                if result.endswith("\\"):
                    result = result[:-1]
                result += f"{{py:obj}}`{self.format_base(sub_target)}`\\"

        if result.endswith("\\"):
            result = result[:-1]

        return result
