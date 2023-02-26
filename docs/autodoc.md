# `autodoc-object` directive

The `autodoc-object` directive can be used to render the documentation for a single Python object.
It takes a single argument, the fully qualified name of the object that should be rendered.

Using the `:literal:` option, the pre-rendered content will be rendered as a literal block,
and the `:literal-lexer:` option can be used to specify the lexer to use for syntax highlighting.

The directive can contain content,
which is read as [TOML](https://toml.io) and will override any of the {ref}`global configuration <config:global>` options (without the `autodoc2_` prefix).

## Literal representation

For example:

````restructuredtext
.. autodoc2-object:: autodoc2.sphinx.docstring._example
    :literal:
    :literal-lexer: restructuredtext

    render_plugin = "rst"
    no_index = true
````

creates:

```{autodoc2-object} autodoc2.sphinx.docstring._example
:literal:
:literal-lexer: restructuredtext

render_plugin = "rst"
no_index = true
```

## Rendered representation

For example:

````restructuredtext
.. autodoc2-object:: autodoc2.sphinx.docstring._example

    render_plugin = "rst"
    no_index = true
````

creates:

```{autodoc2-object} autodoc2.sphinx.docstring._example
render_plugin = "myst"
no_index = true
```

## Rendered representation (signature only)

Or without annotations and docstring:

````restructuredtext
.. autodoc2-object:: autodoc2.sphinx.docstring._example

    render_plugin = "rst"
    no_index = true
    annotations = false
    docstrings = false
````

creates:

```{autodoc2-object} autodoc2.sphinx.docstring._example
render_plugin = "myst"
no_index = true
annotations = false
docstrings = false
```
