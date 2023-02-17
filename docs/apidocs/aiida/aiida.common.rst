:py:mod:`aiida.common`
======================

.. py:module:: aiida.common


Description
-----------

Common data structures, utility classes and functions

.. note:: Modules in this sub package have to run without a loaded database environment


Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AttributeDict <aiida.common.extendeddicts.AttributeDict>`
     - This class internally stores values in a dictionary, but exposes the keys also as attributes, i.e. asking for attrdict.key will return the value of attrdict['key'] and so on.
   * - :py:obj:`CalcInfo <aiida.common.datastructures.CalcInfo>`
     - This object will store the data returned by the calculation plugin and to be passed to the ExecManager.
   * - :py:obj:`CalcJobState <aiida.common.datastructures.CalcJobState>`
     - The sub state of a CalcJobNode while its Process is in an active state (i.e. Running or Waiting).
   * - :py:obj:`CodeInfo <aiida.common.datastructures.CodeInfo>`
     - This attribute-dictionary contains the information needed to execute a code. Possible attributes are:
   * - :py:obj:`CodeRunMode <aiida.common.datastructures.CodeRunMode>`
     - Enum to indicate the way the codes of a calculation should be run.
   * - :py:obj:`DefaultFieldsAttributeDict <aiida.common.extendeddicts.DefaultFieldsAttributeDict>`
     - A dictionary with access to the keys as attributes, and with an internal value storing the 'default' keys to be distinguished from extra fields.
   * - :py:obj:`FixedFieldsAttributeDict <aiida.common.extendeddicts.FixedFieldsAttributeDict>`
     - A dictionary with access to the keys as attributes, and with filtering of valid attributes. This is only the base class, without valid attributes; use a derived class to do the actual work. E.g.
   * - :py:obj:`GraphTraversalRules <aiida.common.links.GraphTraversalRules>`
     - Graph traversal rules when deleting or exporting nodes.
   * - :py:obj:`LinkType <aiida.common.links.LinkType>`
     - A simple enum of allowed link types.
   * - :py:obj:`ProgressReporterAbstract <aiida.common.progress_reporter.ProgressReporterAbstract>`
     - An abstract class for incrementing a progress reporter.
   * - :py:obj:`StashMode <aiida.common.datastructures.StashMode>`
     - Mode to use when stashing files from the working directory of a completed calculation job for safekeeping.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`create_callback <aiida.common.progress_reporter.create_callback>`
     - Create a callback function to update the progress reporter.
   * - :py:obj:`get_progress_reporter <aiida.common.progress_reporter.get_progress_reporter>`
     - Return the progress reporter
   * - :py:obj:`override_log_level <aiida.common.log.override_log_level>`
     - Temporarily adjust the log-level of logger.
   * - :py:obj:`set_progress_bar_tqdm <aiida.common.progress_reporter.set_progress_bar_tqdm>`
     - Set a `tqdm <https://github.com/tqdm/tqdm>`__ implementation of the progress reporter interface.
   * - :py:obj:`set_progress_reporter <aiida.common.progress_reporter.set_progress_reporter>`
     - Set the progress reporter implementation
   * - :py:obj:`validate_link_label <aiida.common.links.validate_link_label>`
     - Validate the given link label.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AIIDA_LOGGER <aiida.common.log.AIIDA_LOGGER>`
     - 
   * - :py:obj:`GraphTraversalRule <aiida.common.links.GraphTraversalRule>`
     - A namedtuple that defines a graph traversal rule.
   * - :py:obj:`TQDM_BAR_FORMAT <aiida.common.progress_reporter.TQDM_BAR_FORMAT>`
     - 

API
~~~

.. py:data:: AIIDA_LOGGER
   :canonical: aiida.common.log.AIIDA_LOGGER
   :value: None

.. py:exception:: AiidaException()
   :canonical: aiida.common.exceptions.AiidaException

   Bases: :py:obj:`Exception`

   Base class for all AiiDA exceptions.

   Each module will have its own subclass, inherited from this
   (e.g. ExecManagerException, TransportException, ...)


.. py:class:: AttributeDict(dictionary=None)
   :canonical: aiida.common.extendeddicts.AttributeDict

   Bases: :py:obj:`dict`

   This class internally stores values in a dictionary, but exposes
   the keys also as attributes, i.e. asking for attrdict.key
   will return the value of attrdict['key'] and so on.

   Raises an AttributeError if the key does not exist, when called as an attribute,
   while the usual KeyError if the key does not exist and the dictionary syntax is
   used.


   .. py:method:: __init__(dictionary=None)
      :canonical: aiida.common.extendeddicts.AttributeDict.__init__

      Recursively turn the `dict` and all its nested dictionaries into `AttributeDict` instance.

   .. py:method:: __repr__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__repr__

      Representation of the object.

   .. py:method:: __getattr__(attr)
      :canonical: aiida.common.extendeddicts.AttributeDict.__getattr__

      Read a key as an attribute.

      :raises AttributeError: if the attribute does not correspond to an existing key.


   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.AttributeDict.__setattr__

      Set a key as an attribute.

   .. py:method:: __delattr__(attr)
      :canonical: aiida.common.extendeddicts.AttributeDict.__delattr__

      Delete a key as an attribute.

      :raises AttributeError: if the attribute does not correspond to an existing key.


   .. py:method:: __deepcopy__(memo=None)
      :canonical: aiida.common.extendeddicts.AttributeDict.__deepcopy__

      Deep copy.

   .. py:method:: __getstate__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__getstate__

      Needed for pickling this class.

   .. py:method:: __setstate__(dictionary)
      :canonical: aiida.common.extendeddicts.AttributeDict.__setstate__

      Needed for pickling this class.

   .. py:method:: __dir__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__dir__

      Default dir() implementation.

.. py:class:: CalcInfo(dictionary=None)
   :canonical: aiida.common.datastructures.CalcInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   This object will store the data returned by the calculation plugin and to be
   passed to the ExecManager.

   In the following descriptions all paths have to be considered relative

   * retrieve_list: a list of strings or tuples that indicate files that are to be retrieved from the remote after the
       calculation has finished and stored in the ``retrieved_folder`` output node of type ``FolderData``. If the entry
       in the list is just a string, it is assumed to be the filepath on the remote and it will be copied to the base
       directory of the retrieved folder, where the name corresponds to the basename of the remote relative path. This
       means that any remote folder hierarchy is ignored entirely.

       Remote folder hierarchy can be (partially) maintained by using a tuple instead, with the following format

           (source, target, depth)

       The ``source`` and ``target`` elements are relative filepaths in the remote and retrieved folder. The contents
       of ``source`` (whether it is a file or folder) are copied in its entirety to the ``target`` subdirectory in the
       retrieved folder. If no subdirectory should be created, ``'.'`` should be specified for ``target``.

       The ``source`` filepaths support glob patterns ``*`` in case the exact name of the files that are to be
       retrieved are not know a priori.

       The ``depth`` element can be used to control what level of nesting of the source folder hierarchy should be
       maintained. If ``depth`` equals ``0`` or ``1`` (they are equivalent), only the basename of the ``source``
       filepath is kept. For each additional level, another subdirectory of the remote hierarchy is kept. For example:

           ('path/sub/file.txt', '.', 2)

       will retrieve the ``file.txt`` and store it under the path:

           sub/file.txt

   * retrieve_temporary_list: a list of strings or tuples that indicate files that will be retrieved
       and stored temporarily in a FolderData, that will be available only during the parsing call.
       The format of the list is the same as that of 'retrieve_list'

   * local_copy_list: a list of tuples with format ('node_uuid', 'filename', relativedestpath')
   * remote_copy_list: a list of tuples with format ('remotemachinename', 'remoteabspath', 'relativedestpath')
   * remote_symlink_list: a list of tuples with format ('remotemachinename', 'remoteabspath', 'relativedestpath')
   * provenance_exclude_list: a sequence of relative paths of files in the sandbox folder of a `CalcJob` instance that
       should not be stored permanantly in the repository folder of the corresponding `CalcJobNode` that will be
       created, but should only be copied to the remote working directory on the target computer. This is useful for
       input files that should be copied to the working directory but should not be copied as well to the repository
       either, for example, because they contain proprietary information or because they are big and their content is
       already indirectly present in the repository through one of the data nodes passed as input to the calculation.
   * codes_info: a list of dictionaries used to pass the info of the execution of a code
   * codes_run_mode: the mode of execution in which the codes will be run (`CodeRunMode.SERIAL` by default,
       but can also be `CodeRunMode.PARALLEL`)
   * skip_submit: a flag that, when set to True, orders the engine to skip the submit/update steps (so no code will
       run, it will only upload the files and then retrieve/parse).


   .. py:attribute:: _default_fields
      :canonical: aiida.common.datastructures.CalcInfo._default_fields
      :value: ('job_environment', 'email', 'email_on_started', 'email_on_terminated', 'uuid', 'prepend_text', 'app...

.. py:class:: CalcJobState
   :canonical: aiida.common.datastructures.CalcJobState

   Bases: :py:obj:`enum.Enum`

   The sub state of a CalcJobNode while its Process is in an active state (i.e. Running or Waiting).

   .. py:attribute:: UPLOADING
      :canonical: aiida.common.datastructures.CalcJobState.UPLOADING
      :value: 'uploading'

   .. py:attribute:: SUBMITTING
      :canonical: aiida.common.datastructures.CalcJobState.SUBMITTING
      :value: 'submitting'

   .. py:attribute:: WITHSCHEDULER
      :canonical: aiida.common.datastructures.CalcJobState.WITHSCHEDULER
      :value: 'withscheduler'

   .. py:attribute:: STASHING
      :canonical: aiida.common.datastructures.CalcJobState.STASHING
      :value: 'stashing'

   .. py:attribute:: RETRIEVING
      :canonical: aiida.common.datastructures.CalcJobState.RETRIEVING
      :value: 'retrieving'

   .. py:attribute:: PARSING
      :canonical: aiida.common.datastructures.CalcJobState.PARSING
      :value: 'parsing'

.. py:exception:: ClosedStorage()
   :canonical: aiida.common.exceptions.ClosedStorage

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when trying to access data from a closed storage backend.

.. py:class:: CodeInfo(dictionary=None)
   :canonical: aiida.common.datastructures.CodeInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   This attribute-dictionary contains the information needed to execute a code.
   Possible attributes are:

   * ``cmdline_params``: a list of strings, containing parameters to be written on
     the command line right after the call to the code, as for example::

       code.x cmdline_params[0] cmdline_params[1] ... < stdin > stdout

   * ``stdin_name``: (optional) the name of the standard input file. Note, it is
     only possible to use the stdin with the syntax::

       code.x < stdin_name

     If no stdin_name is specified, the string "< stdin_name" will not be
     passed to the code.
     Note: it is not possible to substitute/remove the '<' if stdin_name is specified;
     if that is needed, avoid stdin_name and use instead the cmdline_params to
     specify a suitable syntax.
   * ``stdout_name``: (optional) the name of the standard output file. Note, it is
     only possible to pass output to stdout_name with the syntax::

       code.x ... > stdout_name

     If no stdout_name is specified, the string "> stdout_name" will not be
     passed to the code.
     Note: it is not possible to substitute/remove the '>' if stdout_name is specified;
     if that is needed, avoid stdout_name and use instead the cmdline_params to
     specify a suitable syntax.
   * ``stderr_name``: (optional) a string, the name of the error file of the code.
   * ``join_files``: (optional) if True, redirects the error to the output file.
     If join_files=True, the code will be called as::

       code.x ... > stdout_name 2>&1

     otherwise, if join_files=False and stderr is passed::

       code.x ... > stdout_name 2> stderr_name

   * ``withmpi``: if True, executes the code with mpirun (or another MPI installed
     on the remote computer)
   * ``code_uuid``: the uuid of the code associated to the CodeInfo


   .. py:attribute:: _default_fields
      :canonical: aiida.common.datastructures.CodeInfo._default_fields
      :value: ('cmdline_params', 'stdin_name', 'stdout_name', 'stderr_name', 'join_files', 'withmpi', 'code_uuid')

.. py:class:: CodeRunMode()
   :canonical: aiida.common.datastructures.CodeRunMode

   Bases: :py:obj:`enum.IntEnum`

   Enum to indicate the way the codes of a calculation should be run.

   For PARALLEL, the codes for a given calculation will be run in parallel by running them in the background::

       code1.x &
       code2.x &

   For the SERIAL option, codes will be executed sequentially by running for example the following::

       code1.x
       code2.x


   .. py:attribute:: SERIAL
      :canonical: aiida.common.datastructures.CodeRunMode.SERIAL
      :value: 0

   .. py:attribute:: PARALLEL
      :canonical: aiida.common.datastructures.CodeRunMode.PARALLEL
      :value: 1

.. py:exception:: ConfigurationError()
   :canonical: aiida.common.exceptions.ConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Error raised when there is a configuration error in AiiDA.


.. py:exception:: ConfigurationVersionError()
   :canonical: aiida.common.exceptions.ConfigurationVersionError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   Configuration error raised when the configuration file version is not
   compatible with the current version.


.. py:exception:: ContentNotExistent()
   :canonical: aiida.common.exceptions.ContentNotExistent

   Bases: :py:obj:`aiida.common.exceptions.NotExistent`

   Raised when trying to access an attribute, a key or a file in the result
   nodes that is not present


.. py:exception:: CorruptStorage()
   :canonical: aiida.common.exceptions.CorruptStorage

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   Raised when the storage is not found to be internally consistent on validation.

.. py:exception:: DbContentError()
   :canonical: aiida.common.exceptions.DbContentError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when the content of the DB is not valid.
   This should never happen if the user does not play directly
   with the DB.


.. py:class:: DefaultFieldsAttributeDict(dictionary=None)
   :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   A dictionary with access to the keys as attributes, and with an
   internal value storing the 'default' keys to be distinguished
   from extra fields.

   Extra methods defaultkeys() and extrakeys() divide the set returned by
   keys() in default keys (i.e. those defined at definition time)
   and other keys.
   There is also a method get_default_fields() to return the internal list.

   Moreover, for undefined default keys, it returns None instead of raising a
   KeyError/AttributeError exception.

   Remember to define the _default_fields in a subclass!
   E.g.::

       class TestExample(DefaultFieldsAttributeDict):
           _default_fields = ('a','b','c')

   When the validate() method is called, it calls in turn all validate_KEY
   methods, where KEY is one of the default keys.
   If the method is not present, the field is considered to be always valid.
   Each validate_KEY method should accept a single argument 'value' that will
   contain the value to be checked.

   It raises a ValidationError if any of the validate_KEY
   function raises an exception, otherwise it simply returns.
   NOTE: the `validate_*` functions are called also for unset fields, so if the
   field can be empty on validation, you have to start your validation
   function with something similar to::

       if value is None:
           return

   .. todo::
       Decide behavior if I set to None a field.
       Current behavior, if
       ``a`` is an instance and 'def_field' one of the default fields, that is
       undefined, we get:

       * ``a.get('def_field')``: None
       * ``a.get('def_field','whatever')``: 'whatever'
       * Note that ``a.defaultkeys()`` does NOT contain 'def_field'

       if we do ``a.def_field = None``, then the behavior becomes

       * ``a.get('def_field')``: None
       * ``a.get('def_field','whatever')``: None
       * Note that ``a.defaultkeys()`` DOES contain 'def_field'

       See if we want that setting a default field to None means deleting it.


   .. py:attribute:: _default_fields
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict._default_fields
      :value: None

   .. py:method:: validate()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.validate

      Validate the keys, if any ``validate_*`` method is available.


   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__setattr__

      Overridden to allow direct access to fields with underscore.


   .. py:method:: __getitem__(key)
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__getitem__

      Return None instead of raising an exception if the key does not exist
      but is in the list of default fields.


   .. py:method:: get_default_fields()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.get_default_fields
      :classmethod:

      Return the list of default fields, either defined in the instance or not.


   .. py:method:: defaultkeys()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.defaultkeys

      Return the default keys defined in the instance.


   .. py:method:: extrakeys()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.extrakeys

      Return the extra keys defined in the instance.


.. py:exception:: EntryPointError()
   :canonical: aiida.common.exceptions.EntryPointError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when an entry point cannot be uniquely resolved and imported.

.. py:exception:: FailedError()
   :canonical: aiida.common.exceptions.FailedError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when accessing a calculation that is in the FAILED status


.. py:exception:: FeatureDisabled()
   :canonical: aiida.common.exceptions.FeatureDisabled

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when a feature is requested, but the user has chosen to disable
   it (e.g., for submissions on disabled computers).


.. py:exception:: FeatureNotAvailable()
   :canonical: aiida.common.exceptions.FeatureNotAvailable

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when a feature is requested from a plugin, that is not available.


.. py:class:: FixedFieldsAttributeDict(init=None)
   :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   A dictionary with access to the keys as attributes, and with filtering
   of valid attributes.
   This is only the base class, without valid attributes;
   use a derived class to do the actual work.
   E.g.::

       class TestExample(FixedFieldsAttributeDict):
           _valid_fields = ('a','b','c')


   .. py:attribute:: _valid_fields
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict._valid_fields
      :value: None

   .. py:method:: __init__(init=None)
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__init__

      Recursively turn the `dict` and all its nested dictionaries into `AttributeDict` instance.

   .. py:method:: __setitem__(item, value)
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setitem__

      Set a key as an attribute.


   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setattr__

      Overridden to allow direct access to fields with underscore.


   .. py:method:: get_valid_fields()
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.get_valid_fields
      :classmethod:

      Return the list of valid fields.


   .. py:method:: __dir__()
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__dir__

      Default dir() implementation.

.. py:data:: GraphTraversalRule
   :canonical: aiida.common.links.GraphTraversalRule
   :value: None

   A namedtuple that defines a graph traversal rule.

   When starting from a certain sub set of nodes, the graph traversal rules specify which links should be followed to
   add adjacent nodes to finally arrive at a set of nodes that represent a valid and consistent sub graph.

   :param link_type: the `LinkType` that the rule applies to
   :param direction: whether the link type should be followed backwards or forwards
   :param toggleable: boolean to indicate whether the rule can be changed from the default value. If this is `False` it
       means the default value can never be changed as it will result in an inconsistent graph.
   :param default: boolean, the default value of the rule, if `True` means that the link type for the given direction
       should be followed.

.. py:class:: GraphTraversalRules
   :canonical: aiida.common.links.GraphTraversalRules

   Bases: :py:obj:`enum.Enum`

   Graph traversal rules when deleting or exporting nodes.

   .. py:attribute:: DEFAULT
      :canonical: aiida.common.links.GraphTraversalRules.DEFAULT
      :value: None

   .. py:attribute:: DELETE
      :canonical: aiida.common.links.GraphTraversalRules.DELETE
      :value: None

   .. py:attribute:: EXPORT
      :canonical: aiida.common.links.GraphTraversalRules.EXPORT
      :value: None

.. py:exception:: HashingError()
   :canonical: aiida.common.exceptions.HashingError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when an attempt to hash an object fails via a known failure mode


.. py:exception:: IncompatibleStorageSchema()
   :canonical: aiida.common.exceptions.IncompatibleStorageSchema

   Bases: :py:obj:`aiida.common.exceptions.IncompatibleDatabaseSchema`

   Raised when the storage schema is incompatible with that of the code.

.. py:exception:: InputValidationError()
   :canonical: aiida.common.exceptions.InputValidationError

   Bases: :py:obj:`aiida.common.exceptions.ValidationError`

   The input data for a calculation did not validate (e.g., missing
   required input data, wrong data, ...)


.. py:exception:: IntegrityError()
   :canonical: aiida.common.exceptions.IntegrityError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when there is an underlying data integrity error.  This can be database related
   or a general data integrity error.  This can happen if, e.g., a foreign key check fails.
   See PEP 249 for details.


.. py:exception:: InternalError()
   :canonical: aiida.common.exceptions.InternalError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Error raised when there is an internal error of AiiDA.


.. py:exception:: InvalidEntryPointTypeError()
   :canonical: aiida.common.exceptions.InvalidEntryPointTypeError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   Raised when a loaded entry point has a type that is not supported by the corresponding entry point group.

.. py:exception:: InvalidOperation()
   :canonical: aiida.common.exceptions.InvalidOperation

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   The allowed operation is not valid (e.g., when trying to add a non-internal attribute
   before saving the entry), or deleting an entry that is protected (e.g.,
   because it is referenced by foreign keys)


.. py:exception:: LicensingException()
   :canonical: aiida.common.exceptions.LicensingException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when requirements for data licensing are not met.


.. py:class:: LinkType
   :canonical: aiida.common.links.LinkType

   Bases: :py:obj:`enum.Enum`

   A simple enum of allowed link types.

   .. py:attribute:: CREATE
      :canonical: aiida.common.links.LinkType.CREATE
      :value: 'create'

   .. py:attribute:: RETURN
      :canonical: aiida.common.links.LinkType.RETURN
      :value: 'return'

   .. py:attribute:: INPUT_CALC
      :canonical: aiida.common.links.LinkType.INPUT_CALC
      :value: 'input_calc'

   .. py:attribute:: INPUT_WORK
      :canonical: aiida.common.links.LinkType.INPUT_WORK
      :value: 'input_work'

   .. py:attribute:: CALL_CALC
      :canonical: aiida.common.links.LinkType.CALL_CALC
      :value: 'call_calc'

   .. py:attribute:: CALL_WORK
      :canonical: aiida.common.links.LinkType.CALL_WORK
      :value: 'call_work'

.. py:exception:: LoadingEntryPointError()
   :canonical: aiida.common.exceptions.LoadingEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   Raised when the resource corresponding to requested entry point cannot be imported.

.. py:exception:: LockedProfileError()
   :canonical: aiida.common.exceptions.LockedProfileError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised if attempting to access a locked profile


.. py:exception:: LockingProfileError()
   :canonical: aiida.common.exceptions.LockingProfileError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised if the profile can`t be locked


