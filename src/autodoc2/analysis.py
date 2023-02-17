"""Analyse of Python code using astroid.

The core function though `analyse_module` is agnostic to the implementation,
It simply yields `ItemData` typed-dicts.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import itertools
import os
from pathlib import Path
import sys
import typing as t

from astroid import nodes
from astroid.builder import AstroidBuilder

from . import astroid_utils

if t.TYPE_CHECKING:
    from .utils import PROPERTY_TYPE, ItemData

__all__ = ["analyse_module"]


def analyse_module(
    file_path: Path, name: str, exclude_external_imports: t.Pattern[str] | None = None
) -> t.Iterable[ItemData]:
    """Analyse the given module and yield items.

    :param file_path: The path to the module.
    :param name: The name of the module, e.g. "foo.bar".
    :param record_external_imports: If given, record these external imports on the module.
        These are only used to determine what is exposed by __all__,
        which is only usually objects in the same package.
        But if you want to expose objects from other packages,
        you can use this to record them.
    """
    # TODO expose record_external_imports everywhere analyse_module is used
    node = AstroidBuilder().file_build(os.fsdecode(file_path), name)
    yield from walk_node(
        node, State(node.name.split(".", 1)[0], [], exclude_external_imports)
    )


_dc_kwargs: dict[str, bool] = {"frozen": True}
if sys.version_info >= (3, 10):
    _dc_kwargs["slots"] = True


@dataclass(**_dc_kwargs)
class State:
    package_name: str
    name_stack: list[str]
    exclude_external_imports: t.Pattern[str] | None

    def copy(self, **kwargs: t.Any) -> State:
        """Copy the state and update the given attributes."""
        return replace(self, **kwargs)


def _get_full_name(name: str, name_stack: list[str]) -> str:
    """Get the full name of a node."""
    return ".".join([*name_stack, name])


def _get_parent_name(name: str) -> str:
    """Get the parent name of a node."""
    return ".".join(name.split(".")[:-1])


def clean_docstring(s: None | str, tabsize: int = 8) -> str:
    """Remove common leading indentation,
    where the indentation of the first line is ignored.
    """
    if s is None:
        return ""
    lines = s.expandtabs(tabsize).splitlines()
    # Find minimum indentation of any non-blank lines after ignored lines.
    margin = sys.maxsize
    for line in lines[1:]:
        content = len(line.lstrip())
        if content:
            indent = len(line) - content
            margin = min(margin, indent)
    # Remove indentation from the first line.
    if len(lines):
        lines[0] = lines[0].lstrip()
    if margin < sys.maxsize:
        for i in range(1, len(lines)):
            lines[i] = lines[i][margin:]
    # Remove any leading blank lines.
    while lines and not lines[0]:
        lines.pop(0)

    return "\n".join(lines)


def walk_node(node: nodes.NodeNG, state: State) -> t.Iterable[ItemData]:
    func = _FUNC_MAPPER.get(type(node))
    if func is not None:
        yield from func(node, state)


def yield_module(node: nodes.Module, state: State) -> t.Iterable[ItemData]:
    path = node.path
    if isinstance(node.path, list):
        path = node.path[0] if node.path else None

    parent: ItemData = {
        "type": "package" if node.package else "module",
        "full_name": node.name,
        "doc": clean_docstring(node.doc),
        "file_path": path,
        "encoding": node.file_encoding,
        "all": astroid_utils.get_module_all(node),
    }

    for child in node.get_children():
        if isinstance(child, nodes.ImportFrom):
            # Note, the code below restricts to local imports, which was in sphinx-autoapi
            # However, we potentially need all imports, to be able to resolve __all__ exports
            # (i.e. the public API) since packages could expose aspects of other packages
            # To limit what we store in the database, we allow for filtering out imports
            # for example, it might be reasonably assumed that nothing imported from the typing module
            # is part of the public API
            if not (
                child.level
                or child.modname == state.package_name
                or child.modname.startswith(state.package_name + ".")
            ) and (
                child.modname
                and state.exclude_external_imports
                and state.exclude_external_imports.fullmatch(child.modname)
            ):
                continue

            imports = parent.setdefault("imports", [])
            for name, alias in child.names:
                original_path = astroid_utils.get_full_import_name(child, alias or name)
                imports.append((original_path, alias))

    yield parent

    for child in node.get_children():
        yield from walk_node(child, state.copy(name_stack=[node.name]))


def yield_annotation_assign(
    node: nodes.AnnAssign, state: State
) -> t.Iterable[ItemData]:
    """Yield data for an annotation assignment node."""
    if not isinstance(node.target, nodes.AssignAttr):
        yield from _yield_assign(node, state)


def yield_assign(node: nodes.Assign, state: State) -> t.Iterable[ItemData]:
    """Yield data for an assignment node."""
    if not any(isinstance(target, nodes.AssignAttr) for target in node.targets):
        yield from _yield_assign(node, state)


def _yield_assign(
    node: nodes.Assign | nodes.AnnAssign, state: State
) -> t.Iterable[ItemData]:
    """Yield data for an assignment node."""
    doc = ""
    doc_node = node.next_sibling()
    if isinstance(doc_node, nodes.Expr) and isinstance(doc_node.value, nodes.Const):
        doc = doc_node.value.value

    type_ = "data"
    if isinstance(node.scope(), nodes.ClassDef) or astroid_utils.is_constructor(
        node.scope()
    ):
        type_ = "attribute"

    assign_value = astroid_utils.get_assign_value(node)
    if not assign_value:
        return

    target = assign_value[0]
    value = assign_value[1]

    annotation = astroid_utils.get_assign_annotation(node)

    data: ItemData = {
        "type": type_,
        "full_name": _get_full_name(target, state.name_stack),
        "doc": clean_docstring(doc),
        "value": value,
        "annotation": annotation,
    }
    if node.fromlineno is not None and node.tolineno is not None:
        data["range"] = (node.fromlineno, node.tolineno)
    yield data


def yield_function_def(
    node: nodes.FunctionDef | nodes.AsyncFunctionDef, state: State
) -> t.Iterable[ItemData]:
    """Yield data for a function definition node."""
    if astroid_utils.is_decorated_with_property_setter(node):
        return
    if astroid_utils.is_decorated_as_singledispatch_register(node):
        # functools.singledispatch registers, we just ignore these for now,
        # since they are not really functions
        return

    type_ = "method"
    properties: list[PROPERTY_TYPE] = []

    if node.type == "function":
        type_ = "function"

        if isinstance(node, nodes.AsyncFunctionDef):
            properties.append("async")
        if astroid_utils.is_decorated_with_singledispatch(node):
            properties.append("singledispatch")
    elif astroid_utils.is_decorated_with_property(node):
        type_ = "property"
        if node.type == "classmethod":
            properties.append(node.type)
        if node.is_abstract(pass_is_abstract=False):
            properties.append("abstractmethod")
    else:
        # "__new__" method is implicit classmethod
        if node.type in ("staticmethod", "classmethod") and node.name != "__new__":
            properties.append(node.type)
        if node.is_abstract(pass_is_abstract=False):
            properties.append("abstractmethod")
        if isinstance(node, nodes.AsyncFunctionDef):
            properties.append("async")

    if astroid_utils.is_decorated_with_overload(node):
        type_ = "overload"

    data: ItemData = {
        "type": type_,
        "full_name": _get_full_name(node.name, state.name_stack),
        "doc": clean_docstring(astroid_utils.get_func_docstring(node)),
        "args": astroid_utils.get_args_info(node.args),
        "return_annotation": astroid_utils.get_return_annotation(node),
    }
    if node.fromlineno is not None and node.tolineno is not None:
        data["range"] = (node.fromlineno, node.tolineno)
    if properties:
        data["properties"] = properties

    yield data

    if node.name == "__init__":
        for child in node.get_children():
            if isinstance(child, (nodes.Assign, nodes.AnnAssign)):
                child_data = _yield_assign(child, state)
                for data in child_data:
                    if data["doc"]:
                        yield data


def yield_class_def(node: nodes.ClassDef, state: State) -> t.Iterable[ItemData]:
    """Yield data for a class definition node."""
    type_ = "class"
    if astroid_utils.is_exception(node):
        type_ = "exception"

    basenames = [astroid_utils.resolve_annotation(base) for base in node.bases]

    parent: ItemData = {
        "type": type_,
        "full_name": _get_full_name(node.name, state.name_stack),
        "bases": basenames,
        "doc": clean_docstring(astroid_utils.get_class_docstring(node)),
    }
    if node.fromlineno is not None and node.tolineno is not None:
        parent["range"] = (node.fromlineno, node.tolineno)
    yield parent

    new_state = state.copy(name_stack=[*state.name_stack, node.name])

    overridden: t.Set[str] = set()  # a list of methods overridden by class inheritance
    for base in itertools.chain(iter((node,)), node.ancestors()):
        seen: t.Set[str] = set()
        if base.qname() in (
            "__builtins__.object",
            "builtins.object",
            "builtins.type",
        ):
            continue
        for child in base.get_children():
            name = getattr(child, "name", None)
            if isinstance(child, (nodes.Assign, nodes.AnnAssign)):
                assign_value = astroid_utils.get_assign_value(child)
                if not assign_value:
                    continue
                name = assign_value[0]

            if not name or name in overridden:
                continue
            seen.add(name)

            for ancestor in walk_node(child, new_state):
                if (
                    _get_parent_name(ancestor["full_name"]) == parent["full_name"]
                ) and (base is not node):
                    ancestor["inherited"] = True

                yield ancestor

        overridden.update(seen)


_FUNC_MAPPER: dict[
    nodes.NodeNG, t.Callable[[nodes.NodeNG, State], t.Iterable[ItemData]]
] = {
    nodes.Module: yield_module,
    nodes.AnnAssign: yield_annotation_assign,
    nodes.Assign: yield_assign,
    nodes.FunctionDef: yield_function_def,
    nodes.AsyncFunctionDef: yield_function_def,
    nodes.ClassDef: yield_class_def,
}
