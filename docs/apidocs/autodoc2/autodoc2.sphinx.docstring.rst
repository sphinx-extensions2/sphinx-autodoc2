:py:mod:`autodoc2.sphinx.docstring`
===================================

.. py:module:: autodoc2.sphinx.docstring

.. autodoc2-docstring:: autodoc2.sphinx.docstring
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DocstringRenderer <autodoc2.sphinx.docstring.DocstringRenderer>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`parser_options <autodoc2.sphinx.docstring.parser_options>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring.parser_options
          :summary:
   * - :py:obj:`summary_option <autodoc2.sphinx.docstring.summary_option>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring.summary_option
          :summary:
   * - :py:obj:`parsing_context <autodoc2.sphinx.docstring.parsing_context>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring.parsing_context
          :summary:
   * - :py:obj:`change_source <autodoc2.sphinx.docstring.change_source>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring.change_source
          :summary:
   * - :py:obj:`_example <autodoc2.sphinx.docstring._example>`
     - .. autodoc2-docstring:: autodoc2.sphinx.docstring._example
          :parser: myst
          :summary:

API
~~~

.. py:function:: parser_options(argument: str) -> docutils.parsers.Parser | None
   :canonical: autodoc2.sphinx.docstring.parser_options

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.parser_options

.. py:function:: summary_option(argument: str) -> int | None
   :canonical: autodoc2.sphinx.docstring.summary_option

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.summary_option

.. py:class:: DocstringRenderer(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
   :canonical: autodoc2.sphinx.docstring.DocstringRenderer

   Bases: :py:obj:`sphinx.util.docutils.SphinxDirective`

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.__init__

   .. py:attribute:: has_content
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.has_content
      :value: False

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.has_content

   .. py:attribute:: required_arguments
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.required_arguments
      :value: 1

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.required_arguments

   .. py:attribute:: optional_arguments
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.optional_arguments
      :value: 0

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.optional_arguments

   .. py:attribute:: final_argument_whitespace
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.final_argument_whitespace
      :value: True

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.final_argument_whitespace

   .. py:attribute:: option_spec
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.option_spec
      :type: typing.ClassVar[dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.option_spec

   .. py:method:: run() -> list[docutils.nodes.Node]
      :canonical: autodoc2.sphinx.docstring.DocstringRenderer.run

      .. autodoc2-docstring:: autodoc2.sphinx.docstring.DocstringRenderer.run

.. py:function:: parsing_context() -> typing.Generator[None, None, None]
   :canonical: autodoc2.sphinx.docstring.parsing_context

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.parsing_context

.. py:function:: change_source(state: docutils.parsers.rst.states.RSTStateMachine, source_path: str, line_offset: int) -> typing.Generator[None, None, None]
   :canonical: autodoc2.sphinx.docstring.change_source

   .. autodoc2-docstring:: autodoc2.sphinx.docstring.change_source

.. py:function:: _example(a: int, b: str) -> None
   :canonical: autodoc2.sphinx.docstring._example

   .. autodoc2-docstring:: autodoc2.sphinx.docstring._example
      :parser: myst
