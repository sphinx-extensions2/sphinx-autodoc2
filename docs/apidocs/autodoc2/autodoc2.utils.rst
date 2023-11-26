:py:mod:`autodoc2.utils`
========================

.. py:module:: autodoc2.utils

.. autodoc2-docstring:: autodoc2.utils
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
          :summary:
   * - :py:obj:`WarningSubtypes <autodoc2.utils.WarningSubtypes>`
     - .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`yield_modules <autodoc2.utils.yield_modules>`
     - .. autodoc2-docstring:: autodoc2.utils.yield_modules
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PROPERTY_TYPE <autodoc2.utils.PROPERTY_TYPE>`
     - .. autodoc2-docstring:: autodoc2.utils.PROPERTY_TYPE
          :summary:
   * - :py:obj:`ARGS_TYPE <autodoc2.utils.ARGS_TYPE>`
     - .. autodoc2-docstring:: autodoc2.utils.ARGS_TYPE
          :summary:

API
~~~

.. py:data:: PROPERTY_TYPE
   :canonical: autodoc2.utils.PROPERTY_TYPE
   :value: None

   .. autodoc2-docstring:: autodoc2.utils.PROPERTY_TYPE

.. py:data:: ARGS_TYPE
   :canonical: autodoc2.utils.ARGS_TYPE
   :value: None

   .. autodoc2-docstring:: autodoc2.utils.ARGS_TYPE

.. py:class:: ItemData()
   :canonical: autodoc2.utils.ItemData

   Bases: :py:obj:`typing.TypedDict`

   .. autodoc2-docstring:: autodoc2.utils.ItemData

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.utils.ItemData.__init__

   .. py:attribute:: type
      :canonical: autodoc2.utils.ItemData.type
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.type

   .. py:attribute:: full_name
      :canonical: autodoc2.utils.ItemData.full_name
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.full_name

   .. py:attribute:: doc
      :canonical: autodoc2.utils.ItemData.doc
      :type: typing_extensions.Required[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.doc

   .. py:attribute:: range
      :canonical: autodoc2.utils.ItemData.range
      :type: tuple[int, int]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.range

   .. py:attribute:: file_path
      :canonical: autodoc2.utils.ItemData.file_path
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.file_path

   .. py:attribute:: encoding
      :canonical: autodoc2.utils.ItemData.encoding
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.encoding

   .. py:attribute:: all
      :canonical: autodoc2.utils.ItemData.all
      :type: None | list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.all

   .. py:attribute:: imports
      :canonical: autodoc2.utils.ItemData.imports
      :type: list[tuple[str, str | None]]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.imports

   .. py:attribute:: value
      :canonical: autodoc2.utils.ItemData.value
      :type: None | str | typing.Any
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.value

   .. py:attribute:: annotation
      :canonical: autodoc2.utils.ItemData.annotation
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.annotation

   .. py:attribute:: properties
      :canonical: autodoc2.utils.ItemData.properties
      :type: list[autodoc2.utils.PROPERTY_TYPE]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.properties

   .. py:attribute:: args
      :canonical: autodoc2.utils.ItemData.args
      :type: autodoc2.utils.ARGS_TYPE
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.args

   .. py:attribute:: return_annotation
      :canonical: autodoc2.utils.ItemData.return_annotation
      :type: None | str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.return_annotation

   .. py:attribute:: bases
      :canonical: autodoc2.utils.ItemData.bases
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.bases

   .. py:attribute:: doc_inherited
      :canonical: autodoc2.utils.ItemData.doc_inherited
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.doc_inherited

   .. py:attribute:: inherited
      :canonical: autodoc2.utils.ItemData.inherited
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.utils.ItemData.inherited

.. py:class:: WarningSubtypes(*args, **kwds)
   :canonical: autodoc2.utils.WarningSubtypes

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.__init__

   .. py:attribute:: CONFIG_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.CONFIG_ERROR
      :value: 'config_error'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.CONFIG_ERROR

   .. py:attribute:: GIT_CLONE_FAILED
      :canonical: autodoc2.utils.WarningSubtypes.GIT_CLONE_FAILED
      :value: 'git_clone'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.GIT_CLONE_FAILED

   .. py:attribute:: MISSING_MODULE
      :canonical: autodoc2.utils.WarningSubtypes.MISSING_MODULE
      :value: 'missing_module'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.MISSING_MODULE

   .. py:attribute:: DUPLICATE_ITEM
      :canonical: autodoc2.utils.WarningSubtypes.DUPLICATE_ITEM
      :value: 'dup_item'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.DUPLICATE_ITEM

   .. py:attribute:: RENDER_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.RENDER_ERROR
      :value: 'render'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.RENDER_ERROR

   .. py:attribute:: ALL_MISSING
      :canonical: autodoc2.utils.WarningSubtypes.ALL_MISSING
      :value: 'all_missing'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.ALL_MISSING

   .. py:attribute:: ALL_RESOLUTION
      :canonical: autodoc2.utils.WarningSubtypes.ALL_RESOLUTION
      :value: 'all_resolve'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.ALL_RESOLUTION

   .. py:attribute:: NAME_NOT_FOUND
      :canonical: autodoc2.utils.WarningSubtypes.NAME_NOT_FOUND
      :value: 'missing'

      .. autodoc2-docstring:: autodoc2.utils.WarningSubtypes.NAME_NOT_FOUND

.. py:function:: yield_modules(folder: str | pathlib.Path, *, root_module: str | None = None, extensions: typing.Sequence[str] = ('.py', '.pyi'), exclude_dirs: typing.Sequence[str] = ('__pycache__', ), exclude_files: typing.Sequence[str] = ()) -> typing.Iterable[tuple[pathlib.Path, str]]
   :canonical: autodoc2.utils.yield_modules

   .. autodoc2-docstring:: autodoc2.utils.yield_modules
