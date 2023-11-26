:py:mod:`aiida.schedulers`
==========================

.. py:module:: aiida.schedulers

.. autodoc2-docstring:: aiida.schedulers
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`JobInfo <aiida.schedulers.datastructures.JobInfo>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo
          :summary:
   * - :py:obj:`JobResource <aiida.schedulers.datastructures.JobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource
          :summary:
   * - :py:obj:`JobState <aiida.schedulers.datastructures.JobState>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState
          :summary:
   * - :py:obj:`JobTemplate <aiida.schedulers.datastructures.JobTemplate>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate
          :summary:
   * - :py:obj:`MachineInfo <aiida.schedulers.datastructures.MachineInfo>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo
          :summary:
   * - :py:obj:`NodeNumberJobResource <aiida.schedulers.datastructures.NodeNumberJobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource
          :summary:
   * - :py:obj:`ParEnvJobResource <aiida.schedulers.datastructures.ParEnvJobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource
          :summary:
   * - :py:obj:`Scheduler <aiida.schedulers.scheduler.Scheduler>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler
          :summary:
   * - :py:obj:`SchedulerError <aiida.schedulers.scheduler.SchedulerError>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerError
          :summary:
   * - :py:obj:`SchedulerParsingError <aiida.schedulers.scheduler.SchedulerParsingError>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerParsingError
          :summary:

API
~~~

