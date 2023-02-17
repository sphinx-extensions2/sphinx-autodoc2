:py:mod:`autodoc2.utils`
========================

.. py:module:: autodoc2.utils


Description
-----------

Utility functions and types.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ItemData <autodoc2.utils.ItemData>`
     - A data item, for the results of the analysis.
   * - :py:obj:`WarningSubtypes <autodoc2.utils.WarningSubtypes>`
     - The subtypes of warnings for the extension.
   * - :py:obj:`ResolvedDict <autodoc2.utils.ResolvedDict>`
     - The outcome of resolving a packages's __all__ attributes.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`yield_modules <autodoc2.utils.yield_modules>`
     - Walk the given folder and yield all required modules.
   * - :py:obj:`resolve_all <autodoc2.utils.resolve_all>`
     - Give a module name, yield all names that would be imported by star.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PROPERTY_TYPE <autodoc2.utils.PROPERTY_TYPE>`
     - 
   * - :py:obj:`ARGS_TYPE <autodoc2.utils.ARGS_TYPE>`
     - 

API
~~~

.. py:data:: PROPERTY_TYPE
   :canonical: autodoc2.utils.PROPERTY_TYPE
   :value: None

.. py:data:: ARGS_TYPE
   :canonical: autodoc2.utils.ARGS_TYPE
   :value: None

.. py:class:: ItemData()
   :canonical: autodoc2.utils.ItemData

   Bases: :py:obj:`typing.TypedDict`

   A data item, for the results of the analysis.

   .. py:attribute:: type
      :canonical: autodoc2.utils.ItemData.type
      :type: typing_extensions.Required[str]
      :value: None

   .. py:attribute:: full_name
      :canonical: autodoc2.utils.ItemData.full_name
      :type: typing_extensions.Required[str]
      :value: None

   .. py:attribute:: doc
      :canonical: autodoc2.utils.ItemData.doc
      :type: typing_extensions.Required[str]
      :value: None

   .. py:attribute:: range
      :canonical: autodoc2.utils.ItemData.range
      :type: tuple[int, int]
      :value: None

   .. py:attribute:: file_path
      :canonical: autodoc2.utils.ItemData.file_path
      :type: None | str
      :value: None

   .. py:attribute:: encoding
      :canonical: autodoc2.utils.ItemData.encoding
      :type: str
      :value: None

   .. py:attribute:: all
      :canonical: autodoc2.utils.ItemData.all
      :type: None | list[str]
      :value: None

   .. py:attribute:: imports
      :canonical: autodoc2.utils.ItemData.imports
      :type: list[tuple[str, str | None]]
      :value: None

   .. py:attribute:: value
      :canonical: autodoc2.utils.ItemData.value
      :type: None | str | typing.Any
      :value: None

   .. py:attribute:: annotation
      :canonical: autodoc2.utils.ItemData.annotation
      :type: None | str
      :value: None

   .. py:attribute:: properties
      :canonical: autodoc2.utils.ItemData.properties
      :type: list[autodoc2.utils.PROPERTY_TYPE]
      :value: None

   .. py:attribute:: args
      :canonical: autodoc2.utils.ItemData.args
      :type: autodoc2.utils.ARGS_TYPE
      :value: None

   .. py:attribute:: return_annotation
      :canonical: autodoc2.utils.ItemData.return_annotation
      :type: None | str
      :value: None

   .. py:attribute:: bases
      :canonical: autodoc2.utils.ItemData.bases
      :type: list[str]
      :value: None

   .. py:attribute:: inherited
      :canonical: autodoc2.utils.ItemData.inherited
      :type: bool
      :value: None

.. py:class:: WarningSubtypes
   :canonical: autodoc2.utils.WarningSubtypes

   Bases: :py:obj:`enum.Enum`

   The subtypes of warnings for the extension.

   .. py:attribute:: CONFIG_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.CONFIG_ERROR
      :value: 'config_error'

      Issue with configuration validation.

   .. py:attribute:: GIT_CLONE_FAILED
      :canonical: autodoc2.utils.WarningSubtypes.GIT_CLONE_FAILED
      :value: 'git_clone'

      Failed to clone a git repository.

   .. py:attribute:: MISSING_MODULE
      :canonical: autodoc2.utils.WarningSubtypes.MISSING_MODULE
      :value: 'missing_module'

      If the package file/folder does not exist.

   .. py:attribute:: DUPLICATE_ITEM
      :canonical: autodoc2.utils.WarningSubtypes.DUPLICATE_ITEM
      :value: 'dup_item'

      Duplicate fully qualified name found during package analysis.

   .. py:attribute:: RENDER_ERROR
      :canonical: autodoc2.utils.WarningSubtypes.RENDER_ERROR
      :value: 'render'

      Generic rendering error.

   .. py:attribute:: ALL_MISSING
      :canonical: autodoc2.utils.WarningSubtypes.ALL_MISSING
      :value: 'all_missing'

      __all__ attribute missing or empty in a module.

   .. py:attribute:: ALL_RESOLUTION
      :canonical: autodoc2.utils.WarningSubtypes.ALL_RESOLUTION
      :value: 'all_resolve'

      Issue with resolution of an item in a module's __all__ attribute.

.. py:function:: yield_modules(folder: str | pathlib.Path, *, root_module: str | None = None, extensions: typing.Sequence[str] = ('.py', '.pyi'), exclude_dirs: typing.Sequence[str] = ('__pycache__', ), exclude_files: typing.Sequence[str] = ()) -> typing.Iterable[tuple[pathlib.Path, str]]
   :canonical: autodoc2.utils.yield_modules

   Walk the given folder and yield all required modules.

   :param folder: The path to walk.
   :param root_module: The name of the root module,
       otherwise the folder name is used.
   :param extensions: The extensions to include.
       If multiple files with the same stem,
       only the first extension will be used.
   :param exclude_dirs: Directory names to exclude (matched with fnmatch).
   :param exclude_files: File names to exclude (matched with fnmatch).


.. py:class:: ResolvedDict()
   :canonical: autodoc2.utils.ResolvedDict

   Bases: :py:obj:`typing.TypedDict`

   The outcome of resolving a packages's __all__ attributes.

   .. py:attribute:: resolved
      :canonical: autodoc2.utils.ResolvedDict.resolved
      :type: dict[str, set[str]]
      :value: None

      These are names in __all__ that we have successfully resolved,
      to one or more items.


   .. py:attribute:: unresolved
      :canonical: autodoc2.utils.ResolvedDict.unresolved
      :type: set[str]
      :value: None

      These are names in __all__ that we have not been able to resolve.

   .. py:attribute:: stars_unresolved
      :canonical: autodoc2.utils.ResolvedDict.stars_unresolved
      :type: set[str]
      :value: None

      These are star imports in the module, that we have not yet resolved.

   .. py:attribute:: stars_no_all
      :canonical: autodoc2.utils.ResolvedDict.stars_no_all
      :type: set[str]
      :value: None

      These are star imports in the module, that have no recognised __all__.
      At present we do not resolve them.


   .. py:attribute:: stars_unknown
      :canonical: autodoc2.utils.ResolvedDict.stars_unknown
      :type: set[str]
      :value: None

      These are star imports in the module, that we cannot resolve.
      Because they point to a module that is not in the database.


.. py:function:: resolve_all(db: autodoc2.db.Database, package_name: str) -> dict[str, autodoc2.utils.ResolvedDict]
   :canonical: autodoc2.utils.resolve_all

   Give a module name, yield all names that would be imported by star.
