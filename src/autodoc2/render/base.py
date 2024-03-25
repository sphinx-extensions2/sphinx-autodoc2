"""Convert the database items into documentation."""

# note, for the directives and options see:
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html
from __future__ import annotations

import abc
from collections import OrderedDict
import typing as t

from autodoc2.resolve_all import AllResolver
from autodoc2.utils import WarningSubtypes

if t.TYPE_CHECKING:
    from autodoc2.config import Config
    from autodoc2.db import Database
    from autodoc2.utils import ARGS_TYPE, ItemData


class RendererBase(abc.ABC):
    """The base renderer."""

    EXTENSION: t.ClassVar[str] = ".txt"
    """The extension for the output files."""

    def __init__(
        self,
        db: Database,
        config: Config,
        *,
        warn: t.Callable[[str, WarningSubtypes], None] | None = None,
        all_resolver: AllResolver | None = None,
        standalone: bool = True,
    ) -> None:
        """Initialise the renderer.

        :param db: The database to obtain objects from.
        :param config: The configuration.
        :param warn: The function to use to log warnings.
        :param all_resolver: The resolver to use, for following __all__ children.
        :param standalone: If True, this renderer is being used to create a standalone document
        """
        self._db = db
        self._config = config
        self._standalone = standalone
        self._warn = warn or (lambda msg, type_: None)
        self._all_resolver = (
            AllResolver(
                self._db, lambda x: self._warn(x, WarningSubtypes.ALL_RESOLUTION)
            )
            if all_resolver is None
            else all_resolver
        )
        self._is_hidden_cache: OrderedDict[str, bool] = OrderedDict()
        """Cache for the is_hidden function: full_name -> bool."""

    @property
    def config(self) -> Config:
        """The configuration."""
        return self._config

    @property
    def standalone(self) -> bool:
        """If True, this renderer is being used to create a standalone document."""
        return self._standalone

    def warn(
        self, msg: str, type_: WarningSubtypes = WarningSubtypes.RENDER_ERROR
    ) -> None:
        """Warn the user."""
        self._warn(msg, type_)

    def get_item(self, full_name: str) -> ItemData | None:
        """Get an item from the database, by full_name."""
        return self._db.get_item(full_name)

    def get_children(
        self,
        item: ItemData,
        types: None | set[str] = None,
        *,
        omit_hidden: bool = True,
    ) -> t.Iterable[ItemData]:
        """Get the children of this item, sorted according to the config.

        If module and full_name in module_all_regexes,
        it will use the __all__ list instead of the children.

        :param item: The item to get the children of.
        :param types: If given, only return items of these types.
        :param omit_hidden: If True, omit hidden items.
        """
        if item["type"] in {"module", "package"} and any(
            pat.fullmatch(item["full_name"]) for pat in self.config.module_all_regexes
        ):
            resolved = self._all_resolver.get_resolved_all(item["full_name"])[
                "resolved"
            ]

            for all_name in (
                sorted(item.get("all") or [])
                if self.config.sort_names
                else item.get("all") or []
            ):
                if all_name not in resolved:
                    continue
                resolved_name = resolved[all_name]

                resolved_item: None | ItemData
                if (
                    types == {"external"}
                    and resolved_name.split(".")[0] != item["full_name"].split(".")[0]
                ):
                    # special case, for use only in the summary table
                    # These are items that are not in the same module as the parent,
                    # that were exposed via __all__.
                    resolved_item = {
                        "full_name": resolved_name,
                        "type": "external",
                        "doc": "",
                    }
                else:
                    resolved_item = self._db.get_item(resolved_name)
                if not (
                    resolved_item is None
                    or (types is not None and resolved_item["type"] not in types)
                    or (omit_hidden and self.is_hidden(resolved_item))
                ):
                    yield resolved_item
        else:
            for child in self._db.get_children(
                item["full_name"], types=types, sort_name=self.config.sort_names
            ):
                if omit_hidden and self.is_hidden(child):
                    continue
                yield child

    def is_hidden(self, item: ItemData) -> bool:
        """Whether this object should be displayed in documentation.

        Based on configuration regarding:

        - does i match a hidden regex pattern
        - does it have documentation
        - is it a dunder, i.e. __name__
        - is it a private member, i.e. starts with _, but not a dunder
        - is it an inherited member of a class
        """
        if item["full_name"] in self._is_hidden_cache:
            return self._is_hidden_cache[item["full_name"]]
        # TODO also whether it is imported, but this is only when following __all__
        short_name = item["full_name"].split(".")[-1]
        is_hidden: bool = (
            any(p.fullmatch(item["full_name"]) for p in self.config.hidden_regexes)
            or (
                item["type"] in ("module", "package")
                and any(
                    p.fullmatch(item["full_name"])
                    for p in self.config.skip_module_regexes
                )
            )
            or ("undoc" in self.config.hidden_objects and not item.get("doc", ""))
            or (
                "inherited" in self.config.hidden_objects
                and bool(item.get("inherited", False))
            )
            or (
                "dunder" in self.config.hidden_objects
                and short_name.startswith("__")
                and short_name.endswith("__")
            )
            or (
                "private" in self.config.hidden_objects
                and short_name.startswith("_")
                and not short_name.endswith("__")
            )
        )
        self._is_hidden_cache[item["full_name"]] = is_hidden
        if len(self._is_hidden_cache) > 1000:
            self._is_hidden_cache.popitem(last=False)
        return is_hidden

    def is_module_deprecated(self, item: ItemData) -> bool:
        """Whether this module is deprecated."""
        return any(
            p.fullmatch(item["full_name"])
            for p in self.config.deprecated_module_regexes
        )

    def no_index(self, item: ItemData) -> bool:
        """Whether this item should be excluded from search engines."""
        return self.config.no_index

    def show_module_summary(self, item: ItemData) -> bool:
        """Whether to show a summary for this module/package."""
        return self.config.module_summary

    def show_class_inheritance(self, item: ItemData) -> bool:
        """Whether to show the inheritance for this class."""
        return self.config.class_inheritance

    def show_annotations(self, item: ItemData) -> bool:
        """Whether to show type annotations."""
        return self.config.annotations

    def show_docstring(self, item: ItemData) -> bool:
        """Whether to show the docstring."""
        if self.config.docstrings == "all":
            return True
        if self.config.docstrings == "direct" and not (
            (item.get("inherited")) or (item.get("doc_inherited"))
        ):
            return True
        return False

    @abc.abstractmethod
    def render_item(self, full_name: str) -> t.Iterable[str]:
        """Yield the content for a single item."""

    def format_args(
        self,
        args_info: ARGS_TYPE,
        include_annotations: bool = True,
        ignore_self: None | str = None,
    ) -> str:
        """Format the arguments of a function or method."""
        result = []

        for i, (prefix, name, annotation, default) in enumerate(args_info):
            if i == 0 and ignore_self is not None and name == ignore_self:
                continue
            annotation = self.format_annotation(annotation)
            formatted = (
                (prefix or "")
                + (name or "")
                + (f": {annotation}" if annotation and include_annotations else "")
                + (
                    (" = {}" if annotation else "={}").format(default)
                    if default
                    else ""
                )
            )
            result.append(formatted)

        return ", ".join(result)

    def format_annotation(self, annotation: None | str) -> str:
        """Format a single type annotation."""
        if annotation:
            # TODO can this be optimised?
            # could do something like in init:
            # rgx = re.compile("(" + "|".join(re.escape(i) for i in r) + ")")
            # then here: rgx.sub(lambda x: r[x.group(1)], annotation)
            for in_, out_ in self.config.replace_annotations:
                annotation = annotation.replace(in_, out_)
        return annotation or ""

    def format_base(self, base: None | str) -> str:
        """Format a single class base type."""
        if base:
            for in_, out_ in self.config.replace_bases:
                base = base.replace(in_, out_)
        return base or ""

    def get_doc_parser(self, full_name: str) -> str:
        """Get the parser for the docstring of this item.

        Returns `""` if it should be parsed using the current parser.
        """
        for pattern, parser in self.config.docstring_parser_regexes:
            if pattern.fullmatch(full_name):
                return parser
        return ""

    @abc.abstractmethod
    def generate_summary(
        self, objects: list[ItemData], alias: dict[str, str] | None = None
    ) -> t.Iterable[str]:
        """Generate a summary of the objects.

        :param objects: A list of fully qualified names.
        :param alias: A mapping of fully qualified names to a display alias.
        """
