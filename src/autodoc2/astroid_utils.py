"""Utilities for working with astroid nodes.
"""
from __future__ import annotations

import builtins
import itertools
import re
import typing as t

import astroid
from astroid import nodes


def resolve_import_alias(name: str, import_names: list[tuple[str, str | None]]) -> str:
    """Resolve a name from an aliased import to its original name.

    :param name: The potentially aliased name to resolve.
    :param import_names: The pairs of original names and aliases
        from the import.

    :returns: The original name.
    """
    resolved_name = name

    for import_name, imported_as in import_names:
        if import_name == name:
            break
        if imported_as == name:
            resolved_name = import_name
            break

    return resolved_name


def is_constructor(node: nodes.NodeNG) -> bool:
    """Check if the function is a constructor."""
    return (
        node.parent
        and isinstance(node.parent.scope(), nodes.ClassDef)
        and node.name == "__init__"
    )


def get_full_import_name(import_from: nodes.ImportFrom, name: str) -> str:
    """Get the full path of a name from a ``from x import y`` statement.

    :returns: The full import path of the name.
    """
    partial_basename = resolve_import_alias(name, import_from.names)

    module_name = import_from.modname
    if import_from.level:
        module = import_from.root()
        assert isinstance(module, nodes.Module)
        module_name = module.relative_to_absolute_name(
            import_from.modname, level=import_from.level
        )

    return f"{module_name}.{partial_basename}"


def get_assign_value(node: nodes.NodeNG) -> None | tuple[str, t.Any]:
    """Get the name and value of the assignment of the given node.

    Assignments to multiple names are ignored, as per PEP 257.

    :param node: The node to get the assignment value from.

    :returns: The name that is assigned to,
        and the value assigned to the name (if it can be converted).
    """
    try:
        targets = node.targets
    except AttributeError:
        targets = [node.target]

    if len(targets) == 1:
        target = targets[0]
        if isinstance(target, nodes.AssignName):
            name = target.name
        elif isinstance(target, nodes.AssignAttr):
            name = target.attrname
        else:
            return None
        return (name, get_const_values(node.value))

    return None


def get_const_values(node: nodes.NodeNG) -> t.Any:
    """Get the value of a constant node."""
    # TODO its not ideal that this goes to None if not understood
    # TODO better typing
    value: t.Any = None

    if isinstance(node, (nodes.List, nodes.Tuple)):
        new_value = []
        for element in node.elts:
            if isinstance(element, nodes.Const):
                new_value.append(element.value)
            elif isinstance(element, (nodes.List, nodes.Tuple)):
                new_value.append(get_const_values(element))
            else:
                break
        else:
            value = new_value

        if isinstance(node, nodes.Tuple):
            value = tuple(new_value)
    elif isinstance(node, nodes.Const):
        value = node.value

    return value


def get_assign_annotation(node: nodes.Assign) -> None | str:
    """Get the type annotation of the assignment of the given node.

    :returns: The type annotation as a string, or None if one does not exist.
    """
    annotation_node = None
    try:
        annotation_node = node.annotation
    except AttributeError:
        annotation_node = node.type_annotation

    if annotation_node is None:
        return None

    return resolve_annotation(annotation_node)


