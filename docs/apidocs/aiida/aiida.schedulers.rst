:py:mod:`aiida.schedulers`
==========================

.. py:module:: aiida.schedulers


Description
-----------

.. autodoc2-docstring:: aiida.schedulers
   :renderer: rst
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
          :renderer: rst
          :summary:
   * - :py:obj:`JobResource <aiida.schedulers.datastructures.JobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource
          :renderer: rst
          :summary:
   * - :py:obj:`JobState <aiida.schedulers.datastructures.JobState>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState
          :renderer: rst
          :summary:
   * - :py:obj:`JobTemplate <aiida.schedulers.datastructures.JobTemplate>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate
          :renderer: rst
          :summary:
   * - :py:obj:`MachineInfo <aiida.schedulers.datastructures.MachineInfo>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo
          :renderer: rst
          :summary:
   * - :py:obj:`NodeNumberJobResource <aiida.schedulers.datastructures.NodeNumberJobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource
          :renderer: rst
          :summary:
   * - :py:obj:`ParEnvJobResource <aiida.schedulers.datastructures.ParEnvJobResource>`
     - .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource
          :renderer: rst
          :summary:
   * - :py:obj:`Scheduler <aiida.schedulers.scheduler.Scheduler>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler
          :renderer: rst
          :summary:
   * - :py:obj:`SchedulerError <aiida.schedulers.scheduler.SchedulerError>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerError
          :renderer: rst
          :summary:
   * - :py:obj:`SchedulerParsingError <aiida.schedulers.scheduler.SchedulerParsingError>`
     - .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerParsingError
          :renderer: rst
          :summary:

API
~~~

.. py:class:: JobInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobInfo._default_fields
      :value: ('job_id', 'title', 'exit_status', 'terminating_signal', 'annotation', 'job_state', 'job_substate', ...

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._default_fields
         :renderer: rst

   .. py:attribute:: _special_serializers
      :canonical: aiida.schedulers.datastructures.JobInfo._special_serializers
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._special_serializers
         :renderer: rst

   .. py:method:: _serialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_job_state
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._serialize_job_state
         :renderer: rst

   .. py:method:: _deserialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_job_state
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._deserialize_job_state
         :renderer: rst

   .. py:method:: _serialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_date
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._serialize_date
         :renderer: rst

   .. py:method:: _deserialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_date
      :staticmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo._deserialize_date
         :renderer: rst

   .. py:method:: serialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize_field
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.serialize_field
         :renderer: rst

   .. py:method:: deserialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.deserialize_field
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.deserialize_field
         :renderer: rst

   .. py:method:: serialize()
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.serialize
         :renderer: rst

   .. py:method:: get_dict()
      :canonical: aiida.schedulers.datastructures.JobInfo.get_dict

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.get_dict
         :renderer: rst

   .. py:method:: load_from_dict(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_dict
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.load_from_dict
         :renderer: rst

   .. py:method:: load_from_serialized(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobInfo.load_from_serialized
         :renderer: rst

.. py:class:: JobResource(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobResource

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobResource._default_fields
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource._default_fields
         :renderer: rst

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.JobResource.validate_resources
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.validate_resources
         :renderer: rst

   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.JobResource.get_valid_keys
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.get_valid_keys
         :renderer: rst

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_mpiprocs_per_machine
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.accepts_default_mpiprocs_per_machine
         :renderer: rst

   .. py:method:: accepts_default_memory_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_memory_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.accepts_default_memory_per_machine
         :renderer: rst

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.JobResource.get_tot_num_mpiprocs
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobResource.get_tot_num_mpiprocs
         :renderer: rst

.. py:class:: JobState
   :canonical: aiida.schedulers.datastructures.JobState

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState
      :renderer: rst

   .. py:attribute:: UNDETERMINED
      :canonical: aiida.schedulers.datastructures.JobState.UNDETERMINED
      :value: 'undetermined'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.UNDETERMINED
         :renderer: rst

   .. py:attribute:: QUEUED
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED
      :value: 'queued'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.QUEUED
         :renderer: rst

   .. py:attribute:: QUEUED_HELD
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED_HELD
      :value: 'queued held'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.QUEUED_HELD
         :renderer: rst

   .. py:attribute:: RUNNING
      :canonical: aiida.schedulers.datastructures.JobState.RUNNING
      :value: 'running'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.RUNNING
         :renderer: rst

   .. py:attribute:: SUSPENDED
      :canonical: aiida.schedulers.datastructures.JobState.SUSPENDED
      :value: 'suspended'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.SUSPENDED
         :renderer: rst

   .. py:attribute:: DONE
      :canonical: aiida.schedulers.datastructures.JobState.DONE
      :value: 'done'

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobState.DONE
         :renderer: rst

.. py:class:: JobTemplate(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobTemplate

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobTemplate._default_fields
      :value: ('shebang', 'submit_as_hold', 'rerunnable', 'job_environment', 'environment_variables_double_quotes'...

      .. autodoc2-docstring:: aiida.schedulers.datastructures.JobTemplate._default_fields
         :renderer: rst

.. py:class:: MachineInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.MachineInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.MachineInfo._default_fields
      :value: ('name', 'num_mpiprocs', 'num_cpus')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.MachineInfo._default_fields
         :renderer: rst

.. py:class:: NodeNumberJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.NodeNumberJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource._default_fields
      :value: ('num_machines', 'num_mpiprocs_per_machine', 'num_cores_per_machine', 'num_cores_per_mpiproc')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource._default_fields
         :renderer: rst

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.validate_resources
         :renderer: rst

   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_valid_keys
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.get_valid_keys
         :renderer: rst

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.accepts_default_mpiprocs_per_machine
         :renderer: rst

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_tot_num_mpiprocs

      .. autodoc2-docstring:: aiida.schedulers.datastructures.NodeNumberJobResource.get_tot_num_mpiprocs
         :renderer: rst

.. py:class:: ParEnvJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.ParEnvJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.__init__
      :renderer: rst

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource._default_fields
      :value: ('parallel_env', 'tot_num_mpiprocs')

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource._default_fields
         :renderer: rst

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.validate_resources
         :renderer: rst

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.accepts_default_mpiprocs_per_machine
         :renderer: rst

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.get_tot_num_mpiprocs

      .. autodoc2-docstring:: aiida.schedulers.datastructures.ParEnvJobResource.get_tot_num_mpiprocs
         :renderer: rst

.. py:class:: Scheduler()
   :canonical: aiida.schedulers.scheduler.Scheduler

   .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.__init__
      :renderer: rst

   .. py:attribute:: _logger
      :canonical: aiida.schedulers.scheduler.Scheduler._logger
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._logger
         :renderer: rst

   .. py:attribute:: _features
      :canonical: aiida.schedulers.scheduler.Scheduler._features
      :type: typing.Dict[str, bool]
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._features
         :renderer: rst

   .. py:attribute:: _job_resource_class
      :canonical: aiida.schedulers.scheduler.Scheduler._job_resource_class
      :type: typing.Type[aiida.schedulers.datastructures.JobResource]
      :value: None

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._job_resource_class
         :renderer: rst

   .. py:method:: __str__()
      :canonical: aiida.schedulers.scheduler.Scheduler.__str__

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.__str__
         :renderer: rst

   .. py:method:: preprocess_resources(resources, default_mpiprocs_per_machine=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.preprocess_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.preprocess_resources
         :renderer: rst

   .. py:method:: validate_resources(**resources)
      :canonical: aiida.schedulers.scheduler.Scheduler.validate_resources
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.validate_resources
         :renderer: rst

   .. py:method:: get_short_doc()
      :canonical: aiida.schedulers.scheduler.Scheduler.get_short_doc
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_short_doc
         :renderer: rst

   .. py:method:: get_feature(feature_name: str) -> bool
      :canonical: aiida.schedulers.scheduler.Scheduler.get_feature

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_feature
         :renderer: rst

   .. py:property:: logger
      :canonical: aiida.schedulers.scheduler.Scheduler.logger

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.logger
         :renderer: rst

   .. py:method:: job_resource_class() -> typing.Type[aiida.schedulers.datastructures.JobResource]
      :canonical: aiida.schedulers.scheduler.Scheduler.job_resource_class

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.job_resource_class
         :renderer: rst

   .. py:method:: create_job_resource(**kwargs)
      :canonical: aiida.schedulers.scheduler.Scheduler.create_job_resource
      :classmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.create_job_resource
         :renderer: rst

   .. py:method:: get_submit_script(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_submit_script

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_submit_script
         :renderer: rst

   .. py:method:: _get_submit_script_environment_variables(template)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_environment_variables

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_environment_variables
         :renderer: rst

   .. py:method:: _get_submit_script_header(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_header
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_header
         :renderer: rst

   .. py:method:: _get_submit_script_footer(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_footer

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_script_footer
         :renderer: rst

   .. py:method:: _get_run_line(codes_info, codes_run_mode)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_run_line

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_run_line
         :renderer: rst

   .. py:method:: _get_joblist_command(jobs=None, user=None)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_joblist_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_joblist_command
         :renderer: rst

   .. py:method:: _get_detailed_job_info_command(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_detailed_job_info_command

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_detailed_job_info_command
         :renderer: rst

   .. py:method:: get_detailed_job_info(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_detailed_job_info

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_detailed_job_info
         :renderer: rst

   .. py:method:: _parse_joblist_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_joblist_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_joblist_output
         :renderer: rst

   .. py:method:: get_jobs(jobs=None, user=None, as_dict=False)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_jobs

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.get_jobs
         :renderer: rst

   .. py:property:: transport
      :canonical: aiida.schedulers.scheduler.Scheduler.transport

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.transport
         :renderer: rst

   .. py:method:: set_transport(transport)
      :canonical: aiida.schedulers.scheduler.Scheduler.set_transport

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.set_transport
         :renderer: rst

   .. py:method:: _get_submit_command(submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_submit_command
         :renderer: rst

   .. py:method:: _parse_submit_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_submit_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_submit_output
         :renderer: rst

   .. py:method:: submit_from_script(working_directory, submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler.submit_from_script

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.submit_from_script
         :renderer: rst

   .. py:method:: kill(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler.kill

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.kill
         :renderer: rst

   .. py:method:: _get_kill_command(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_kill_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._get_kill_command
         :renderer: rst

   .. py:method:: _parse_kill_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_kill_output
      :abstractmethod:

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler._parse_kill_output
         :renderer: rst

   .. py:method:: parse_output(detailed_job_info=None, stdout=None, stderr=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.parse_output

      .. autodoc2-docstring:: aiida.schedulers.scheduler.Scheduler.parse_output
         :renderer: rst

.. py:class:: SchedulerError
   :canonical: aiida.schedulers.scheduler.SchedulerError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerError
      :renderer: rst

.. py:class:: SchedulerParsingError
   :canonical: aiida.schedulers.scheduler.SchedulerParsingError

   Bases: :py:obj:`aiida.schedulers.scheduler.SchedulerError`

   .. autodoc2-docstring:: aiida.schedulers.scheduler.SchedulerParsingError
      :renderer: rst
