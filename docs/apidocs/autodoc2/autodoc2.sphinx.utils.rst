:py:mod:`autodoc2.sphinx.utils`
===============================

.. py:module:: autodoc2.sphinx.utils

.. autodoc2-docstring:: autodoc2.sphinx.utils
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`load_config <autodoc2.sphinx.utils.load_config>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.load_config
          :summary:
   * - :py:obj:`warn_sphinx <autodoc2.sphinx.utils.warn_sphinx>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.warn_sphinx
          :summary:
   * - :py:obj:`get_database <autodoc2.sphinx.utils.get_database>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.get_database
          :summary:
   * - :py:obj:`_warn <autodoc2.sphinx.utils._warn>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils._warn
          :summary:
   * - :py:obj:`get_all_analyser <autodoc2.sphinx.utils.get_all_analyser>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.get_all_analyser
          :summary:
   * - :py:obj:`nested_parse_generated <autodoc2.sphinx.utils.nested_parse_generated>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.nested_parse_generated
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`LOGGER <autodoc2.sphinx.utils.LOGGER>`
     - .. autodoc2-docstring:: autodoc2.sphinx.utils.LOGGER
          :summary:

API
~~~

.. py:data:: LOGGER
   :canonical: autodoc2.sphinx.utils.LOGGER
   :value: None

   .. autodoc2-docstring:: autodoc2.sphinx.utils.LOGGER

.. py:function:: load_config(app: sphinx.application.Sphinx, *, overrides: None | dict[str, typing.Any] = None, location: None | docutils.nodes.Element = None) -> autodoc2.config.Config
   :canonical: autodoc2.sphinx.utils.load_config

   .. autodoc2-docstring:: autodoc2.sphinx.utils.load_config

.. py:function:: warn_sphinx(msg: str, subtype: autodoc2.utils.WarningSubtypes, location: None | docutils.nodes.Element = None) -> None
   :canonical: autodoc2.sphinx.utils.warn_sphinx

   .. autodoc2-docstring:: autodoc2.sphinx.utils.warn_sphinx

.. py:function:: get_database(env: sphinx.environment.BuildEnvironment) -> autodoc2.db.Database
   :canonical: autodoc2.sphinx.utils.get_database

   .. autodoc2-docstring:: autodoc2.sphinx.utils.get_database

.. py:function:: _warn(msg: str) -> None
   :canonical: autodoc2.sphinx.utils._warn

   .. autodoc2-docstring:: autodoc2.sphinx.utils._warn

.. py:function:: get_all_analyser(env: sphinx.environment.BuildEnvironment) -> autodoc2.resolve_all.AllResolver
   :canonical: autodoc2.sphinx.utils.get_all_analyser

   .. autodoc2-docstring:: autodoc2.sphinx.utils.get_all_analyser

.. py:function:: nested_parse_generated(state: docutils.parsers.rst.states.RSTStateMachine, content: list[str], source: str, line: int, *, match_titles: bool = False, base: docutils.nodes.Element | None = None) -> docutils.nodes.Element
   :canonical: autodoc2.sphinx.utils.nested_parse_generated

   .. autodoc2-docstring:: autodoc2.sphinx.utils.nested_parse_generated