def resolve_annotation(annotation: nodes.NodeNG) -> str:
    """Resolve a type annotation to a string."""
    resolved: str
    if isinstance(annotation, nodes.Const):
        resolved = resolve_qualname(annotation, str(annotation.value))
    elif isinstance(annotation, nodes.Name):
        resolved = resolve_qualname(annotation, annotation.name)
    elif isinstance(annotation, nodes.Attribute):
        resolved = resolve_qualname(annotation, annotation.as_string())
    elif isinstance(annotation, nodes.Subscript):
        value = resolve_annotation(annotation.value)
        slice_node = annotation.slice
        if isinstance(slice_node, nodes.Index):
            slice_node = slice_node.value
        if isinstance(slice_node, nodes.Tuple):
            slice_ = ", ".join(resolve_annotation(elt) for elt in slice_node.elts)
        else:
            slice_ = resolve_annotation(slice_node)
        resolved = f"{value}[{slice_}]"
    elif isinstance(annotation, nodes.Tuple):
        resolved = (
            "(" + ", ".join(resolve_annotation(elt) for elt in annotation.elts) + ")"
        )
    elif isinstance(annotation, nodes.List):
        resolved = (
            "[" + ", ".join(resolve_annotation(elt) for elt in annotation.elts) + "]"
        )
    elif isinstance(annotation, nodes.BinOp):
        resolved = (
            resolve_annotation(annotation.left)
            + " "
            + annotation.op
            + " "
            + resolve_annotation(annotation.right)
        )
    else:
        resolved = annotation.as_string()

    # note sphinx-autoapi had this, but
    # (a) its not needed, because sphinx strips it in the rendered HTML
    # and (b) it could lead to incorrect links for name clashes

    # if resolved.startswith("typing."):
    #     return resolved[len("typing.") :]

    # Note, sphinx-autoapi had this, with the rationale:
    # > Sphinx is capable of linking anything in the same module
    # > without needing a fully qualified path.
    # However, (a) this breaks if following __all__ and
    # (b) lead to hard to decipher missing references
    # this does though lead to the fully qualified names
    # showing in the type annotations of the output HTML
    # TODO make sphinx not show fully qualified names of type annotations

    # module_prefix = annotation.root().name + "."
    # if resolved.startswith(module_prefix):
    #     return resolved[len(module_prefix) :]

    # TODO sphinx type resolver does not understand Ellipsis, maybe it should?
    if resolved == "Ellipsis":
        return "..."

    return resolved


def resolve_qualname(node: nodes.NodeNG, basename: str) -> str:
    """Resolve where a node is defined to get its fully qualified name.

    :param node: The node representing the base name.
    :param basename: The partial base name to resolve.

    :returns: The fully resolved base name.
    """
    full_basename = basename

    top_level_name = re.sub(r"\(.*\)", "", basename).split(".", 1)[0]
    # Disable until pylint uses astroid 2.7
    lookup_node = (
        node if isinstance(node, nodes.node_classes.LookupMixIn) else node.scope()
    )

    assigns = lookup_node.lookup(top_level_name)[1]

    for assignment in assigns:
        if isinstance(assignment, nodes.ImportFrom):
            import_name = get_full_import_name(assignment, top_level_name)
            full_basename = basename.replace(top_level_name, import_name, 1)
            break
        if isinstance(assignment, nodes.Import):
            import_name = resolve_import_alias(top_level_name, assignment.names)
            full_basename = basename.replace(top_level_name, import_name, 1)
            break
        if isinstance(assignment, nodes.ClassDef):
            full_basename = assignment.qname()
            break
        if isinstance(assignment, nodes.AssignName):
            full_basename = f"{assignment.scope().qname()}.{assignment.name}"

    if isinstance(node, nodes.Call):
        full_basename = re.sub(r"\(.*\)", "()", full_basename)

    if full_basename.startswith("builtins."):
        return full_basename[len("builtins.") :]

    if full_basename.startswith("__builtin__."):
        return full_basename[len("__builtin__.") :]

    return full_basename


def get_module_all(node: nodes.Module) -> None | list[str]:
    """Get the contents of the ``__all__`` variable from a module."""
    all_ = None

    if "__all__" in node.locals:
        assigned = next(node.igetattr("__all__"))
        if assigned is not astroid.Uninferable:
            all_ = []
            for elt in getattr(assigned, "elts", ()):
                try:
                    elt_name = next(elt.infer())
                except astroid.InferenceError:
                    continue

                if elt_name is astroid.Uninferable:
                    continue

                if isinstance(elt_name, nodes.Const) and isinstance(
                    elt_name.value, str
                ):
                    all_.append(elt_name.value)

    return all_


def is_decorated_with_singledispatch(
    node: nodes.FunctionDef | nodes.AsyncFunctionDef,
) -> bool:
    """Check if the function is decorated as a singledispatch."""
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if not isinstance(decorator, astroid.Name):
            continue

        try:
            if is_singledispatch_decorator(decorator):
                return True
        except astroid.InferenceError:
            pass

    return False


def is_singledispatch_decorator(decorator: astroid.Name) -> bool:
    """Check if the decorator is a singledispatch."""

    def _is_singledispatch_func(func_node: nodes.FunctionDef) -> bool:
        return (  # type: ignore[no-any-return]
            func_node.name == "singledispatch" and func_node.root().name == "functools"
        )

    for inferred in decorator.infer():
        if not isinstance(inferred, nodes.FunctionDef):
            continue

        if _is_singledispatch_func(inferred):
            return True

    return False