.. py:exception:: MissingConfigurationError()
   :canonical: aiida.common.exceptions.MissingConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   Configuration error raised when the configuration file is missing.


.. py:exception:: MissingEntryPointError()
   :canonical: aiida.common.exceptions.MissingEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   Raised when the requested entry point is not registered with the entry point manager.

.. py:exception:: ModificationNotAllowed()
   :canonical: aiida.common.exceptions.ModificationNotAllowed

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when the user tries to modify a field, object, property, ... that should not
   be modified.


.. py:exception:: MultipleEntryPointError()
   :canonical: aiida.common.exceptions.MultipleEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   Raised when the requested entry point cannot uniquely be resolved by the entry point manager.

.. py:exception:: MultipleObjectsError()
   :canonical: aiida.common.exceptions.MultipleObjectsError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when more than one entity is found in the DB, but only one was
   expected.


.. py:exception:: NotExistent()
   :canonical: aiida.common.exceptions.NotExistent

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when the required entity does not exist.


.. py:exception:: NotExistentAttributeError()
   :canonical: aiida.common.exceptions.NotExistentAttributeError

   Bases: :py:obj:`AttributeError`, :py:obj:`aiida.common.exceptions.NotExistent`

   Raised when the required entity does not exist, when fetched as an attribute.


