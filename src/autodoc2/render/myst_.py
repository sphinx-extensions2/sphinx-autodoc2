"""Renderer for MyST."""
from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase, format_args

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


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

    def generate_summary(self, items: list[ItemData]) -> t.Iterable[str]:
        """Generate a summary of the items."""
        for item in items:
            short_name = item["full_name"].split(".")[-1]
            summary = ""
            # get the first paragraph, allowing for the first line to be blank
            for i, line in enumerate(item["doc"].splitlines()):
                if i > 0 and not line.strip():
                    break
                summary += line.rstrip() + " "
            summary = summary.strip()
            # TODO get signature (for functions, etc), plus sphinx also runs rst.escape
            yield f"* - {{py:obj}}`{short_name} <{item['full_name']}>`"
            yield f"  - {summary}"

    @staticmethod
    def enclosing_backticks(text: str) -> str:
        """Ensure the enclosing backticks are more than any inner ones."""
        backticks = "```"
        while backticks in text:
            backticks += "`"
        return backticks

    def render_package(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a package."""
        if self.is_hidden(item):
            yield from ["---", "orphan: true", "---", ""]

        full_name = item["full_name"]

        yield f"# {{py:mod}}`{full_name}`"
        yield ""

        yield f"```{{py:module}} {full_name}"
        if self.is_module_deprecated(item):
            yield ":deprecated:"
        yield from ["```", ""]

        if item["doc"]:
            yield "## Description"
            yield ""
            for line in item["doc"].splitlines():
                if _MD_HEAD_RE.match(line):
                    # if its a heading, then we want to make sure it will be
                    # a sub heading of description
                    yield "##" + line
                else:
                    yield line
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
                    yield from [
                        f"### {heading}",
                        "",
                        "```{list-table}",
                        ":class: autosummary longtable",
                        ":align: left",
                        "",
                    ]
                    yield from self.generate_summary(visible_items)
                    yield "```"
                    yield ""

            yield from ["### API", ""]
            for name in visible_children:
                yield from self.render_item(name)

    def render_module(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a module."""
        yield from self.render_package(item)

    def render_function(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a function."""
        if self.is_hidden(item):
            return

        short_name = item["full_name"].split(".")[-1]
        show_annotations = self.show_annotations(item)
        sig = f"{short_name}({format_args(item['args'], show_annotations)})"
        if show_annotations and item.get("return_annotation"):
            sig += f" -> {item['return_annotation']}"

        backticks = self.enclosing_backticks(item["doc"] or "")

        yield f"{backticks}{{py:function}} {sig}"
        yield f":canonical: {item['full_name']}"
        # TODO overloads
        if "async" in item.get("properties", []):
            yield ":async:"
            # TODO it would also be good to highlight if singledispatch decorated,
            # or, more broadly speaking, decorated at all
        yield ""
        if item["doc"]:
            yield item["doc"]
            yield ""
        yield backticks
        yield ""

    def render_exception(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an exception."""
        yield from self.render_class(item)

    def render_class(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a class."""
        if self.is_hidden(item):
            return

        short_name = item["full_name"].split(".")[-1]
        constructor = self.get_item(f"{item['full_name']}.__init__")
        sig = short_name
        if constructor and "args" in constructor:
            sig += f"({format_args(constructor['args'], self.show_annotations(item), ignore_self='self')})"

        # note, here we can cannot yield by line,
        # because we need to look ahead to know the length of the backticks

        lines: list[str] = []

        lines += [
            f":canonical: {item['full_name']}",
            "",
        ]

        # TODO overloads

        if item.get("bases") and self.show_class_inheritance(item):
            lines += [
                "Bases: "
                + ", ".join(
                    [_reformat_cls_base_myst(b) for b in item.get("bases", [])]
                ),
                "",
            ]

        # TODO inheritance diagram

        if item["doc"]:
            lines += [item["doc"], ""]

        for child in self.get_children(
            item, {"class", "property", "attribute", "method"}
        ):
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
        if self.is_hidden(item):
            return

        backticks = self.enclosing_backticks(item["doc"] or "")

        short_name = item["full_name"].split(".")[-1]
        yield f"{backticks}{{py:property}} {short_name}"
        yield f":canonical: {item['full_name']}"
        for prop in ("abstractmethod", "classmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"
        if item.get("return_annotation"):
            yield f":type: {item['return_annotation']}"
        yield ""

        if item["doc"]:
            yield item["doc"]
            yield ""

        yield backticks
        yield ""

    def render_method(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a method."""
        if self.is_hidden(item):
            return

        short_name = item["full_name"].split(".")[-1]
        show_annotations = self.show_annotations(item)
        sig = f"{short_name}({format_args(item['args'], show_annotations, ignore_self='self')})"
        if show_annotations and item.get("return_annotation"):
            sig += f" -> {item['return_annotation']}"

        backticks = self.enclosing_backticks(item["doc"] or "")

        yield f"{backticks}{{py:method}} {sig}"
        yield f":canonical: {item['full_name']}"
        # TODO overloads
        # TODO collect final decorated in analysis
        for prop in ("abstractmethod", "async", "classmethod", "final", "staticmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"
        yield ""

        if item["doc"]:
            yield item["doc"]
            yield ""

        yield backticks
        yield ""

    def render_attribute(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an attribute."""
        yield from self.render_data(item)

    def render_data(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a data item."""
        if self.is_hidden(item):
            return

        backticks = self.enclosing_backticks(item["doc"] or "")
        short_name = item["full_name"].split(".")[-1]

        yield f"{backticks}{{py:{item['type']}}} {short_name}"
        yield f":canonical: {item['full_name']}"
        for prop in ("abstractmethod", "classmethod"):
            if prop in item.get("properties", []):
                yield f":{prop}:"
        if item.get("annotation"):
            yield f":type: {item['annotation']}"
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
        if item["doc"]:
            yield item["doc"]
            yield ""

        yield backticks
        yield ""


_MD_HEAD_RE = re.compile(r"^[#]+\s")
_RE_DELIMS = re.compile(r"(\s*[\[\]\(\),]\s*)")


def _reformat_cls_base_myst(value: str) -> str:
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
            result += f"{{py:obj}}`{sub_target}`\\"

    if result.endswith("\\"):
        result = result[:-1]

    return result