def is_decorated_as_singledispatch_register(
    node: nodes.FunctionDef | nodes.AsyncFunctionDef,
) -> bool:
    """Check if the function is decorated as a singledispatch register."""
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if not isinstance(decorator, nodes.Call):
            continue
        if not isinstance(decorator.func, nodes.Attribute):
            continue
        if decorator.func.attrname == "register":
            return True
        # TODO any more checking?

    return False


def is_decorated_with_property(
    node: nodes.FunctionDef | nodes.AsyncFunctionDef,
) -> bool:
    """Check if the function is decorated as a property."""
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if not isinstance(decorator, astroid.Name):
            continue

        try:
            if is_property_decorator(decorator):
                return True
        except astroid.InferenceError:
            pass

    return False


def is_property_decorator(decorator: astroid.Name) -> bool:
    """Check if the decorator is a property."""

    def _is_property_class(class_node: nodes.ClassDef) -> bool:
        return (  # type: ignore[no-any-return]
            class_node.name == "property"
            and class_node.root().name == builtins.__name__
        )

    for inferred in decorator.infer():
        if not isinstance(inferred, nodes.ClassDef):
            continue

        if _is_property_class(inferred):
            return True

        if any(_is_property_class(ancestor) for ancestor in inferred.ancestors()):
            return True

    return False


def is_decorated_with_property_setter(
    node: nodes.FunctionDef | nodes.AsyncFunctionDef,
) -> bool:
    """Check if the function is decorated as a property setter.

    :param node: The node to check.

    :returns: True if the function is a property setter, False otherwise.
    """
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if (
            isinstance(decorator, astroid.nodes.Attribute)
            and decorator.attrname == "setter"
        ):
            return True

    return False


def get_class_docstring(node: nodes.ClassDef) -> str:
    """Get the docstring of a node, using a parent docstring if needed."""
    doc = node.doc

    if doc is None:
        for base in node.ancestors():
            if base.qname() in (
                "__builtins__.object",
                "builtins.object",
                "builtins.type",
            ):
                continue
            if base.doc is not None:
                return str(base.doc)

    return doc or ""


def is_exception(node: nodes.ClassDef) -> bool:
    """Check if a class is an exception."""
    if node.name in ("Exception", "BaseException") and node.root().name == "builtins":
        return True

    if not hasattr(node, "ancestors"):
        return False

    return any(is_exception(parent) for parent in node.ancestors(recurs=True))


def is_decorated_with_overload(node: nodes.FunctionDef) -> bool:
    """Check if the function is decorated as an overload definition."""
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if not isinstance(decorator, (astroid.Name, astroid.Attribute)):
            continue

        try:
            if is_overload_decorator(decorator):
                return True
        except astroid.InferenceError:
            pass

    return False


def is_overload_decorator(decorator: astroid.Name | astroid.Attribute) -> bool:
    for inferred in decorator.infer():
        if not isinstance(inferred, astroid.nodes.FunctionDef):
            continue

        if inferred.name == "overload" and inferred.root().name == "typing":
            return True

    return False


def get_func_docstring(node: nodes.FunctionDef) -> str:
    """Get the docstring of a node, using a parent docstring if needed."""
    doc = node.doc

    if doc is None and isinstance(node.parent, nodes.ClassDef):
        for base in node.parent.ancestors():
            if node.name in ("__init__", "__new__") and base.qname() in (
                "__builtins__.object",
                "builtins.object",
                "builtins.type",
            ):
                continue
            for child in base.get_children():
                if (
                    isinstance(child, node.__class__)
                    and child.name == node.name
                    and child.doc is not None
                ):
                    return str(child.doc)

    return doc or ""


def get_return_annotation(node: nodes.FunctionDef) -> None | str:
    """Get the return annotation of a node."""
    if node.returns:
        return resolve_annotation(node.returns)
    if node.type_comment_returns:
        return resolve_annotation(node.type_comment_returns)

    return None


