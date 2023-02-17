:py:mod:`autodoc2`
==================

.. py:module:: autodoc2


Description
-----------

Analyse a python project and create documentation for it.

Subpackages
-----------

.. toctree::
   :titlesonly:
   :maxdepth: 3

   autodoc2.render

Submodules
----------

.. toctree::
   :titlesonly:
   :maxdepth: 1

   autodoc2.db
   autodoc2.config
   autodoc2.analysis
   autodoc2.cli
   autodoc2.utils
   autodoc2.extension
   autodoc2.astroid_utils

Package Contents
----------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`setup <autodoc2.setup>`
     - Entrypoint for sphinx.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__version__ <autodoc2.__version__>`
     - 

API
~~~

.. py:data:: __version__
   :canonical: autodoc2.__version__
   :value: '0.1.0'

.. py:function:: setup(app)
   :canonical: autodoc2.setup

   Entrypoint for sphinx.
