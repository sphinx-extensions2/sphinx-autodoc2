:py:mod:`autodoc2.extension`
============================

.. py:module:: autodoc2.extension


Description
-----------

.. autodoc2-docstring:: autodoc2.extension
   :renderer: rst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EnvCache <autodoc2.extension.EnvCache>`
     - .. autodoc2-docstring:: autodoc2.extension.EnvCache
          :renderer: rst
          :summary:
   * - :py:obj:`DocstringRenderer <autodoc2.extension.DocstringRenderer>`
     - .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`warn <autodoc2.extension.warn>`
     - .. autodoc2-docstring:: autodoc2.extension.warn
          :renderer: rst
          :summary:
   * - :py:obj:`setup <autodoc2.extension.setup>`
     - .. autodoc2-docstring:: autodoc2.extension.setup
          :renderer: rst
          :summary:
   * - :py:obj:`run_autodoc <autodoc2.extension.run_autodoc>`
     - .. autodoc2-docstring:: autodoc2.extension.run_autodoc
          :renderer: rst
          :summary:
   * - :py:obj:`run_autodoc_package <autodoc2.extension.run_autodoc_package>`
     - .. autodoc2-docstring:: autodoc2.extension.run_autodoc_package
          :renderer: rst
          :summary:
   * - :py:obj:`get_git_clone <autodoc2.extension.get_git_clone>`
     - .. autodoc2-docstring:: autodoc2.extension.get_git_clone
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`LOGGER <autodoc2.extension.LOGGER>`
     - .. autodoc2-docstring:: autodoc2.extension.LOGGER
          :renderer: rst
          :summary:

API
~~~

.. py:data:: LOGGER
   :canonical: autodoc2.extension.LOGGER
   :value: None

   .. autodoc2-docstring:: autodoc2.extension.LOGGER
      :renderer: rst

.. py:function:: warn(msg: str, subtype: autodoc2.utils.WarningSubtypes) -> None
   :canonical: autodoc2.extension.warn

   .. autodoc2-docstring:: autodoc2.extension.warn
      :renderer: rst

.. py:function:: setup(app: sphinx.application.Sphinx) -> dict[str, str | bool]
   :canonical: autodoc2.extension.setup

   .. autodoc2-docstring:: autodoc2.extension.setup
      :renderer: rst

.. py:function:: run_autodoc(app: sphinx.application.Sphinx) -> None
   :canonical: autodoc2.extension.run_autodoc

   .. autodoc2-docstring:: autodoc2.extension.run_autodoc
      :renderer: rst

.. py:function:: run_autodoc_package(app: sphinx.application.Sphinx, config: autodoc2.config.Config, pkg_index: int) -> str | None
   :canonical: autodoc2.extension.run_autodoc_package

   .. autodoc2-docstring:: autodoc2.extension.run_autodoc_package
      :renderer: rst

.. py:function:: get_git_clone(app: sphinx.application.Sphinx, url: str, branch_tag: str, config: autodoc2.config.Config) -> None | pathlib.Path
   :canonical: autodoc2.extension.get_git_clone

   .. autodoc2-docstring:: autodoc2.extension.get_git_clone
      :renderer: rst

.. py:class:: EnvCache()
   :canonical: autodoc2.extension.EnvCache

   Bases: :py:obj:`typing.TypedDict`

   .. autodoc2-docstring:: autodoc2.extension.EnvCache
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.extension.EnvCache.__init__
      :renderer: rst

   .. py:attribute:: hash
      :canonical: autodoc2.extension.EnvCache.hash
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.extension.EnvCache.hash
         :renderer: rst

   .. py:attribute:: db
      :canonical: autodoc2.extension.EnvCache.db
      :type: autodoc2.db.InMemoryDb
      :value: None

      .. autodoc2-docstring:: autodoc2.extension.EnvCache.db
         :renderer: rst

.. py:class:: DocstringRenderer(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
   :canonical: autodoc2.extension.DocstringRenderer

   Bases: :py:obj:`sphinx.util.docutils.SphinxDirective`

   .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.__init__
      :renderer: rst

   .. py:attribute:: has_content
      :canonical: autodoc2.extension.DocstringRenderer.has_content
      :value: False

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.has_content
         :renderer: rst

   .. py:attribute:: required_arguments
      :canonical: autodoc2.extension.DocstringRenderer.required_arguments
      :value: 1

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.required_arguments
         :renderer: rst

   .. py:attribute:: optional_arguments
      :canonical: autodoc2.extension.DocstringRenderer.optional_arguments
      :value: 0

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.optional_arguments
         :renderer: rst

   .. py:attribute:: final_argument_whitespace
      :canonical: autodoc2.extension.DocstringRenderer.final_argument_whitespace
      :value: True

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.final_argument_whitespace
         :renderer: rst

   .. py:attribute:: option_spec
      :canonical: autodoc2.extension.DocstringRenderer.option_spec
      :value: None

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.option_spec
         :renderer: rst

   .. py:method:: run() -> list[docutils.nodes.Node]
      :canonical: autodoc2.extension.DocstringRenderer.run

      .. autodoc2-docstring:: autodoc2.extension.DocstringRenderer.run
         :renderer: rst
