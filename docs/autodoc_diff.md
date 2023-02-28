(autodoc-differences)=
# Differences from `sphinx.ext.autodoc`

The the main differences between `sphinx-autodoc2` and [`sphinx.ext.autodoc`](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc):

1. `sphinx-autodoc2` analyses the source code using **static analysis**,
   rather than **dynamic introspection**.

   - This means that it can be used to document code that is not importable,
     or that is not installed in the same environment as the documentation.
   - The analysis can infer information not available at runtime,
     such as type strings of attributes and imports under `TYPE_CHECKING` block.
   - The analysis does not lead to any un-desirable side-effects,
     that could occur on importing the code.

2. `sphinx-autodoc2` integrates auto-documentation within the sphinx build process,
    rather than requiring the separate `sphinx-apidoc` CLI tool.
    - This allows it to optimise rebuilds, by only re-generating documentation for objects that have changed.

3. `sphinx-autodoc2` allows for docstrings not written in RestructuredText, principally [MyST](https://myst-parser.readthedocs.io).
    - `sphinx.ext.autodoc` assumes that your docstings are written in RestructuredText,
      and that you are using the directives in a RestructuredText document.
    - `sphinx-autodoc2` allows you to write your docstrings in either RestructuredText or MyST,
        and to use the directives in either RestructuredText or MyST documents.
