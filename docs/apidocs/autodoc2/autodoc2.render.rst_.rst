:py:mod:`autodoc2.render.rst_`
==============================

.. py:module:: autodoc2.render.rst_

.. autodoc2-docstring:: autodoc2.render.rst_
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
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_RE_DELIMS <autodoc2.render.rst_._RE_DELIMS>`
     - .. autodoc2-docstring:: autodoc2.render.rst_._RE_DELIMS
          :summary:

API
~~~

.. py:data:: _RE_DELIMS
   :canonical: autodoc2.render.rst_._RE_DELIMS
   :value: None

   .. autodoc2-docstring:: autodoc2.render.rst_._RE_DELIMS

.. py:class:: RstRenderer(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
   :canonical: autodoc2.render.rst_.RstRenderer

   Bases: :py:obj:`autodoc2.render.base.RendererBase`

   .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.__init__

   .. py:attribute:: EXTENSION
      :canonical: autodoc2.render.rst_.RstRenderer.EXTENSION
      :value: '.rst'

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.EXTENSION

   .. py:method:: render_item(full_name: str) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_item

   .. py:method:: generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.generate_summary

   .. py:method:: render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_package

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_package

   .. py:method:: render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_module

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_module

   .. py:method:: render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_function

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_function

   .. py:method:: render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_exception

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_exception

   .. py:method:: render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_class

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_class

   .. py:method:: render_property(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_property

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_property

   .. py:method:: render_method(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_method

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_method

   .. py:method:: render_attribute(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_attribute

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_attribute

   .. py:method:: render_data(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
      :canonical: autodoc2.render.rst_.RstRenderer.render_data

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer.render_data

   .. py:method:: _reformat_cls_base_rst(value: str) -> str
      :canonical: autodoc2.render.rst_.RstRenderer._reformat_cls_base_rst

      .. autodoc2-docstring:: autodoc2.render.rst_.RstRenderer._reformat_cls_base_rst
