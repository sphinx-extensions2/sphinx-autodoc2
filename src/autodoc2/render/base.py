"""Convert the database items into documentation."""
# note, for the directives and options see:
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html
from __future__ import annotations

import abc
from collections import OrderedDict
import typing as t

from autodoc2.utils import WarningSubtypes

if t.TYPE_CHECKING:
    from autodoc2.config import RenderConfig
    from autodoc2.db import Database
    from autodoc2.utils import ARGS_TYPE, ItemData, ResolvedDict


class RendererBase(abc.ABC):
    """The base renderer."""

    EXTENSION: t.ClassVar[str] = ".txt"
    """The extension for the output files."""

    def __init__(
        self,
        db: Database,
        config: RenderConfig,
        warn: t.Callable[[str, WarningSubtypes], None] | None = None,
        resolved_all: dict[str, ResolvedDict] | None = None,
    ) -> None:
        """Initialise the renderer."""
        self._db = db
        self._config = config
        self._warn = warn or (lambda msg, type_: None)
        self._resolved_all = resolved_all
        self._resolve_all_warned: set[str] = set()
        """The full_names of modules that have already been warned about, regarding __all__ resolution"""
        self._is_hidden_cache: OrderedDict[str, bool] = OrderedDict()
        """Cache for the is_hidden function: full_name -> bool."""

    @property
    def config(self) -> RenderConfig:
        """The configuration."""
        return self._config

    def warn(
        self, msg: str, type_: WarningSubtypes = WarningSubtypes.RENDER_ERROR
    ) -> None:
        """Warn the user."""
        self._warn(msg, type_)

    def get_item(self, full_name: str) -> t.Optional[ItemData]:
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
            warn = item["full_name"] not in self._resolve_all_warned
            self._resolve_all_warned.add(item["full_name"])
            if item.get("all") is None and warn:
                self.warn(
                    f"__all__ missing or empty in {item['full_name']}",
                    WarningSubtypes.ALL_MISSING,
                )
            resolved_data = (
                self._resolved_all.get(item["full_name"])
                if self._resolved_all
                else None
            )
            if resolved_data is None:
                if warn:
                    self.warn(
                        f"Could not resolve {item['full_name']}.__all__",
                        WarningSubtypes.ALL_RESOLUTION,
                    )
                return
            if warn:
                for key, message in (
                    (
                        "unresolved",
                        "Could not resolve {names!r}, in {full_name}.__all__",
                    ),
                    (
                        "stars_unknown",
                        "* imports from unknown {names!r}, in {full_name}.__all__",
                    ),
                    (
                        "stars_no_all",
                        "* imports from modules with no __all__ {names!r}, in {full_name}.__all__",
                    ),
                    (
                        "stars_unresolved",
                        "* imports from modules with no resolved __all__ {names!r}, in {full_name}.__all__",
                    ),
                ):
                    names = resolved_data[key]  # type: ignore
                    if names:
                        self.warn(
                            message.format(names=names, full_name=item["full_name"]),
                            WarningSubtypes.ALL_RESOLUTION,
                        )
            for all_name in (
                sorted(item.get("all") or [])
                if self.config.sort_names
                else item.get("all") or []
            ):
                if all_name not in resolved_data["resolved"]:
                    continue
                resolved_names = resolved_data["resolved"][all_name]
                if len(resolved_names) > 1 and warn:
                    self.warn(
                        f"Found multiple items for {all_name!r} in "
                        f"{item['full_name']}.__all__: {resolved_names!r}",
                        WarningSubtypes.ALL_RESOLUTION,
                    )
                for resolved_name in resolved_names:
                    resolved_item: None | ItemData
                    if (
                        types == {"external"}
                        and resolved_name.split(".")[0]
                        != item["full_name"].split(".")[0]
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
        is_hidden = (
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
                and item.get("inherited", False)
            )
            or (
                "dunder" in self.config.hidden_objects
                and item["full_name"].startswith("__")
                and item["full_name"].endswith("__")
            )
            or (
                "private" in self.config.hidden_objects
                and item["full_name"].startswith("_")
                and not item["full_name"].endswith("__")
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

    # TODO allow for adding :noindex:

    def show_module_summary(self, item: ItemData) -> bool:
        """Whether to show a summary for this module/package."""
        return self.config.module_summary

    def show_class_inheritance(self, item: ItemData) -> bool:
        """Whether to show the inheritance for this class."""
        return self.config.class_inheritance

    def show_annotations(self, item: ItemData) -> bool:
        """Whether to show type annotations."""
        return self.config.annotations

    @abc.abstractmethod
    def render_item(self, full_name: str) -> t.Iterable[str]:
        """Yield the content for a single item."""


def format_args(
    args_info: ARGS_TYPE,
    include_annotations: bool = True,
    ignore_self: None | str = None,
) -> str:
    """Format the arguments of a function or method."""
    result = []

    for i, (prefix, name, annotation, default) in enumerate(args_info):
        if i == 0 and ignore_self is not None and name == ignore_self:
            continue
        formatted = (
            (prefix or "")
            + (name or "")
            + (f": {annotation}" if annotation and include_annotations else "")
            + ((" = {}" if annotation else "={}").format(default) if default else "")
        )
        result.append(formatted)

    return ", ".join(result)
