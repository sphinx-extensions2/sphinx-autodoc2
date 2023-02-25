:py:mod:`autodoc2.sphinx.extension`
===================================

.. py:module:: autodoc2.sphinx.extension

.. autodoc2-docstring:: autodoc2.sphinx.extension
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EnvCache <autodoc2.sphinx.extension.EnvCache>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.EnvCache
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`setup <autodoc2.sphinx.extension.setup>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.setup
          :summary:
   * - :py:obj:`load_config <autodoc2.sphinx.extension.load_config>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.load_config
          :summary:
   * - :py:obj:`run_autodoc <autodoc2.sphinx.extension.run_autodoc>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.run_autodoc
          :summary:
   * - :py:obj:`run_autodoc_package <autodoc2.sphinx.extension.run_autodoc_package>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.run_autodoc_package
          :summary:
   * - :py:obj:`get_git_clone <autodoc2.sphinx.extension.get_git_clone>`
     - .. autodoc2-docstring:: autodoc2.sphinx.extension.get_git_clone
          :summary:

API
~~~

.. py:function:: setup(app: sphinx.application.Sphinx) -> dict[str, str | bool]
   :canonical: autodoc2.sphinx.extension.setup

   .. autodoc2-docstring:: autodoc2.sphinx.extension.setup
      :parser: 

.. py:function:: load_config(app: sphinx.application.Sphinx, *, overrides: None | dict[str, typing.Any] = None, location: None | docutils.nodes.Element = None) -> autodoc2.config.Config
   :canonical: autodoc2.sphinx.extension.load_config

   .. autodoc2-docstring:: autodoc2.sphinx.extension.load_config
      :parser: 

.. py:function:: run_autodoc(app: sphinx.application.Sphinx) -> None
   :canonical: autodoc2.sphinx.extension.run_autodoc

   .. autodoc2-docstring:: autodoc2.sphinx.extension.run_autodoc
      :parser: 

.. py:function:: run_autodoc_package(app: sphinx.application.Sphinx, config: autodoc2.config.Config, pkg_index: int) -> str | None
   :canonical: autodoc2.sphinx.extension.run_autodoc_package

   .. autodoc2-docstring:: autodoc2.sphinx.extension.run_autodoc_package
      :parser: 

.. py:function:: get_git_clone(app: sphinx.application.Sphinx, url: str, branch_tag: str, config: autodoc2.config.Config) -> None | pathlib.Path
   :canonical: autodoc2.sphinx.extension.get_git_clone

   .. autodoc2-docstring:: autodoc2.sphinx.extension.get_git_clone
      :parser: 

.. py:class:: EnvCache()
   :canonical: autodoc2.sphinx.extension.EnvCache

   Bases: :py:obj:`typing.TypedDict`

   .. autodoc2-docstring:: autodoc2.sphinx.extension.EnvCache

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.sphinx.extension.EnvCache.__init__

   .. py:attribute:: hash
      :canonical: autodoc2.sphinx.extension.EnvCache.hash
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.sphinx.extension.EnvCache.hash

   .. py:attribute:: db
      :canonical: autodoc2.sphinx.extension.EnvCache.db
      :type: autodoc2.db.InMemoryDb
      :value: None

      .. autodoc2-docstring:: autodoc2.sphinx.extension.EnvCache.db
