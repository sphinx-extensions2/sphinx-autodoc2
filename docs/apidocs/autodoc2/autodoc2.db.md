# {py:mod}`autodoc2.db`

```{py:module} autodoc2.db
```

## Description

A database interface for storing and querying the analysis items.

## Module Contents

### Classes

```{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Database <autodoc2.db.Database>`
  - A simple interface for storing and querying the analysis items, from a single package.
* - {py:obj}`InMemoryDb <autodoc2.db.InMemoryDb>`
  - A simple in-memory database for storing and querying the analysis items.
```

### Data

```{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_LIKE_REGEX <autodoc2.db._LIKE_REGEX>`
  - 
```

### API

```{py:exception} UniqueError()
:canonical: autodoc2.db.UniqueError

Bases: {py:obj}`KeyError`

An error raised when a unique constraint is violated.

```

````{py:class} Database
:canonical: autodoc2.db.Database

Bases: {py:obj}`typing.Protocol`

A simple interface for storing and querying the analysis items, from a single package.

This allows for potential extensibility in the future,
e.g. using a persistent sqlite database.


```{py:method} add(item: autodoc2.utils.ItemData) -> None
:canonical: autodoc2.db.Database.add

Add an item to the database.

```

```{py:method} __contains__(full_name: str) -> bool
:canonical: autodoc2.db.Database.__contains__

Check if an item is in the database, by full_name.

```

```{py:method} get_item(full_name: str) -> typing.Optional[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_item

Get an item from the database, by full_name.

```

```{py:method} get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_items_like

Get an item from the database, matching the wildcards `*` and `?`.

`*` matches any number of characters, and `?` matches any single character.


```

```{py:method} get_type(full_name: str) -> None | str
:canonical: autodoc2.db.Database.get_type

Get the type of an item from the database, by full_name.

```

```{py:method} get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_by_type

Get all items from the database, by type.

```

```{py:method} get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_overloads

Get all function overloads for this name.

```

```{py:method} get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_children

Get all items that are direct children of this name, i.e. `{full_name}.{name}`.

:param full_name: The full name of the item.
:param types: If given, only return items of these types.
:param sort_name: If True, sort the names alphabetically.


```

```{py:method} get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
:canonical: autodoc2.db.Database.get_children_names

Get all names of direct children of this name, i.e. `{full_name}.{name}`.

:param full_name: The full name of the item.
:param types: If given, only return items of these types.
:param sort_name: If True, sort the names alphabetically.


```

````

```{py:data} _LIKE_REGEX
:canonical: autodoc2.db._LIKE_REGEX
:value: >
   None

```

````{py:class} InMemoryDb()
:canonical: autodoc2.db.InMemoryDb

Bases: {py:obj}`autodoc2.db.Database`

A simple in-memory database for storing and querying the analysis items.

```{py:method} __init__() -> None
:canonical: autodoc2.db.InMemoryDb.__init__

Create the database.

```

```{py:method} add(item: autodoc2.utils.ItemData) -> None
:canonical: autodoc2.db.InMemoryDb.add

Add an item to the database.

```

```{py:method} __contains__(full_name: str) -> bool
:canonical: autodoc2.db.InMemoryDb.__contains__

Check if an item is in the database, by full_name.

```

```{py:method} get_item(full_name: str) -> typing.Optional[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_item

Get an item from the database, by full_name.

```

```{py:method} get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_items_like

Get an item from the database, matching the wildcards `*` and `?`.

`*` matches any number of characters, and `?` matches any single character.


```

```{py:method} get_type(full_name: str) -> None | str
:canonical: autodoc2.db.InMemoryDb.get_type

Get the type of an item from the database, by full_name.

```

```{py:method} get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_by_type

Get all items from the database, by type.

```

```{py:method} get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_overloads

Get all function overloads for this name.

```

```{py:method} get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_children

Get all items that are direct children of this name, i.e. `{full_name}.{name}`.

:param full_name: The full name of the item.
:param types: If given, only return items of these types.
:param sort_name: If True, sort the names alphabetically.


```

```{py:method} get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
:canonical: autodoc2.db.InMemoryDb.get_children_names

Get all names of direct children of this name, i.e. `{full_name}.{name}`.

:param full_name: The full name of the item.
:param types: If given, only return items of these types.
:param sort_name: If True, sort the names alphabetically.


```

```{py:method} write(stream: typing.TextIO) -> None
:canonical: autodoc2.db.InMemoryDb.write

Write the database to a file.

```

```{py:method} read(stream: typing.TextIO) -> autodoc2.db.InMemoryDb
:canonical: autodoc2.db.InMemoryDb.read
:classmethod:

Read the database from a file.

```

````
