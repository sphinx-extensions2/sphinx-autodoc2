:py:mod:`autodoc2.render.myst_`
===============================

.. py:module:: autodoc2.render.myst_


Description
-----------

Renderer for MyST.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`MystRenderer <autodoc2.render.myst_.MystRenderer>`
     - Render the documentation as MyST.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_reformat_cls_base_myst <autodoc2.render.myst_._reformat_cls_base_myst>`
     - Reformat the base of a class for RST.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_MD_HEAD_RE <autodoc2.render.myst_._MD_HEAD_RE>`
     - 
   * - :py:obj:`_RE_DELIMS <autodoc2.render.myst_._RE_DELIMS>`
     - 

API
~~~

.. py:class:: MystRenderer(db: autodoc2.db.Database, config: autodoc2.config.RenderConfig, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, resolved_all: dict[str, autodoc2.utils.ResolvedDict] | None = None)
   :canonical: autodoc2.render.myst_.MystRenderer

   Bases: :py:obj:`autodoc2.render.base.RendererBase`

   Render the documentation as MyST.

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.myst_.MystRenderer.EXTENSION
      :value: '.md'

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_item

      Yield the content for a single item.

   .. py:method:: generate_summary(items: list[autodoc2.utils.ItemData]) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.generate_summary

      Generate a summary of the items.

   .. py:method:: enclosing_backticks(text: str) -> str
      :canonical: autodoc2.render.myst_.MystRenderer.enclosing_backticks
      :staticmethod:

      Ensure the enclosing backticks are more than any inner ones.

   .. py:method:: render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_package

      Create the content for a package.

   .. py:method:: render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_module

      Create the content for a module.

   .. py:method:: render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_function

      Create the content for a function.

   .. py:method:: render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_exception

      Create the content for an exception.

   .. py:method:: render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_class

      Create the content for a class.

   .. py:method:: render_property(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_property

      Create the content for a property.

   .. py:method:: render_method(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_method

      Create the content for a method.

   .. py:method:: render_attribute(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_attribute

      Create the content for an attribute.

   .. py:method:: render_data(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.myst_.MystRenderer.render_data

      Create the content for a data item.

.. py:data:: _MD_HEAD_RE
   :canonical: autodoc2.render.myst_._MD_HEAD_RE
   :value: None

.. py:data:: _RE_DELIMS
   :canonical: autodoc2.render.myst_._RE_DELIMS
   :value: None

.. py:function:: _reformat_cls_base_myst(value: str) -> str
   :canonical: autodoc2.render.myst_._reformat_cls_base_myst

   Reformat the base of a class for RST.

   Base annotations can come in the form::

       A[B, C, D]

   which we want to reformat as::

       {py:obj}`A`\[{py:obj}`B`, {py:obj}`C`, {py:obj}`D`\]


