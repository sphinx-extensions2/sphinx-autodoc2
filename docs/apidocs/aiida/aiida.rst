:py:mod:`aiida`
===============

.. py:module:: aiida

.. autodoc2-docstring:: aiida
   :allowtitles:

Subpackages
-----------

.. toctree::
   :titlesonly:
   :maxdepth: 3

   aiida.repository
   aiida.parsers
   aiida.tools
   aiida.plugins
   aiida.transports
   aiida.cmdline
   aiida.common
   aiida.manage
   aiida.orm
   aiida.engine
   aiida.schedulers

Package Contents
----------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`get_strict_version <aiida.get_strict_version>`
     - .. autodoc2-docstring:: aiida.get_strict_version
          :summary:
   * - :py:obj:`get_version <aiida.get_version>`
     - .. autodoc2-docstring:: aiida.get_version
          :summary:
   * - :py:obj:`_get_raw_file_header <aiida._get_raw_file_header>`
     - .. autodoc2-docstring:: aiida._get_raw_file_header
          :summary:
   * - :py:obj:`get_file_header <aiida.get_file_header>`
     - .. autodoc2-docstring:: aiida.get_file_header
          :summary:
   * - :py:obj:`load_ipython_extension <aiida.load_ipython_extension>`
     - .. autodoc2-docstring:: aiida.load_ipython_extension
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__copyright__ <aiida.__copyright__>`
     - .. autodoc2-docstring:: aiida.__copyright__
          :summary:
   * - :py:obj:`__license__ <aiida.__license__>`
     - .. autodoc2-docstring:: aiida.__license__
          :summary:
   * - :py:obj:`__version__ <aiida.__version__>`
     - .. autodoc2-docstring:: aiida.__version__
          :summary:
   * - :py:obj:`__authors__ <aiida.__authors__>`
     - .. autodoc2-docstring:: aiida.__authors__
          :summary:
   * - :py:obj:`__paper__ <aiida.__paper__>`
     - .. autodoc2-docstring:: aiida.__paper__
          :summary:
   * - :py:obj:`__paper_short__ <aiida.__paper_short__>`
     - .. autodoc2-docstring:: aiida.__paper_short__
          :summary:

API
~~~

.. py:data:: __copyright__
   :canonical: aiida.__copyright__
   :value: 'Copyright (c), This file is part of the AiiDA platform. For further information please visit http://...'

   .. autodoc2-docstring:: aiida.__copyright__

.. py:data:: __license__
   :canonical: aiida.__license__
   :value: 'MIT license, see LICENSE.txt file.'

   .. autodoc2-docstring:: aiida.__license__

.. py:data:: __version__
   :canonical: aiida.__version__
   :value: '2.2.2'

   .. autodoc2-docstring:: aiida.__version__

.. py:data:: __authors__
   :canonical: aiida.__authors__
   :value: 'The AiiDA team.'

   .. autodoc2-docstring:: aiida.__authors__

.. py:data:: __paper__
   :canonical: aiida.__paper__
   :value: 'S. P. Huber et al., "AiiDA 1.0, a scalable computational infrastructure for automated reproducible w...'

   .. autodoc2-docstring:: aiida.__paper__

.. py:data:: __paper_short__
   :canonical: aiida.__paper_short__
   :value: 'S. P. Huber et al., Scientific Data 7, 300 (2020).'

   .. autodoc2-docstring:: aiida.__paper_short__

.. py:function:: get_strict_version()
   :canonical: aiida.get_strict_version

   .. autodoc2-docstring:: aiida.get_strict_version

.. py:function:: get_version() -> str
   :canonical: aiida.get_version

   .. autodoc2-docstring:: aiida.get_version

.. py:function:: _get_raw_file_header() -> str
   :canonical: aiida._get_raw_file_header

   .. autodoc2-docstring:: aiida._get_raw_file_header

.. py:function:: get_file_header(comment_char: str = '# ') -> str
   :canonical: aiida.get_file_header

   .. autodoc2-docstring:: aiida.get_file_header

.. py:function:: load_ipython_extension(ipython)
   :canonical: aiida.load_ipython_extension

   .. autodoc2-docstring:: aiida.load_ipython_extension
