:py:mod:`autodoc2.render.base`
==============================

.. py:module:: autodoc2.render.base

.. autodoc2-docstring:: autodoc2.render.base
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
          :summary:

API
~~~

.. py:class:: RendererBase(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
   :canonical: autodoc2.render.base.RendererBase

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: autodoc2.render.base.RendererBase

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.render.base.RendererBase.__init__

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.base.RendererBase.EXTENSION
      :type: typing.ClassVar[str]
      :value: '.txt'

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.EXTENSION

   .. py:attribute:: _is_hidden_cache
      :canonical: autodoc2.render.base.RendererBase._is_hidden_cache
      :type: collections.OrderedDict[str, bool]
      :value: None

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase._is_hidden_cache

   .. py:property:: config
      :canonical: autodoc2.render.base.RendererBase.config
      :type: autodoc2.config.Config

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.config

   .. py:property:: standalone
      :canonical: autodoc2.render.base.RendererBase.standalone
      :type: bool

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.standalone

   .. py:method:: warn(msg: str, type_: autodoc2.utils.WarningSubtypes = WarningSubtypes.RENDER_ERROR) -> None
      :canonical: autodoc2.render.base.RendererBase.warn

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.warn

   .. py:method:: get_item(full_name: str) -> autodoc2.utils.ItemData | None
      :canonical: autodoc2.render.base.RendererBase.get_item

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.get_item

   .. py:method:: get_children(item: autodoc2.utils.ItemData, types: None | set[str] = None, *, omit_hidden: bool = True) -> typing.Iterable[autodoc2.utils.ItemData]
      :canonical: autodoc2.render.base.RendererBase.get_children

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.get_children

   .. py:method:: is_hidden(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_hidden

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.is_hidden

   .. py:method:: is_module_deprecated(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_module_deprecated

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.is_module_deprecated

   .. py:method:: no_index(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.no_index

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.no_index

   .. py:method:: show_module_summary(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_module_summary

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_module_summary

   .. py:method:: show_class_inheritance(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_class_inheritance

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_class_inheritance

   .. py:method:: show_annotations(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_annotations

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_annotations

   .. py:method:: show_docstring(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_docstring

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.show_docstring

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.base.RendererBase.render_item
      :abstractmethod:

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.render_item

   .. py:method:: format_args(args_info: autodoc2.utils.ARGS_TYPE, include_annotations: bool = True, ignore_self: None | str = None) -> str
      :canonical: autodoc2.render.base.RendererBase.format_args

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_args

   .. py:method:: format_annotation(annotation: None | str) -> str
      :canonical: autodoc2.render.base.RendererBase.format_annotation

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_annotation

   .. py:method:: format_base(base: None | str) -> str
      :canonical: autodoc2.render.base.RendererBase.format_base

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.format_base

   .. py:method:: get_doc_parser(full_name: str) -> str
      :canonical: autodoc2.render.base.RendererBase.get_doc_parser

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.get_doc_parser

   .. py:method:: generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
      :canonical: autodoc2.render.base.RendererBase.generate_summary
      :abstractmethod:

      .. autodoc2-docstring:: autodoc2.render.base.RendererBase.generate_summary
