# `autodoc2-summary` directive

The `autodoc2-summary` directive is used to render a summary of a list of objects.
This is useful for creating a table of contents for a module, or a list of objects in a package.

For example, the following:

````restructuredtext
.. autodoc2-summary::
    :renderer: myst

    aiida.orm.Node
    ~aiida.orm.Dict
    autodoc2.sphinx.docstring._example my example
````

creates:

```{autodoc2-summary}
:renderer: myst

aiida.orm.Node
~aiida.orm.Dict
autodoc2.sphinx.docstring._example my example
```

Note that fully qualified names can be used to refer to objects in other packages,
and they will also resolve against public API names, i.e. if the object is specified in an `__all__` variable.

Any text after the fully qualified name will be used as the title for the object,
or alternatively, if the name begins with `~` then the last component will be used as the title.

The `:renderer:` option can also be used to specify the renderer to use for the summary.

The summary renders the first block of text in the docstring of each object,
these renderings are governed by the {confval}`autodoc2_docstrings` and {confval}`autodoc2_docstring_parser_regexes` configuration option.
