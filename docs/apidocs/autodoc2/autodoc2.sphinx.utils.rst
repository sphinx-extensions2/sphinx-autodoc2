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
