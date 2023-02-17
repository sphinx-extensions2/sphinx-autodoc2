:py:mod:`aiida`
===============

.. py:module:: aiida


Description
-----------

AiiDA is a flexible and scalable informatics' infrastructure to manage,
preserve, and disseminate the simulations, data, and workflows of
modern-day computational science.

Able to store the full provenance of each object, and based on a
tailored database built for efficient data mining of heterogeneous results,
AiiDA gives the user the ability to interact seamlessly with any number of
remote HPC resources and codes, thanks to its flexible plugin interface
and workflow engine for the automation of complex sequences of simulations.

More information at http://www.aiida.net

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
     - Return a distutils StrictVersion instance with the current distribution version
   * - :py:obj:`get_version <aiida.get_version>`
     - Return the current AiiDA distribution version
   * - :py:obj:`_get_raw_file_header <aiida._get_raw_file_header>`
     - Get the default header for source AiiDA source code files. Note: is not preceded by comment character.
   * - :py:obj:`get_file_header <aiida.get_file_header>`
     - Get the default header for source AiiDA source code files.
   * - :py:obj:`load_ipython_extension <aiida.load_ipython_extension>`
     - Load the AiiDA IPython extension, using ``%load_ext aiida``.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__copyright__ <aiida.__copyright__>`
     - 
   * - :py:obj:`__license__ <aiida.__license__>`
     - 
   * - :py:obj:`__version__ <aiida.__version__>`
     - 
   * - :py:obj:`__authors__ <aiida.__authors__>`
     - 
   * - :py:obj:`__paper__ <aiida.__paper__>`
     - 
   * - :py:obj:`__paper_short__ <aiida.__paper_short__>`
     - 

API
~~~

.. py:data:: __copyright__
   :canonical: aiida.__copyright__
   :value: 'Copyright (c), This file is part of the AiiDA platform. For further information please visit http://...'

.. py:data:: __license__
   :canonical: aiida.__license__
   :value: 'MIT license, see LICENSE.txt file.'

.. py:data:: __version__
   :canonical: aiida.__version__
   :value: '2.2.2'

.. py:data:: __authors__
   :canonical: aiida.__authors__
   :value: 'The AiiDA team.'

.. py:data:: __paper__
   :canonical: aiida.__paper__
   :value: 'S. P. Huber et al., "AiiDA 1.0, a scalable computational infrastructure for automated reproducible w...'

.. py:data:: __paper_short__
   :canonical: aiida.__paper_short__
   :value: 'S. P. Huber et al., Scientific Data 7, 300 (2020).'

.. py:function:: get_strict_version()
   :canonical: aiida.get_strict_version

   Return a distutils StrictVersion instance with the current distribution version

   :returns: StrictVersion instance with the current version
   :rtype: :class:`!distutils.version.StrictVersion`


.. py:function:: get_version() -> str
   :canonical: aiida.get_version

   Return the current AiiDA distribution version

   :returns: the current version


.. py:function:: _get_raw_file_header() -> str
   :canonical: aiida._get_raw_file_header

   Get the default header for source AiiDA source code files.
   Note: is not preceded by comment character.

   :return: default AiiDA source file header


.. py:function:: get_file_header(comment_char: str = '# ') -> str
   :canonical: aiida.get_file_header

   Get the default header for source AiiDA source code files.

   .. note::

       Prepend by comment character.

   :param comment_char: string put in front of each line

   :return: default AiiDA source file header


.. py:function:: load_ipython_extension(ipython)
   :canonical: aiida.load_ipython_extension

   Load the AiiDA IPython extension, using ``%load_ext aiida``.
