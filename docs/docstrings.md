# `autodoc2-docstring` directive

One of the key features of autodoc2 is the ability to identify object docstrings
and render them in the documentation, using a given parser.

The `autodoc2-docstring` directive is used to render a docstring.
It takes a single argument, the fully qualified name of the object whose docstring should be rendered.

Using the `:literal:` option, the docstring will be rendered as a literal block.

- the `:literal-linenos:` option can be used to enable line numbers for the literal block, based on the line number in the source document,
- the `:literal-lexer:` option can be used to specify the lexer to use for syntax highlighting.

````restructuredtext
.. autodoc2-docstring:: autodoc2.sphinx.docstring._example
    :literal:
    :literal-linenos:
    :literal-lexer: markdown
````

creates:

```{autodoc2-docstring} autodoc2.sphinx.docstring._example
:literal:
:literal-linenos:
:literal-lexer: markdown
```

Omitting the `:literal:` option will render the docstring as a nested syntax block.

- the `parser` option can be used to specify the parser to use for the docstring, such as `myst`, `rst` or a the fully qualified name of a custom parser class,
  If not specified the docstring will be rendered using the current parser.
- the `:allowtitles:` option can be used to allow the docstring to contain heading, and can be used if the `autodoc2-docstring` is at the top level of the document.

````restructuredtext
.. autodoc2-docstring:: autodoc2.sphinx.docstring._example
    :parser: myst
    :allowtitles:
````

creates:

```{autodoc2-docstring} autodoc2.sphinx.docstring._example
:parser: myst
:allowtitles:
```

## Specifying the parser for auto-generated documentation

When auto-documenting source code,
by default the docstring will be rendered using the current parser.

To list specific parsers for specific objects,
you can use the {confval}`autodoc2_docstring_parser_regexes` configuration option.

```python
autodoc2_docstring_parser_regexes = [
    (r"autodoc2\.sphinx\.docstring\._example", "myst"),
]
```

You can see this in action at {py:func}`autodoc2.sphinx.docstring._example`
