"""A database interface for storing and querying the analysis items."""
from __future__ import annotations

import json
import re
import typing as t

if t.TYPE_CHECKING:
    from .utils import ItemData


class UniqueError(KeyError):
    """An error raised when a unique constraint is violated."""


class Database(t.Protocol):
    """A simple interface for storing and querying the analysis items, from a single package.

    This allows for potential extensibility in the future,
    e.g. using a persistent sqlite database.
    """

    def add(self, item: ItemData) -> None:
        """Add an item to the database."""

    def __contains__(self, full_name: str) -> bool:
        """Check if an item is in the database, by full_name."""

    def get_item(self, full_name: str) -> t.Optional[ItemData]:
        """Get an item from the database, by full_name."""

    def get_items_like(self, full_name: str) -> t.Iterable[ItemData]:
        """Get an item from the database, matching the wildcards `*` and `?`.

        `*` matches any number of characters, and `?` matches any single character.
        """

    def get_type(self, full_name: str) -> None | str:
        """Get the type of an item from the database, by full_name."""

    def get_by_type(self, type_: str) -> t.Iterable[ItemData]:
        """Get all items from the database, by type."""

    def get_overloads(self, full_name: str) -> t.Iterable[ItemData]:
        """Get all function overloads for this name."""

    def get_children(
        self, full_name: str, types: None | set[str] = None, *, sort_name: bool = False
    ) -> t.Iterable[ItemData]:
        """Get all items that are direct children of this name, i.e. `{full_name}.{name}`.

        :param full_name: The full name of the item.
        :param types: If given, only return items of these types.
        :param sort_name: If True, sort the names alphabetically.
        """

    def get_children_names(
        self, full_name: str, types: None | set[str] = None, *, sort_name: bool = False
    ) -> t.Iterable[str]:
        """Get all names of direct children of this name, i.e. `{full_name}.{name}`.

        :param full_name: The full name of the item.
        :param types: If given, only return items of these types.
        :param sort_name: If True, sort the names alphabetically.
        """


_LIKE_REGEX = re.compile(r"([\*\?])")


class InMemoryDb(Database):
    """A simple in-memory database for storing and querying the analysis items."""

    def __init__(self) -> None:
        """Create the database."""
        self._items: t.Dict[str, ItemData] = {}
        self._overloads: t.Dict[str, t.List[ItemData]] = {}

    def add(self, item: ItemData) -> None:
        if item["type"] == "overload":
            # note we do this here and not in the analyser,
            # because overloads come before the function they overload
            # and we don't want the analyzer to have to "look ahead"
            self._overloads.setdefault(item["full_name"], []).append(item)
            return
        if item["full_name"] in self._items:
            raise UniqueError(f"Item {item['full_name']} already exists")
        self._items[item["full_name"]] = item

    def __contains__(self, full_name: str) -> bool:
        return full_name in self._items

    def get_item(self, full_name: str) -> t.Optional[ItemData]:
        return self._items.get(full_name)

    def get_items_like(self, full_name: str) -> t.Iterable[ItemData]:
        parts = _LIKE_REGEX.split(full_name)
        pattern = re.compile(
            "".join(
                [
                    ".*" if part == "*" else ("." if part == "?" else re.escape(part))
                    for part in parts
                ]
            )
        )
        return (
            item
            for item in self._items.values()
            if pattern.fullmatch(item["full_name"])
        )

    def get_type(self, full_name: str) -> None | str:
        item = self._items.get(full_name)
        if item is None:
            return None
        return item["type"]

    def get_by_type(self, type_: str) -> t.Iterable[ItemData]:
        return (item for item in self._items.values() if item["type"] == type_)

    def get_overloads(self, full_name: str) -> t.Iterable[ItemData]:
        return self._overloads.get(full_name, [])

    def get_children(
        self, full_name: str, types: None | set[str] = None, *, sort_name: bool = False
    ) -> t.Iterable[ItemData]:
        generator = (
            item
            for item in self._items.values()
            if item["full_name"].startswith(full_name + ".")
            and "." not in item["full_name"][len(full_name) + 1 :]
            and ((types is None) or (item["type"] in types))
        )
        if sort_name:
            return sorted(generator, key=lambda item: item["full_name"])
        return generator

    def get_children_names(
        self, full_name: str, types: None | set[str] = None, *, sort_name: bool = False
    ) -> t.Iterable[str]:
        generator = (
            item["full_name"]
            for item in self._items.values()
            if item["full_name"].startswith(full_name + ".")
            and "." not in item["full_name"][len(full_name) + 1 :]
            and ((types is None) or (item["type"] in types))
        )
        if sort_name:
            return sorted(generator)
        return generator

    def write(self, stream: t.TextIO) -> None:
        """Write the database to a file."""
        json.dump({"items": self._items, "overloads": self._overloads}, stream)

    @classmethod
    def read(cls, stream: t.TextIO) -> InMemoryDb:
        """Read the database from a file."""
        items = json.load(stream)
        db = cls()
        db._items = items["items"]
        db._overloads = items["overloads"]
        return db
