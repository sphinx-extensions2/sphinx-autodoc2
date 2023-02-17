:py:mod:`autodoc2.astroid_utils`
================================

.. py:module:: autodoc2.astroid_utils


Description
-----------

Utilities for working with astroid nodes.

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`resolve_import_alias <autodoc2.astroid_utils.resolve_import_alias>`
     - Resolve a name from an aliased import to its original name.
   * - :py:obj:`is_constructor <autodoc2.astroid_utils.is_constructor>`
     - Check if the function is a constructor.
   * - :py:obj:`get_full_import_name <autodoc2.astroid_utils.get_full_import_name>`
     - Get the full path of a name from a ``from x import y`` statement.
   * - :py:obj:`get_assign_value <autodoc2.astroid_utils.get_assign_value>`
     - Get the name and value of the assignment of the given node.
   * - :py:obj:`get_const_values <autodoc2.astroid_utils.get_const_values>`
     - Get the value of a constant node.
   * - :py:obj:`get_assign_annotation <autodoc2.astroid_utils.get_assign_annotation>`
     - Get the type annotation of the assignment of the given node.
   * - :py:obj:`resolve_annotation <autodoc2.astroid_utils.resolve_annotation>`
     - Resolve a type annotation to a string.
   * - :py:obj:`resolve_qualname <autodoc2.astroid_utils.resolve_qualname>`
     - Resolve where a node is defined to get its fully qualified name.
   * - :py:obj:`get_module_all <autodoc2.astroid_utils.get_module_all>`
     - Get the contents of the ``__all__`` variable from a module.
   * - :py:obj:`is_decorated_with_singledispatch <autodoc2.astroid_utils.is_decorated_with_singledispatch>`
     - Check if the function is decorated as a singledispatch.
   * - :py:obj:`is_singledispatch_decorator <autodoc2.astroid_utils.is_singledispatch_decorator>`
     - Check if the decorator is a singledispatch.
   * - :py:obj:`is_decorated_as_singledispatch_register <autodoc2.astroid_utils.is_decorated_as_singledispatch_register>`
     - Check if the function is decorated as a singledispatch register.
   * - :py:obj:`is_decorated_with_property <autodoc2.astroid_utils.is_decorated_with_property>`
     - Check if the function is decorated as a property.
   * - :py:obj:`is_property_decorator <autodoc2.astroid_utils.is_property_decorator>`
     - Check if the decorator is a property.
   * - :py:obj:`is_decorated_with_property_setter <autodoc2.astroid_utils.is_decorated_with_property_setter>`
     - Check if the function is decorated as a property setter.
   * - :py:obj:`get_class_docstring <autodoc2.astroid_utils.get_class_docstring>`
     - Get the docstring of a node, using a parent docstring if needed.
   * - :py:obj:`is_exception <autodoc2.astroid_utils.is_exception>`
     - Check if a class is an exception.
   * - :py:obj:`is_decorated_with_overload <autodoc2.astroid_utils.is_decorated_with_overload>`
     - Check if the function is decorated as an overload definition.
   * - :py:obj:`is_overload_decorator <autodoc2.astroid_utils.is_overload_decorator>`
     - 
   * - :py:obj:`get_func_docstring <autodoc2.astroid_utils.get_func_docstring>`
     - Get the docstring of a node, using a parent docstring if needed.
   * - :py:obj:`get_return_annotation <autodoc2.astroid_utils.get_return_annotation>`
     - Get the return annotation of a node.
   * - :py:obj:`get_args_info <autodoc2.astroid_utils.get_args_info>`
     - Get the arguments of a function.
   * - :py:obj:`_iter_args <autodoc2.astroid_utils._iter_args>`
     - Iterate over arguments.
   * - :py:obj:`_merge_annotations <autodoc2.astroid_utils._merge_annotations>`
     - 
   * - :py:obj:`_is_ellipsis <autodoc2.astroid_utils._is_ellipsis>`
     - 

API
~~~

.. py:function:: resolve_import_alias(name: str, import_names: list[tuple[str, str | None]]) -> str
   :canonical: autodoc2.astroid_utils.resolve_import_alias

   Resolve a name from an aliased import to its original name.

   :param name: The potentially aliased name to resolve.
   :param import_names: The pairs of original names and aliases
       from the import.

   :returns: The original name.


.. py:function:: is_constructor(node: astroid.nodes.NodeNG) -> bool
   :canonical: autodoc2.astroid_utils.is_constructor

   Check if the function is a constructor.

