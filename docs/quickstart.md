# Quickstart

This section describes how to get started with `sphinx-autodoc2` 🎉

## Installation

Install from PyPI:

```{code-block} bash
pip install sphinx-autodoc2
```

## Sphinx Extension

Add `autodoc2` to the `extensions` list in your `conf.py` file and, as as a minimum, set the `autodoc2_packages` configuration option to the list of packages you want to document:

```python
extensions = [
    "autodoc2",
]
autodoc2_packages = [
    "../my_package",
]
```

This will generate documentation for the `my_package` package, and all of its sub-packages and modules, within the `apidocs` (or {confval}`autodoc2_output_dir`) directory,
which you can include in a `toctree` directive.

```restructuredtext
.. toctree::
   :maxdepth: 2

   apidocs/index
```

```{seealso}
{ref}`config:package` for more information on how to configure the packages to document.
```

## Command Line Tool

If installed with the `cli` extra, `sphinx-autodoc2` will install the `autodoc2` command line tool.

```{code-block} console
$ pip install sphinx-autodoc2[cli]
$ autodoc2 --help
```

## Documenting only the public API (*via* `__all__`)

By default, `sphinx-autodoc2` will document all objects within each package/module, and reference direct children of them.

If you want to document only the public API of your package, you can use the `__all__` variables to specify which objects to document.
For example:

```python
from .my_module import MyClass
__all__ = [
    "MyClass",
    "my_function",
]
def my_function(): ...
```

```{seealso}
The [Python import documentation](https://docs.python.org/3/reference/simple_stmts.html#import)
```

To enable this feature, set the {confval}`autodoc2_module_all_regexes` (or {confval}`autodoc2_packages[module_all_regexes]`) configuration option in your `conf.py`:

```python
autodoc2_module_all_regexes = [
    r"my_package\..*",
]
```

You can see an axample of this in the [Example documentation of the `aiida` package](aiida).

Note, when following `__all__` imports,
since the `:canonical:` option is added to each object,
[intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
will record both the canonical and non-canonical names of the object.
For example, if there is a package `my_package` with the following `__init__.py`:

```python
from .my_module import MyClass
__all__ = [
    "MyClass",
]
```

Then you will be able to reference `MyClass` in your documentation as either `my_package.MyClass` or `my_package.my_module.MyClass`.

## Using Markdown (MyST) docstrings

By default, `sphinx-autodoc2` will render the file of each module/package as `.rst`.
This means that the docstrings of each object within that module will also be interpreted as `.rst`.

If you want to use Markdown ([MyST](https://myst-parser.readthedocs.io)) docstrings, you can set the {confval}`autodoc2_render_plugin` configuration option in your `conf.py`:

```python
autodoc2_render_plugin = "myst"
```

This will now create all files with the ".md" extension, and thus the docstrings will be interpreted as Markdown.

To specify at a module level which docstrings to render as Markdown or RestructuredText, you can set the {confval}`autodoc2_render_plugin_regexes` configuration option in your `conf.py`:

```python
autodoc2_render_plugin_regexes = [
    (r"autodoc2\.db", "myst")
]
```

Which for example, created this page using Markdown docstrings: {py:mod}`autodoc2.db`

````{tip}
If you are looking to use Markdown docstrings,
with the default [sphinx-style](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists), for example:

```python
def my_function(a: str, b: int) -> bool:
    """This is my function.

    :param arg1: The first argument.
    :param arg2: The second argument.
    :return: The return value.
    """
```

Then you should enable the [MyST `fieldlist` extension](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#field-lists) in your `conf.py`:

```python
myst_enable_extensions = ["fieldlist"]
```

**Important**: There is a current "gotcha" in this extensions, as to how the alignment of multi-line values is handled:
The field body is aligned either by the start of the body on the first line or, if no body content is on the first line, by 2 spaces.

```markdown
:field1: This is the body of the field.
         It is aligned by the start of the body on the first line.
:field2: This is the body of the field.
  It is aligned by 2 spaces.
```

This is different to RsT, where the body is aligned by the start of the body on the first line.

I hope to fix this at some point.

````

## Global Configuration

This section describes the configuration options for `sphinx-autodoc2`, that you can set in the `conf.py` file.

```{autodoc2-config}
```

(config:package)=
## Package Configuration

In the `autodoc2_packages` configuration option, an item can be a string, or a dictionary such as:

```python
autodoc2_packages = [
    "../src/autodoc2",
    {
        "path": "../src/other/module",
        "module": "other.module",
    },
]
```

The following are keys allowed in the dictionary:

```{autodoc2-config-package}
```
