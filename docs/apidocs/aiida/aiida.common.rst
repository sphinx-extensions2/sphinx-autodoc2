:py:mod:`aiida.common`
======================

.. py:module:: aiida.common


Description
-----------

.. autodoc2-docstring:: aiida.common
   :renderer: rst
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AttributeDict <aiida.common.extendeddicts.AttributeDict>`
     - .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict
          :renderer: rst
          :summary:
   * - :py:obj:`CalcInfo <aiida.common.datastructures.CalcInfo>`
     - .. autodoc2-docstring:: aiida.common.datastructures.CalcInfo
          :renderer: rst
          :summary:
   * - :py:obj:`CalcJobState <aiida.common.datastructures.CalcJobState>`
     - .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState
          :renderer: rst
          :summary:
   * - :py:obj:`CodeInfo <aiida.common.datastructures.CodeInfo>`
     - .. autodoc2-docstring:: aiida.common.datastructures.CodeInfo
          :renderer: rst
          :summary:
   * - :py:obj:`CodeRunMode <aiida.common.datastructures.CodeRunMode>`
     - .. autodoc2-docstring:: aiida.common.datastructures.CodeRunMode
          :renderer: rst
          :summary:
   * - :py:obj:`DefaultFieldsAttributeDict <aiida.common.extendeddicts.DefaultFieldsAttributeDict>`
     - .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict
          :renderer: rst
          :summary:
   * - :py:obj:`FixedFieldsAttributeDict <aiida.common.extendeddicts.FixedFieldsAttributeDict>`
     - .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict
          :renderer: rst
          :summary:
   * - :py:obj:`GraphTraversalRules <aiida.common.links.GraphTraversalRules>`
     - .. autodoc2-docstring:: aiida.common.links.GraphTraversalRules
          :renderer: rst
          :summary:
   * - :py:obj:`LinkType <aiida.common.links.LinkType>`
     - .. autodoc2-docstring:: aiida.common.links.LinkType
          :renderer: rst
          :summary:
   * - :py:obj:`ProgressReporterAbstract <aiida.common.progress_reporter.ProgressReporterAbstract>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract
          :renderer: rst
          :summary:
   * - :py:obj:`StashMode <aiida.common.datastructures.StashMode>`
     - .. autodoc2-docstring:: aiida.common.datastructures.StashMode
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`create_callback <aiida.common.progress_reporter.create_callback>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.create_callback
          :renderer: rst
          :summary:
   * - :py:obj:`get_progress_reporter <aiida.common.progress_reporter.get_progress_reporter>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.get_progress_reporter
          :renderer: rst
          :summary:
   * - :py:obj:`override_log_level <aiida.common.log.override_log_level>`
     - .. autodoc2-docstring:: aiida.common.log.override_log_level
          :renderer: rst
          :summary:
   * - :py:obj:`set_progress_bar_tqdm <aiida.common.progress_reporter.set_progress_bar_tqdm>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.set_progress_bar_tqdm
          :renderer: rst
          :summary:
   * - :py:obj:`set_progress_reporter <aiida.common.progress_reporter.set_progress_reporter>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.set_progress_reporter
          :renderer: rst
          :summary:
   * - :py:obj:`validate_link_label <aiida.common.links.validate_link_label>`
     - .. autodoc2-docstring:: aiida.common.links.validate_link_label
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AIIDA_LOGGER <aiida.common.log.AIIDA_LOGGER>`
     - .. autodoc2-docstring:: aiida.common.log.AIIDA_LOGGER
          :renderer: rst
          :summary:
   * - :py:obj:`GraphTraversalRule <aiida.common.links.GraphTraversalRule>`
     - .. autodoc2-docstring:: aiida.common.links.GraphTraversalRule
          :renderer: rst
          :summary:
   * - :py:obj:`TQDM_BAR_FORMAT <aiida.common.progress_reporter.TQDM_BAR_FORMAT>`
     - .. autodoc2-docstring:: aiida.common.progress_reporter.TQDM_BAR_FORMAT
          :renderer: rst
          :summary:

API
~~~

.. py:data:: AIIDA_LOGGER
   :canonical: aiida.common.log.AIIDA_LOGGER
   :value: None

   .. autodoc2-docstring:: aiida.common.log.AIIDA_LOGGER
      :renderer: rst

.. py:exception:: AiidaException()
   :canonical: aiida.common.exceptions.AiidaException

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: aiida.common.exceptions.AiidaException
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.AiidaException.__init__
      :renderer: rst

.. py:class:: AttributeDict(dictionary=None)
   :canonical: aiida.common.extendeddicts.AttributeDict

   Bases: :py:obj:`dict`

   .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__init__
      :renderer: rst

   .. py:method:: __repr__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__repr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__repr__
         :renderer: rst

   .. py:method:: __getattr__(attr)
      :canonical: aiida.common.extendeddicts.AttributeDict.__getattr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__getattr__
         :renderer: rst

   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.AttributeDict.__setattr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__setattr__
         :renderer: rst

   .. py:method:: __delattr__(attr)
      :canonical: aiida.common.extendeddicts.AttributeDict.__delattr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__delattr__
         :renderer: rst

   .. py:method:: __deepcopy__(memo=None)
      :canonical: aiida.common.extendeddicts.AttributeDict.__deepcopy__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__deepcopy__
         :renderer: rst

   .. py:method:: __getstate__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__getstate__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__getstate__
         :renderer: rst

   .. py:method:: __setstate__(dictionary)
      :canonical: aiida.common.extendeddicts.AttributeDict.__setstate__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__setstate__
         :renderer: rst

   .. py:method:: __dir__()
      :canonical: aiida.common.extendeddicts.AttributeDict.__dir__

      .. autodoc2-docstring:: aiida.common.extendeddicts.AttributeDict.__dir__
         :renderer: rst

.. py:class:: CalcInfo(dictionary=None)
   :canonical: aiida.common.datastructures.CalcInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.common.datastructures.CalcInfo
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.datastructures.CalcInfo.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.common.datastructures.CalcInfo._default_fields
      :value: ('job_environment', 'email', 'email_on_started', 'email_on_terminated', 'uuid', 'prepend_text', 'app...

      .. autodoc2-docstring:: aiida.common.datastructures.CalcInfo._default_fields
         :renderer: rst

.. py:class:: CalcJobState
   :canonical: aiida.common.datastructures.CalcJobState

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState
      :renderer: rst

   .. py:attribute:: UPLOADING
      :canonical: aiida.common.datastructures.CalcJobState.UPLOADING
      :value: 'uploading'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.UPLOADING
         :renderer: rst

   .. py:attribute:: SUBMITTING
      :canonical: aiida.common.datastructures.CalcJobState.SUBMITTING
      :value: 'submitting'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.SUBMITTING
         :renderer: rst

   .. py:attribute:: WITHSCHEDULER
      :canonical: aiida.common.datastructures.CalcJobState.WITHSCHEDULER
      :value: 'withscheduler'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.WITHSCHEDULER
         :renderer: rst

   .. py:attribute:: STASHING
      :canonical: aiida.common.datastructures.CalcJobState.STASHING
      :value: 'stashing'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.STASHING
         :renderer: rst

   .. py:attribute:: RETRIEVING
      :canonical: aiida.common.datastructures.CalcJobState.RETRIEVING
      :value: 'retrieving'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.RETRIEVING
         :renderer: rst

   .. py:attribute:: PARSING
      :canonical: aiida.common.datastructures.CalcJobState.PARSING
      :value: 'parsing'

      .. autodoc2-docstring:: aiida.common.datastructures.CalcJobState.PARSING
         :renderer: rst

.. py:exception:: ClosedStorage()
   :canonical: aiida.common.exceptions.ClosedStorage

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.ClosedStorage
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ClosedStorage.__init__
      :renderer: rst

.. py:class:: CodeInfo(dictionary=None)
   :canonical: aiida.common.datastructures.CodeInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.common.datastructures.CodeInfo
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.datastructures.CodeInfo.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.common.datastructures.CodeInfo._default_fields
      :value: ('cmdline_params', 'stdin_name', 'stdout_name', 'stderr_name', 'join_files', 'withmpi', 'code_uuid')

      .. autodoc2-docstring:: aiida.common.datastructures.CodeInfo._default_fields
         :renderer: rst

.. py:class:: CodeRunMode()
   :canonical: aiida.common.datastructures.CodeRunMode

   Bases: :py:obj:`enum.IntEnum`

   .. autodoc2-docstring:: aiida.common.datastructures.CodeRunMode
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.datastructures.CodeRunMode.__init__
      :renderer: rst

   .. py:attribute:: SERIAL
      :canonical: aiida.common.datastructures.CodeRunMode.SERIAL
      :value: 0

      .. autodoc2-docstring:: aiida.common.datastructures.CodeRunMode.SERIAL
         :renderer: rst

   .. py:attribute:: PARALLEL
      :canonical: aiida.common.datastructures.CodeRunMode.PARALLEL
      :value: 1

      .. autodoc2-docstring:: aiida.common.datastructures.CodeRunMode.PARALLEL
         :renderer: rst

.. py:exception:: ConfigurationError()
   :canonical: aiida.common.exceptions.ConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.ConfigurationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ConfigurationError.__init__
      :renderer: rst

.. py:exception:: ConfigurationVersionError()
   :canonical: aiida.common.exceptions.ConfigurationVersionError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   .. autodoc2-docstring:: aiida.common.exceptions.ConfigurationVersionError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ConfigurationVersionError.__init__
      :renderer: rst

.. py:exception:: ContentNotExistent()
   :canonical: aiida.common.exceptions.ContentNotExistent

   Bases: :py:obj:`aiida.common.exceptions.NotExistent`

   .. autodoc2-docstring:: aiida.common.exceptions.ContentNotExistent
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ContentNotExistent.__init__
      :renderer: rst

.. py:exception:: CorruptStorage()
   :canonical: aiida.common.exceptions.CorruptStorage

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   .. autodoc2-docstring:: aiida.common.exceptions.CorruptStorage
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.CorruptStorage.__init__
      :renderer: rst

.. py:exception:: DbContentError()
   :canonical: aiida.common.exceptions.DbContentError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.DbContentError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.DbContentError.__init__
      :renderer: rst

.. py:class:: DefaultFieldsAttributeDict(dictionary=None)
   :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict._default_fields
      :value: None

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict._default_fields
         :renderer: rst

   .. py:method:: validate()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.validate

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.validate
         :renderer: rst

   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__setattr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__setattr__
         :renderer: rst

   .. py:method:: __getitem__(key)
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__getitem__

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.__getitem__
         :renderer: rst

   .. py:method:: get_default_fields()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.get_default_fields
      :classmethod:

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.get_default_fields
         :renderer: rst

   .. py:method:: defaultkeys()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.defaultkeys

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.defaultkeys
         :renderer: rst

   .. py:method:: extrakeys()
      :canonical: aiida.common.extendeddicts.DefaultFieldsAttributeDict.extrakeys

      .. autodoc2-docstring:: aiida.common.extendeddicts.DefaultFieldsAttributeDict.extrakeys
         :renderer: rst

.. py:exception:: EntryPointError()
   :canonical: aiida.common.exceptions.EntryPointError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.EntryPointError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.EntryPointError.__init__
      :renderer: rst

.. py:exception:: FailedError()
   :canonical: aiida.common.exceptions.FailedError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.FailedError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.FailedError.__init__
      :renderer: rst

.. py:exception:: FeatureDisabled()
   :canonical: aiida.common.exceptions.FeatureDisabled

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.FeatureDisabled
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.FeatureDisabled.__init__
      :renderer: rst

.. py:exception:: FeatureNotAvailable()
   :canonical: aiida.common.exceptions.FeatureNotAvailable

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.FeatureNotAvailable
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.FeatureNotAvailable.__init__
      :renderer: rst

.. py:class:: FixedFieldsAttributeDict(init=None)
   :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict.__init__
      :renderer: rst

   .. py:attribute:: _valid_fields
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict._valid_fields
      :value: None

      .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict._valid_fields
         :renderer: rst

   .. py:method:: __setitem__(item, value)
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setitem__

      .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setitem__
         :renderer: rst

   .. py:method:: __setattr__(attr, value)
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setattr__

      .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict.__setattr__
         :renderer: rst

   .. py:method:: get_valid_fields()
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.get_valid_fields
      :classmethod:

      .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict.get_valid_fields
         :renderer: rst

   .. py:method:: __dir__()
      :canonical: aiida.common.extendeddicts.FixedFieldsAttributeDict.__dir__

      .. autodoc2-docstring:: aiida.common.extendeddicts.FixedFieldsAttributeDict.__dir__
         :renderer: rst

.. py:data:: GraphTraversalRule
   :canonical: aiida.common.links.GraphTraversalRule
   :value: None

   .. autodoc2-docstring:: aiida.common.links.GraphTraversalRule
      :renderer: rst

.. py:class:: GraphTraversalRules
   :canonical: aiida.common.links.GraphTraversalRules

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.common.links.GraphTraversalRules
      :renderer: rst

   .. py:attribute:: DEFAULT
      :canonical: aiida.common.links.GraphTraversalRules.DEFAULT
      :value: None

      .. autodoc2-docstring:: aiida.common.links.GraphTraversalRules.DEFAULT
         :renderer: rst

   .. py:attribute:: DELETE
      :canonical: aiida.common.links.GraphTraversalRules.DELETE
      :value: None

      .. autodoc2-docstring:: aiida.common.links.GraphTraversalRules.DELETE
         :renderer: rst

   .. py:attribute:: EXPORT
      :canonical: aiida.common.links.GraphTraversalRules.EXPORT
      :value: None

      .. autodoc2-docstring:: aiida.common.links.GraphTraversalRules.EXPORT
         :renderer: rst

.. py:exception:: HashingError()
   :canonical: aiida.common.exceptions.HashingError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.HashingError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.HashingError.__init__
      :renderer: rst

.. py:exception:: IncompatibleStorageSchema()
   :canonical: aiida.common.exceptions.IncompatibleStorageSchema

   Bases: :py:obj:`aiida.common.exceptions.IncompatibleDatabaseSchema`

   .. autodoc2-docstring:: aiida.common.exceptions.IncompatibleStorageSchema
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.IncompatibleStorageSchema.__init__
      :renderer: rst

.. py:exception:: InputValidationError()
   :canonical: aiida.common.exceptions.InputValidationError

   Bases: :py:obj:`aiida.common.exceptions.ValidationError`

   .. autodoc2-docstring:: aiida.common.exceptions.InputValidationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.InputValidationError.__init__
      :renderer: rst

.. py:exception:: IntegrityError()
   :canonical: aiida.common.exceptions.IntegrityError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.IntegrityError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.IntegrityError.__init__
      :renderer: rst

.. py:exception:: InternalError()
   :canonical: aiida.common.exceptions.InternalError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.InternalError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.InternalError.__init__
      :renderer: rst

.. py:exception:: InvalidEntryPointTypeError()
   :canonical: aiida.common.exceptions.InvalidEntryPointTypeError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   .. autodoc2-docstring:: aiida.common.exceptions.InvalidEntryPointTypeError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.InvalidEntryPointTypeError.__init__
      :renderer: rst

.. py:exception:: InvalidOperation()
   :canonical: aiida.common.exceptions.InvalidOperation

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.InvalidOperation
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.InvalidOperation.__init__
      :renderer: rst

.. py:exception:: LicensingException()
   :canonical: aiida.common.exceptions.LicensingException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.LicensingException
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.LicensingException.__init__
      :renderer: rst

.. py:class:: LinkType
   :canonical: aiida.common.links.LinkType

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.common.links.LinkType
      :renderer: rst

   .. py:attribute:: CREATE
      :canonical: aiida.common.links.LinkType.CREATE
      :value: 'create'

      .. autodoc2-docstring:: aiida.common.links.LinkType.CREATE
         :renderer: rst

   .. py:attribute:: RETURN
      :canonical: aiida.common.links.LinkType.RETURN
      :value: 'return'

      .. autodoc2-docstring:: aiida.common.links.LinkType.RETURN
         :renderer: rst

   .. py:attribute:: INPUT_CALC
      :canonical: aiida.common.links.LinkType.INPUT_CALC
      :value: 'input_calc'

      .. autodoc2-docstring:: aiida.common.links.LinkType.INPUT_CALC
         :renderer: rst

   .. py:attribute:: INPUT_WORK
      :canonical: aiida.common.links.LinkType.INPUT_WORK
      :value: 'input_work'

      .. autodoc2-docstring:: aiida.common.links.LinkType.INPUT_WORK
         :renderer: rst

   .. py:attribute:: CALL_CALC
      :canonical: aiida.common.links.LinkType.CALL_CALC
      :value: 'call_calc'

      .. autodoc2-docstring:: aiida.common.links.LinkType.CALL_CALC
         :renderer: rst

   .. py:attribute:: CALL_WORK
      :canonical: aiida.common.links.LinkType.CALL_WORK
      :value: 'call_work'

      .. autodoc2-docstring:: aiida.common.links.LinkType.CALL_WORK
         :renderer: rst

.. py:exception:: LoadingEntryPointError()
   :canonical: aiida.common.exceptions.LoadingEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   .. autodoc2-docstring:: aiida.common.exceptions.LoadingEntryPointError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.LoadingEntryPointError.__init__
      :renderer: rst

.. py:exception:: LockedProfileError()
   :canonical: aiida.common.exceptions.LockedProfileError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.LockedProfileError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.LockedProfileError.__init__
      :renderer: rst

.. py:exception:: LockingProfileError()
   :canonical: aiida.common.exceptions.LockingProfileError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.LockingProfileError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.LockingProfileError.__init__
      :renderer: rst

.. py:exception:: MissingConfigurationError()
   :canonical: aiida.common.exceptions.MissingConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   .. autodoc2-docstring:: aiida.common.exceptions.MissingConfigurationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.MissingConfigurationError.__init__
      :renderer: rst

.. py:exception:: MissingEntryPointError()
   :canonical: aiida.common.exceptions.MissingEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   .. autodoc2-docstring:: aiida.common.exceptions.MissingEntryPointError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.MissingEntryPointError.__init__
      :renderer: rst

.. py:exception:: ModificationNotAllowed()
   :canonical: aiida.common.exceptions.ModificationNotAllowed

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.ModificationNotAllowed
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ModificationNotAllowed.__init__
      :renderer: rst

.. py:exception:: MultipleEntryPointError()
   :canonical: aiida.common.exceptions.MultipleEntryPointError

   Bases: :py:obj:`aiida.common.exceptions.EntryPointError`

   .. autodoc2-docstring:: aiida.common.exceptions.MultipleEntryPointError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.MultipleEntryPointError.__init__
      :renderer: rst

.. py:exception:: MultipleObjectsError()
   :canonical: aiida.common.exceptions.MultipleObjectsError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.MultipleObjectsError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.MultipleObjectsError.__init__
      :renderer: rst

.. py:exception:: NotExistent()
   :canonical: aiida.common.exceptions.NotExistent

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistent
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistent.__init__
      :renderer: rst

.. py:exception:: NotExistentAttributeError()
   :canonical: aiida.common.exceptions.NotExistentAttributeError

   Bases: :py:obj:`AttributeError`, :py:obj:`aiida.common.exceptions.NotExistent`

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistentAttributeError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistentAttributeError.__init__
      :renderer: rst

.. py:exception:: NotExistentKeyError()
   :canonical: aiida.common.exceptions.NotExistentKeyError

   Bases: :py:obj:`KeyError`, :py:obj:`aiida.common.exceptions.NotExistent`

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistentKeyError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.NotExistentKeyError.__init__
      :renderer: rst

.. py:exception:: OutputParsingError()
   :canonical: aiida.common.exceptions.OutputParsingError

   Bases: :py:obj:`aiida.common.exceptions.ParsingError`

   .. autodoc2-docstring:: aiida.common.exceptions.OutputParsingError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.OutputParsingError.__init__
      :renderer: rst

.. py:exception:: ParsingError()
   :canonical: aiida.common.exceptions.ParsingError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.ParsingError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ParsingError.__init__
      :renderer: rst

.. py:exception:: PluginInternalError()
   :canonical: aiida.common.exceptions.PluginInternalError

   Bases: :py:obj:`aiida.common.exceptions.InternalError`

   .. autodoc2-docstring:: aiida.common.exceptions.PluginInternalError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.PluginInternalError.__init__
      :renderer: rst

.. py:exception:: ProfileConfigurationError()
   :canonical: aiida.common.exceptions.ProfileConfigurationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   .. autodoc2-docstring:: aiida.common.exceptions.ProfileConfigurationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ProfileConfigurationError.__init__
      :renderer: rst

.. py:class:: ProgressReporterAbstract(*, total: int, desc: typing.Optional[str] = None, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.ProgressReporterAbstract

   .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.__init__
      :renderer: rst

   .. py:property:: total
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.total
      :type: int

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.total
         :renderer: rst

   .. py:property:: desc
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.desc
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.desc
         :renderer: rst

   .. py:property:: n
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.n
      :type: int

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.n
         :renderer: rst

   .. py:method:: __enter__() -> aiida.common.progress_reporter.ProgressReporterAbstract
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.__enter__

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.__enter__
         :renderer: rst

   .. py:method:: __exit__(exctype: typing.Optional[typing.Type[BaseException]], excinst: typing.Optional[BaseException], exctb: typing.Optional[types.TracebackType])
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.__exit__

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.__exit__
         :renderer: rst

   .. py:method:: set_description_str(text: typing.Optional[str] = None, refresh: bool = True)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.set_description_str

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.set_description_str
         :renderer: rst

   .. py:method:: update(n: int = 1)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.update

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.update
         :renderer: rst

   .. py:method:: reset(total: typing.Optional[int] = None)
      :canonical: aiida.common.progress_reporter.ProgressReporterAbstract.reset

      .. autodoc2-docstring:: aiida.common.progress_reporter.ProgressReporterAbstract.reset
         :renderer: rst

.. py:exception:: RemoteOperationError()
   :canonical: aiida.common.exceptions.RemoteOperationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.RemoteOperationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.RemoteOperationError.__init__
      :renderer: rst

.. py:class:: StashMode
   :canonical: aiida.common.datastructures.StashMode

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.common.datastructures.StashMode
      :renderer: rst

   .. py:attribute:: COPY
      :canonical: aiida.common.datastructures.StashMode.COPY
      :value: 'copy'

      .. autodoc2-docstring:: aiida.common.datastructures.StashMode.COPY
         :renderer: rst

.. py:exception:: StorageMigrationError()
   :canonical: aiida.common.exceptions.StorageMigrationError

   Bases: :py:obj:`aiida.common.exceptions.DatabaseMigrationError`

   .. autodoc2-docstring:: aiida.common.exceptions.StorageMigrationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.StorageMigrationError.__init__
      :renderer: rst

.. py:exception:: StoringNotAllowed()
   :canonical: aiida.common.exceptions.StoringNotAllowed

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.StoringNotAllowed
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.StoringNotAllowed.__init__
      :renderer: rst

.. py:data:: TQDM_BAR_FORMAT
   :canonical: aiida.common.progress_reporter.TQDM_BAR_FORMAT
   :value: '{desc:40.40}{percentage:6.1f}%|{bar}| {n_fmt}/{total_fmt}'

   .. autodoc2-docstring:: aiida.common.progress_reporter.TQDM_BAR_FORMAT
      :renderer: rst

.. py:exception:: TestsNotAllowedError()
   :canonical: aiida.common.exceptions.TestsNotAllowedError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.TestsNotAllowedError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.TestsNotAllowedError.__init__
      :renderer: rst

.. py:exception:: TransportTaskException()
   :canonical: aiida.common.exceptions.TransportTaskException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.TransportTaskException
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.TransportTaskException.__init__
      :renderer: rst

.. py:exception:: UniquenessError()
   :canonical: aiida.common.exceptions.UniquenessError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.UniquenessError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.UniquenessError.__init__
      :renderer: rst

.. py:exception:: UnsupportedSpeciesError()
   :canonical: aiida.common.exceptions.UnsupportedSpeciesError

   Bases: :py:obj:`ValueError`

   .. autodoc2-docstring:: aiida.common.exceptions.UnsupportedSpeciesError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.UnsupportedSpeciesError.__init__
      :renderer: rst

.. py:exception:: ValidationError()
   :canonical: aiida.common.exceptions.ValidationError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.common.exceptions.ValidationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.common.exceptions.ValidationError.__init__
      :renderer: rst

.. py:function:: create_callback(progress_reporter: aiida.common.progress_reporter.ProgressReporterAbstract) -> typing.Callable[[str, typing.Any], None]
   :canonical: aiida.common.progress_reporter.create_callback

   .. autodoc2-docstring:: aiida.common.progress_reporter.create_callback
      :renderer: rst

.. py:function:: get_progress_reporter() -> typing.Type[aiida.common.progress_reporter.ProgressReporterAbstract]
   :canonical: aiida.common.progress_reporter.get_progress_reporter

   .. autodoc2-docstring:: aiida.common.progress_reporter.get_progress_reporter
      :renderer: rst

.. py:function:: override_log_level(level=logging.CRITICAL)
   :canonical: aiida.common.log.override_log_level

   .. autodoc2-docstring:: aiida.common.log.override_log_level
      :renderer: rst

.. py:function:: set_progress_bar_tqdm(bar_format: typing.Optional[str] = TQDM_BAR_FORMAT, leave: typing.Optional[bool] = False, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.set_progress_bar_tqdm

   .. autodoc2-docstring:: aiida.common.progress_reporter.set_progress_bar_tqdm
      :renderer: rst

.. py:function:: set_progress_reporter(reporter: typing.Optional[typing.Type[aiida.common.progress_reporter.ProgressReporterAbstract]] = None, **kwargs: typing.Any)
   :canonical: aiida.common.progress_reporter.set_progress_reporter

   .. autodoc2-docstring:: aiida.common.progress_reporter.set_progress_reporter
      :renderer: rst

.. py:function:: validate_link_label(link_label)
   :canonical: aiida.common.links.validate_link_label

   .. autodoc2-docstring:: aiida.common.links.validate_link_label
      :renderer: rst
