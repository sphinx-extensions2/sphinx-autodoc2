:py:mod:`autodoc2.render.base`
==============================

.. py:module:: autodoc2.render.base


Description
-----------

Convert the database items into documentation.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RendererBase <autodoc2.render.base.RendererBase>`
     - The base renderer.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`format_args <autodoc2.render.base.format_args>`
     - Format the arguments of a function or method.

API
~~~

.. py:class:: RendererBase(db: autodoc2.db.Database, config: autodoc2.config.RenderConfig, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, resolved_all: dict[str, autodoc2.utils.ResolvedDict] | None = None)
   :canonical: autodoc2.render.base.RendererBase

   Bases: :py:obj:`abc.ABC`

   The base renderer.

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.base.RendererBase.EXTENSION
      :type: typing.ClassVar[str]
      :value: '.txt'

      The extension for the output files.

   .. py:method:: __init__(db: autodoc2.db.Database, config: autodoc2.config.RenderConfig, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, resolved_all: dict[str, autodoc2.utils.ResolvedDict] | None = None) -> None
      :canonical: autodoc2.render.base.RendererBase.__init__

      Initialise the renderer.

   .. py:attribute:: _resolve_all_warned
      :canonical: autodoc2.render.base.RendererBase._resolve_all_warned
      :type: set[str]
      :value: None

      The full_names of modules that have already been warned about, regarding __all__ resolution

   .. py:attribute:: _is_hidden_cache
      :canonical: autodoc2.render.base.RendererBase._is_hidden_cache
      :type: collections.OrderedDict[str, bool]
      :value: None

      Cache for the is_hidden function: full_name -> bool.

   .. py:property:: config
      :canonical: autodoc2.render.base.RendererBase.config
      :type: autodoc2.config.RenderConfig

      The configuration.

   .. py:method:: warn(msg: str, type_: autodoc2.utils.WarningSubtypes = WarningSubtypes.RENDER_ERROR) -> None
      :canonical: autodoc2.render.base.RendererBase.warn

      Warn the user.

   .. py:method:: get_item(full_name: str) -> typing.Optional[autodoc2.utils.ItemData]
      :canonical: autodoc2.render.base.RendererBase.get_item

      Get an item from the database, by full_name.

   .. py:method:: get_children(item: autodoc2.utils.ItemData, types: None | set[str] = None, *, omit_hidden: bool = True) -> typing.Iterable[autodoc2.utils.ItemData]
      :canonical: autodoc2.render.base.RendererBase.get_children

      Get the children of this item, sorted according to the config.

      If module and full_name in module_all_regexes,
      it will use the __all__ list instead of the children.

      :param item: The item to get the children of.
      :param types: If given, only return items of these types.
      :param omit_hidden: If True, omit hidden items.


   .. py:method:: is_hidden(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_hidden

      Whether this object should be displayed in documentation.

      Based on configuration regarding:

      - does i match a hidden regex pattern
      - does it have documentation
      - is it a dunder, i.e. __name__
      - is it a private member, i.e. starts with _, but not a dunder
      - is it an inherited member of a class


   .. py:method:: is_module_deprecated(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.is_module_deprecated

      Whether this module is deprecated.

   .. py:method:: show_module_summary(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_module_summary

      Whether to show a summary for this module/package.

   .. py:method:: show_class_inheritance(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_class_inheritance

      Whether to show the inheritance for this class.

   .. py:method:: show_annotations(item: autodoc2.utils.ItemData) -> bool
      :canonical: autodoc2.render.base.RendererBase.show_annotations

      Whether to show type annotations.

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.base.RendererBase.render_item
      :abstractmethod:

      Yield the content for a single item.

.. py:function:: format_args(args_info: autodoc2.utils.ARGS_TYPE, include_annotations: bool = True, ignore_self: None | str = None) -> str
   :canonical: autodoc2.render.base.format_args

   Format the arguments of a function or method.
