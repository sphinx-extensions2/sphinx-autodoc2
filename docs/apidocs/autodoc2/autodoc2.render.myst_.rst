:py:mod:`autodoc2.render.myst_`
===============================

.. py:module:: autodoc2.render.myst_

.. autodoc2-docstring:: autodoc2.render.myst_
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`MystRenderer <autodoc2.render.myst_.MystRenderer>`
     - .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_RE_DELIMS <autodoc2.render.myst_._RE_DELIMS>`
     - .. autodoc2-docstring:: autodoc2.render.myst_._RE_DELIMS
          :summary:

API
~~~

.. py:data:: _RE_DELIMS
   :canonical: autodoc2.render.myst_._RE_DELIMS
   :value: None

   .. autodoc2-docstring:: autodoc2.render.myst_._RE_DELIMS

.. py:class:: MystRenderer(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
   :canonical: autodoc2.render.myst_.MystRenderer

   Bases: :py:obj:`autodoc2.render.base.RendererBase`

   .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.__init__

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.myst_.MystRenderer.EXTENSION
      :value: '.md'

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.EXTENSION

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_item

   .. py:method:: generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.generate_summary

   .. py:method:: enclosing_backticks(text: str) -> str
      :canonical: autodoc2.render.myst_.MystRenderer.enclosing_backticks
      :staticmethod:

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.enclosing_backticks

   .. py:method:: render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_package

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_package

   .. py:method:: render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_module

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_module

   .. py:method:: render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_function

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_function

   .. py:method:: render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_exception

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_exception

   .. py:method:: render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_class

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_class

   .. py:method:: render_property(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_property

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_property

   .. py:method:: render_method(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_method

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_method

   .. py:method:: render_attribute(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_attribute

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_attribute

   .. py:method:: render_data(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_data

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer.render_data

   .. py:method:: _reformat_cls_base_myst(value: str) -> str
      :canonical: autodoc2.render.myst_.MystRenderer._reformat_cls_base_myst

      .. autodoc2-docstring:: autodoc2.render.myst_.MystRenderer._reformat_cls_base_myst
