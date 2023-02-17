# {py:mod}`package`

```{py:module} package
```

## Description

This is a test package.

## Subpackages

```{toctree}
:titlesonly:
:maxdepth: 3

package.a
```

## Package Contents

### Classes

```{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Class <package.Class>`
  - This is a class.
```

### Functions

```{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`func <package.func>`
  - This is a function.
```

### Data

```{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <package.__all__>`
  - 
* - {py:obj}`p <package.p>`
  - p can be documented here.
```

### API

```{py:data} __all__
:canonical: package.__all__
:value: >
   ['p', 'a1', 'alias']

```

```{py:data} p
:canonical: package.p
:value: >
   1

p can be documented here.

```

```{py:function} func(a: str, b: int) -> package.a.c.ac1
:canonical: package.func

This is a function.

```

````{py:class} Class
:canonical: package.Class

This is a class.

```{py:attribute} x
:canonical: package.Class.x
:type: int
:value: >
   1

x can be documented here.

```

```{py:method} method(a: str, b: int) -> ...
:canonical: package.Class.method

This is a method.

```

```{py:property} prop
:canonical: package.Class.prop
:type: package.a.c.ac1 | None

This is a property.

```

```{py:class} Nested
:canonical: package.Class.Nested

This is a nested class.

```

````
