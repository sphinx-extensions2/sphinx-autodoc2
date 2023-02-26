# Quickstart

This section describes how to get started with `sphinx-autodoc2` 🎉

## Installation

Install from PyPI:

```{code-block} bash
pip install sphinx-autodoc2
```

## Enabling the extension

Add `autodoc2` to the `extensions` list in your `conf.py` file and, as as a minimum, set the {confval}`autodoc2_packages` configuration option to the list of packages you want to document:

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

```{tip}
If you don't want to include the `apidocs` directory in your repository,
you may want to add a `.gitignore` in the `apidocs` folder with `*` in it.
```

## Manually documenting select objects

`sphinx-autodoc2` can be used in one or both of two "modes":

1. **auto mode** (default) - Automatically generate files for all modules and packages specified by the {confval}`autodoc2_packages` configuration option.

2. **manual mode** - Use the [`autodoc2-object` directive](autodoc.md) to manually specify which objects to document.

To turn off auto mode, set the {confval}`autodoc2_packages[auto_mode]` configuration option to `False`:

```python
extensions = [
    "autodoc2",
]
autodoc2_packages = [
    {
        "path": "../my_package",
        "auto_mode": False,
    },
]
```

You can even render only the docstring of any object, see: [](docstrings.md).

## Ignoring autodoc2 warnings

When running `autodoc2` in Sphinx, you may see warnings such as:

```console
WARNING: autodoc2_packages must not be empty [autodoc2.config_error]
```

All warnings emitted by `sphinx-autodoc2` will have the `autodoc2` type and a related subtype, so you can ignore them by adding them to the
[Sphinx `suppress_warnings` configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-suppress_warnings)
in your `conf.py`:

```python
suppress_warnings = [
    "autodoc2.*",  # suppress all
    "autodoc2.config_error",  # suppress specific
]
```

## Dealing with `"reference target not found"` warnings

When running `autodoc2` in Sphinx (in nitpick mode), you may see warnings such as:

```console
path/to/module.rst:62: WARNING: py:class reference target not found: package.module.MyClass
```

These are potentially from type annotations,
for packages that you have not included in your
[intersphinx configuration](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html).

Alternatively, they may be from imports that are named differently in the external project's intersphinx inventory,
For example, if you import `MyClass` from `package`,
but the external project exposes it only as `package.module.MyClass`.
In this case, you can use the {confval}`autodoc2_replace_annotations` and {confval}`autodoc2_replace_bases` configuration options to replace the annotation/class base with the correct reference.

```python
autodoc2_replace_annotations = {
    "package.MyClass": "package.module.MyClass",
}
autodoc2_replace_bases = {
    "package.MyClass": "package.module.MyClass",
}
```

If you cannot, or do not, wish to fix them,
then you can suppress these warnings using the
[`nitpick_ignore` or `nitpick_ignore_regex`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpick_ignore) configurations.
In your `conf.py`:

```python
# ignore all warnings from this package
nitpick_ignore_regex = [
    ("py:.*", r"package\..*"),
]
# ignore a specific warning
nitpick_ignore = [
    ("py:class", "package.module.MyClass"),
]
```

```{tip}
To find out what references an external project exposes to intersphinx,
you can use the `myst-inv` command line tool.
See [MyST cross-project links](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#cross-project-inventory-links).
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

To enable this feature, set the {confval}`autodoc2_module_all_regexes` configuration option in your `conf.py`:

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

By default, `sphinx-autodoc2` will generate the file for each module/package as `.rst`,
and the docstrings of each object within that module will also be interpreted as `rst`.

If you want to use Markdown ([MyST](https://myst-parser.readthedocs.io)) docstrings,
you can set the {confval}`autodoc2_docstring_parser_regexes` for objects that use Markdown docstrings:

```python
autodoc2_docstring_parser_regexes = [
    # this will render all docstrings as Markdown
    (r".*", "myst"),
    # this will render select docstrings as Markdown
    (r"autodoc2\..*", "myst"),
]
```

Alternatively, you can set the {confval}`autodoc2_render_plugin` configuration option in your `conf.py`:

```python
autodoc2_render_plugin = "myst"
```

This will now create all files with the ".md" extension, and thus the docstrings will be interpreted as MyST by default.

To specify at a module level which files to render as Markdown or RestructuredText, you can set the {confval}`autodoc2_render_plugin_regexes` configuration option in your `conf.py`:

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

```{important}
It is advised that you ensure the `mdit-py-plugins`, which `myst-parser` depends on, is pinned to `>0.3.4`,
since this version introduces improvements to the `fieldlist` extension
(see [`executablebooks/mdit-py-plugins#65`](https://github.com/executablebooks/mdit-py-plugins/pull/65))
```

````

## Command Line Tool

If installed with the `cli` extra, `sphinx-autodoc2` will install the `autodoc2` command line tool.

```console
$ pip install sphinx-autodoc2[cli]
$ autodoc2 --help
```