def get_args_info(
    args_node: astroid.Arguments,
) -> list[tuple[None | str, None | str, None | str, None | str]]:
    """Get the arguments of a function.

    :returns: a list of (type, name, annotation, default)
    """
    result: list[tuple[None | str, None | str, None | str, None | str]] = []
    positional_only_defaults = []
    positional_or_keyword_defaults = args_node.defaults
    if args_node.defaults:
        args = args_node.args or []
        positional_or_keyword_defaults = args_node.defaults[-len(args) :]
        positional_only_defaults = args_node.defaults[
            : len(args_node.defaults) - len(args)
        ]

    plain_annotations = args_node.annotations or ()

    func_comment_annotations = args_node.parent.type_comment_args or []
    if args_node.parent.type in ("method", "classmethod"):
        func_comment_annotations = [None, *func_comment_annotations]

    comment_annotations = args_node.type_comment_posonlyargs
    comment_annotations += args_node.type_comment_args or []
    comment_annotations += args_node.type_comment_kwonlyargs
    annotations = list(
        _merge_annotations(
            plain_annotations,
            _merge_annotations(func_comment_annotations, comment_annotations),
        )
    )
    annotation_offset = 0

    if args_node.posonlyargs:
        posonlyargs_annotations = args_node.posonlyargs_annotations
        if not any(args_node.posonlyargs_annotations):
            num_args = len(args_node.posonlyargs)
            posonlyargs_annotations = annotations[
                annotation_offset : annotation_offset + num_args
            ]

        for arg, annotation, default in _iter_args(
            args_node.posonlyargs, posonlyargs_annotations, positional_only_defaults
        ):
            result.append((None, arg, annotation, default))

        result.append(("/", None, None, None))

        if not any(args_node.posonlyargs_annotations):
            annotation_offset += num_args

    if args_node.args:
        num_args = len(args_node.args)
        for arg, annotation, default in _iter_args(
            args_node.args,
            annotations[annotation_offset : annotation_offset + num_args],
            positional_or_keyword_defaults,
        ):
            result.append((None, arg, annotation, default))

        annotation_offset += num_args

    if args_node.vararg:
        annotation = None
        if args_node.varargannotation:
            annotation = resolve_annotation(args_node.varargannotation)
        elif len(annotations) > annotation_offset and annotations[annotation_offset]:
            annotation = resolve_annotation(annotations[annotation_offset])
            annotation_offset += 1
        result.append(("*", args_node.vararg, annotation, None))

    if args_node.kwonlyargs:
        if not args_node.vararg:
            result.append(("*", None, None, None))

        kwonlyargs_annotations = args_node.kwonlyargs_annotations
        if not any(args_node.kwonlyargs_annotations):
            num_args = len(args_node.kwonlyargs)
            kwonlyargs_annotations = annotations[
                annotation_offset : annotation_offset + num_args
            ]

        for arg, annotation, default in _iter_args(
            args_node.kwonlyargs,
            kwonlyargs_annotations,
            args_node.kw_defaults,
        ):
            result.append((None, arg, annotation, default))

        if not any(args_node.kwonlyargs_annotations):
            annotation_offset += num_args

    if args_node.kwarg:
        annotation = None
        if args_node.kwargannotation:
            annotation = resolve_annotation(args_node.kwargannotation)
        elif len(annotations) > annotation_offset and annotations[annotation_offset]:
            annotation = resolve_annotation(annotations[annotation_offset])
            annotation_offset += 1
        result.append(("**", args_node.kwarg, annotation, None))

    if args_node.parent.type in ("method", "classmethod") and result:
        result.pop(0)

    return result


def _iter_args(
    args: list[nodes.NodeNG],
    annotations: list[nodes.NodeNG],
    defaults: list[nodes.NodeNG],
) -> t.Iterable[t.Tuple[str, None | str, str | None]]:
    """Iterate over arguments."""
    default_offset = len(args) - len(defaults)
    packed = itertools.zip_longest(args, annotations)
    for i, (arg, annotation) in enumerate(packed):
        default = None
        if (defaults is not None and i >= default_offset) and (
            defaults[i - default_offset] is not None
        ):
            default = defaults[i - default_offset].as_string()

        name = arg.name
        if isinstance(arg, astroid.Tuple):
            argument_names = ", ".join(x.name for x in arg.elts)
            name = f"({argument_names})"

        yield (
            name,
            resolve_annotation(annotation) if annotation else None,
            default,
        )


def _merge_annotations(
    annotations: t.Iterable[t.Any], comment_annotations: t.Iterable[t.Any]
) -> t.Iterable[t.Any]:
    for ann, comment_ann in itertools.zip_longest(annotations, comment_annotations):
        if ann and not _is_ellipsis(ann):
            yield ann
        elif comment_ann and not _is_ellipsis(comment_ann):
            yield comment_ann
        else:
            yield None


def _is_ellipsis(node: t.Any) -> bool:
    return isinstance(node, astroid.Const) and node.value == Ellipsis
