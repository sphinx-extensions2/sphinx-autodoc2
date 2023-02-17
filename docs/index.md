# sphinx-autodoc2

`sphinx-autodoc2` is a Sphinx extension that automatically generates API documentation for your Python packages.

Static analysis of Python code
: There is no need to install your package to generate the documentation, and `sphinx-autodoc2` will correctly handle `if TYPE_CHECKING` blocks and other typing only features.
: You can even document packages from outside the project (via `git clone`)!

Optimized for rebuilds
: Analysis of packages and file rendering are cached, so you can use `sphinx-autodoc2` in your development workflow.

Support for `__all__`
: `sphinx-autodoc2` can follow `__all__` variable, to only document the public API.

Support for both `rst` and `md` docstrings
: `sphinx-autodoc2` supports both `rst` and `md` ([MyST](https://myst-parser.readthedocs.io)) docstrings, which can be mixed within the same project.

Highly configurable
: `sphinx-autodoc2` is highly configurable, with many options to control the analysis and output of the documentation.

Decoupled analysis and rendering
: The analysis and rendering of the documentation are decoupled, and not dependent on Sphinx.
: This means that you can use `sphinx-autodoc2` to generate documentation outside of Sphinx (see the `autodoc2` command line tool).

Get started with the [Quickstart Guide](quickstart.md) ⏩

Or checkout the the [Example API Documentation](apidocs/index.rst) ✨

[![GitHub Repo stars](https://img.shields.io/github/stars/chrisjsewell/sphinx-autodoc2?label=Like%20and%20Share%21&style=social)](https://github.com/chrisjsewell/sphinx-autodoc2)
[![PyPI](https://img.shields.io/pypi/v/sphinx-autodoc2?label=PyPI&logo=pypi&style=social)](https://pypi.org/project/sphinx-autodoc2/)

```{toctree}
:maxdepth: 2

quickstart
apidocs/index
```
