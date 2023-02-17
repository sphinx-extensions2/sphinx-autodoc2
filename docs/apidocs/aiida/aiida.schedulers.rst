:py:mod:`aiida.schedulers`
==========================

.. py:module:: aiida.schedulers


Description
-----------

Module for classes and utilities to interact with cluster schedulers.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`JobInfo <aiida.schedulers.datastructures.JobInfo>`
     - Contains properties for a job in the queue. Most of the fields are taken from DRMAA v.2.
   * - :py:obj:`JobResource <aiida.schedulers.datastructures.JobResource>`
     - Data structure to store job resources.
   * - :py:obj:`JobState <aiida.schedulers.datastructures.JobState>`
     - Enumeration of possible scheduler states of a CalcJob.
   * - :py:obj:`JobTemplate <aiida.schedulers.datastructures.JobTemplate>`
     - A template for submitting jobs to a scheduler.
   * - :py:obj:`MachineInfo <aiida.schedulers.datastructures.MachineInfo>`
     - Similarly to what is defined in the DRMAA v.2 as SlotInfo; this identifies each machine (also called 'node' on some schedulers) on which a job is running, and how many CPUs are being used. (Some of them could be undefined)
   * - :py:obj:`NodeNumberJobResource <aiida.schedulers.datastructures.NodeNumberJobResource>`
     - `JobResource` for schedulers that support the specification of a number of nodes and cpus per node.
   * - :py:obj:`ParEnvJobResource <aiida.schedulers.datastructures.ParEnvJobResource>`
     - `JobResource` for schedulers that support the specification of a parallel environment and number of MPI procs.
   * - :py:obj:`Scheduler <aiida.schedulers.scheduler.Scheduler>`
     - Base class for a job scheduler.
   * - :py:obj:`SchedulerError <aiida.schedulers.scheduler.SchedulerError>`
     - 
   * - :py:obj:`SchedulerParsingError <aiida.schedulers.scheduler.SchedulerParsingError>`
     - 

API
~~~

