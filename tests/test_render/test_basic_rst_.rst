:py:mod:`package`
=================

.. py:module:: package


Description
-----------

.. autodoc2-docstring:: package
   :renderer: rst
   :allowtitles:

Subpackages
-----------

.. toctree::
   :titlesonly:
   :maxdepth: 3

   package.a

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Class <package.Class>`
     - .. autodoc2-docstring:: package.Class
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`func <package.func>`
     - .. autodoc2-docstring:: package.func
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <package.__all__>`
     - .. autodoc2-docstring:: package.__all__
          :renderer: rst
          :summary:
   * - :py:obj:`p <package.p>`
     - .. autodoc2-docstring:: package.p
          :renderer: rst
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: package.__all__
   :value: ['p', 'a1', 'alias']

   .. autodoc2-docstring:: package.__all__
      :renderer: rst

.. py:data:: p
   :canonical: package.p
   :value: 1

   .. autodoc2-docstring:: package.p
      :renderer: rst

.. py:function:: func(a: str, b: int) -> package.a.c.ac1
   :canonical: package.func

   .. autodoc2-docstring:: package.func
      :renderer: rst

.. py:class:: Class
   :canonical: package.Class

   .. autodoc2-docstring:: package.Class
      :renderer: rst

   .. py:attribute:: x
      :canonical: package.Class.x
      :type: int
      :value: 1

      .. autodoc2-docstring:: package.Class.x
         :renderer: rst

   .. py:method:: method(a: str, b: int) -> ...
      :canonical: package.Class.method

      .. autodoc2-docstring:: package.Class.method
         :renderer: rst

   .. py:property:: prop
      :canonical: package.Class.prop
      :type: package.a.c.ac1 | None

      .. autodoc2-docstring:: package.Class.prop
         :renderer: rst

   .. py:class:: Nested
      :canonical: package.Class.Nested

      .. autodoc2-docstring:: package.Class.Nested
         :renderer: rst
