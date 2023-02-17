:py:mod:`autodoc2.extension`
============================

.. py:module:: autodoc2.extension


Description
-----------

The sphinx extension for the package.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EnvCache <autodoc2.extension.EnvCache>`
     - Cache for the environment.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`warn <autodoc2.extension.warn>`
     - Log a warning.
   * - :py:obj:`setup <autodoc2.extension.setup>`
     - Entry point for sphinx.
   * - :py:obj:`run_autodoc <autodoc2.extension.run_autodoc>`
     - The primary sphinx call back event for sphinx.
   * - :py:obj:`run_autodoc_package <autodoc2.extension.run_autodoc_package>`
     - Run autodoc for a single package.
   * - :py:obj:`get_git_clone <autodoc2.extension.get_git_clone>`
     - Download a git repository to the given folder.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`LOGGER <autodoc2.extension.LOGGER>`
     - 

API
~~~

.. py:data:: LOGGER
   :canonical: autodoc2.extension.LOGGER
   :value: None

.. py:function:: warn(msg: str, subtype: autodoc2.utils.WarningSubtypes) -> None
   :canonical: autodoc2.extension.warn

   Log a warning.

.. py:function:: setup(app: sphinx.application.Sphinx) -> dict[str, str | bool]
   :canonical: autodoc2.extension.setup

   Entry point for sphinx.

.. py:function:: run_autodoc(app: sphinx.application.Sphinx) -> None
   :canonical: autodoc2.extension.run_autodoc

   The primary sphinx call back event for sphinx.

.. py:function:: run_autodoc_package(app: sphinx.application.Sphinx, config: autodoc2.config.Config, pkg_index: int) -> str | None
   :canonical: autodoc2.extension.run_autodoc_package

   Run autodoc for a single package.

   :return: The top level module name, relative to the api directory.


.. py:function:: get_git_clone(app: sphinx.application.Sphinx, url: str, branch_tag: str, config: autodoc2.config.Config) -> None | pathlib.Path
   :canonical: autodoc2.extension.get_git_clone

   Download a git repository to the given folder.

.. py:class:: EnvCache()
   :canonical: autodoc2.extension.EnvCache

   Bases: :py:obj:`typing.TypedDict`

   Cache for the environment.

   .. py:attribute:: hash
      :canonical: autodoc2.extension.EnvCache.hash
      :type: str
      :value: None

   .. py:attribute:: db
      :canonical: autodoc2.extension.EnvCache.db
      :type: autodoc2.db.InMemoryDb
      :value: None