.. py:class:: JobInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   Contains properties for a job in the queue.
   Most of the fields are taken from DRMAA v.2.

   Note that default fields may be undefined. This
   is an expected behavior and the application must cope with this
   case. An example for instance is the exit_status for jobs that have
   not finished yet; or features not supported by the given scheduler.

   Fields:

      * ``job_id``: the job ID on the scheduler
      * ``title``: the job title, as known by the scheduler
      * ``exit_status``: the exit status of the job as reported by the operating
        system on the execution host
      * ``terminating_signal``: the UNIX signal that was responsible for the end
        of the job.
      * ``annotation``: human-readable description of the reason for the job
        being in the current state or substate.
      * ``job_state``: the job state (one of those defined in
        ``aiida.schedulers.datastructures.JobState``)
      * ``job_substate``: a string with the implementation-specific sub-state
      * ``allocated_machines``: a list of machines used for the current job.
        This is a list of :py:class:`aiida.schedulers.datastructures.MachineInfo` objects.
      * ``job_owner``: the job owner as reported by the scheduler
      * ``num_mpiprocs``: the *total* number of requested MPI procs
      * ``num_cpus``: the *total* number of requested CPUs (cores) [may be undefined]
      * ``num_machines``: the number of machines (i.e., nodes), required by the
        job. If ``allocated_machines`` is not None, this number must be equal to
        ``len(allocated_machines)``. Otherwise, for schedulers not supporting
        the retrieval of the full list of allocated machines, this
        attribute can be used to know at least the number of machines.
      * ``queue_name``: The name of the queue in which the job is queued or
        running.
      * ``account``: The account/projectid in which the job is queued or
        running in.
      * ``qos``: The quality of service in which the job is queued or
        running in.
      * ``wallclock_time_seconds``: the accumulated wallclock time, in seconds
      * ``requested_wallclock_time_seconds``: the requested wallclock time,
        in seconds
      * ``cpu_time``: the accumulated cpu time, in seconds
      * ``submission_time``: the absolute time at which the job was submitted,
        of type datetime.datetime
      * ``dispatch_time``: the absolute time at which the job first entered the
        'started' state, of type datetime.datetime
      * ``finish_time``: the absolute time at which the job first entered the
        'finished' state, of type datetime.datetime


   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobInfo._default_fields
      :value: ('job_id', 'title', 'exit_status', 'terminating_signal', 'annotation', 'job_state', 'job_substate', ...

   .. py:attribute:: _special_serializers
      :canonical: aiida.schedulers.datastructures.JobInfo._special_serializers
      :value: None

   .. py:method:: _serialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_job_state
      :staticmethod:

      Return the serialized value of the JobState instance.

   .. py:method:: _deserialize_job_state(job_state)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_job_state
      :staticmethod:

      Return an instance of JobState from the job_state string.

   .. py:method:: _serialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._serialize_date
      :staticmethod:

      Serialise a data value
      :param value: The value to serialise
      :return: The serialised value


   .. py:method:: _deserialize_date(value)
      :canonical: aiida.schedulers.datastructures.JobInfo._deserialize_date
      :staticmethod:

      Deserialise a date
      :param value: The date vlue
      :return: The deserialised date


   .. py:method:: serialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize_field
      :classmethod:

      Serialise a particular field value

      :param value: The value to serialise
      :param field_type: The field type
      :return: The serialised value


   .. py:method:: deserialize_field(value, field_type)
      :canonical: aiida.schedulers.datastructures.JobInfo.deserialize_field
      :classmethod:

      Deserialise the value of a particular field with a type
      :param value: The value
      :param field_type: The field type
      :return: The deserialised value


   .. py:method:: serialize()
      :canonical: aiida.schedulers.datastructures.JobInfo.serialize

      Serialize the current data (as obtained by ``self.get_dict()``) into a JSON string.

      :return: A string with serialised representation of the current data.


   .. py:method:: get_dict()
      :canonical: aiida.schedulers.datastructures.JobInfo.get_dict

      Serialise the current data into a dictionary that is JSON-serializable.

      :return: A dictionary


   .. py:method:: load_from_dict(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_dict
      :classmethod:

      Create a new instance loading the values from serialised data in dictionary form

      :param data: The dictionary with the data to load from


   .. py:method:: load_from_serialized(data)
      :canonical: aiida.schedulers.datastructures.JobInfo.load_from_serialized
      :classmethod:

      Create a new instance loading the values from JSON-serialised data as a string

      :param data: The string with the JSON-serialised data to load from


.. py:class:: JobResource(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobResource

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   Data structure to store job resources.

   Each `Scheduler` implementation must define the `_job_resource_class` attribute to be a subclass of this class.
   It should at least define the `get_tot_num_mpiprocs` method, plus a constructor to accept its set of variables.

   Typical attributes are:

   * ``num_machines``
   * ``num_mpiprocs_per_machine``

   or (e.g. for SGE)

   * ``tot_num_mpiprocs``
   * ``parallel_env``

   The constructor should take care of checking the values.
   The init should raise only ValueError or TypeError on invalid parameters.


   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobResource._default_fields
      :value: None

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.JobResource.validate_resources
      :abstractmethod:
      :classmethod:

      Validate the resources against the job resource class of this scheduler.

      :param kwargs: dictionary of values to define the job resources
      :raises ValueError: if the resources are invalid or incomplete
      :return: optional tuple of parsed resource settings


   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.JobResource.get_valid_keys
      :classmethod:

      Return a list of valid keys to be passed to the constructor.

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_mpiprocs_per_machine
      :abstractmethod:
      :classmethod:

      Return True if this subclass accepts a `default_mpiprocs_per_machine` key, False otherwise.

   .. py:method:: accepts_default_memory_per_machine()
      :canonical: aiida.schedulers.datastructures.JobResource.accepts_default_memory_per_machine
      :classmethod:

      Return True if this subclass accepts a `default_memory_per_machine` key, False otherwise.

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.JobResource.get_tot_num_mpiprocs
      :abstractmethod:

      Return the total number of cpus of this job resource.

.. py:class:: JobState
   :canonical: aiida.schedulers.datastructures.JobState

   Bases: :py:obj:`enum.Enum`

   Enumeration of possible scheduler states of a CalcJob.

   There is no FAILED state as every completed job is put in DONE, regardless of success.


   .. py:attribute:: UNDETERMINED
      :canonical: aiida.schedulers.datastructures.JobState.UNDETERMINED
      :value: 'undetermined'

   .. py:attribute:: QUEUED
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED
      :value: 'queued'

   .. py:attribute:: QUEUED_HELD
      :canonical: aiida.schedulers.datastructures.JobState.QUEUED_HELD
      :value: 'queued held'

   .. py:attribute:: RUNNING
      :canonical: aiida.schedulers.datastructures.JobState.RUNNING
      :value: 'running'

   .. py:attribute:: SUSPENDED
      :canonical: aiida.schedulers.datastructures.JobState.SUSPENDED
      :value: 'suspended'

   .. py:attribute:: DONE
      :canonical: aiida.schedulers.datastructures.JobState.DONE
      :value: 'done'

.. py:class:: JobTemplate(dictionary=None)
   :canonical: aiida.schedulers.datastructures.JobTemplate

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   A template for submitting jobs to a scheduler.

   This contains all required information to create the job header.

   The required fields are: working_directory, job_name, num_machines, num_mpiprocs_per_machine, argv.

   Fields:

     * ``shebang line``: The first line of the submission script
     * ``submit_as_hold``: if set, the job will be in a 'hold' status right
       after the submission
     * ``rerunnable``: if the job is rerunnable (boolean)
     * ``job_environment``: a dictionary with environment variables to set
       before the execution of the code.
     * ``environment_variables_double_quotes``: if set to True, use double quotes
       instead of single quotes to escape the environment variables specified
       in ``environment_variables``.
     * ``working_directory``: the working directory for this job. During
       submission, the transport will first do a 'chdir' to this directory,
       and then possibly set a scheduler parameter, if this is supported
       by the scheduler.
     * ``email``: an email address for sending emails on job events.
     * ``email_on_started``: if True, ask the scheduler to send an email when the
       job starts.
     * ``email_on_terminated``: if True, ask the scheduler to send an email when
       the job ends. This should also send emails on job failure, when
       possible.
     * ``job_name``: the name of this job. The actual name of the job can be
       different from the one specified here, e.g. if there are unsupported
       characters, or the name is too long.
     * ``sched_output_path``: a (relative) file name for the stdout of this job
     * ``sched_error_path``: a (relative) file name for the stdout of this job
     * ``sched_join_files``: if True, write both stdout and stderr on the same
       file (the one specified for stdout)
     * ``queue_name``: the name of the scheduler queue (sometimes also called
       partition), on which the job will be submitted.
     * ``account``: the name of the scheduler account (sometimes also called
       projectid), on which the job will be submitted.
     * ``qos``: the quality of service of the scheduler account,
       on which the job will be submitted.
     * ``job_resource``: a suitable :py:class:`JobResource`
       subclass with information on how many
       nodes and cpus it should use. It must be an instance of the
       ``aiida.schedulers.Scheduler.job_resource_class`` class.
       Use the Scheduler.create_job_resource method to create it.
     * ``num_machines``: how many machines (or nodes) should be used
     * ``num_mpiprocs_per_machine``: how many MPI procs should be used on each
       machine (or node).
     * ``priority``: a priority for this job. Should be in the format accepted
       by the specific scheduler.
     * ``max_memory_kb``: The maximum amount of memory the job is allowed
       to allocate ON EACH NODE, in kilobytes
     * ``max_wallclock_seconds``: The maximum wall clock time that all processes
       of a job are allowed to exist, in seconds
     * ``custom_scheduler_commands``: a string that will be inserted right
       after the last scheduler command, and before any other non-scheduler
       command; useful if some specific flag needs to be added and is not
       supported by the plugin
     * ``prepend_text``: a (possibly multi-line) string to be inserted
       in the scheduler script before the main execution line
     * ``append_text``: a (possibly multi-line) string to be inserted
       in the scheduler script after the main execution line
     * ``import_sys_environment``: import the system environment variables
     * ``codes_info``: a list of aiida.scheduler.datastructures.JobTemplateCodeInfo objects.
       Each contains the information necessary to run a single code. At the
       moment, it can contain:

       * ``cmdline_parameters``: a list of strings with the command line arguments
         of the program to run. This is the main program to be executed.
         NOTE: The first one is the executable name.
         For MPI runs, this will probably be "mpirun" or a similar program;
         this has to be chosen at a upper level.
       * ``stdin_name``: the (relative) file name to be used as stdin for the
         program specified with argv.
       * ``stdout_name``: the (relative) file name to be used as stdout for the
         program specified with argv.
       * ``stderr_name``: the (relative) file name to be used as stderr for the
         program specified with argv.
       * ``join_files``: if True, stderr is redirected on the same file
         specified for stdout.

     * ``codes_run_mode``: sets the run_mode with which the (multiple) codes
       have to be executed. For example, parallel execution::

         mpirun -np 8 a.x &
         mpirun -np 8 b.x &
         wait

       The serial execution would be without the &'s.
       Values are given by aiida.common.datastructures.CodeRunMode.


   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.JobTemplate._default_fields
      :value: ('shebang', 'submit_as_hold', 'rerunnable', 'job_environment', 'environment_variables_double_quotes'...

.. py:class:: MachineInfo(dictionary=None)
   :canonical: aiida.schedulers.datastructures.MachineInfo

   Bases: :py:obj:`aiida.common.extendeddicts.DefaultFieldsAttributeDict`

   Similarly to what is defined in the DRMAA v.2 as SlotInfo; this identifies
   each machine (also called 'node' on some schedulers)
   on which a job is running, and how many CPUs are being used. (Some of them
   could be undefined)

   * ``name``: name of the machine
   * ``num_cpus``: number of cores used by the job on this machine
   * ``num_mpiprocs``: number of MPI processes used by the job on this machine


   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.MachineInfo._default_fields
      :value: ('name', 'num_mpiprocs', 'num_cpus')

.. py:class:: NodeNumberJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.NodeNumberJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   `JobResource` for schedulers that support the specification of a number of nodes and cpus per node.

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource._default_fields
      :value: ('num_machines', 'num_mpiprocs_per_machine', 'num_cores_per_machine', 'num_cores_per_mpiproc')

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.validate_resources
      :classmethod:

      Validate the resources against the job resource class of this scheduler.

      :param kwargs: dictionary of values to define the job resources
      :return: attribute dictionary with the parsed parameters populated
      :raises ValueError: if the resources are invalid or incomplete


   .. py:method:: __init__(**kwargs)
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.__init__

      Initialize the job resources from the passed arguments.

      :raises ValueError: if the resources are invalid or incomplete


   .. py:method:: get_valid_keys()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_valid_keys
      :classmethod:

      Return a list of valid keys to be passed to the constructor.

   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      Return True if this subclass accepts a `default_mpiprocs_per_machine` key, False otherwise.

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.NodeNumberJobResource.get_tot_num_mpiprocs

      Return the total number of cpus of this job resource.

.. py:class:: ParEnvJobResource(**kwargs)
   :canonical: aiida.schedulers.datastructures.ParEnvJobResource

   Bases: :py:obj:`aiida.schedulers.datastructures.JobResource`

   `JobResource` for schedulers that support the specification of a parallel environment and number of MPI procs.

   .. py:attribute:: _default_fields
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource._default_fields
      :value: ('parallel_env', 'tot_num_mpiprocs')

   .. py:method:: validate_resources(**kwargs)
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.validate_resources
      :classmethod:

      Validate the resources against the job resource class of this scheduler.

      :param kwargs: dictionary of values to define the job resources
      :return: attribute dictionary with the parsed parameters populated
      :raises ValueError: if the resources are invalid or incomplete


   .. py:method:: __init__(**kwargs)
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.__init__

      Initialize the job resources from the passed arguments (the valid keys can be
      obtained with the function self.get_valid_keys()).

      :raises ValueError: if the resources are invalid or incomplete


   .. py:method:: accepts_default_mpiprocs_per_machine()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.accepts_default_mpiprocs_per_machine
      :classmethod:

      Return True if this subclass accepts a `default_mpiprocs_per_machine` key, False otherwise.

   .. py:method:: get_tot_num_mpiprocs()
      :canonical: aiida.schedulers.datastructures.ParEnvJobResource.get_tot_num_mpiprocs

      Return the total number of cpus of this job resource.

.. py:class:: Scheduler()
   :canonical: aiida.schedulers.scheduler.Scheduler

   Base class for a job scheduler.

   .. py:attribute:: _logger
      :canonical: aiida.schedulers.scheduler.Scheduler._logger
      :value: None

   .. py:attribute:: _features
      :canonical: aiida.schedulers.scheduler.Scheduler._features
      :type: typing.Dict[str, bool]
      :value: None

   .. py:attribute:: _job_resource_class
      :canonical: aiida.schedulers.scheduler.Scheduler._job_resource_class
      :type: typing.Type[aiida.schedulers.datastructures.JobResource]
      :value: None

   .. py:method:: __str__()
      :canonical: aiida.schedulers.scheduler.Scheduler.__str__

      Return str(self).

   .. py:method:: preprocess_resources(resources, default_mpiprocs_per_machine=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.preprocess_resources
      :classmethod:

      Pre process the resources.

      Add the `num_mpiprocs_per_machine` key to the `resources` if it is not already defined and it cannot be deduced
      from the `num_machines` and `tot_num_mpiprocs` being defined. The value is also not added if the job resource
      class of this scheduler does not accept the `num_mpiprocs_per_machine` keyword. Note that the changes are made
      in place to the `resources` argument passed.


   .. py:method:: validate_resources(**resources)
      :canonical: aiida.schedulers.scheduler.Scheduler.validate_resources
      :classmethod:

      Validate the resources against the job resource class of this scheduler.

      :param resources: keyword arguments to define the job resources
      :raises ValueError: if the resources are invalid or incomplete


   .. py:method:: __init__()
      :canonical: aiida.schedulers.scheduler.Scheduler.__init__

   .. py:method:: get_short_doc()
      :canonical: aiida.schedulers.scheduler.Scheduler.get_short_doc
      :classmethod:

      Return the first non-empty line of the class docstring, if available.

   .. py:method:: get_feature(feature_name: str) -> bool
      :canonical: aiida.schedulers.scheduler.Scheduler.get_feature

   .. py:property:: logger
      :canonical: aiida.schedulers.scheduler.Scheduler.logger

      Return the internal logger.

   .. py:method:: job_resource_class() -> typing.Type[aiida.schedulers.datastructures.JobResource]
      :canonical: aiida.schedulers.scheduler.Scheduler.job_resource_class

   .. py:method:: create_job_resource(**kwargs)
      :canonical: aiida.schedulers.scheduler.Scheduler.create_job_resource
      :classmethod:

      Create a suitable job resource from the kwargs specified.

   .. py:method:: get_submit_script(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_submit_script

      Return the submit script as a string.

      :parameter job_tmpl: a `aiida.schedulers.datastrutures.JobTemplate` instance.

      The plugin returns something like

      #!/bin/bash <- this shebang line is configurable to some extent
      scheduler_dependent stuff to choose numnodes, numcores, walltime, ...
      prepend_computer [also from calcinfo, joined with the following?]
      prepend_code [from calcinfo]
      output of _get_script_main_content
      postpend_code
      postpend_computer


   .. py:method:: _get_submit_script_environment_variables(template)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_environment_variables

      Return the part of the submit script header that defines environment variables.

      :parameter template: a `aiida.schedulers.datastrutures.JobTemplate` instance.
      :return: string containing environment variable declarations.


   .. py:method:: _get_submit_script_header(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_header
      :abstractmethod:

      Return the submit script header, using the parameters from the job template.

      :param job_tmpl: a `JobTemplate` instance with relevant parameters set.


   .. py:method:: _get_submit_script_footer(job_tmpl)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_script_footer

      Return the submit script final part, using the parameters from the job template.

      :param job_tmpl: a `JobTemplate` instance with relevant parameters set.


   .. py:method:: _get_run_line(codes_info, codes_run_mode)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_run_line

      Return a string with the line to execute a specific code with specific arguments.

      :parameter codes_info: a list of `aiida.scheduler.datastructures.JobTemplateCodeInfo` objects.
          Each contains the information needed to run the code. I.e. `cmdline_params`, `stdin_name`,
          `stdout_name`, `stderr_name`, `join_files`. See
          the documentation of `JobTemplate` and `JobTemplateCodeInfo`.
      :parameter codes_run_mode: instance of `aiida.common.datastructures.CodeRunMode` contains the information on how
          to launch the multiple codes.
      :return: string with format: [executable] [args] {[ < stdin ]} {[ < stdout ]} {[2>&1 | 2> stderr]}


   .. py:method:: _get_joblist_command(jobs=None, user=None)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_joblist_command
      :abstractmethod:

      Return the command to get the most complete description possible of currently active jobs.

      .. note::

          Typically one can pass only either jobs or user, depending on the specific plugin. The choice can be done
          according to the value returned by `self.get_feature('can_query_by_user')`

      :param jobs: either None to get a list of all jobs in the machine, or a list of jobs.
      :param user: either None, or a string with the username (to show only jobs of the specific user).


   .. py:method:: _get_detailed_job_info_command(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_detailed_job_info_command

      Return the command to run to get detailed information for a given job.

      This is typically called after the job has finished, to retrieve the most detailed information possible about
      the job. This is done because most schedulers just make finished jobs disappear from the `qstat` command, and
      instead sometimes it is useful to know some more detailed information about the job exit status, etc.

      :raises: :class:`aiida.common.exceptions.FeatureNotAvailable`


   .. py:method:: get_detailed_job_info(job_id)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_detailed_job_info

      Return the detailed job info.

      This will be a dictionary with the return value, stderr and stdout content returned by calling the command that
      is returned by `_get_detailed_job_info_command`.

      :param job_id: the job identifier
      :return: dictionary with `retval`, `stdout` and `stderr`.


   .. py:method:: _parse_joblist_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_joblist_output
      :abstractmethod:

      Parse the joblist output as returned by executing the command returned by `_get_joblist_command` method.

      :return: list of `JobInfo` objects, one of each job each with at least its default params implemented.


   .. py:method:: get_jobs(jobs=None, user=None, as_dict=False)
      :canonical: aiida.schedulers.scheduler.Scheduler.get_jobs

      Return the list of currently active jobs.

      .. note:: typically, only either jobs or user can be specified. See also comments in `_get_joblist_command`.

      :param list jobs: a list of jobs to check; only these are checked
      :param str user: a string with a user: only jobs of this user are checked
      :param list as_dict: if False (default), a list of JobInfo objects is returned. If True, a dictionary is
          returned, having as key the job_id and as value the JobInfo object.
      :return: list of active jobs


   .. py:property:: transport
      :canonical: aiida.schedulers.scheduler.Scheduler.transport

      Return the transport set for this scheduler.

   .. py:method:: set_transport(transport)
      :canonical: aiida.schedulers.scheduler.Scheduler.set_transport

      Set the transport to be used to query the machine or to submit scripts.

      This class assumes that the transport is open and active.


   .. py:method:: _get_submit_command(submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_submit_command
      :abstractmethod:

      Return the string to execute to submit a given script.

      .. warning:: the `submit_script` should already have been bash-escaped

      :param submit_script: the path of the submit script relative to the working directory.
      :return: the string to execute to submit a given script.


   .. py:method:: _parse_submit_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_submit_output
      :abstractmethod:

      Parse the output of the submit command returned by calling the `_get_submit_command` command.

      :return: a string with the job ID.


   .. py:method:: submit_from_script(working_directory, submit_script)
      :canonical: aiida.schedulers.scheduler.Scheduler.submit_from_script

      Submit the submission script to the scheduler.

      :return: return a string with the job ID in a valid format to be used for querying.


   .. py:method:: kill(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler.kill

      Kill a remote job and parse the return value of the scheduler to check if the command succeeded.

      ..note::

          On some schedulers, even if the command is accepted, it may take some seconds for the job to actually
          disappear from the queue.

      :param jobid: the job ID to be killed
      :return: True if everything seems ok, False otherwise.


   .. py:method:: _get_kill_command(jobid)
      :canonical: aiida.schedulers.scheduler.Scheduler._get_kill_command
      :abstractmethod:

      Return the command to kill the job with specified jobid.

   .. py:method:: _parse_kill_output(retval, stdout, stderr)
      :canonical: aiida.schedulers.scheduler.Scheduler._parse_kill_output
      :abstractmethod:

      Parse the output of the kill command.

      :return: True if everything seems ok, False otherwise.


   .. py:method:: parse_output(detailed_job_info=None, stdout=None, stderr=None)
      :canonical: aiida.schedulers.scheduler.Scheduler.parse_output

      Parse the output of the scheduler.

      :param detailed_job_info: dictionary with the output returned by the `Scheduler.get_detailed_job_info` command.
          This should contain the keys `retval`, `stdout` and `stderr` corresponding to the return value, stdout and
          stderr returned by the accounting command executed for a specific job id.
      :param stdout: string with the output written by the scheduler to stdout.
      :param stderr: string with the output written by the scheduler to stderr.
      :return: None or an instance of :class:`aiida.engine.processes.exit_code.ExitCode`.


.. py:class:: SchedulerError
   :canonical: aiida.schedulers.scheduler.SchedulerError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

.. py:class:: SchedulerParsingError
   :canonical: aiida.schedulers.scheduler.SchedulerParsingError

   Bases: :py:obj:`aiida.schedulers.scheduler.SchedulerError`