.. py:class:: JobInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobInfo._default_fields
      :value: ('job_id', 'title', 'exit_status', 'terminating_signal', 'annotation', 'job_state', 'job_substate', ...

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._default_fields

   .. py:attribute:: _special_serializers
      :canonical: aiida.schedulers.datastructures.JobInfo._special_serializers
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._special_serializers

   .. py:method:: _serialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_job_state
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._serialize_job_state

   .. py:method:: _deserialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_job_state
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._deserialize_job_state

   .. py:method:: _serialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_date
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._serialize_date

   .. py:method:: _deserialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_date
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._deserialize_date

   .. py:method:: serialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize_field
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.serialize_field

   .. py:method:: deserialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.deserialize_field
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.deserialize_field

   .. py:method:: serialize()
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.serialize

   .. py:method:: get_dict()
      :canonical: aiida.schedulers.datastructures.JobInfo.get_dict

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.get_dict

   .. py:method:: load_from_dict(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_dict
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.load_from_dict

   .. py:method:: load_from_serialized(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.load_from_serialized

.. py:class:: JobResource(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobResource

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobResource._default_fields
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource._default_fields

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.JobResource.validate_resources
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.validate_resources

   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.JobResource.get_valid_keys
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.get_valid_keys

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_mpiprocs_per_machine
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.accepts_default_mpiprocs_per_machine

   .. py:method:: accepts_default_memory_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_memory_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.accepts_default_memory_per_machine

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.JobResource.get_tot_num_mpiprocs
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.get_tot_num_mpiprocs

.. py:class:: JobState(*args, **kwds)
   :canonical: aiida.schedulers.datastructures.JobState

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.__init__

   .. py:attribute:: UNDETERMINED
      :canonical: aiida.schedulers.datastructures.JobState.UNDETERMINED
      :value: 'undetermined'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.UNDETERMINED

   .. py:attribute:: QUEUED
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED
      :value: 'queued'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.QUEUED

   .. py:attribute:: QUEUED_HELD
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED_HELD
      :value: 'queued held'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.QUEUED_HELD

   .. py:attribute:: RUNNING
      :canonical: aiida.schedulers.datastructures.JobState.RUNNING
      :value: 'running'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.RUNNING

   .. py:attribute:: SUSPENDED
      :canonical: aiida.schedulers.datastructures.JobState.SUSPENDED
      :value: 'suspended'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.SUSPENDED

   .. py:attribute:: DONE
      :canonical: aiida.schedulers.datastructures.JobState.DONE
      :value: 'done'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.DONE

.. py:class:: JobTemplate(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobTemplate

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobTemplate._default_fields
      :value: ('shebang', 'submit_as_hold', 'rerunnable', 'job_environment', 'environment_variables_double_quotes'...

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate._default_fields

.. py:class:: MachineInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.MachineInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.MachineInfo._default_fields
      :value: ('name', 'num_mpiprocs', 'num_cpus')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo._default_fields

.. py:class:: NodeNumberJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.NodeNumberJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource._default_fields
      :value: ('num_machines', 'num_mpiprocs_per_machine', 'num_cores_per_machine', 'num_cores_per_mpiproc')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource._default_fields

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.validate_resources

   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_valid_keys
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.get_valid_keys

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.accepts_default_mpiprocs_per_machine

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_tot_num_mpiprocs

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.get_tot_num_mpiprocs

.. py:class:: ParEnvJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.ParEnvJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.__init__

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource._default_fields
      :value: ('parallel_env', 'tot_num_mpiprocs')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource._default_fields

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.validate_resources

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.accepts_default_mpiprocs_per_machine

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.get_tot_num_mpiprocs

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.get_tot_num_mpiprocs

.. py:class:: Scheduler()
   :canonical: aiida.schedulers.scheduler.Scheduler

   .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.__init__

   .. py:attribute:: _logger
      :canonical: aiida.schedulers.scheduler.Scheduler._logger
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._logger

   .. py:attribute:: _features
      :canonical: aiida.schedulers.scheduler.Scheduler._features
      :type: typing.Dict[str, bool]
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._features

   .. py:attribute:: _job_resource_class
      :canonical: aiida.schedulers.scheduler.Scheduler._job_resource_class
      :type: typing.Type[aiida.schedulers.datastructures.JobResource]
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._job_resource_class

   .. py:method:: __str__()
      :canonical: aiida.schedulers.scheduler.Scheduler.__str__

   .. py:method:: preprocess_resources(resources, default_mpiprocs_per_machine=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.preprocess_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.preprocess_resources

   .. py:method:: validate_resources(**resources)
      :canonical: aiida.schedulers.scheduler.Scheduler.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.validate_resources

   .. py:method:: get_short_doc()
      :canonical: aiida.schedulers.scheduler.Scheduler.get_short_doc
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_short_doc

   .. py:method:: get_feature(feature_name: str) -> bool
      :canonical: aiida.schedulers.scheduler.Scheduler.get_feature

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_feature

   .. py:property:: logger
      :canonical: aiida.schedulers.scheduler.Scheduler.logger

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.logger

   .. py:method:: job_resource_class() -> typing.Type[aiida.schedulers.datastructures.JobResource]
      :canonical: aiida.schedulers.scheduler.Scheduler.job_resource_class

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.job_resource_class

   .. py:method:: create_job_resource(**kwargs)
      :canonical: aiida.schedulers.scheduler.Scheduler.create_job_resource
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.create_job_resource

   .. py:method:: get_submit_script(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_submit_script

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_submit_script

   .. py:method:: _get_submit_script_environment_variables(template)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_environment_variables

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_environment_variables

   .. py:method:: _get_submit_script_header(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_header
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_header

   .. py:method:: _get_submit_script_footer(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_footer

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_footer

   .. py:method:: _get_run_line(codes_info, codes_run_mode)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_run_line

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_run_line

   .. py:method:: _get_joblist_command(jobs=None, user=None)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_joblist_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_joblist_command

   .. py:method:: _get_detailed_job_info_command(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_detailed_job_info_command

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_detailed_job_info_command

   .. py:method:: get_detailed_job_info(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_detailed_job_info

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_detailed_job_info

   .. py:method:: _parse_joblist_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_joblist_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_joblist_output

   .. py:method:: get_jobs(jobs=None, user=None, as_dict=False)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_jobs

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_jobs

   .. py:property:: transport
      :canonical: aiida.schedulers.scheduler.Scheduler.transport

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.transport

   .. py:method:: set_transport(transport)
      :canonical: aiida.schedulers.scheduler.Scheduler.set_transport

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.set_transport

   .. py:method:: _get_submit_command(submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_command

   .. py:method:: _parse_submit_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_submit_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_submit_output

   .. py:method:: submit_from_script(working_directory, submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler.submit_from_script

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.submit_from_script

   .. py:method:: kill(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler.kill

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.kill

   .. py:method:: _get_kill_command(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_kill_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_kill_command

   .. py:method:: _parse_kill_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_kill_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_kill_output

   .. py:method:: parse_output(detailed_job_info=None, stdout=None, stderr=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.parse_output

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.parse_output

.. py:class:: SchedulerError
   :canonical: aiida.schedulers.scheduler.SchedulerError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerError

.. py:class:: SchedulerParsingError
   :canonical: aiida.schedulers.scheduler.SchedulerParsingError

   Bases: :py:obj:`aiida.schedulers.scheduler.SchedulerError`

   .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerParsingError
