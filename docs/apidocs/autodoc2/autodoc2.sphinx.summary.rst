:py:mod:`autodoc2.sphinx.summary`
=================================

.. py:module:: autodoc2.sphinx.summary

.. autodoc2-docstring:: autodoc2.sphinx.summary
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AutodocSummary <autodoc2.sphinx.summary.AutodocSummary>`
     - .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary
          :summary:

API
~~~

.. py:class:: AutodocSummary(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
   :canonical: autodoc2.sphinx.summary.AutodocSummary

   Bases: :py:obj:`sphinx.util.docutils.SphinxDirective`

   .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.__init__

   .. py:attribute:: has_content
      :canonical: autodoc2.sphinx.summary.AutodocSummary.has_content
      :value: True

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.has_content

   .. py:attribute:: required_arguments
      :canonical: autodoc2.sphinx.summary.AutodocSummary.required_arguments
      :value: 0

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.required_arguments

   .. py:attribute:: optional_arguments
      :canonical: autodoc2.sphinx.summary.AutodocSummary.optional_arguments
      :value: 0

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.optional_arguments

   .. py:attribute:: final_argument_whitespace
      :canonical: autodoc2.sphinx.summary.AutodocSummary.final_argument_whitespace
      :value: False

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.final_argument_whitespace

   .. py:attribute:: option_spec
      :canonical: autodoc2.sphinx.summary.AutodocSummary.option_spec
      :type: typing.ClassVar[dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.option_spec

   .. py:method:: run() -> list[docutils.nodes.Node]
      :canonical: autodoc2.sphinx.summary.AutodocSummary.run

      .. autodoc2-docstring:: autodoc2.sphinx.summary.AutodocSummary.run
