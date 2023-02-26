:py:mod:`autodoc2.analysis`
===========================

.. py:module:: autodoc2.analysis

.. autodoc2-docstring:: autodoc2.analysis
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`State <autodoc2.analysis.State>`
     - .. autodoc2-docstring:: autodoc2.analysis.State
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`analyse_module <autodoc2.analysis.analyse_module>`
     - .. autodoc2-docstring:: autodoc2.analysis.analyse_module
          :summary:
   * - :py:obj:`_get_full_name <autodoc2.analysis._get_full_name>`
     - .. autodoc2-docstring:: autodoc2.analysis._get_full_name
          :summary:
   * - :py:obj:`_get_parent_name <autodoc2.analysis._get_parent_name>`
     - .. autodoc2-docstring:: autodoc2.analysis._get_parent_name
          :summary:
   * - :py:obj:`fix_docstring_indent <autodoc2.analysis.fix_docstring_indent>`
     - .. autodoc2-docstring:: autodoc2.analysis.fix_docstring_indent
          :summary:
   * - :py:obj:`walk_node <autodoc2.analysis.walk_node>`
     - .. autodoc2-docstring:: autodoc2.analysis.walk_node
          :summary:
   * - :py:obj:`yield_module <autodoc2.analysis.yield_module>`
     - .. autodoc2-docstring:: autodoc2.analysis.yield_module
          :summary:
   * - :py:obj:`yield_annotation_assign <autodoc2.analysis.yield_annotation_assign>`
     - .. autodoc2-docstring:: autodoc2.analysis.yield_annotation_assign
          :summary:
   * - :py:obj:`yield_assign <autodoc2.analysis.yield_assign>`
     - .. autodoc2-docstring:: autodoc2.analysis.yield_assign
          :summary:
   * - :py:obj:`_yield_assign <autodoc2.analysis._yield_assign>`
     - .. autodoc2-docstring:: autodoc2.analysis._yield_assign
          :summary:
   * - :py:obj:`yield_function_def <autodoc2.analysis.yield_function_def>`
     - .. autodoc2-docstring:: autodoc2.analysis.yield_function_def
          :summary:
   * - :py:obj:`yield_class_def <autodoc2.analysis.yield_class_def>`
     - .. autodoc2-docstring:: autodoc2.analysis.yield_class_def
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <autodoc2.analysis.__all__>`
     - .. autodoc2-docstring:: autodoc2.analysis.__all__
          :summary:
   * - :py:obj:`_dc_kwargs <autodoc2.analysis._dc_kwargs>`
     - .. autodoc2-docstring:: autodoc2.analysis._dc_kwargs
          :summary:
   * - :py:obj:`_FUNC_MAPPER <autodoc2.analysis._FUNC_MAPPER>`
     - .. autodoc2-docstring:: autodoc2.analysis._FUNC_MAPPER
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: autodoc2.analysis.__all__
   :value: ['analyse_module']

   .. autodoc2-docstring:: autodoc2.analysis.__all__

.. py:function:: analyse_module(file_path: pathlib.Path, name: str, exclude_external_imports: typing.Pattern[str] | None = None) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.analyse_module

   .. autodoc2-docstring:: autodoc2.analysis.analyse_module

.. py:data:: _dc_kwargs
   :canonical: autodoc2.analysis._dc_kwargs
   :type: dict[str, bool]
   :value: None

   .. autodoc2-docstring:: autodoc2.analysis._dc_kwargs

.. py:class:: State
   :canonical: autodoc2.analysis.State

   .. autodoc2-docstring:: autodoc2.analysis.State

   .. py:attribute:: package_name
      :canonical: autodoc2.analysis.State.package_name
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.analysis.State.package_name

   .. py:attribute:: name_stack
      :canonical: autodoc2.analysis.State.name_stack
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.analysis.State.name_stack

   .. py:attribute:: exclude_external_imports
      :canonical: autodoc2.analysis.State.exclude_external_imports
      :type: typing.Pattern[str] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.analysis.State.exclude_external_imports

   .. py:method:: copy(**kwargs: typing.Any) -> autodoc2.analysis.State
      :canonical: autodoc2.analysis.State.copy

      .. autodoc2-docstring:: autodoc2.analysis.State.copy

.. py:function:: _get_full_name(name: str, name_stack: list[str]) -> str
   :canonical: autodoc2.analysis._get_full_name

   .. autodoc2-docstring:: autodoc2.analysis._get_full_name

.. py:function:: _get_parent_name(name: str) -> str
   :canonical: autodoc2.analysis._get_parent_name

   .. autodoc2-docstring:: autodoc2.analysis._get_parent_name

.. py:function:: fix_docstring_indent(s: None | str, tabsize: int = 8) -> str
   :canonical: autodoc2.analysis.fix_docstring_indent

   .. autodoc2-docstring:: autodoc2.analysis.fix_docstring_indent

.. py:function:: walk_node(node: astroid.nodes.NodeNG, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.walk_node

   .. autodoc2-docstring:: autodoc2.analysis.walk_node

.. py:function:: yield_module(node: astroid.nodes.Module, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_module

   .. autodoc2-docstring:: autodoc2.analysis.yield_module

.. py:function:: yield_annotation_assign(node: astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_annotation_assign

   .. autodoc2-docstring:: autodoc2.analysis.yield_annotation_assign

.. py:function:: yield_assign(node: astroid.nodes.Assign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_assign

   .. autodoc2-docstring:: autodoc2.analysis.yield_assign

.. py:function:: _yield_assign(node: astroid.nodes.Assign | astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis._yield_assign

   .. autodoc2-docstring:: autodoc2.analysis._yield_assign

.. py:function:: yield_function_def(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_function_def

   .. autodoc2-docstring:: autodoc2.analysis.yield_function_def

.. py:function:: yield_class_def(node: astroid.nodes.ClassDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
   :canonical: autodoc2.analysis.yield_class_def

   .. autodoc2-docstring:: autodoc2.analysis.yield_class_def

.. py:data:: _FUNC_MAPPER
   :canonical: autodoc2.analysis._FUNC_MAPPER
   :type: dict[astroid.nodes.NodeNG, typing.Callable[[astroid.nodes.NodeNG, autodoc2.analysis.State], typing.Iterable[autodoc2.utils.ItemData]]]
   :value: None

   .. autodoc2-docstring:: autodoc2.analysis._FUNC_MAPPER