.. py:function:: get_full_import_name(import_from: astroid.nodes.ImportFrom, name: str) -> str
   :canonical: autodoc2.astroid_utils.get_full_import_name

   Get the full path of a name from a ``from x import y`` statement.

   :returns: The full import path of the name.


.. py:function:: get_assign_value(node: astroid.nodes.NodeNG) -> None | tuple[str, typing.Any]
   :canonical: autodoc2.astroid_utils.get_assign_value

   Get the name and value of the assignment of the given node.

   Assignments to multiple names are ignored, as per PEP 257.

   :param node: The node to get the assignment value from.

   :returns: The name that is assigned to,
       and the value assigned to the name (if it can be converted).


.. py:function:: get_const_values(node: astroid.nodes.NodeNG) -> typing.Any
   :canonical: autodoc2.astroid_utils.get_const_values

   Get the value of a constant node.

.. py:function:: get_assign_annotation(node: astroid.nodes.Assign) -> None | str
   :canonical: autodoc2.astroid_utils.get_assign_annotation

   Get the type annotation of the assignment of the given node.

   :returns: The type annotation as a string, or None if one does not exist.


.. py:function:: resolve_annotation(annotation: astroid.nodes.NodeNG) -> str
   :canonical: autodoc2.astroid_utils.resolve_annotation

   Resolve a type annotation to a string.

.. py:function:: resolve_qualname(node: astroid.nodes.NodeNG, basename: str) -> str
   :canonical: autodoc2.astroid_utils.resolve_qualname

   Resolve where a node is defined to get its fully qualified name.

   :param node: The node representing the base name.
   :param basename: The partial base name to resolve.

   :returns: The fully resolved base name.


.. py:function:: get_module_all(node: astroid.nodes.Module) -> None | list[str]
   :canonical: autodoc2.astroid_utils.get_module_all

   Get the contents of the ``__all__`` variable from a module.

.. py:function:: is_decorated_with_singledispatch(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_singledispatch

   Check if the function is decorated as a singledispatch.

.. py:function:: is_singledispatch_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_singledispatch_decorator

   Check if the decorator is a singledispatch.

.. py:function:: is_decorated_as_singledispatch_register(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_as_singledispatch_register

   Check if the function is decorated as a singledispatch register.

.. py:function:: is_decorated_with_property(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property

   Check if the function is decorated as a property.

.. py:function:: is_property_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_property_decorator

   Check if the decorator is a property.

.. py:function:: is_decorated_with_property_setter(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property_setter

   Check if the function is decorated as a property setter.

   :param node: The node to check.

   :returns: True if the function is a property setter, False otherwise.


.. py:function:: get_class_docstring(node: astroid.nodes.ClassDef) -> str
   :canonical: autodoc2.astroid_utils.get_class_docstring

   Get the docstring of a node, using a parent docstring if needed.

.. py:function:: is_exception(node: astroid.nodes.ClassDef) -> bool
   :canonical: autodoc2.astroid_utils.is_exception

   Check if a class is an exception.

.. py:function:: is_decorated_with_overload(node: astroid.nodes.FunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_overload

   Check if the function is decorated as an overload definition.

.. py:function:: is_overload_decorator(decorator: astroid.Name | astroid.Attribute) -> bool
   :canonical: autodoc2.astroid_utils.is_overload_decorator

.. py:function:: get_func_docstring(node: astroid.nodes.FunctionDef) -> str
   :canonical: autodoc2.astroid_utils.get_func_docstring

   Get the docstring of a node, using a parent docstring if needed.

.. py:function:: get_return_annotation(node: astroid.nodes.FunctionDef) -> None | str
   :canonical: autodoc2.astroid_utils.get_return_annotation

   Get the return annotation of a node.

.. py:function:: get_args_info(args_node: astroid.Arguments) -> list[tuple[None | str, None | str, None | str, None | str]]
   :canonical: autodoc2.astroid_utils.get_args_info

   Get the arguments of a function.

   :returns: a list of (type, name, annotation, default)


.. py:function:: _iter_args(args: list[astroid.nodes.NodeNG], annotations: list[astroid.nodes.NodeNG], defaults: list[astroid.nodes.NodeNG]) -> typing.Iterable[typing.Tuple[str, None | str, str | None]]
   :canonical: autodoc2.astroid_utils._iter_args

   Iterate over arguments.

.. py:function:: _merge_annotations(annotations: typing.Iterable[typing.Any], comment_annotations: typing.Iterable[typing.Any]) -> typing.Iterable[typing.Any]
   :canonical: autodoc2.astroid_utils._merge_annotations

.. py:function:: _is_ellipsis(node: typing.Any) -> bool
   :canonical: autodoc2.astroid_utils._is_ellipsis
