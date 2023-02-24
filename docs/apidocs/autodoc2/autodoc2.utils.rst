:py:mod:`autodoc2.utils`
========================

.. py:module:: autodoc2.utils


Description
-----------

.. autodoc2-docstring:: autodoc2.utils
   :renderer: rst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ItemData <autodoc2.utils.ItemData>`
     - .. autodoc2-docstring:: autodoc2.utils.ItemData
          :renderer: rst
          :summary:
   * - :py:obj:`WarningSubtypes <autodoc2.utils.WarningSubtypes>`
     - .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes
          :renderer: rst
          :summary:
   * - :py:obj:`ResolvedDict <autodoc2.utils.ResolvedDict>`
     - .. autodoc2-docstring:: autodoc2.utils.ResolvedDict
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`yield_modules <autodoc2.utils.yield_modules>`
     - .. autodoc2-docstring:: autodoc2.utils.yield_modules
          :renderer: rst
          :summary:
   * - :py:obj:`resolve_all <autodoc2.utils.resolve_all>`
     - .. autodoc2-docstring:: autodoc2.utils.resolve_all
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PROPERTY_TYPE <autodoc2.utils.PROPERTY_TYPE>`
     - .. autodoc2-docstring:: autodoc2.utils.PROPERTY_TYPE
          :renderer: rst
          :summary:
   * - :py:obj:`ARGS_TYPE <autodoc2.utils.ARGS_TYPE>`
     - .. autodoc2-docstring:: autodoc2.utils.ARGS_TYPE
          :renderer: rst
          :summary:

API
~~~

.. py:data:: PROPERTY_TYPE
   :canonical: autodoc2.utils.PROPERTY_TYPE
   :value: None

   .. autodoc2-docstring:: autodoc2.utils.PROPERTY_TYPE
      :renderer: rst

.. py:data:: ARGS_TYPE
   :canonical: autodoc2.utils.ARGS_TYPE
   :value: None

   .. autodoc2-docstring:: autodoc2.utils.ARGS_TYPE
      :renderer: rst

.. py:class:: ItemData()
   :canonical: autodoc2.utils.ItemData

   Bases: :py:obj:`typing.TypedDict`

   .. autodoc2-docstring:: autodoc2.utils.ItemData
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.utils.ItemData.__init__
      :renderer: rst

   .. py:attribute:: type
      :canonical: autodoc2.utils.ItemData.type
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.type
         :renderer: rst

   .. py:attribute:: full_name
      :canonical: autodoc2.utils.ItemData.full_name
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.full_name
         :renderer: rst

   .. py:attribute:: doc
      :canonical: autodoc2.utils.ItemData.doc
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.doc
         :renderer: rst

   .. py:attribute:: range
      :canonical: autodoc2.utils.ItemData.range
      :type: tuple[int, int]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.range
         :renderer: rst

   .. py:attribute:: file_path
      :canonical: autodoc2.utils.ItemData.file_path
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.file_path
         :renderer: rst

   .. py:attribute:: encoding
      :canonical: autodoc2.utils.ItemData.encoding
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.encoding
         :renderer: rst

   .. py:attribute:: all
      :canonical: autodoc2.utils.ItemData.all
      :type: None | list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.all
         :renderer: rst

   .. py:attribute:: imports
      :canonical: autodoc2.utils.ItemData.imports
      :type: list[tuple[str, str | None]]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.imports
         :renderer: rst

   .. py:attribute:: value
      :canonical: autodoc2.utils.ItemData.value
      :type: None | str | typing.Any
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.value
         :renderer: rst

   .. py:attribute:: annotation
      :canonical: autodoc2.utils.ItemData.annotation
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.annotation
         :renderer: rst

   .. py:attribute:: properties
      :canonical: autodoc2.utils.ItemData.properties
      :type: list[autodoc2.utils.PROPERTY_TYPE]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.properties
         :renderer: rst

   .. py:attribute:: args
      :canonical: autodoc2.utils.ItemData.args
      :type: autodoc2.utils.ARGS_TYPE
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.args
         :renderer: rst

   .. py:attribute:: return_annotation
      :canonical: autodoc2.utils.ItemData.return_annotation
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.return_annotation
         :renderer: rst

   .. py:attribute:: bases
      :canonical: autodoc2.utils.ItemData.bases
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.bases
         :renderer: rst

   .. py:attribute:: inherited
      :canonical: autodoc2.utils.ItemData.inherited
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.inherited
         :renderer: rst

