:py:mod:`autodoc2.astroid_utils`
================================

.. py:module:: autodoc2.astroid_utils

.. autodoc2-docstring:: autodoc2.astroid_utils
   :renderer: rst
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
          :renderer: rst
          :summary:
   * - :py:obj:`is_constructor <autodoc2.astroid_utils.is_constructor>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_constructor
          :renderer: rst
          :summary:
   * - :py:obj:`get_full_import_name <autodoc2.astroid_utils.get_full_import_name>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_full_import_name
          :renderer: rst
          :summary:
   * - :py:obj:`get_assign_value <autodoc2.astroid_utils.get_assign_value>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_value
          :renderer: rst
          :summary:
   * - :py:obj:`get_const_values <autodoc2.astroid_utils.get_const_values>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_const_values
          :renderer: rst
          :summary:
   * - :py:obj:`get_assign_annotation <autodoc2.astroid_utils.get_assign_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_annotation
          :renderer: rst
          :summary:
   * - :py:obj:`resolve_annotation <autodoc2.astroid_utils.resolve_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_annotation
          :renderer: rst
          :summary:
   * - :py:obj:`resolve_qualname <autodoc2.astroid_utils.resolve_qualname>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_qualname
          :renderer: rst
          :summary:
   * - :py:obj:`get_module_all <autodoc2.astroid_utils.get_module_all>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_module_all
          :renderer: rst
          :summary:
   * - :py:obj:`is_decorated_with_singledispatch <autodoc2.astroid_utils.is_decorated_with_singledispatch>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_singledispatch
          :renderer: rst
          :summary:
   * - :py:obj:`is_singledispatch_decorator <autodoc2.astroid_utils.is_singledispatch_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_singledispatch_decorator
          :renderer: rst
          :summary:
   * - :py:obj:`is_decorated_as_singledispatch_register <autodoc2.astroid_utils.is_decorated_as_singledispatch_register>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_as_singledispatch_register
          :renderer: rst
          :summary:
   * - :py:obj:`is_decorated_with_property <autodoc2.astroid_utils.is_decorated_with_property>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property
          :renderer: rst
          :summary:
   * - :py:obj:`is_property_decorator <autodoc2.astroid_utils.is_property_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_property_decorator
          :renderer: rst
          :summary:
   * - :py:obj:`is_decorated_with_property_setter <autodoc2.astroid_utils.is_decorated_with_property_setter>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property_setter
          :renderer: rst
          :summary:
   * - :py:obj:`get_class_docstring <autodoc2.astroid_utils.get_class_docstring>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_class_docstring
          :renderer: rst
          :summary:
   * - :py:obj:`is_exception <autodoc2.astroid_utils.is_exception>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_exception
          :renderer: rst
          :summary:
   * - :py:obj:`is_decorated_with_overload <autodoc2.astroid_utils.is_decorated_with_overload>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_overload
          :renderer: rst
          :summary:
   * - :py:obj:`is_overload_decorator <autodoc2.astroid_utils.is_overload_decorator>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.is_overload_decorator
          :renderer: rst
          :summary:
   * - :py:obj:`get_func_docstring <autodoc2.astroid_utils.get_func_docstring>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_func_docstring
          :renderer: rst
          :summary:
   * - :py:obj:`get_return_annotation <autodoc2.astroid_utils.get_return_annotation>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_return_annotation
          :renderer: rst
          :summary:
   * - :py:obj:`get_args_info <autodoc2.astroid_utils.get_args_info>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils.get_args_info
          :renderer: rst
          :summary:
   * - :py:obj:`_iter_args <autodoc2.astroid_utils._iter_args>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._iter_args
          :renderer: rst
          :summary:
   * - :py:obj:`_merge_annotations <autodoc2.astroid_utils._merge_annotations>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._merge_annotations
          :renderer: rst
          :summary:
   * - :py:obj:`_is_ellipsis <autodoc2.astroid_utils._is_ellipsis>`
     - .. autodoc2-docstring:: autodoc2.astroid_utils._is_ellipsis
          :renderer: rst
          :summary:

API
~~~

.. py:function:: resolve_import_alias(name: str, import_names: list[tuple[str, str | None]]) -> str
   :canonical: autodoc2.astroid_utils.resolve_import_alias

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_import_alias
      :renderer: rst

.. py:function:: is_constructor(node: astroid.nodes.NodeNG) -> bool
   :canonical: autodoc2.astroid_utils.is_constructor

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_constructor
      :renderer: rst

.. py:function:: get_full_import_name(import_from: astroid.nodes.ImportFrom, name: str) -> str
   :canonical: autodoc2.astroid_utils.get_full_import_name

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_full_import_name
      :renderer: rst

.. py:function:: get_assign_value(node: astroid.nodes.NodeNG) -> None | tuple[str, typing.Any]
   :canonical: autodoc2.astroid_utils.get_assign_value

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_value
      :renderer: rst

.. py:function:: get_const_values(node: astroid.nodes.NodeNG) -> typing.Any
   :canonical: autodoc2.astroid_utils.get_const_values

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_const_values
      :renderer: rst

.. py:function:: get_assign_annotation(node: astroid.nodes.Assign) -> None | str
   :canonical: autodoc2.astroid_utils.get_assign_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_assign_annotation
      :renderer: rst

.. py:function:: resolve_annotation(annotation: astroid.nodes.NodeNG) -> str
   :canonical: autodoc2.astroid_utils.resolve_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_annotation
      :renderer: rst

.. py:function:: resolve_qualname(node: astroid.nodes.NodeNG, basename: str) -> str
   :canonical: autodoc2.astroid_utils.resolve_qualname

   .. autodoc2-docstring:: autodoc2.astroid_utils.resolve_qualname
      :renderer: rst

.. py:function:: get_module_all(node: astroid.nodes.Module) -> None | list[str]
   :canonical: autodoc2.astroid_utils.get_module_all

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_module_all
      :renderer: rst

.. py:function:: is_decorated_with_singledispatch(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_singledispatch

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_singledispatch
      :renderer: rst

.. py:function:: is_singledispatch_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_singledispatch_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_singledispatch_decorator
      :renderer: rst

.. py:function:: is_decorated_as_singledispatch_register(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_as_singledispatch_register

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_as_singledispatch_register
      :renderer: rst

.. py:function:: is_decorated_with_property(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property
      :renderer: rst

.. py:function:: is_property_decorator(decorator: astroid.Name) -> bool
   :canonical: autodoc2.astroid_utils.is_property_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_property_decorator
      :renderer: rst

.. py:function:: is_decorated_with_property_setter(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_property_setter

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_property_setter
      :renderer: rst

.. py:function:: get_class_docstring(node: astroid.nodes.ClassDef) -> str
   :canonical: autodoc2.astroid_utils.get_class_docstring

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_class_docstring
      :renderer: rst

.. py:function:: is_exception(node: astroid.nodes.ClassDef) -> bool
   :canonical: autodoc2.astroid_utils.is_exception

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_exception
      :renderer: rst

.. py:function:: is_decorated_with_overload(node: astroid.nodes.FunctionDef) -> bool
   :canonical: autodoc2.astroid_utils.is_decorated_with_overload

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_decorated_with_overload
      :renderer: rst

.. py:function:: is_overload_decorator(decorator: astroid.Name | astroid.Attribute) -> bool
   :canonical: autodoc2.astroid_utils.is_overload_decorator

   .. autodoc2-docstring:: autodoc2.astroid_utils.is_overload_decorator
      :renderer: rst

.. py:function:: get_func_docstring(node: astroid.nodes.FunctionDef) -> str
   :canonical: autodoc2.astroid_utils.get_func_docstring

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_func_docstring
      :renderer: rst

.. py:function:: get_return_annotation(node: astroid.nodes.FunctionDef) -> None | str
   :canonical: autodoc2.astroid_utils.get_return_annotation

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_return_annotation
      :renderer: rst

.. py:function:: get_args_info(args_node: astroid.Arguments) -> list[tuple[None | str, None | str, None | str, None | str]]
   :canonical: autodoc2.astroid_utils.get_args_info

   .. autodoc2-docstring:: autodoc2.astroid_utils.get_args_info
      :renderer: rst

.. py:function:: _iter_args(args: list[astroid.nodes.NodeNG], annotations: list[astroid.nodes.NodeNG], defaults: list[astroid.nodes.NodeNG]) -> typing.Iterable[typing.Tuple[str, None | str, str | None]]
   :canonical: autodoc2.astroid_utils._iter_args

   .. autodoc2-docstring:: autodoc2.astroid_utils._iter_args
      :renderer: rst

.. py:function:: _merge_annotations(annotations: typing.Iterable[typing.Any], comment_annotations: typing.Iterable[typing.Any]) -> typing.Iterable[typing.Any]
   :canonical: autodoc2.astroid_utils._merge_annotations

   .. autodoc2-docstring:: autodoc2.astroid_utils._merge_annotations
      :renderer: rst

.. py:function:: _is_ellipsis(node: typing.Any) -> bool
   :canonical: autodoc2.astroid_utils._is_ellipsis

   .. autodoc2-docstring:: autodoc2.astroid_utils._is_ellipsis
      :renderer: rst
