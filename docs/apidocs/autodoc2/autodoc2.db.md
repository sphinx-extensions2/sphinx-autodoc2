# {py:mod}`autodoc2.db`

```{py:module} autodoc2.db
```

```{autodoc2-docstring} autodoc2.db
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Database <autodoc2.db.Database>`
  - ```{autodoc2-docstring} autodoc2.db.Database
    :summary:
    ```
* - {py:obj}`InMemoryDb <autodoc2.db.InMemoryDb>`
  - ```{autodoc2-docstring} autodoc2.db.InMemoryDb
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_LIKE_REGEX <autodoc2.db._LIKE_REGEX>`
  - ```{autodoc2-docstring} autodoc2.db._LIKE_REGEX
    :summary:
    ```
````

### API

````{py:exception} UniqueError()
:canonical: autodoc2.db.UniqueError

Bases: {py:obj}`KeyError`

```{autodoc2-docstring} autodoc2.db.UniqueError
```

```{rubric} Initialization
```

```{autodoc2-docstring} autodoc2.db.UniqueError.__init__
```

````

`````{py:class} Database
:canonical: autodoc2.db.Database

Bases: {py:obj}`typing.Protocol`

```{autodoc2-docstring} autodoc2.db.Database
```

````{py:method} add(item: autodoc2.utils.ItemData) -> None
:canonical: autodoc2.db.Database.add

```{autodoc2-docstring} autodoc2.db.Database.add
```

````

````{py:method} remove(full_name: str, descendants: bool) -> None
:canonical: autodoc2.db.Database.remove

```{autodoc2-docstring} autodoc2.db.Database.remove
```

````

````{py:method} __contains__(full_name: str) -> bool
:canonical: autodoc2.db.Database.__contains__

```{autodoc2-docstring} autodoc2.db.Database.__contains__
```

````

````{py:method} get_item(full_name: str) -> autodoc2.utils.ItemData | None
:canonical: autodoc2.db.Database.get_item

```{autodoc2-docstring} autodoc2.db.Database.get_item
```

````

````{py:method} get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_items_like

```{autodoc2-docstring} autodoc2.db.Database.get_items_like
```

````

````{py:method} get_type(full_name: str) -> None | str
:canonical: autodoc2.db.Database.get_type

```{autodoc2-docstring} autodoc2.db.Database.get_type
```

````

````{py:method} get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_by_type

```{autodoc2-docstring} autodoc2.db.Database.get_by_type
```

````

````{py:method} get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_overloads

```{autodoc2-docstring} autodoc2.db.Database.get_overloads
```

````

````{py:method} get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.Database.get_children

```{autodoc2-docstring} autodoc2.db.Database.get_children
```

````

````{py:method} get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
:canonical: autodoc2.db.Database.get_children_names

```{autodoc2-docstring} autodoc2.db.Database.get_children_names
```

````

````{py:method} get_ancestors(full_name: str, include_self: bool) -> typing.Iterable[autodoc2.utils.ItemData | None]
:canonical: autodoc2.db.Database.get_ancestors

```{autodoc2-docstring} autodoc2.db.Database.get_ancestors
```

````

`````

````{py:data} _LIKE_REGEX
:canonical: autodoc2.db._LIKE_REGEX
:value: >
   None

```{autodoc2-docstring} autodoc2.db._LIKE_REGEX
```

````

`````{py:class} InMemoryDb()
:canonical: autodoc2.db.InMemoryDb

Bases: {py:obj}`autodoc2.db.Database`

```{autodoc2-docstring} autodoc2.db.InMemoryDb
```

```{rubric} Initialization
```

```{autodoc2-docstring} autodoc2.db.InMemoryDb.__init__
```

````{py:method} add(item: autodoc2.utils.ItemData) -> None
:canonical: autodoc2.db.InMemoryDb.add

````

````{py:method} remove(full_name: str, descendants: bool) -> None
:canonical: autodoc2.db.InMemoryDb.remove

````

````{py:method} __contains__(full_name: str) -> bool
:canonical: autodoc2.db.InMemoryDb.__contains__

````

````{py:method} get_item(full_name: str) -> autodoc2.utils.ItemData | None
:canonical: autodoc2.db.InMemoryDb.get_item

````

````{py:method} get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_items_like

````

````{py:method} get_type(full_name: str) -> None | str
:canonical: autodoc2.db.InMemoryDb.get_type

````

````{py:method} get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_by_type

````

````{py:method} get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_overloads

````

````{py:method} get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
:canonical: autodoc2.db.InMemoryDb.get_children

````

````{py:method} get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
:canonical: autodoc2.db.InMemoryDb.get_children_names

````

````{py:method} get_ancestors(full_name: str, include_self: bool) -> typing.Iterable[autodoc2.utils.ItemData | None]
:canonical: autodoc2.db.InMemoryDb.get_ancestors

````

````{py:method} write(stream: typing.TextIO) -> None
:canonical: autodoc2.db.InMemoryDb.write

```{autodoc2-docstring} autodoc2.db.InMemoryDb.write
```

````

````{py:method} read(stream: typing.TextIO) -> autodoc2.db.InMemoryDb
:canonical: autodoc2.db.InMemoryDb.read
:classmethod:

```{autodoc2-docstring} autodoc2.db.InMemoryDb.read
```

````

`````
