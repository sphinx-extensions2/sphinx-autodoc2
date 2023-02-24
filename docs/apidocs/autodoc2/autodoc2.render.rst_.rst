:py:mod:`autodoc2.render.rst_`
==============================

.. py:module:: autodoc2.render.rst_


Description
-----------

.. autodoc2-docstring:: autodoc2.render.rst_
   :renderer: rst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RstRenderer <autodoc2.render.rst_.RstRenderer>`
     - .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_RE_DELIMS <autodoc2.render.rst_._RE_DELIMS>`
     - .. autodoc2-docstring:: autodoc2.render.rst_._RE_DELIMS
          :renderer: rst
          :summary:

API
~~~

.. py:data:: _RE_DELIMS
   :canonical: autodoc2.render.rst_._RE_DELIMS
   :value: None

   .. autodoc2-docstring:: autodoc2.render.rst_._RE_DELIMS
      :renderer: rst

.. py:class:: RstRenderer(db: autodoc2.db.Database, config: autodoc2.config.RenderConfig, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, resolved_all: dict[str, autodoc2.utils.ResolvedDict] | None = None)
   :canonical: autodoc2.render.rst_.RstRenderer

   Bases: :py:obj:`autodoc2.render.base.RendererBase`

   .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.__init__
      :renderer: rst

   .. py:attribute:: NAME
      :canonical: autodoc2.render.rst_.RstRenderer.NAME
      :value: 'rst'

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.NAME
         :renderer: rst

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.rst_.RstRenderer.EXTENSION
      :value: '.rst'

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.EXTENSION
         :renderer: rst

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_item

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_item
         :renderer: rst

   .. py:method:: generate_summary(items: list[autodoc2.utils.ItemData]) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.generate_summary

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.generate_summary
         :renderer: rst

   .. py:method:: render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_package

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_package
         :renderer: rst

   .. py:method:: render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_module

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_module
         :renderer: rst

   .. py:method:: render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_function

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_function
         :renderer: rst

   .. py:method:: render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_exception

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_exception
         :renderer: rst

   .. py:method:: render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_class

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_class
         :renderer: rst

   .. py:method:: render_property(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_property

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_property
         :renderer: rst

   .. py:method:: render_method(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_method

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_method
         :renderer: rst

   .. py:method:: render_attribute(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_attribute

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_attribute
         :renderer: rst

   .. py:method:: render_data(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_data

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_data
         :renderer: rst

   .. py:method:: _reformat_cls_base_rst(value: str) -> str
      :canonical: autodoc2.render.rst_.RstRenderer._reformat_cls_base_rst

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer._reformat_cls_base_rst
         :renderer: rst
