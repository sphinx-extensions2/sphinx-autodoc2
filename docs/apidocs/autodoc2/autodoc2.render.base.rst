:py:mod:`autodoc2.render.base`
==============================

.. py:module:: autodoc2.render.base

.. autodoc2-docstring:: autodoc2.render.base
   :renderer: rst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RendererBase <autodoc2.render.base.RendererBase>`
     - .. autodoc2-docstring:: autodoc2.render.base.RendererBase
          :renderer: rst
          :summary:

API
~~~

.. py:class:: RendererBase(db: autodoc2.db.Database, config: autodoc2.config.RenderConfig, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, resolved_all: dict[str, autodoc2.utils.ResolvedDict] | None = None)
   :canonical: autodoc2.render.base.RendererBase

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: autodoc2.render.base.RendererBase
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.render.base.RendererBase.__init__
      :renderer: rst

   .. py:attribute:: NAME
      :canonical: autodoc2.render.base.RendererBase.NAME
      :type: typing.ClassVar[str]
      :value: 'base'

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.NAME
         :renderer: rst

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.base.RendererBase.EXTENSION
      :type: typing.ClassVar[str]
      :value: '.txt'

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.EXTENSION
         :renderer: rst

   .. py:attribute:: _resolve_all_warned
      :canonical: autodoc2.render.base.RendererBase._resolve_all_warned
      :type: set[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase._resolve_all_warned
         :renderer: rst

   .. py:attribute:: _is_hidden_cache
      :canonical: autodoc2.render.base.RendererBase._is_hidden_cache
      :type: collections.OrderedDict[str, bool]
      :value: None

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase._is_hidden_cache
         :renderer: rst

   .. py:property:: config
      :canonical: autodoc2.render.base.RendererBase.config
      :type: autodoc2.config.RenderConfig

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.config
         :renderer: rst

   .. py:method:: warn(msg: str, type_: autodoc2.utils.WarningSubtypes = WarningSubtypes.RENDER_ERROR) -> None
      :canonical: autodoc2.render.base.RendererBase.warn

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.warn
         :renderer: rst

   .. py:method:: get_item(full_name: str) -> typing.Optional[autodoc2.utils.ItemData]
      :canonical: autodoc2.render.base.RendererBase.get_item

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.get_item
         :renderer: rst

   .. py:method:: get_children(item: autodoc2.utils.ItemData, types: None | set[str] = None, *, omit_hidden: bool = True) -> typing.Iterable[autodoc2.utils.ItemData]
      :canonical: autodoc2.render.base.RendererBase.get_children

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.get_children
         :renderer: rst

   .. py:method:: is_hidden(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_hidden

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.is_hidden
         :renderer: rst

   .. py:method:: is_module_deprecated(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_module_deprecated

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.is_module_deprecated
         :renderer: rst

   .. py:method:: no_index(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.no_index

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.no_index
         :renderer: rst

   .. py:method:: show_module_summary(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_module_summary

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_module_summary
         :renderer: rst

   .. py:method:: show_class_inheritance(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_class_inheritance

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_class_inheritance
         :renderer: rst

   .. py:method:: show_annotations(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_annotations

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_annotations
         :renderer: rst

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.base.RendererBase.render_item
      :abstractmethod:

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.render_item
         :renderer: rst

   .. py:method:: format_args(args_info: autodoc2.utils.ARGS_TYPE, include_annotations: bool = True, ignore_self: None | str = None) -> str
      :canonical: autodoc2.render.base.RendererBase.format_args

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_args
         :renderer: rst

   .. py:method:: format_annotation(annotation: None | str) -> str
      :canonical: autodoc2.render.base.RendererBase.format_annotation

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_annotation
         :renderer: rst

   .. py:method:: format_base(base: None | str) -> str
      :canonical: autodoc2.render.base.RendererBase.format_base

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_base
         :renderer: rst
