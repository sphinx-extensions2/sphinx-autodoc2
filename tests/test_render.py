"""Tests for the rendering."""
import io
from pathlib import Path
from textwrap import dedent

import pytest
from sphinx.testing.util import SphinxTestApp
from sphinx.testing.util import path as sphinx_path

from autodoc2.analysis import analyse_module
from autodoc2.config import Config
from autodoc2.db import InMemoryDb
from autodoc2.render.base import RendererBase
from autodoc2.render.myst_ import MystRenderer
from autodoc2.render.rst_ import RstRenderer
from autodoc2.utils import yield_modules


@pytest.mark.parametrize(
    "renderer,extension",
    [
        (RstRenderer, ".rst"),
        (MystRenderer, ".md"),
    ],
    ids=["rst", "myst"],
)
def test_basic(renderer: RendererBase, extension: str, tmp_path: Path, file_regression):
    """Test basic rendering."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)
    content = "\n".join(renderer(db, Config()).render_item(package.name))
    file_regression.check(content, extension=extension)


@pytest.mark.parametrize(
    "with_rebuild",
    [True, False],
    ids=["with_rebuild", "without_rebuild"],
)
def test_sphinx_build(tmp_path: Path, with_rebuild: bool):
    """Test building the Sphinx docs."""
    build_package(tmp_path)
    source = tmp_path / "source"
    source.mkdir()
    source.joinpath("index.rst").write_text(
        dedent(
            """\
        Test
        ====

        .. toctree::

            apidocs/index
        """
        ),
        "utf-8",
    )
    source.joinpath("conf.py").write_text(
        dedent(
            """\
        project = "tester"
        extensions = ["autodoc2"]
        autodoc2_packages = ["../package"]
        """
        ),
        "utf-8",
    )
    warnings = io.StringIO()
    build = tmp_path / "build"
    app = SphinxTestApp(
        buildername="html",
        srcdir=sphinx_path(source),
        builddir=sphinx_path(build),
        warning=warnings,
    )
    try:
        app.build()
    finally:
        app.cleanup()

    assertions = {}  # catch all the assertion failures, before failing the test
    if warnings.getvalue():
        assertions["warnings"] = warnings.getvalue()
    # print([p.relative_to(tmp_path).as_posix() for p in tmp_path.glob("**/*")])
    package_source = source / "apidocs" / "package" / "package.rst"
    if not (source / "apidocs" / "package" / "package.rst").exists():
        assertions["source/apidocs/package/package.rst"] = "not found"
    else:
        package_source_mtime = package_source.stat().st_mtime
    if not (build / "html" / "index.html").exists():
        assertions["build/index.html"] = "not found"
    if not (build / "html" / "apidocs" / "index.html").exists():
        assertions["build/apidocs/index.html"] = "not found"
    package_html = build / "html" / "apidocs" / "package" / "package.html"
    if not package_html.exists():
        assertions["build/apidocs/package/package.html"] = "not found"
    else:
        package_html_mtime = package_html.stat().st_mtime

    if not hasattr(app.env, "autodoc2_cache"):
        assertions["autodoc2_cache"] = "not found"
    if not getattr(app.env, "autodoc2_cache"):  # noqa: B009
        assertions["autodoc2_cache"] = "empty"

    if assertions:
        pytest.fail(f"Failed assertions {assertions}")

    if not with_rebuild:
        return

    # test rebuild
    rebuild_warnings = io.StringIO()
    rebuild_app = SphinxTestApp(
        buildername="html",
        srcdir=sphinx_path(source),
        builddir=sphinx_path(build),
        warning=rebuild_warnings,
    )
    try:
        rebuild_app.build()
    finally:
        rebuild_app.cleanup()

    if rebuild_warnings.getvalue():
        pytest.fail(f"Warnings on rebuild: {rebuild_warnings.getvalue()}")
    if package_source.stat().st_mtime != package_source_mtime:
        pytest.fail("Rebuild did not use cached source")
    if package_html.stat().st_mtime != package_html_mtime:
        pytest.fail("Rebuild did not use cached html")


def build_package(tmp_path: Path) -> Path:
    """Build a simple package for testing."""
    package = tmp_path / "package"
    package.mkdir()
    package.joinpath("__init__.py").write_text(
        dedent(
            """\
        '''This is a test package.'''
        from package.a import a1
        from package.a.c import ac1 as alias
        __all__ = ['p', 'a1', 'alias']
        p = 1
        '''p can be documented here.'''

        def func(a: str, b: int) -> alias:
            '''This is a function.'''

        class Class:
            '''This is a class.'''

            x: int = 1
            '''x can be documented here.'''

            def method(self, a: str, b: int) -> ...:
                '''This is a method.'''

            @property
            def prop(self) -> alias | None:
                '''This is a property.'''

            class Nested:
                '''This is a nested class.'''
        """
        ),
        "utf-8",
    )
    package.joinpath("a").mkdir()
    package.joinpath("a", "__init__.py").write_text(
        dedent(
            """\
        '''This is a test module.'''
        from .c import *
        from .d import *
        __all__ = ['a1', 'ac1', 'ad1', 'ade1', 'adf1']
        a1 = 1
        """
        ),
        "utf-8",
    )
    package.joinpath("a", "c.py").write_text(
        dedent(
            """\
        '''This is also a test module.'''
        __all__ = ['ac1']
        ac1 = 1
        """
        ),
        "utf-8",
    )
    return package
