"""Tests for the database."""

from pathlib import Path
from textwrap import dedent

from autodoc2.analysis import analyse_module
from autodoc2.db import InMemoryDb
from autodoc2.resolve_all import AllResolver
from autodoc2.utils import yield_modules


def test_all_resolution(tmp_path: Path, data_regression):
    """Test __all__ resolution"""
    package = tmp_path / "package"
    package.mkdir()
    package.joinpath("__init__.py").write_text(
        dedent(
            """\
        from package.a import a1
        from package.a.c import ac1 as alias
        from unknown import something
        from .b import *
        from .d import *
        from other import *
        __all__ = ['p', 'a1', 'alias', 'something', 'unknown']
        p = 1
        """
        ),
        "utf-8",
    )
    package.joinpath("a").mkdir()
    package.joinpath("a", "__init__.py").write_text(
        dedent(
            """\
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
        __all__ = ['ac1']
        ac1 = 1
        """
        ),
        "utf-8",
    )
    package.joinpath("b.py").touch()
    package.joinpath("d.py").write_text(
        # circular import
        dedent(
            """\
        from package import *
        __all__ = ['p']
        """
        ),
        "utf-8",
    )

    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    warnings = []
    resolver = AllResolver(db, warnings.append)
    result = resolver.get_resolved_all("package")

    data_regression.check({"result": result, "warnings": warnings})
