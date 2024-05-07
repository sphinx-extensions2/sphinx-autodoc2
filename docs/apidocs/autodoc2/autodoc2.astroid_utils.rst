:py:mod:`autodoc2.astroid_utils`
================================

.. py:module:: autodoc2.astroid_utils

.. autodoc2-docstring:: autodoc2.astroid_utils
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`resolve_import_alias <autodoc2.astroid_utils.resolve_import_alias>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_import_alias
          :summary:
   * - :py:obj:`is_constructor <autodoc2.astroid_utils.is_constructor>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_constructor
          :summary:
   * - :py:obj:`get_full_import_name <autodoc2.astroid_utils.get_full_import_name>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_full_import_name
          :summary:
   * - :py:obj:`get_assign_value <autodoc2.astroid_utils.get_assign_value>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_value
          :summary:
   * - :py:obj:`get_const_values <autodoc2.astroid_utils.get_const_values>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_const_values
          :summary:
   * - :py:obj:`get_assign_annotation <autodoc2.astroid_utils.get_assign_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_annotation
          :summary:
   * - :py:obj:`resolve_annotation <autodoc2.astroid_utils.resolve_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_annotation
          :summary:
   * - :py:obj:`resolve_qualname <autodoc2.astroid_utils.resolve_qualname>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_qualname
          :summary:
   * - :py:obj:`get_module_all <autodoc2.astroid_utils.get_module_all>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_module_all
          :summary:
   * - :py:obj:`is_decorated_with_singledispatch <autodoc2.astroid_utils.is_decorated_with_singledispatch>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_singledispatch
          :summary:
   * - :py:obj:`is_singledispatch_decorator <autodoc2.astroid_utils.is_singledispatch_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_singledispatch_decorator
          :summary:
   * - :py:obj:`is_decorated_as_singledispatch_register <autodoc2.astroid_utils.is_decorated_as_singledispatch_register>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_as_singledispatch_register
          :summary:
   * - :py:obj:`is_decorated_with_property <autodoc2.astroid_utils.is_decorated_with_property>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property
          :summary:
   * - :py:obj:`is_property_decorator <autodoc2.astroid_utils.is_property_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_property_decorator
          :summary:
   * - :py:obj:`is_decorated_with_property_setter <autodoc2.astroid_utils.is_decorated_with_property_setter>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property_setter
          :summary:
   * - :py:obj:`get_class_docstring <autodoc2.astroid_utils.get_class_docstring>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_class_docstring
          :summary:
   * - :py:obj:`is_exception <autodoc2.astroid_utils.is_exception>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_exception
          :summary:
   * - :py:obj:`is_decorated_with_overload <autodoc2.astroid_utils.is_decorated_with_overload>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_overload
          :summary:
   * - :py:obj:`is_overload_decorator <autodoc2.astroid_utils.is_overload_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_overload_decorator
          :summary:
   * - :py:obj:`get_func_docstring <autodoc2.astroid_utils.get_func_docstring>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_func_docstring
          :summary:
   * - :py:obj:`get_return_annotation <autodoc2.astroid_utils.get_return_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_return_annotation
          :summary:
   * - :py:obj:`get_args_info <autodoc2.astroid_utils.get_args_info>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_args_info
          :summary:
   * - :py:obj:`_iter_args <autodoc2.astroid_utils._iter_args>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._iter_args
          :summary:
   * - :py:obj:`_merge_annotations <autodoc2.astroid_utils._merge_annotations>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._merge_annotations
          :summary:
   * - :py:obj:`_is_ellipsis <autodoc2.astroid_utils._is_ellipsis>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._is_ellipsis
          :summary:

API
~~~

.. py:function:: resolve_import_alias(name: str, import_names: list[tuple[str, str | None]]) -> str
   :canonical: autodoc2.astroid_utils.resolve_import_alias

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_import_alias

.. py:function:: is_constructor(node: astroid.nodes.NodeNG) -> bool
   :canonical: autodoc2.astroid_utils.is_constructor

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_constructor

.. py:function:: get_full_import_name(import_from: astroid.nodes.ImportFrom, name: str) -> str
   :canonical: autodoc2.astroid_utils.get_full_import_name

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_full_import_name

.. py:function:: get_assign_value(node: astroid.nodes.NodeNG) -> None | tuple[str, typing.Any]
   :canonical: autodoc2.astroid_utils.get_assign_value

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_value

.. py:function:: get_const_values(node: astroid.nodes.NodeNG) -> typing.Any
   :canonical: autodoc2.astroid_utils.get_const_values

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_const_values

.. py:function:: get_assign_annotation(node: astroid.nodes.Assign) -> None | str
   :canonical: autodoc2.astroid_utils.get_assign_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_annotation

.. py:function:: resolve_annotation(annotation: astroid.nodes.NodeNG) -> str
   :canonical: autodoc2.astroid_utils.resolve_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_annotation

.. py:function:: resolve_qualname(node: astroid.nodes.NodeNG, basename: str) -> str
   :canonical: autodoc2.astroid_utils.resolve_qualname

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_qualname

.. py:function:: get_module_all(node: astroid.nodes.Module) -> None | list[str]
   :canonical: autodoc2.astroid_utils.get_module_all

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_module_all

.. py:function:: is_decorated_with_singledispatch(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_singledispatch

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_singledispatch

.. py:function:: is_singledispatch_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_singledispatch_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_singledispatch_decorator

.. py:function:: is_decorated_as_singledispatch_register(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_as_singledispatch_register

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_as_singledispatch_register

.. py:function:: is_decorated_with_property(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property

.. py:function:: is_property_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_property_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_property_decorator

.. py:function:: is_decorated_with_property_setter(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property_setter

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property_setter

.. py:function:: get_class_docstring(node: astroid.nodes.ClassDef) -> tuple[str, str | None]
   :canonical: autodoc2.astroid_utils.get_class_docstring

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_class_docstring

.. py:function:: is_exception(node: astroid.nodes.ClassDef) -> bool
   :canonical: autodoc2.astroid_utils.is_exception

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_exception

.. py:function:: is_decorated_with_overload(node: astroid.nodes.FunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_overload

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_overload

.. py:function:: is_overload_decorator(decorator: astroid.Name | astroid.Attribute) -> bool
   :canonical: autodoc2.astroid_utils.is_overload_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_overload_decorator

.. py:function:: get_func_docstring(node: astroid.nodes.FunctionDef) -> tuple[str, None | str]
   :canonical: autodoc2.astroid_utils.get_func_docstring

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_func_docstring

.. py:function:: get_return_annotation(node: astroid.nodes.FunctionDef) -> None | str
   :canonical: autodoc2.astroid_utils.get_return_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_return_annotation

.. py:function:: get_args_info(args_node: astroid.Arguments) -> list[tuple[None | str, None | str, None | str, None | str]]
   :canonical: autodoc2.astroid_utils.get_args_info

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_args_info

.. py:function:: _iter_args(args: list[astroid.nodes.NodeNG], annotations: list[astroid.nodes.NodeNG], defaults: list[astroid.nodes.NodeNG]) -> typing.Iterable[tuple[str, None | str, str | None]]
   :canonical: autodoc2.astroid_utils._iter_args

   .. autodoc2-docstring:: autodoc2.astroid_utils._iter_args

.. py:function:: _merge_annotations(annotations: typing.Iterable[typing.Any], comment_annotations: typing.Iterable[typing.Any]) -> typing.Iterable[typing.Any]
   :canonical: autodoc2.astroid_utils._merge_annotations

   .. autodoc2-docstring:: autodoc2.astroid_utils._merge_annotations

.. py:function:: _is_ellipsis(node: typing.Any) -> bool
   :canonical: autodoc2.astroid_utils._is_ellipsis

   .. autodoc2-docstring:: autodoc2.astroid_utils._is_ellipsis
