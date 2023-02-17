:py:mod:`autodoc2.analysis`
===========================

.. py:module:: autodoc2.analysis


Description
-----------

Analyse of Python code using astroid.

The core function though `analyse_module` is agnostic to the implementation,
It simply yields `ItemData` typed-dicts.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`State <autodoc2.analysis.State>`
     - 

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`analyse_module <autodoc2.analysis.analyse_module>`
     - Analyse the given module and yield items.
   * - :py:obj:`_get_full_name <autodoc2.analysis._get_full_name>`
     - Get the full name of a node.
   * - :py:obj:`_get_parent_name <autodoc2.analysis._get_parent_name>`
     - Get the parent name of a node.
   * - :py:obj:`clean_docstring <autodoc2.analysis.clean_docstring>`
     - Remove common leading indentation, where the indentation of the first line is ignored.
   * - :py:obj:`walk_node <autodoc2.analysis.walk_node>`
     - 
   * - :py:obj:`yield_module <autodoc2.analysis.yield_module>`
     - 
   * - :py:obj:`yield_annotation_assign <autodoc2.analysis.yield_annotation_assign>`
     - Yield data for an annotation assignment node.
   * - :py:obj:`yield_assign <autodoc2.analysis.yield_assign>`
     - Yield data for an assignment node.
   * - :py:obj:`_yield_assign <autodoc2.analysis._yield_assign>`
     - Yield data for an assignment node.
   * - :py:obj:`yield_function_def <autodoc2.analysis.yield_function_def>`
     - Yield data for a function definition node.
   * - :py:obj:`yield_class_def <autodoc2.analysis.yield_class_def>`
     - Yield data for a class definition node.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <autodoc2.analysis.__all__>`
     - 
   * - :py:obj:`_dc_kwargs <autodoc2.analysis._dc_kwargs>`
     - 
   * - :py:obj:`_FUNC_MAPPER <autodoc2.analysis._FUNC_MAPPER>`
     - 

API
~~~

.. py:data:: __all__
   :canonical: autodoc2.analysis.__all__
   :value: ['analyse_module']

.. py:function:: analyse_module(file_path: pathlib.Path, name: str, exclude_external_imports: typing.Pattern[str] | None = None) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.analyse_module

   Analyse the given module and yield items.

   :param file_path: The path to the module.
   :param name: The name of the module, e.g. "foo.bar".
   :param record_external_imports: If given, record these external imports on the module.
       These are only used to determine what is exposed by __all__,
       which is only usually objects in the same package.
       But if you want to expose objects from other packages,
       you can use this to record them.


.. py:data:: _dc_kwargs
   :canonical: autodoc2.analysis._dc_kwargs
   :type: dict[str, bool]
   :value: None

.. py:class:: State
   :canonical: autodoc2.analysis.State

   .. py:attribute:: package_name
      :canonical: autodoc2.analysis.State.package_name
      :type: str
      :value: None

   .. py:attribute:: name_stack
      :canonical: autodoc2.analysis.State.name_stack
      :type: list[str]
      :value: None

   .. py:attribute:: exclude_external_imports
      :canonical: autodoc2.analysis.State.exclude_external_imports
      :type: typing.Pattern[str] | None
      :value: None

   .. py:method:: copy(**kwargs: typing.Any) -> autodoc2.analysis.State
      :canonical: autodoc2.analysis.State.copy

      Copy the state and update the given attributes.

.. py:function:: _get_full_name(name: str, name_stack: list[str]) -> str
   :canonical: autodoc2.analysis._get_full_name

   Get the full name of a node.

.. py:function:: _get_parent_name(name: str) -> str
   :canonical: autodoc2.analysis._get_parent_name

   Get the parent name of a node.

.. py:function:: clean_docstring(s: None | str, tabsize: int = 8) -> str
   :canonical: autodoc2.analysis.clean_docstring

   Remove common leading indentation,
   where the indentation of the first line is ignored.


.. py:function:: walk_node(node: astroid.nodes.NodeNG, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.walk_node

.. py:function:: yield_module(node: astroid.nodes.Module, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_module

.. py:function:: yield_annotation_assign(node: astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_annotation_assign

   Yield data for an annotation assignment node.

.. py:function:: yield_assign(node: astroid.nodes.Assign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_assign

   Yield data for an assignment node.

.. py:function:: _yield_assign(node: astroid.nodes.Assign | astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis._yield_assign

   Yield data for an assignment node.

.. py:function:: yield_function_def(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_function_def

   Yield data for a function definition node.

.. py:function:: yield_class_def(node: astroid.nodes.ClassDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_class_def

   Yield data for a class definition node.

.. py:data:: _FUNC_MAPPER
   :canonical: autodoc2.analysis._FUNC_MAPPER
   :type: dict[astroid.nodes.NodeNG, typing.Callable[[astroid.nodes.NodeNG, autodoc2.analysis.State], typing.Iterable[autodoc2.utils.ItemData]]]
   :value: None