.. py:class:: WarningSubtypes
   :canonical: autodoc2.utils.WarningSubtypes

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes
      :renderer: rst

   .. py:attribute:: CONFIG_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.CONFIG_ERROR
      :value: 'config_error'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.CONFIG_ERROR
         :renderer: rst

   .. py:attribute:: GIT_CLONE_FAILED
      :canonical: autodoc2.utils.WarningSubtypes.GIT_CLONE_FAILED
      :value: 'git_clone'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.GIT_CLONE_FAILED
         :renderer: rst

   .. py:attribute:: MISSING_MODULE
      :canonical: autodoc2.utils.WarningSubtypes.MISSING_MODULE
      :value: 'missing_module'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.MISSING_MODULE
         :renderer: rst

   .. py:attribute:: DUPLICATE_ITEM
      :canonical: autodoc2.utils.WarningSubtypes.DUPLICATE_ITEM
      :value: 'dup_item'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.DUPLICATE_ITEM
         :renderer: rst

   .. py:attribute:: RENDER_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.RENDER_ERROR
      :value: 'render'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.RENDER_ERROR
         :renderer: rst

   .. py:attribute:: ALL_MISSING
      :canonical: autodoc2.utils.WarningSubtypes.ALL_MISSING
      :value: 'all_missing'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.ALL_MISSING
         :renderer: rst

   .. py:attribute:: ALL_RESOLUTION
      :canonical: autodoc2.utils.WarningSubtypes.ALL_RESOLUTION
      :value: 'all_resolve'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.ALL_RESOLUTION
         :renderer: rst

   .. py:attribute:: DOCSTRING_NOT_FOUND
      :canonical: autodoc2.utils.WarningSubtypes.DOCSTRING_NOT_FOUND
      :value: 'docstring'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.DOCSTRING_NOT_FOUND
         :renderer: rst

.. py:function:: yield_modules(folder: str | pathlib.Path, *, root_module: str | None = None, extensions: typing.Sequence[str] = ('.py', '.pyi'), exclude_dirs: typing.Sequence[str] = ('__pycache__', ), exclude_files: typing.Sequence[str] = ()) -> typing.Iterable[tuple[pathlib.Path, str]]
   :canonical: autodoc2.utils.yield_modules

   .. autodoc2-docstring:: autodoc2.utils.yield_modules
      :renderer: rst

.. py:class:: ResolvedDict()
   :canonical: autodoc2.utils.ResolvedDict

   Bases: :py:obj:`typing.TypedDict`

   .. autodoc2-docstring:: autodoc2.utils.ResolvedDict
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.__init__
      :renderer: rst

   .. py:attribute:: resolved
      :canonical: autodoc2.utils.ResolvedDict.resolved
      :type: dict[str, set[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.resolved
         :renderer: rst

   .. py:attribute:: unresolved
      :canonical: autodoc2.utils.ResolvedDict.unresolved
      :type: set[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.unresolved
         :renderer: rst

   .. py:attribute:: stars_unresolved
      :canonical: autodoc2.utils.ResolvedDict.stars_unresolved
      :type: set[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.stars_unresolved
         :renderer: rst

   .. py:attribute:: stars_no_all
      :canonical: autodoc2.utils.ResolvedDict.stars_no_all
      :type: set[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.stars_no_all
         :renderer: rst

   .. py:attribute:: stars_unknown
      :canonical: autodoc2.utils.ResolvedDict.stars_unknown
      :type: set[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ResolvedDict.stars_unknown
         :renderer: rst

.. py:function:: resolve_all(db: autodoc2.db.Database, package_name: str) -> dict[str, autodoc2.utils.ResolvedDict]
   :canonical: autodoc2.utils.resolve_all

   .. autodoc2-docstring:: autodoc2.utils.resolve_all
      :renderer: rst