.. py:exception:: NotExistentKeyError()
   :canonical: aiida.common.exceptions.NotExistentKeyError

   Bases: :py:obj:`KeyError`, :py:obj:`aiida.common.exceptions.NotExistent`

   Raised when the required entity does not exist, when fetched as a dictionary key.


.. py:exception:: OutputParsingError()
   :canonical: aiida.common.exceptions.OutputParsingError

   Bases: :py:obj:`aiida.common.exceptions.ParsingError`

   Can be raised by a Parser when it fails to parse the output generated by a `CalcJob` process.


.. py:exception:: ParsingError()
   :canonical: aiida.common.exceptions.ParsingError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Generic error raised when there is a parsing error


.. py:exception:: PluginInternalError()
   :canonical: aiida.common.exceptions.PluginInternalError

   Bases: :py:obj:`aiida.common.exceptions.InternalError`

   Error raised when there is an internal error which is due to a plugin
   and not to the AiiDA infrastructure.


.. py:exception:: ProfileConfigurationError()
   :canonical: aiida.common.exceptions.ProfileConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   Configuration error raised when a wrong/inexistent profile is requested.


.. py:class:: ProgressReporterAbstract(*, total: int, desc: typing.Optional[str] = None, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.ProgressReporterAbstract

   An abstract class for incrementing a progress reporter.

   This class provides the base interface for any `ProgressReporter` class.

   Example Usage::

       with ProgressReporter(total=10, desc="A process:") as progress:
           for i in range(10):
               progress.set_description_str(f"A process: {i}")
               progress.update()



   .. py:method:: __init__(*, total: int, desc: typing.Optional[str] = None, **kwargs: typing.Any)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.__init__

      Initialise the progress reporting contextmanager.

      :param total: The number of expected iterations.
      :param desc: A description of the process



   .. py:property:: total
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.total
      :type: int

      Return the total iterations expected.

   .. py:property:: desc
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.desc
      :type: typing.Optional[str]

      Return the description of the process.

   .. py:property:: n
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.n
      :type: int

      Return the current iteration.

   .. py:method:: __enter__() -> aiida.common.progress_reporter.ProgressReporterAbstract
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.__enter__

      Enter the contextmanager.

   .. py:method:: __exit__(exctype: typing.Optional[typing.Type[BaseException]], excinst: typing.Optional[BaseException], exctb: typing.Optional[types.TracebackType])
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.__exit__

      Exit the contextmanager.

   .. py:method:: set_description_str(text: typing.Optional[str] = None, refresh: bool = True)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.set_description_str

      Set the text shown by the progress reporter.

      :param text: The text to show
      :param refresh: Force refresh of the progress reporter



   .. py:method:: update(n: int = 1)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.update

      Update the progress counter.

      :param n: Increment to add to the internal counter of iterations



   .. py:method:: reset(total: typing.Optional[int] = None)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.reset

      Resets current iterations to 0.

      :param total: If not None, update number of expected iterations.



.. py:exception:: RemoteOperationError()
   :canonical: aiida.common.exceptions.RemoteOperationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when an error in a remote operation occurs, as in a failed kill()
   of a scheduler job.


.. py:class:: StashMode
   :canonical: aiida.common.datastructures.StashMode

   Bases: :py:obj:`enum.Enum`

   Mode to use when stashing files from the working directory of a completed calculation job for safekeeping.

   .. py:attribute:: COPY
      :canonical: aiida.common.datastructures.StashMode.COPY
      :value: 'copy'

.. py:exception:: StorageMigrationError()
   :canonical: aiida.common.exceptions.StorageMigrationError

   Bases: :py:obj:`aiida.common.exceptions.DatabaseMigrationError`

   Raised if a critical error is encountered during a storage migration.

.. py:exception:: StoringNotAllowed()
   :canonical: aiida.common.exceptions.StoringNotAllowed

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when the user tries to store an unstorable node (e.g. a base Node class)


.. py:data:: TQDM_BAR_FORMAT
   :canonical: aiida.common.progress_reporter.TQDM_BAR_FORMAT
   :value: '{desc:40.40}{percentage:6.1f}%|{bar}| {n_fmt}/{total_fmt}'

.. py:exception:: TestsNotAllowedError()
   :canonical: aiida.common.exceptions.TestsNotAllowedError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when tests are required to be run/loaded, but we are not in a testing environment.

   This is to prevent data loss.


.. py:exception:: TransportTaskException()
   :canonical: aiida.common.exceptions.TransportTaskException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when a TransportTask, an task to be completed by the engine that requires transport, fails


.. py:exception:: UniquenessError()
   :canonical: aiida.common.exceptions.UniquenessError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when the user tries to violate a uniqueness constraint (on the
   DB, for instance).


.. py:exception:: UnsupportedSpeciesError()
   :canonical: aiida.common.exceptions.UnsupportedSpeciesError

   Bases: :py:obj:`ValueError`

   Raised when StructureData operations are fed species that are not supported by AiiDA such as Deuterium


.. py:exception:: ValidationError()
   :canonical: aiida.common.exceptions.ValidationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Error raised when there is an error during the validation phase
   of a property.


.. py:function:: create_callback(progress_reporter: aiida.common.progress_reporter.ProgressReporterAbstract) -> typing.Callable[[str, typing.Any], None]
   :canonical: aiida.common.progress_reporter.create_callback

   Create a callback function to update the progress reporter.

   :returns: a callback to report on the process, ``callback(action, value)``,
       with the following callback signatures:

       - ``callback('init', {'total': <int>, 'description': <str>})``,
           to reset the progress with a new total iterations and description
       - ``callback('update', <int>)``,
           to update the progress by a certain number of iterations



.. py:function:: get_progress_reporter() -> typing.Type[aiida.common.progress_reporter.ProgressReporterAbstract]
   :canonical: aiida.common.progress_reporter.get_progress_reporter

   Return the progress reporter

   Example Usage::

       with get_progress_reporter()(total=10, desc="A process:") as progress:
           for i in range(10):
               progress.set_description_str(f"A process: {i}")
               progress.update()



.. py:function:: override_log_level(level=logging.CRITICAL)
   :canonical: aiida.common.log.override_log_level

   Temporarily adjust the log-level of logger.

.. py:function:: set_progress_bar_tqdm(bar_format: typing.Optional[str] = TQDM_BAR_FORMAT, leave: typing.Optional[bool] = False, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.set_progress_bar_tqdm

   Set a `tqdm <https://github.com/tqdm/tqdm>`__ implementation of the progress reporter interface.

   See :func:`~aiida.common.progress_reporter.set_progress_reporter` for details.

   :param bar_format: Specify a custom bar string format.
   :param leave: If True, keeps all traces of the progressbar upon termination of iteration.
           If `None`, will leave only if `position` is `0`.
   :param kwargs: pass to the tqdm init



.. py:function:: set_progress_reporter(reporter: typing.Optional[typing.Type[aiida.common.progress_reporter.ProgressReporterAbstract]] = None, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.set_progress_reporter

   Set the progress reporter implementation

   :param reporter: A progress reporter for a process.  If None, reset to ``ProgressReporterNull``.

   :param kwargs: If present, set a partial function with these kwargs

   The reporter should be a context manager that implements the
   :func:`~aiida.common.progress_reporter.ProgressReporterAbstract` interface.

   Example Usage::

       set_progress_reporter(ProgressReporterNull)
       with get_progress_reporter()(total=10, desc="A process:") as progress:
           for i in range(10):
               progress.set_description_str(f"A process: {i}")
               progress.update()



.. py:function:: validate_link_label(link_label)
   :canonical: aiida.common.links.validate_link_label

   Validate the given link label.

   Valid link labels adhere to the following restrictions:

       * Has to be a valid python identifier
       * Can only contain alphanumeric characters and underscores
       * Can not start or end with an underscore

   :raises TypeError: if the link label is not a string type
   :raises ValueError: if the link label is invalid

