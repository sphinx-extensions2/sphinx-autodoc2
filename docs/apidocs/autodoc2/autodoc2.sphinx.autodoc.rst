:py:mod:`autodoc2.sphinx.autodoc`
=================================

.. py:module:: autodoc2.sphinx.autodoc

.. autodoc2-docstring:: autodoc2.sphinx.autodoc
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AutodocObject <autodoc2.sphinx.autodoc.AutodocObject>`
     - .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_set_parents <autodoc2.sphinx.autodoc._set_parents>`
     - .. autodoc2-docstring:: autodoc2.sphinx.autodoc._set_parents
          :summary:

API
~~~

.. py:class:: AutodocObject(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
   :canonical: autodoc2.sphinx.autodoc.AutodocObject

   Bases: :py:obj:`sphinx.util.docutils.SphinxDirective`

   .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.__init__

   .. py:attribute:: required_arguments
      :canonical: autodoc2.sphinx.autodoc.AutodocObject.required_arguments
      :value: 1

      .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.required_arguments

   .. py:attribute:: final_argument_whitespace
      :canonical: autodoc2.sphinx.autodoc.AutodocObject.final_argument_whitespace
      :value: False

      .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.final_argument_whitespace

   .. py:attribute:: has_content
      :canonical: autodoc2.sphinx.autodoc.AutodocObject.has_content
      :value: True

      .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.has_content

   .. py:attribute:: option_spec
      :canonical: autodoc2.sphinx.autodoc.AutodocObject.option_spec
      :type: typing.ClassVar[dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.option_spec

   .. py:method:: run() -> list[docutils.nodes.Node]
      :canonical: autodoc2.sphinx.autodoc.AutodocObject.run

      .. autodoc2-docstring:: autodoc2.sphinx.autodoc.AutodocObject.run

.. py:function:: _set_parents(env: sphinx.environment.BuildEnvironment, mod: autodoc2.utils.ItemData, klass: autodoc2.utils.ItemData | None) -> typing.Generator[None, None, None]
   :canonical: autodoc2.sphinx.autodoc._set_parents

   .. autodoc2-docstring:: autodoc2.sphinx.autodoc._set_parents
