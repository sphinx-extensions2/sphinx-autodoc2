"""Basic tests for the analysis module."""
from __future__ import annotations

import typing as t

import pytest

from autodoc2.analysis import analyse_module


def clean_item(item: dict[str, t.Any]) -> dict[str, t.Any]:
    """Remove non-deterministic data."""
    return {
        key: value
        for key, value in item.items()
        if key not in ("modified", "file_path", "encoding")
    }


test_items = {
    # module
    "module_docstring": "'''Docstring'''",
    "module_all": "__all__ = ['a', 'b', 'c']",
    # annotation only assign
    "assign_annotation": "a: str",
    "assign_annotation_union": "a: str | int",
    # assign with annotation
    "assign_string": "a: str = 'Hello World'\n'''Docstring'''",
    "assign_bytes": "a: bytes = b'Hello World'",
    "assign_int": "a: int = 42",
    "assign_float": "a: float = 3.14",
    "assign_list": "a: list = [1, 2, 3]",
    "assign_tuple": "a: tuple = (1, 2, 3)",
    "assign_dict": "a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}",
    "assign_set": "a: set[int] = {1, 2, 3}",
    "assign_with_docstring": "a: str = 'Hello World'\n'''Docstring'''",
    # function with annotation
    "func_basic": "def a() -> str: ...",
    "func_1arg": "def a(b: int) -> str: ...",
    "func_args": "def a(*b: int) -> str: ...",
    "func_1kwarg": "def a(*, b: int) -> str: ...",
    "func_kwargs": "def a(**kw: float) -> str: ...",
    "func_docstring": "def a() -> str:\n    '''Docstring'''\n",
    "func_async": "async def a() -> str: ...",
    # class with annotation
    "class_basic": "class A: ...",
    "class_inherit": "class A(B): ...",
    "class_inherit_multi": "class A(B, C): ...",
    "class_inherit_generic": "class A(B[int]): ...",
    "class_docstring": "class A:\n    '''Docstring'''\n",
    "class_attribute": "class A:\n    a: str",
    "class_attribute_with_docstring": "class A:\n    a: str\n    '''Docstring'''\n",
    # class method with annotation
    "class_method_basic": "class A:\n    def a(self) -> str: ...",
    # class property with annotation
    "class_property_basic": "class A:\n    @property\n    def a(self) -> str: ...",
    # class static method with annotation
    "class_staticmethod_basic": "class A:\n    @staticmethod\n    def a() -> str: ...",
    # class class method with annotation
    "class_classmethod_basic": "class A:\n    @classmethod\n    def a(cls) -> str: ...",
    # class abstract method with annotation
    "class_abstractmethod_basic": "import abc\n\nclass A:\n    @abc.abstractmethod\n    def a(self) -> str: ...",
    "class_inherited": "class A:\n    def a(self) -> str: ...\nclass B(A): ...",
    "class_inherited_with_docstring": "class A:\n    '''Docstring'''\n\n    def a(self) -> str: ...\nclass B(A): ...",
    # overloads
    "overload_basic": "from typing import overload\n\n@overload\ndef a() -> str: ...\n@overload\ndef a(b: int) -> str: ...",
}


@pytest.mark.parametrize(
    "content",
    list(test_items.values()),
    ids=list(test_items),
)
def test_basic(content, tmp_path, data_regression):
    tmp_path.joinpath("test.py").write_text(content)
    data = [clean_item(item) for item in analyse_module(tmp_path / "test.py", "test")]
    data_regression.check(data)


def test_package(tmp_path, data_regression):
    pkg = tmp_path.joinpath("test")
    pkg.mkdir()
    pkg.joinpath("__init__.py").write_text("'''Docstring'''")
    pkg.joinpath("a.py").write_text("a: str = 'Hello World'")
    pkg.joinpath("b.py").write_text(
        "from .a import a\nfrom .a import a as x\nb: str = a"
    )
    data = {
        "init": [
            clean_item(item)
            for item in analyse_module(pkg.joinpath("__init__.py"), "test")
        ],
        "a": [
            clean_item(item) for item in analyse_module(pkg.joinpath("a.py"), "test.a")
        ],
        "b": [
            clean_item(item) for item in analyse_module(pkg.joinpath("b.py"), "test.b")
        ],
    }
    data_regression.check(data)
