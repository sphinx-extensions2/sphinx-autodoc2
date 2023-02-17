:py:mod:`aiida.engine`
======================

.. py:module:: aiida.engine


Description
-----------

Module with all the internals that make up the engine of `aiida-core`.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AiiDAPersister <aiida.engine.persistence.AiiDAPersister>`
     - Persister to take saved process instance states and persisting them to the database.
   * - :py:obj:`Awaitable <aiida.engine.processes.workchains.awaitable.Awaitable>`
     - An attribute dictionary that represents an action that a Process could be waiting for to finish.
   * - :py:obj:`AwaitableAction <aiida.engine.processes.workchains.awaitable.AwaitableAction>`
     - Enum that describes the action to be taken for a given awaitable.
   * - :py:obj:`AwaitableTarget <aiida.engine.processes.workchains.awaitable.AwaitableTarget>`
     - Enum that describes the class of the target a given awaitable.
   * - :py:obj:`BaseRestartWorkChain <aiida.engine.processes.workchains.restart.BaseRestartWorkChain>`
     - Base restart work chain.
   * - :py:obj:`CalcJob <aiida.engine.processes.calcjobs.calcjob.CalcJob>`
     - Implementation of the CalcJob process.
   * - :py:obj:`CalcJobImporter <aiida.engine.processes.calcjobs.importer.CalcJobImporter>`
     - An abstract class, to define an importer for computations completed outside of AiiDA.
   * - :py:obj:`CalcJobOutputPort <aiida.engine.processes.ports.CalcJobOutputPort>`
     - Sub class of plumpy.OutputPort which adds the `_pass_to_parser` attribute.
   * - :py:obj:`CalcJobProcessSpec <aiida.engine.processes.process_spec.CalcJobProcessSpec>`
     - Process spec intended for the `CalcJob` process class.
   * - :py:obj:`DaemonClient <aiida.engine.daemon.client.DaemonClient>`
     - Client to interact with the daemon.
   * - :py:obj:`ExitCode <aiida.engine.processes.exit_code.ExitCode>`
     - A simple data class to define an exit code for a :class:`~aiida.engine.processes.process.Process`.
   * - :py:obj:`ExitCodesNamespace <aiida.engine.processes.exit_code.ExitCodesNamespace>`
     - A namespace of `ExitCode` instances that can be accessed through getattr as well as getitem.
   * - :py:obj:`FunctionProcess <aiida.engine.processes.functions.FunctionProcess>`
     - Function process class used for turning functions into a Process
   * - :py:obj:`InputPort <aiida.engine.processes.ports.InputPort>`
     - Sub class of plumpy.InputPort which mixes in the WithSerialize and WithNonDb mixins to support automatic value serialization to database storable types and support non database storable input types as well.
   * - :py:obj:`InterruptableFuture <aiida.engine.utils.InterruptableFuture>`
     - A future that can be interrupted by calling `interrupt`.
   * - :py:obj:`JobManager <aiida.engine.processes.calcjobs.manager.JobManager>`
     - A manager for :py:class:`~aiida.engine.processes.calcjobs.calcjob.CalcJob` submitted to ``Computer`` instances.
   * - :py:obj:`JobsList <aiida.engine.processes.calcjobs.manager.JobsList>`
     - Manager of calculation jobs submitted with a specific ``AuthInfo``, i.e. computer configured for a specific user.
   * - :py:obj:`ObjectLoader <aiida.engine.persistence.ObjectLoader>`
     - Custom object loader for `aiida-core`.
   * - :py:obj:`PortNamespace <aiida.engine.processes.ports.PortNamespace>`
     - Sub class of plumpy.PortNamespace which implements the serialize method to support automatic recursive serialization of a given mapping onto the ports of the PortNamespace.
   * - :py:obj:`Process <aiida.engine.processes.process.Process>`
     - This class represents an AiiDA process which can be executed and will have full provenance saved in the database.
   * - :py:obj:`ProcessBuilder <aiida.engine.processes.builder.ProcessBuilder>`
     - A process builder that helps setting up the inputs for creating a new process.
   * - :py:obj:`ProcessBuilderNamespace <aiida.engine.processes.builder.ProcessBuilderNamespace>`
     - Input namespace for the `ProcessBuilder`.
   * - :py:obj:`ProcessFuture <aiida.engine.processes.futures.ProcessFuture>`
     - Future that waits for a process to complete using both polling and listening for broadcast events if possible.
   * - :py:obj:`ProcessHandlerReport <aiida.engine.processes.workchains.utils.ProcessHandlerReport>`
     - A namedtuple to define a process handler report for a :class:`aiida.engine.BaseRestartWorkChain`.
   * - :py:obj:`ProcessSpec <aiida.engine.processes.process_spec.ProcessSpec>`
     - Default process spec for process classes defined in `aiida-core`.
   * - :py:obj:`Runner <aiida.engine.runners.Runner>`
     - Class that can launch processes by running in the current interpreter or by submitting them to the daemon.
   * - :py:obj:`WithNonDb <aiida.engine.processes.ports.WithNonDb>`
     - A mixin that adds support to a port to flag that it should not be stored in the database using the non_db=True flag.
   * - :py:obj:`WithSerialize <aiida.engine.processes.ports.WithSerialize>`
     - A mixin that adds support for a serialization function which is automatically applied on inputs that are not AiiDA data types.
   * - :py:obj:`WorkChain <aiida.engine.processes.workchains.workchain.WorkChain>`
     - The `WorkChain` class is the principle component to implement workflows in AiiDA.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`append_ <aiida.engine.processes.workchains.context.append_>`
     - Convenience function that will construct an Awaitable for a given class instance with the context action set to APPEND. When the awaitable target is completed it will be appended to a list in the context for a key that is to be defined later
   * - :py:obj:`assign_ <aiida.engine.processes.workchains.context.assign_>`
     - Convenience function that will construct an Awaitable for a given class instance with the context action set to ASSIGN. When the awaitable target is completed it will be assigned to the context for a key that is to be defined later
   * - :py:obj:`calcfunction <aiida.engine.processes.functions.calcfunction>`
     - A decorator to turn a standard python function into a calcfunction. Example usage:
   * - :py:obj:`construct_awaitable <aiida.engine.processes.workchains.awaitable.construct_awaitable>`
     - Construct an instance of the Awaitable class that will contain the information related to the action to be taken with respect to the context once the awaitable object is completed.
   * - :py:obj:`get_object_loader <aiida.engine.persistence.get_object_loader>`
     - Return the global AiiDA object loader.
   * - :py:obj:`interruptable_task <aiida.engine.utils.interruptable_task>`
     - Turn the given coroutine into an interruptable task by turning it into an InterruptableFuture and returning it.
   * - :py:obj:`is_process_function <aiida.engine.utils.is_process_function>`
     - Return whether the given function is a process function
   * - :py:obj:`process_handler <aiida.engine.processes.workchains.utils.process_handler>`
     - Decorator to register a :class:`~aiida.engine.BaseRestartWorkChain` instance method as a process handler.
   * - :py:obj:`run <aiida.engine.launch.run>`
     - Run the process with the supplied inputs in a local runner that will block until the process is completed.
   * - :py:obj:`run_get_node <aiida.engine.launch.run_get_node>`
     - Run the process with the supplied inputs in a local runner that will block until the process is completed.
   * - :py:obj:`run_get_pk <aiida.engine.launch.run_get_pk>`
     - Run the process with the supplied inputs in a local runner that will block until the process is completed.
   * - :py:obj:`submit <aiida.engine.launch.submit>`
     - Submit the process with the supplied inputs to the daemon immediately returning control to the interpreter.
   * - :py:obj:`workfunction <aiida.engine.processes.functions.workfunction>`
     - A decorator to turn a standard python function into a workfunction. Example usage:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OutputPort <aiida.engine.processes.ports.OutputPort>`
     - 
   * - :py:obj:`PORT_NAMESPACE_SEPARATOR <aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR>`
     - 
   * - :py:obj:`ToContext <aiida.engine.processes.workchains.context.ToContext>`
     - 

External
~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ProcessState <plumpy.process_states.ProcessState>`
     - 
   * - :py:obj:`if_ <plumpy.workchains.if_>`
     - 
   * - :py:obj:`return_ <plumpy.workchains.return_>`
     - 
   * - :py:obj:`while_ <plumpy.workchains.while_>`
     - 

API
~~~

.. py:class:: AiiDAPersister
   :canonical: aiida.engine.persistence.AiiDAPersister

   Bases: :py:obj:`plumpy.persistence.Persister`

   Persister to take saved process instance states and persisting them to the database.

   .. py:method:: save_checkpoint(process: aiida.engine.processes.process.Process, tag: typing.Optional[str] = None)
      :canonical: aiida.engine.persistence.AiiDAPersister.save_checkpoint

      Persist a Process instance.

      :param process: :class:`aiida.engine.Process`
      :param tag: optional checkpoint identifier to allow distinguishing multiple checkpoints for the same process
      :raises: :class:`PersistenceError` Raised if there was a problem saving the checkpoint


   .. py:method:: load_checkpoint(pid: typing.Hashable, tag: typing.Optional[str] = None) -> plumpy.persistence.Bundle
      :canonical: aiida.engine.persistence.AiiDAPersister.load_checkpoint

      Load a process from a persisted checkpoint by its process id.

      :param pid: the process id of the :class:`plumpy.Process`
      :param tag: optional checkpoint identifier to allow retrieving a specific sub checkpoint
      :return: a bundle with the process state
      :rtype: :class:`plumpy.Bundle`
      :raises: :class:`PersistenceError` Raised if there was a problem loading the checkpoint


   .. py:method:: get_checkpoints()
      :canonical: aiida.engine.persistence.AiiDAPersister.get_checkpoints

      Return a list of all the current persisted process checkpoints

      :return: list of PersistedCheckpoint tuples with element containing the process id and optional checkpoint tag.


   .. py:method:: get_process_checkpoints(pid: typing.Hashable)
      :canonical: aiida.engine.persistence.AiiDAPersister.get_process_checkpoints

      Return a list of all the current persisted process checkpoints for the specified process.

      :param pid: the process pid
      :return: list of PersistedCheckpoint tuples with element containing the process id and optional checkpoint tag.


   .. py:method:: delete_checkpoint(pid: typing.Hashable, tag: typing.Optional[str] = None) -> None
      :canonical: aiida.engine.persistence.AiiDAPersister.delete_checkpoint

      Delete a persisted process checkpoint, where no error will be raised if the checkpoint does not exist.

      :param pid: the process id of the :class:`plumpy.Process`
      :param tag: optional checkpoint identifier to allow retrieving a specific sub checkpoint


   .. py:method:: delete_process_checkpoints(pid: typing.Hashable)
      :canonical: aiida.engine.persistence.AiiDAPersister.delete_process_checkpoints

      Delete all persisted checkpoints related to the given process id.

      :param pid: the process id of the :class:`aiida.engine.processes.process.Process`


.. py:class:: Awaitable
   :canonical: aiida.engine.processes.workchains.awaitable.Awaitable

   Bases: :py:obj:`plumpy.utils.AttributesDict`

   An attribute dictionary that represents an action that a Process could be waiting for to finish.

.. py:class:: AwaitableAction
   :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction

   Bases: :py:obj:`enum.Enum`

   Enum that describes the action to be taken for a given awaitable.

   .. py:attribute:: ASSIGN
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction.ASSIGN
      :value: 'assign'

   .. py:attribute:: APPEND
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction.APPEND
      :value: 'append'

.. py:class:: AwaitableTarget
   :canonical: aiida.engine.processes.workchains.awaitable.AwaitableTarget

   Bases: :py:obj:`enum.Enum`

   Enum that describes the class of the target a given awaitable.

   .. py:attribute:: PROCESS
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableTarget.PROCESS
      :value: 'process'

.. py:class:: BaseRestartWorkChain(*args, **kwargs)
   :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain

   Bases: :py:obj:`aiida.engine.processes.workchains.workchain.WorkChain`

   Base restart work chain.

   This work chain serves as the starting point for more complex work chains that will be designed to run a sub process
   that might need multiple restarts to come to a successful end. These restarts may be necessary because a single
   process run is not sufficient to achieve a fully converged result, or certain errors maybe encountered which
   are recoverable.

   This work chain implements the most basic functionality to achieve this goal. It will launch the sub process,
   restarting until it is completed successfully or the maximum number of iterations is reached. After completion of
   the sub process it will be inspected, and a list of process handlers are called successively. These process handlers
   are defined as class methods that are decorated with :meth:`~aiida.engine.process_handler`.

   The idea is to sub class this work chain and leverage the generic error handling that is implemented in the few
   outline methods. The minimally required outline would look something like the following::

       cls.setup
       while_(cls.should_run_process)(
           cls.run_process,
           cls.inspect_process,
       )

   Each of these methods can of course be overriden but they should be general enough to fit most process cycles. The
   `run_process` method will take the inputs for the process from the context under the key `inputs`. The user should,
   therefore, make sure that before the `run_process` method is called, that the to be used inputs are stored under
   `self.ctx.inputs`. One can update the inputs based on the results from a prior process by calling an outline method
   just before the `run_process` step, for example::

       cls.setup
       while_(cls.should_run_process)(
           cls.prepare_inputs,
           cls.run_process,
           cls.inspect_process,
       )

   Where in the `prepare_calculation` method, the inputs dictionary at `self.ctx.inputs` is updated before the next
   process will be run with those inputs.

   The `_process_class` attribute should be set to the `Process` class that should be run in the loop.
   Finally, to define handlers that will be called during the `inspect_process` simply define a class method with the
   signature `(self, node)` and decorate it with the `process_handler` decorator, for example::

       @process_handler
       def handle_problem(self, node):
           if some_problem:
               self.ctx.inputs = improved_inputs
               return ProcessHandlerReport()

   The `process_handler` and `ProcessHandlerReport` support various arguments to control the flow of the logic of the
   `inspect_process`. Refer to their respective documentation for details.


   .. py:attribute:: _process_class
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._process_class
      :type: typing.Optional[typing.Type[aiida.engine.processes.Process]]
      :value: None

   .. py:attribute:: _considered_handlers_extra
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._considered_handlers_extra
      :value: 'considered_handlers'

   .. py:property:: process_class
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.process_class
      :type: typing.Type[aiida.engine.processes.process.Process]

      Return the process class to run in the loop.

   .. py:method:: define(spec: aiida.engine.processes.ProcessSpec) -> None
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.define
      :classmethod:

      Define the process specification.

   .. py:method:: setup() -> None
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.setup

      Initialize context variables that are used during the logical flow of the `BaseRestartWorkChain`.

   .. py:method:: should_run_process() -> bool
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.should_run_process

      Return whether a new process should be run.

      This is the case as long as the last process has not finished successfully and the maximum number of restarts
      has not yet been exceeded.


   .. py:method:: run_process() -> aiida.engine.processes.workchains.context.ToContext
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.run_process

      Run the next process, taking the input dictionary from the context at `self.ctx.inputs`.

   .. py:method:: inspect_process() -> typing.Optional[aiida.engine.processes.ExitCode]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.inspect_process

      Analyse the results of the previous process and call the handlers when necessary.

      If the process is excepted or killed, the work chain will abort. Otherwise any attached handlers will be called
      in order of their specified priority. If the process was failed and no handler returns a report indicating that
      the error was handled, it is considered an unhandled process failure and the process is relaunched. If this
      happens twice in a row, the work chain is aborted. In the case that at least one handler returned a report the
      following matrix determines the logic that is followed:

          Process  Handler    Handler     Action
          result   report?    exit code
          -----------------------------------------
          Success      yes        == 0     Restart
          Success      yes        != 0     Abort
          Failed       yes        == 0     Restart
          Failed       yes        != 0     Abort

      If no handler returned a report and the process finished successfully, the work chain's work is considered done
      and it will move on to the next step that directly follows the `while` conditional, if there is one defined in
      the outline.


   .. py:method:: get_outputs(node) -> typing.Mapping[str, aiida.orm.Node]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_outputs

      Return a mapping of the outputs that should be attached as outputs to the work chain.

      By default this method returns the outputs of the last completed calculation job. This method can be overridden
      if the implementation wants to update those outputs before attaching them. Make sure that if the content of an
      output node is modified that this is done through a calcfunction in order to not lose the provenance.


   .. py:method:: results() -> typing.Optional[aiida.engine.processes.ExitCode]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.results

      Attach the outputs specified in the output specification from the last completed process.

   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.__init__

      Construct the instance.

   .. py:method:: is_process_handler(process_handler_name: typing.Union[str, types.FunctionType]) -> bool
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.is_process_handler
      :classmethod:

      Return whether the given method name corresponds to a process handler of this class.

      :param process_handler_name: string name of the instance method
      :return: boolean, True if corresponds to process handler, False otherwise


   .. py:method:: get_process_handlers() -> typing.List[types.FunctionType]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers
      :classmethod:

   .. py:method:: get_process_handlers_by_priority() -> typing.List[typing.Tuple[int, types.FunctionType]]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers_by_priority

      Return list of process handlers where overrides from ``inputs.handler_overrides`` are taken into account.

   .. py:method:: on_terminated()
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.on_terminated

      Clean the working directories of all child calculation jobs if `clean_workdir=True` in the inputs.

   .. py:method:: _wrap_bare_dict_inputs(port_namespace: aiida.engine.processes.PortNamespace, inputs: typing.Dict[str, typing.Any]) -> aiida.common.AttributeDict
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._wrap_bare_dict_inputs

      Wrap bare dictionaries in `inputs` in a `Dict` node if dictated by the corresponding inputs portnamespace.

      :param port_namespace: a `PortNamespace`
      :param inputs: a dictionary of inputs intended for submission of the process
      :return: an attribute dictionary with all bare dictionaries wrapped in `Dict` if dictated by the port namespace


.. py:class:: CalcJob(*args, **kwargs)
   :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   Implementation of the CalcJob process.

   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._node_class
      :value: None

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._spec_class
      :value: None

   .. py:attribute:: link_label_retrieved
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.link_label_retrieved
      :type: str
      :value: 'retrieved'

   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.__init__

      Construct a CalcJob instance.

      Construct the instance only if it is a sub class of `CalcJob`, otherwise raise `InvalidOperation`.

      See documentation of :class:`aiida.engine.Process`.


   .. py:method:: define(spec: aiida.engine.processes.process_spec.CalcJobProcessSpec) -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.define
      :classmethod:

      Define the process specification, including its inputs, outputs and known exit codes.

      Ports are added to the `metadata` input namespace (inherited from the base Process),
      and a `code` input Port, a `remote_folder` output Port and retrieved folder output Port
      are added.

      :param spec: the calculation job process spec to define.


   .. py:method:: spec_options()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.spec_options

      Return the metadata options port namespace of the process specification of this process.

      :return: options dictionary
      :rtype: dict


   .. py:method:: get_importer(entry_point_name: str | None = None) -> aiida.engine.processes.calcjobs.importer.CalcJobImporter
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_importer
      :classmethod:

      Load the `CalcJobImporter` associated with this `CalcJob` if it exists.

      By default an importer with the same entry point as the ``CalcJob`` will be loaded, however, this can be
      overridden using the ``entry_point_name`` argument.

      :param entry_point_name: optional entry point name of a ``CalcJobImporter`` to override the default.
      :return: the loaded ``CalcJobImporter``.
      :raises: if no importer class could be loaded.


   .. py:property:: options
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.options
      :type: aiida.common.AttributeDict

      Return the options of the metadata that were specified when this process instance was launched.

      :return: options dictionary



   .. py:method:: get_state_classes() -> typing.Dict[typing.Hashable, typing.Type[plumpy.process_states.State]]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_state_classes
      :classmethod:

      A mapping of the State constants to the corresponding state class.

      Overrides the waiting state with the Calcjob specific version.


   .. py:property:: node
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.node
      :type: aiida.orm.CalcJobNode

      Return the ProcessNode used by this process to represent itself in the database.

      :return: instance of sub class of ProcessNode


   .. py:method:: on_terminated() -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.on_terminated

      Cleanup the node by deleting the calulation job state.

      .. note:: This has to be done before calling the super because that will seal the node after we cannot change it


   .. py:method:: run() -> typing.Union[plumpy.process_states.Stop, int, plumpy.process_states.Wait]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.run

      Run the calculation job.

      This means invoking the `presubmit` and storing the temporary folder in the node's repository. Then we move the
      process in the `Wait` state, waiting for the `UPLOAD` transport task to be started.

      :returns: the `Stop` command if a dry run, int if the process has an exit status,
          `Wait` command if the calcjob is to be uploaded



   .. py:method:: prepare_for_submission(folder: aiida.common.folders.Folder) -> aiida.common.datastructures.CalcInfo
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.prepare_for_submission
      :abstractmethod:

      Prepare the calculation for submission.

      Convert the input nodes into the corresponding input files in the format that the code will expect. In addition,
      define and return a `CalcInfo` instance, which is a simple data structure that contains  information for the
      engine, for example, on what files to copy to the remote machine, what files to retrieve once it has completed,
      specific scheduler settings and more.

      :param folder: a temporary folder on the local file system.
      :returns: the `CalcInfo` instance


   .. py:method:: _setup_metadata(metadata: dict) -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_metadata

      Store the metadata on the ProcessNode.

   .. py:method:: _setup_inputs() -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_inputs

      Create the links between the input nodes and the ProcessNode that represents this process.

   .. py:method:: _perform_dry_run()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_dry_run

      Perform a dry run.

      Instead of performing the normal sequence of steps, just the `presubmit` is called, which will call the method
      `prepare_for_submission` of the plugin to generate the input files based on the inputs. Then the upload action
      is called, but using a normal local transport that will copy the files to a local sandbox folder. The generated
      input script and the absolute path to the sandbox folder are stored in the `dry_run_info` attribute of the node
      of this process.


   .. py:method:: _perform_import()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_import

      Perform the import of an already completed calculation.

      The inputs contained a `RemoteData` under the key `remote_folder` signalling that this is not supposed to be run
      as a normal calculation job, but rather the results are already computed outside of AiiDA and merely need to be
      imported.


   .. py:method:: parse(retrieved_temporary_folder: typing.Optional[str] = None, existing_exit_code: aiida.engine.processes.exit_code.ExitCode | None = None) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse

      Parse a retrieved job calculation.

      This is called once it's finished waiting for the calculation to be finished and the data has been retrieved.

      :param retrieved_temporary_folder: The path to the temporary folder



   .. py:method:: terminate(exit_code: aiida.engine.processes.exit_code.ExitCode) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.terminate
      :staticmethod:

      Terminate the process immediately and return the given exit code.

      This method is called by :meth:`aiida.engine.processes.calcjobs.tasks.Waiting.execute` if a monitor triggered
      the job to be terminated and specified the parsing to be skipped. It will construct the running state and tell
      this method to be run, which returns the given exit code which will cause the process to be terminated.

      :param exit_code: The exit code to return.
      :returns: The provided exit code.


   .. py:method:: parse_scheduler_output(retrieved: aiida.orm.Node) -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_scheduler_output

      Parse the output of the scheduler if that functionality has been implemented for the plugin.

   .. py:method:: parse_retrieved_output(retrieved_temporary_folder: typing.Optional[str] = None) -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_retrieved_output

      Parse the retrieved data by calling the parser plugin if it was defined in the inputs.

   .. py:method:: presubmit(folder: aiida.common.folders.Folder) -> aiida.common.datastructures.CalcInfo
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.presubmit

      Prepares the calculation folder with all inputs, ready to be copied to the cluster.

      :param folder: a SandboxFolder that can be used to write calculation input files and the scheduling script.

      :return calcinfo: the CalcInfo object containing the information needed by the daemon to handle operations.



.. py:class:: CalcJobImporter
   :canonical: aiida.engine.processes.calcjobs.importer.CalcJobImporter

   Bases: :py:obj:`abc.ABC`

   An abstract class, to define an importer for computations completed outside of AiiDA.

   This class is used to import the results of a calculation that was completed outside of AiiDA.
   The importer is responsible for parsing the output files of the calculation and creating the
   corresponding AiiDA nodes.


   .. py:method:: parse_remote_data(remote_data: aiida.orm.RemoteData, **kwargs) -> typing.Dict[str, typing.Union[aiida.orm.Node, typing.Dict]]
      :canonical: aiida.engine.processes.calcjobs.importer.CalcJobImporter.parse_remote_data
      :abstractmethod:
      :staticmethod:

      Parse the input nodes from the files in the provided ``RemoteData``.

      :param remote_data: the remote data node containing the raw input files.
      :param kwargs: additional keyword arguments to control the parsing process.
      :returns: a dictionary with the parsed inputs nodes that match the input spec of the associated ``CalcJob``.


.. py:class:: CalcJobOutputPort(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.CalcJobOutputPort

   Bases: :py:obj:`plumpy.ports.OutputPort`

   Sub class of plumpy.OutputPort which adds the `_pass_to_parser` attribute.

   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.ports.CalcJobOutputPort.__init__

   .. py:property:: pass_to_parser
      :canonical: aiida.engine.processes.ports.CalcJobOutputPort.pass_to_parser
      :type: bool

.. py:class:: CalcJobProcessSpec()
   :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec

   Bases: :py:obj:`aiida.engine.processes.process_spec.ProcessSpec`

   Process spec intended for the `CalcJob` process class.

   .. py:attribute:: OUTPUT_PORT_TYPE
      :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec.OUTPUT_PORT_TYPE
      :value: None

   .. py:method:: __init__() -> None
      :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec.__init__

   .. py:property:: default_output_node
      :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec.default_output_node
      :type: typing.Optional[str]

.. py:class:: DaemonClient(profile: aiida.manage.configuration.profile.Profile)
   :canonical: aiida.engine.daemon.client.DaemonClient

   Client to interact with the daemon.

   .. py:attribute:: DAEMON_ERROR_NOT_RUNNING
      :canonical: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_NOT_RUNNING
      :value: 'daemon-error-not-running'

   .. py:attribute:: DAEMON_ERROR_TIMEOUT
      :canonical: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_TIMEOUT
      :value: 'daemon-error-timeout'

   .. py:attribute:: _DAEMON_NAME
      :canonical: aiida.engine.daemon.client.DaemonClient._DAEMON_NAME
      :value: 'aiida-{name}'

   .. py:attribute:: _ENDPOINT_PROTOCOL
      :canonical: aiida.engine.daemon.client.DaemonClient._ENDPOINT_PROTOCOL
      :value: None

   .. py:method:: __init__(profile: aiida.manage.configuration.profile.Profile)
      :canonical: aiida.engine.daemon.client.DaemonClient.__init__

      Construct an instance for a given profile.

      :param profile: The profile instance.


   .. py:property:: profile
      :canonical: aiida.engine.daemon.client.DaemonClient.profile
      :type: aiida.manage.configuration.profile.Profile

   .. py:property:: daemon_name
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_name
      :type: str

      Get the daemon name which is tied to the profile name.

   .. py:property:: _verdi_bin
      :canonical: aiida.engine.daemon.client.DaemonClient._verdi_bin
      :type: str

      Return the absolute path to the ``verdi`` binary.

      :raises ConfigurationError: If the path to ``verdi`` could not be found


   .. py:method:: cmd_start_daemon(number_workers: int = 1, foreground: bool = False) -> list[str]
      :canonical: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon

      Return the command to start the daemon.

      :param number_workers: Number of daemon workers to start.
      :param foreground: Whether to launch the subprocess in the background or not.


   .. py:property:: cmd_start_daemon_worker
      :canonical: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon_worker
      :type: list[str]

      Return the command to start a daemon worker process.

   .. py:property:: loglevel
      :canonical: aiida.engine.daemon.client.DaemonClient.loglevel
      :type: str

   .. py:property:: virtualenv
      :canonical: aiida.engine.daemon.client.DaemonClient.virtualenv
      :type: str | None

   .. py:property:: circus_log_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_log_file
      :type: str

   .. py:property:: circus_pid_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_pid_file
      :type: str

   .. py:property:: circus_port_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_port_file
      :type: str

   .. py:property:: circus_socket_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_socket_file
      :type: str

   .. py:property:: circus_socket_endpoints
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_socket_endpoints
      :type: dict[str, str]

   .. py:property:: daemon_log_file
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_log_file
      :type: str

   .. py:property:: daemon_pid_file
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_pid_file
      :type: str

   .. py:method:: get_circus_port() -> int
      :canonical: aiida.engine.daemon.client.DaemonClient.get_circus_port

      Retrieve the port for the circus controller, which should be written to the circus port file.

      If the daemon is running, the port file should exist and contain the port to which the controller is connected.
      If it cannot be read, a RuntimeError will be thrown. If the daemon is not running, an available port will be
      requested from the operating system, written to the port file and returned.

      :return: The port for the circus controller.


   .. py:method:: get_env() -> dict[str, str]
      :canonical: aiida.engine.daemon.client.DaemonClient.get_env
      :staticmethod:

      Return the environment for this current process.

      This method is used to pass variables from the environment of the current process to a subprocess that is
      spawned when the daemon or a daemon worker is started.

      It replicates the ``PATH``, ``PYTHONPATH` and the ``AIIDA_PATH`` environment variables. The ``PYTHONPATH``
      variable ensures that all Python modules that can be imported by the parent process, are also importable by
      the subprocess. The ``AIIDA_PATH`` variable ensures that the subprocess will use the same AiiDA configuration
      directory as used by the current process.


   .. py:method:: get_circus_socket_directory() -> str
      :canonical: aiida.engine.daemon.client.DaemonClient.get_circus_socket_directory

      Retrieve the absolute path of the directory where the circus sockets are stored.

      If the daemon is running, the sockets file should exist and contain the absolute path of the directory that
      contains the sockets of the circus endpoints. If it cannot be read, a ``RuntimeError`` will be thrown. If the
      daemon is not running, a temporary directory will be created and its path will be written to the sockets file
      and returned.

      .. note:: A temporary folder needs to be used for the sockets because UNIX limits the filepath length to
          107 bytes. Placing the socket files in the AiiDA config folder might seem like the more logical choice
          but that folder can be placed in an arbitrarily nested directory, the socket filename will exceed the
          limit. The solution is therefore to always store them in the temporary directory of the operation system
          whose base path is typically short enough as to not exceed the limit

      :return: The absolute path of directory to write the sockets to.


   .. py:method:: get_daemon_pid() -> int | None
      :canonical: aiida.engine.daemon.client.DaemonClient.get_daemon_pid

      Get the daemon pid which should be written in the daemon pid file specific to the profile.

      :return: The pid of the circus daemon process or None if not found.


   .. py:property:: is_daemon_running
      :canonical: aiida.engine.daemon.client.DaemonClient.is_daemon_running
      :type: bool

      Return whether the daemon is running, which is determined by seeing if the daemon pid file is present.

      :return: True if daemon is running, False otherwise.


   .. py:method:: delete_circus_socket_directory() -> None
      :canonical: aiida.engine.daemon.client.DaemonClient.delete_circus_socket_directory

      Attempt to delete the directory used to store the circus endpoint sockets.

      Will not raise if the directory does not exist.


   .. py:method:: get_available_port()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_available_port
      :classmethod:

      Get an available port from the operating system.

      :return: A currently available port.


   .. py:method:: get_controller_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_controller_endpoint

      Get the endpoint string for the circus controller.

      For the IPC protocol a profile specific socket will be used, whereas for the TCP protocol an available port will
      be found and saved in the profile specific port file.

      :return: The endpoint string.


   .. py:method:: get_pubsub_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_pubsub_endpoint

      Get the endpoint string for the circus pubsub endpoint.

      For the IPC protocol a profile specific socket will be used, whereas for the TCP protocol any available port
      will be used.

      :return: The endpoint string.


   .. py:method:: get_stats_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_stats_endpoint

      Get the endpoint string for the circus stats endpoint.

      For the IPC protocol a profile specific socket will be used, whereas for the TCP protocol any available port
      will be used.

      :return: The endpoint string.


   .. py:method:: get_ipc_endpoint(endpoint)
      :canonical: aiida.engine.daemon.client.DaemonClient.get_ipc_endpoint

      Get the ipc endpoint string for a circus daemon endpoint for a given socket.

      :param endpoint: The circus endpoint for which to return a socket.
      :return: The ipc endpoint string.


   .. py:method:: get_tcp_endpoint(port=None)
      :canonical: aiida.engine.daemon.client.DaemonClient.get_tcp_endpoint

      Get the tcp endpoint string for a circus daemon endpoint.

      If the port is unspecified, the operating system will be asked for a currently available port.

      :param port: A port to use for the endpoint.
      :return: The tcp endpoint string.


   .. py:method:: get_client() -> circus.client.CircusClient
      :canonical: aiida.engine.daemon.client.DaemonClient.get_client

      Return an instance of the CircusClient.

      The endpoint is defined by the controller endpoint, which used the port that was written to the port file upon
      starting of the daemon.

      :return: CircusClient instance


   .. py:method:: call_client(command: aiida.engine.daemon.client.JsonDictType) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.call_client

      Call the client with a specific command.

      Will check whether the daemon is running first by checking for the pid file. When the pid is found yet the call
      still fails with a timeout, this means the daemon was actually not running and it was terminated unexpectedly
      causing the pid file to not be cleaned up properly.

      :param command: Command to call the circus client with.
      :return: The result of the circus client call.


   .. py:method:: get_status() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_status

      Get the daemon running status.

      :return: The client call response. If successful, will will contain 'status' key.


   .. py:method:: get_numprocesses() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_numprocesses

      Get the number of running daemon processes.

      :return: The client call response. If successful, will contain 'numprocesses' key.


   .. py:method:: get_worker_info() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_worker_info

      Get workers statistics for this daemon.

      :return: The client call response. If successful, will contain 'info' key.


   .. py:method:: get_daemon_info() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_daemon_info

      Get statistics about this daemon itself.

      :return: The client call response. If successful, will contain 'info' key.


   .. py:method:: increase_workers(number: int) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.increase_workers

      Increase the number of workers.

      :param number: The number of workers to add.
      :return: The client call response.


   .. py:method:: decrease_workers(number: int) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.decrease_workers

      Decrease the number of workers.

      :param number: The number of workers to remove.
      :return: The client call response.


   .. py:method:: stop_daemon(wait: bool = True, timeout: int = 5) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.stop_daemon

      Stop the daemon.

      :param wait: Boolean to indicate whether to wait for the result of the command.
      :param timeout: Wait this number of seconds for the ``is_daemon_running`` to return ``False`` before raising.
      :return: The client call response.
      :raises DaemonException: If ``is_daemon_running`` returns ``True`` after the ``timeout`` has passed.


   .. py:method:: restart_daemon(wait: bool) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.restart_daemon

      Restart the daemon.

      :param wait: Boolean to indicate whether to wait for the result of the command.
      :return: The client call response.


   .. py:method:: start_daemon(number_workers: int = 1, foreground: bool = False, timeout: int = 5) -> None
      :canonical: aiida.engine.daemon.client.DaemonClient.start_daemon

      Start the daemon in a sub process running in the background.

      :param number_workers: Number of daemon workers to start.
      :param foreground: Whether to launch the subprocess in the background or not.
      :param timeout: Wait this number of seconds for the ``is_daemon_running`` to return ``True`` before raising.
      :raises DaemonException: If the daemon fails to start.
      :raises DaemonException: If the daemon starts but then is unresponsive or in an unexpected state.
      :raises DaemonException: If ``is_daemon_running`` returns ``False`` after the ``timeout`` has passed.


   .. py:method:: _await_condition(condition: typing.Callable, exception: Exception, timeout: int = 5, interval: float = 0.1)
      :canonical: aiida.engine.daemon.client.DaemonClient._await_condition
      :staticmethod:

      Await a condition to evaluate to ``True`` or raise the exception if the timeout is reached.

      :param condition: A callable that is waited for to return ``True``.
      :param exception: Raise this exception if ``condition`` does not return ``True`` after ``timeout`` seconds.
      :param timeout: Wait this number of seconds for ``condition`` to return ``True`` before raising.
      :param interval: The time in seconds to wait between invocations of ``condition``.
      :raises: The exception provided by ``exception`` if timeout is reached.


   .. py:method:: _start_daemon(number_workers: int = 1, foreground: bool = False) -> None
      :canonical: aiida.engine.daemon.client.DaemonClient._start_daemon

      Start the daemon.

      .. warning:: This will daemonize the current process and put it in the background. It is most likely not what
          you want to call if you want to start the daemon from the Python API. Instead you probably will want to use
          the :meth:`aiida.engine.daemon.client.DaemonClient.start_daemon` function instead.

      :param number_workers: Number of daemon workers to start.
      :param foreground: Whether to launch the subprocess in the background or not.


.. py:class:: ExitCode
   :canonical: aiida.engine.processes.exit_code.ExitCode

   Bases: :py:obj:`typing.NamedTuple`

   A simple data class to define an exit code for a :class:`~aiida.engine.processes.process.Process`.

   When an instance of this class is returned from a `Process._run()` call, it will be interpreted that the `Process`
   should be terminated and that the exit status and message of the namedtuple should be set to the corresponding
   attributes of the node.

   :param status: positive integer exit status, where a non-zero value indicated the process failed, default is `0`
   :param message: optional message with more details about the failure mode
   :param invalidates_cache: optional flag, indicating that a process should not be used in caching


   .. py:attribute:: status
      :canonical: aiida.engine.processes.exit_code.ExitCode.status
      :type: int
      :value: 0

   .. py:attribute:: message
      :canonical: aiida.engine.processes.exit_code.ExitCode.message
      :type: typing.Optional[str]
      :value: None

   .. py:attribute:: invalidates_cache
      :canonical: aiida.engine.processes.exit_code.ExitCode.invalidates_cache
      :type: bool
      :value: False

   .. py:method:: format(**kwargs: str) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.exit_code.ExitCode.format

      Create a clone of this exit code where the template message is replaced by the keyword arguments.

      :param kwargs: replacement parameters for the template message



.. py:class:: ExitCodesNamespace(dictionary=None)
   :canonical: aiida.engine.processes.exit_code.ExitCodesNamespace

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   A namespace of `ExitCode` instances that can be accessed through getattr as well as getitem.

   Additionally, the collection can be called with an identifier, that can either reference the integer `status` of the
   `ExitCode` that needs to be retrieved or the key in the collection.


   .. py:method:: __call__(identifier: typing.Union[int, str]) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.exit_code.ExitCodesNamespace.__call__

      Return a specific exit code identified by either its exit status or label.

      :param identifier: the identifier of the exit code. If the type is integer, it will be interpreted as the exit
          code status, otherwise it be interpreted as the exit code label

      :returns: an `ExitCode` instance

      :raises ValueError: if no exit code with the given label is defined for this process


.. py:class:: FunctionProcess(*args, **kwargs)
   :canonical: aiida.engine.processes.functions.FunctionProcess

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   Function process class used for turning functions into a Process

   .. py:attribute:: _func_args
      :canonical: aiida.engine.processes.functions.FunctionProcess._func_args
      :type: typing.Sequence[str]
      :value: ()

   .. py:method:: _func(*_args, **_kwargs) -> dict
      :canonical: aiida.engine.processes.functions.FunctionProcess._func
      :staticmethod:

      This is used internally to store the actual function that is being
      wrapped and will be replaced by the build method.


   .. py:method:: build(func: typing.Callable[..., typing.Any], node_class: typing.Type[aiida.orm.ProcessNode]) -> typing.Type[aiida.engine.processes.functions.FunctionProcess]
      :canonical: aiida.engine.processes.functions.FunctionProcess.build
      :staticmethod:

      Build a Process from the given function.

      All function arguments will be assigned as process inputs. If keyword arguments are specified then
      these will also become inputs.

      :param func: The function to build a process from
      :param node_class: Provide a custom node class to be used, has to be constructable with no arguments. It has to
          be a sub class of `ProcessNode` and the mixin :class:`~aiida.orm.utils.mixins.FunctionCalculationMixin`.

      :return: A Process class that represents the function



   .. py:method:: validate_inputs(*args: typing.Any, **kwargs: typing.Any) -> None
      :canonical: aiida.engine.processes.functions.FunctionProcess.validate_inputs
      :classmethod:

      Validate the positional and keyword arguments passed in the function call.

      :raises TypeError: if more positional arguments are passed than the function defines


   .. py:method:: create_inputs(*args: typing.Any, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.functions.FunctionProcess.create_inputs
      :classmethod:

      Create the input args for the FunctionProcess.

   .. py:method:: args_to_dict(*args: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.functions.FunctionProcess.args_to_dict
      :classmethod:

      Create an input dictionary (of form label -> value) from supplied args.

      :param args: The values to use for the dictionary

      :return: A label -> value dictionary



   .. py:method:: get_or_create_db_record() -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.functions.FunctionProcess.get_or_create_db_record
      :classmethod:

   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.functions.FunctionProcess.__init__

   .. py:property:: process_class
      :canonical: aiida.engine.processes.functions.FunctionProcess.process_class
      :type: typing.Callable[..., typing.Any]

      Return the class that represents this Process, for the FunctionProcess this is the function itself.

      For a standard Process or sub class of Process, this is the class itself. However, for legacy reasons,
      the Process class is a wrapper around another class. This function returns that original class, i.e. the
      class that really represents what was being executed.

      :return: A Process class that represents the function



   .. py:method:: execute() -> typing.Optional[typing.Dict[str, typing.Any]]
      :canonical: aiida.engine.processes.functions.FunctionProcess.execute

      Execute the process.

   .. py:method:: _setup_db_record() -> None
      :canonical: aiida.engine.processes.functions.FunctionProcess._setup_db_record

      Set up the database record for the process.

   .. py:method:: run() -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.functions.FunctionProcess.run

      Run the process.

.. py:class:: InputPort(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.InputPort

   Bases: :py:obj:`aiida.engine.processes.ports.WithSerialize`, :py:obj:`aiida.engine.processes.ports.WithNonDb`, :py:obj:`plumpy.ports.InputPort`

   Sub class of plumpy.InputPort which mixes in the WithSerialize and WithNonDb mixins to support automatic
   value serialization to database storable types and support non database storable input types as well.


   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.ports.InputPort.__init__

      Override the constructor to check the type of the default if set and warn if not immutable.

   .. py:method:: get_description() -> typing.Dict[str, str]
      :canonical: aiida.engine.processes.ports.InputPort.get_description

      Return a description of the InputPort, which will be a dictionary of its attributes

      :returns: a dictionary of the stringified InputPort attributes


.. py:class:: InterruptableFuture(*, loop=None)
   :canonical: aiida.engine.utils.InterruptableFuture

   Bases: :py:obj:`asyncio.Future`

   A future that can be interrupted by calling `interrupt`.

   .. py:method:: interrupt(reason: Exception) -> None
      :canonical: aiida.engine.utils.InterruptableFuture.interrupt

      This method should be called to interrupt the coroutine represented by this InterruptableFuture.

   .. py:method:: with_interrupt(coro: typing.Awaitable[typing.Any]) -> typing.Any
      :canonical: aiida.engine.utils.InterruptableFuture.with_interrupt
      :async:

      return result of a coroutine which will be interrupted if this future is interrupted ::

          import asyncio
          loop = asyncio.get_event_loop()

          interruptable = InterutableFuture()
          loop.call_soon(interruptable.interrupt, RuntimeError("STOP"))
          loop.run_until_complete(interruptable.with_interrupt(asyncio.sleep(2.)))
          >>> RuntimeError: STOP


      :param coro: The coroutine that can be interrupted
      :return: The result of the coroutine


.. py:class:: JobManager(transport_queue: aiida.engine.transports.TransportQueue)
   :canonical: aiida.engine.processes.calcjobs.manager.JobManager

   A manager for :py:class:`~aiida.engine.processes.calcjobs.calcjob.CalcJob` submitted to ``Computer`` instances.

   When a calculation job is submitted to a :py:class:`~aiida.orm.computers.Computer`, it actually uses a specific
   :py:class:`~aiida.orm.authinfos.AuthInfo`, which is a computer configured for a :py:class:`~aiida.orm.users.User`.
   The ``JobManager`` maintains a mapping of :py:class:`~aiida.engine.processes.calcjobs.manager.JobsList` instances
   for each authinfo that has active calculation jobs. These jobslist instances are then responsible for bundling
   scheduler updates for all the jobs they maintain (i.e. that all share the same authinfo) and update their status.

   As long as a :py:class:`~aiida.engine.runners.Runner` will create a single ``JobManager`` instance and use that for
   its lifetime, the guarantees made by the ``JobsList`` about respecting the minimum polling interval of the scheduler
   will be maintained. Note, however, that since each ``Runner`` will create its own job manager, these guarantees
   only hold per runner.


   .. py:method:: __init__(transport_queue: aiida.engine.transports.TransportQueue) -> None
      :canonical: aiida.engine.processes.calcjobs.manager.JobManager.__init__

   .. py:method:: get_jobs_list(authinfo: aiida.orm.AuthInfo) -> aiida.engine.processes.calcjobs.manager.JobsList
      :canonical: aiida.engine.processes.calcjobs.manager.JobManager.get_jobs_list

      Get or create a new `JobLists` instance for the given authinfo.

      :param authinfo: the `AuthInfo`
      :return: a `JobsList` instance


   .. py:method:: request_job_info_update(authinfo: aiida.orm.AuthInfo, job_id: typing.Hashable) -> typing.Iterator[asyncio.Future[JobInfo]]
      :canonical: aiida.engine.processes.calcjobs.manager.JobManager.request_job_info_update

      Get a future that will resolve to information about a given job.

      This is a context manager so that if the user leaves the context the request is automatically cancelled.



.. py:class:: JobsList(authinfo: aiida.orm.AuthInfo, transport_queue: aiida.engine.transports.TransportQueue, last_updated: typing.Optional[float] = None)
   :canonical: aiida.engine.processes.calcjobs.manager.JobsList

   Manager of calculation jobs submitted with a specific ``AuthInfo``, i.e. computer configured for a specific user.

   This container of active calculation jobs is used to update their status periodically in batches, ensuring that
   even when a lot of jobs are running, the scheduler update command is not triggered for each job individually.

   In addition, the :py:class:`~aiida.orm.computers.Computer` for which the :py:class:`~aiida.orm.authinfos.AuthInfo`
   is configured, can define a minimum polling interval. This class will guarantee that the time between update calls
   to the scheduler is larger or equal to that minimum interval.

   Note that since each instance operates on a specific authinfo, the guarantees of batching scheduler update calls
   and the limiting of number of calls per unit time, through the minimum polling interval, is only applicable for jobs
   launched with that particular authinfo. If multiple authinfo instances with the same computer, have active jobs
   these limitations are not respected between them, since there is no communication between ``JobsList`` instances.
   See the :py:class:`~aiida.engine.processes.calcjobs.manager.JobManager` for example usage.


   .. py:method:: __init__(authinfo: aiida.orm.AuthInfo, transport_queue: aiida.engine.transports.TransportQueue, last_updated: typing.Optional[float] = None)
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.__init__

      Construct an instance for the given authinfo and transport queue.

      :param authinfo: The authinfo used to check the jobs list
      :param transport_queue: A transport queue
      :param last_updated: initialize the last updated timestamp



   .. py:property:: logger
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.logger
      :type: logging.Logger

      Return the logger configured for this instance.

      :return: the logger


   .. py:method:: get_minimum_update_interval() -> float
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.get_minimum_update_interval

      Get the minimum interval that should be respected between updates of the list.

      :return: the minimum interval



   .. py:property:: last_updated
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.last_updated
      :type: typing.Optional[float]

      Get the timestamp of when the list was last updated as produced by `time.time()`

      :return: The last update point



   .. py:method:: _get_jobs_from_scheduler() -> typing.Dict[typing.Hashable, aiida.schedulers.datastructures.JobInfo]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_from_scheduler
      :async:

      Get the current jobs list from the scheduler.

      :return: a mapping of job ids to :py:class:`~aiida.schedulers.datastructures.JobInfo` instances



   .. py:method:: _update_job_info() -> None
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._update_job_info
      :async:

      Update all of the job information objects.

      This will set the futures for all pending update requests where the corresponding job has a new status compared
      to the last update.


   .. py:method:: request_job_info_update(job_id: typing.Hashable) -> typing.Iterator[asyncio.Future[JobInfo]]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.request_job_info_update

      Request job info about a job when the job next changes state.

      If the job is not found in the jobs list at the update, the future will resolve to `None`.

      :param job_id: job identifier
      :return: future that will resolve to a `JobInfo` object when the job changes state


   .. py:method:: _ensure_updating() -> None
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._ensure_updating

      Ensure that we are updating the job list from the remote resource.

      This will automatically stop if there are no outstanding requests.


   .. py:method:: _has_job_state_changed(old: typing.Optional[aiida.schedulers.datastructures.JobInfo], new: typing.Optional[aiida.schedulers.datastructures.JobInfo]) -> bool
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._has_job_state_changed
      :staticmethod:

      Return whether the states `old` and `new` are different.


        

   .. py:method:: _get_next_update_delay() -> float
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_next_update_delay

      Calculate when we are next allowed to poll the scheduler.

      This delay is calculated as the minimum polling interval defined by the authentication info for this instance,
      minus time elapsed since the last update.

      :return: delay (in seconds) after which the scheduler may be polled again



   .. py:method:: _update_requests_outstanding() -> bool
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._update_requests_outstanding

   .. py:method:: _get_jobs_with_scheduler() -> typing.List[str]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_with_scheduler

      Get all the jobs that are currently with scheduler.

      :return: the list of jobs with the scheduler
      :rtype: list


.. py:class:: ObjectLoader
   :canonical: aiida.engine.persistence.ObjectLoader

   Bases: :py:obj:`plumpy.loaders.DefaultObjectLoader`

   Custom object loader for `aiida-core`.

   .. py:method:: load_object(identifier: str) -> typing.Any
      :canonical: aiida.engine.persistence.ObjectLoader.load_object

      Attempt to load the object identified by the given `identifier`.

      .. note:: We override the `plumpy.DefaultObjectLoader` to be able to throw an `ImportError` instead of a
          `ValueError` which in the context of `aiida-core` is not as apt, since we are loading classes.

      :param identifier: concatenation of module and resource name
      :return: loaded object
      :raises ImportError: if the object cannot be loaded


.. py:data:: OutputPort
   :canonical: aiida.engine.processes.ports.OutputPort
   :value: None

.. py:data:: PORT_NAMESPACE_SEPARATOR
   :canonical: aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR
   :value: '__'

.. py:exception:: PastException()
   :canonical: aiida.engine.exceptions.PastException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when an attempt is made to continue a Process that has already excepted before.

.. py:class:: PortNamespace(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.PortNamespace

   Bases: :py:obj:`aiida.engine.processes.ports.WithNonDb`, :py:obj:`plumpy.ports.PortNamespace`

   Sub class of plumpy.PortNamespace which implements the serialize method to support automatic recursive
   serialization of a given mapping onto the ports of the PortNamespace.


   .. py:method:: __setitem__(key: str, port: plumpy.ports.Port) -> None
      :canonical: aiida.engine.processes.ports.PortNamespace.__setitem__

      Ensure that a `Port` being added inherits the `non_db` attribute if not explicitly defined at construction.

      The reasoning is that if a `PortNamespace` has `non_db=True`, which is different from the default value, very
      often all leaves should be also `non_db=True`. To prevent a user from having to specify it manually everytime
      we overload the value here, unless it was specifically set during construction.

      Note that the `non_db` attribute is not present for all `Port` sub classes so we have to check for it first.


   .. py:method:: validate_port_name(port_name: str) -> None
      :canonical: aiida.engine.processes.ports.PortNamespace.validate_port_name
      :staticmethod:

      Validate the given port name.

      Valid port names adhere to the following restrictions:

          * Is a valid link label (see below)
          * Does not contain two or more consecutive underscores

      Valid link labels adhere to the following restrictions:

          * Has to be a valid python identifier
          * Can only contain alphanumeric characters and underscores
          * Can not start or end with an underscore

      :param port_name: the proposed name of the port to be added
      :raise TypeError: if the port name is not a string type
      :raise ValueError: if the port name is invalid


   .. py:method:: serialize(mapping: typing.Optional[typing.Dict[str, typing.Any]], breadcrumbs: typing.Sequence[str] = ()) -> typing.Optional[typing.Dict[str, typing.Any]]
      :canonical: aiida.engine.processes.ports.PortNamespace.serialize

      Serialize the given mapping onto this `Portnamespace`.

      It will recursively call this function on any nested `PortNamespace` or the serialize function on any `Ports`.

      :param mapping: a mapping of values to be serialized
      :param breadcrumbs: a tuple with the namespaces of parent namespaces
      :returns: the serialized mapping


.. py:class:: Process(inputs: typing.Optional[typing.Dict[str, typing.Any]] = None, logger: typing.Optional[logging.Logger] = None, runner: typing.Optional[aiida.engine.runners.Runner] = None, parent_pid: typing.Optional[int] = None, enable_persistence: bool = True)
   :canonical: aiida.engine.processes.process.Process

   Bases: :py:obj:`plumpy.processes.Process`

   This class represents an AiiDA process which can be executed and will
   have full provenance saved in the database.


   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.process.Process._node_class
      :value: None

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.process.Process._spec_class
      :value: None

   .. py:attribute:: SINGLE_OUTPUT_LINKNAME
      :canonical: aiida.engine.processes.process.Process.SINGLE_OUTPUT_LINKNAME
      :type: str
      :value: 'result'

   .. py:class:: SaveKeys
      :canonical: aiida.engine.processes.process.Process.SaveKeys

      Bases: :py:obj:`enum.Enum`

      Keys used to identify things in the saved instance state bundle.


      .. py:attribute:: CALC_ID
         :canonical: aiida.engine.processes.process.Process.SaveKeys.CALC_ID
         :type: str
         :value: 'calc_id'

   .. py:method:: spec() -> aiida.engine.processes.process_spec.ProcessSpec
      :canonical: aiida.engine.processes.process.Process.spec
      :classmethod:

   .. py:method:: define(spec: aiida.engine.processes.process_spec.ProcessSpec) -> None
      :canonical: aiida.engine.processes.process.Process.define
      :classmethod:

      Define the specification of the process, including its inputs, outputs and known exit codes.

      A `metadata` input namespace is defined, with optional ports that are not stored in the database.



   .. py:method:: get_builder() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.engine.processes.process.Process.get_builder
      :classmethod:

   .. py:method:: get_or_create_db_record() -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.process.Process.get_or_create_db_record
      :classmethod:

      Create a process node that represents what happened in this process.

      :return: A process node


   .. py:method:: __init__(inputs: typing.Optional[typing.Dict[str, typing.Any]] = None, logger: typing.Optional[logging.Logger] = None, runner: typing.Optional[aiida.engine.runners.Runner] = None, parent_pid: typing.Optional[int] = None, enable_persistence: bool = True) -> None
      :canonical: aiida.engine.processes.process.Process.__init__

      Process constructor.

      :param inputs: process inputs
      :param logger: aiida logger
      :param runner: process runner
      :param parent_pid: id of parent process
      :param enable_persistence: whether to persist this process



   .. py:method:: init() -> None
      :canonical: aiida.engine.processes.process.Process.init

   .. py:method:: get_exit_statuses(exit_code_labels: typing.Iterable[str]) -> typing.List[int]
      :canonical: aiida.engine.processes.process.Process.get_exit_statuses
      :classmethod:

      Return the exit status (integers) for the given exit code labels.

      :param exit_code_labels: a list of strings that reference exit code labels of this process class
      :return: list of exit status integers that correspond to the given exit code labels
      :raises AttributeError: if at least one of the labels does not correspond to an existing exit code


   .. py:method:: exit_codes() -> aiida.engine.processes.exit_code.ExitCodesNamespace
      :canonical: aiida.engine.processes.process.Process.exit_codes

      Return the namespace of exit codes defined for this WorkChain through its ProcessSpec.

      The namespace supports getitem and getattr operations with an ExitCode label to retrieve a specific code.
      Additionally, the namespace can also be called with either the exit code integer status to retrieve it.

      :returns: ExitCodesNamespace of ExitCode named tuples



   .. py:method:: spec_metadata() -> aiida.engine.processes.ports.PortNamespace
      :canonical: aiida.engine.processes.process.Process.spec_metadata

      Return the metadata port namespace of the process specification of this process.

   .. py:property:: node
      :canonical: aiida.engine.processes.process.Process.node
      :type: aiida.orm.ProcessNode

      Return the ProcessNode used by this process to represent itself in the database.

      :return: instance of sub class of ProcessNode


   .. py:property:: uuid
      :canonical: aiida.engine.processes.process.Process.uuid
      :type: str

      Return the UUID of the process which corresponds to the UUID of its associated `ProcessNode`.

      :return: the UUID associated to this process instance


   .. py:property:: metadata
      :canonical: aiida.engine.processes.process.Process.metadata
      :type: aiida.common.extendeddicts.AttributeDict

      Return the metadata that were specified when this process instance was launched.

      :return: metadata dictionary



   .. py:method:: _save_checkpoint() -> None
      :canonical: aiida.engine.processes.process.Process._save_checkpoint

      Save the current state in a chechpoint if persistence is enabled and the process state is not terminal

      If the persistence call excepts with a PersistenceError, it will be caught and a warning will be logged.


   .. py:method:: save_instance_state(out_state: typing.MutableMapping[str, typing.Any], save_context: typing.Optional[plumpy.persistence.LoadSaveContext]) -> None
      :canonical: aiida.engine.processes.process.Process.save_instance_state

      Save instance state.

      See documentation of :meth:`!plumpy.processes.Process.save_instance_state`.


   .. py:method:: get_provenance_inputs_iterator() -> typing.Iterator[typing.Tuple[str, typing.Union[aiida.engine.processes.ports.InputPort, aiida.engine.processes.ports.PortNamespace]]]
      :canonical: aiida.engine.processes.process.Process.get_provenance_inputs_iterator

      Get provenance input iterator.

      :rtype: filter


   .. py:method:: load_instance_state(saved_state: typing.MutableMapping[str, typing.Any], load_context: plumpy.persistence.LoadSaveContext) -> None
      :canonical: aiida.engine.processes.process.Process.load_instance_state

      Load instance state.

      :param saved_state: saved instance state
      :param load_context:



   .. py:method:: kill(msg: typing.Union[str, None] = None) -> typing.Union[bool, plumpy.futures.Future]
      :canonical: aiida.engine.processes.process.Process.kill

      Kill the process and all the children calculations it called

      :param msg: message


   .. py:method:: out(output_port: str, value: typing.Any = None) -> None
      :canonical: aiida.engine.processes.process.Process.out

      Attach output to output port.

      The name of the port will be used as the link label.

      :param output_port: name of output port
      :param value: value to put inside output port



   .. py:method:: out_many(out_dict: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.engine.processes.process.Process.out_many

      Attach outputs to multiple output ports.

      Keys of the dictionary will be used as output port names, values as outputs.

      :param out_dict: output dictionary
      :type out_dict: dict


   .. py:method:: on_create() -> None
      :canonical: aiida.engine.processes.process.Process.on_create

      Called when a Process is created.

   .. py:method:: on_entered(from_state: typing.Optional[plumpy.process_states.State]) -> None
      :canonical: aiida.engine.processes.process.Process.on_entered

      After entering a new state, save a checkpoint and update the latest process state change timestamp.

   .. py:method:: on_terminated() -> None
      :canonical: aiida.engine.processes.process.Process.on_terminated

      Called when a Process enters a terminal state.

   .. py:method:: on_except(exc_info: typing.Tuple[typing.Any, Exception, types.TracebackType]) -> None
      :canonical: aiida.engine.processes.process.Process.on_except

      Log the exception by calling the report method with formatted stack trace from exception info object
      and store the exception string as a node attribute

      :param exc_info: the sys.exc_info() object (type, value, traceback)


   .. py:method:: on_finish(result: typing.Union[int, aiida.engine.processes.exit_code.ExitCode], successful: bool) -> None
      :canonical: aiida.engine.processes.process.Process.on_finish

      Set the finish status on the process node.

      :param result: result of the process
      :param successful: whether execution was successful



   .. py:method:: on_paused(msg: typing.Optional[str] = None) -> None
      :canonical: aiida.engine.processes.process.Process.on_paused

      The Process was paused so set the paused attribute on the process node

      :param msg: message



   .. py:method:: on_playing() -> None
      :canonical: aiida.engine.processes.process.Process.on_playing

      The Process was unpaused so remove the paused attribute on the process node


   .. py:method:: on_output_emitting(output_port: str, value: typing.Any) -> None
      :canonical: aiida.engine.processes.process.Process.on_output_emitting

      The process has emitted a value on the given output port.

      :param output_port: The output port name the value was emitted on
      :param value: The value emitted



   .. py:method:: set_status(status: typing.Optional[str]) -> None
      :canonical: aiida.engine.processes.process.Process.set_status

      The status of the Process is about to be changed, so we reflect this is in node's attribute proxy.

      :param status: the status message



   .. py:method:: submit(process: typing.Type[aiida.engine.processes.process.Process], **kwargs) -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.process.Process.submit

      Submit process for execution.

      :param process: process
      :return: the calculation node of the process



   .. py:property:: runner
      :canonical: aiida.engine.processes.process.Process.runner
      :type: aiida.engine.runners.Runner

      Get process runner.

   .. py:method:: get_parent_calc() -> typing.Optional[aiida.orm.ProcessNode]
      :canonical: aiida.engine.processes.process.Process.get_parent_calc

      Get the parent process node

      :return: the parent process node if there is one



   .. py:method:: build_process_type() -> str
      :canonical: aiida.engine.processes.process.Process.build_process_type
      :classmethod:

      The process type.

      :return: string of the process type

      Note: This could be made into a property 'process_type' but in order to have it be a property of the class
      it would need to be defined in the metaclass, see https://bugs.python.org/issue20659


   .. py:method:: report(msg: str, *args, **kwargs) -> None
      :canonical: aiida.engine.processes.process.Process.report

      Log a message to the logger, which should get saved to the database through the attached DbLogHandler.

      The pk, class name and function name of the caller are prepended to the given message

      :param msg: message to log
      :param args: args to pass to the log call
      :param kwargs: kwargs to pass to the log call



   .. py:method:: _create_and_setup_db_record() -> typing.Union[int, uuid.UUID]
      :canonical: aiida.engine.processes.process.Process._create_and_setup_db_record

      Create and setup the database record for this process

      :return: the uuid or pk of the process



   .. py:method:: encode_input_args(inputs: typing.Dict[str, typing.Any]) -> str
      :canonical: aiida.engine.processes.process.Process.encode_input_args

      Encode input arguments such that they may be saved in a Bundle

      :param inputs: A mapping of the inputs as passed to the process
      :return: The encoded (serialized) inputs


   .. py:method:: decode_input_args(encoded: str) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process.decode_input_args

      Decode saved input arguments as they came from the saved instance state Bundle

      :param encoded: encoded (serialized) inputs
      :return: The decoded input args


   .. py:method:: update_outputs() -> None
      :canonical: aiida.engine.processes.process.Process.update_outputs

      Attach new outputs to the node since the last call.

      Does nothing, if self.metadata.store_provenance is False.


   .. py:method:: _build_process_label() -> str
      :canonical: aiida.engine.processes.process.Process._build_process_label

      Construct the process label that should be set on ``ProcessNode`` instances for this process class.

      .. note:: By default this returns the name of the process class itself. It can be overridden by ``Process``
          subclasses to provide a more specific label.

      :returns: The process label to use for ``ProcessNode`` instances.


   .. py:method:: _setup_db_record() -> None
      :canonical: aiida.engine.processes.process.Process._setup_db_record

      Create the database record for this process and the links with respect to its inputs

      This function will set various attributes on the node that serve as a proxy for attributes of the Process.
      This is essential as otherwise this information could only be introspected through the Process itself, which
      is only available to the interpreter that has it in memory. To make this data introspectable from any
      interpreter, for example for the command line interface, certain Process attributes are proxied through the
      calculation node.

      In addition, the parent calculation will be setup with a CALL link if applicable and all inputs will be
      linked up as well.


   .. py:method:: _setup_version_info() -> None
      :canonical: aiida.engine.processes.process.Process._setup_version_info

      Store relevant plugin version information.

   .. py:method:: _setup_metadata(metadata: dict) -> None
      :canonical: aiida.engine.processes.process.Process._setup_metadata

      Store the metadata on the ProcessNode.

   .. py:method:: _setup_inputs() -> None
      :canonical: aiida.engine.processes.process.Process._setup_inputs

      Create the links between the input nodes and the ProcessNode that represents this process.

   .. py:method:: _flat_inputs() -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process._flat_inputs

      Return a flattened version of the parsed inputs dictionary.

      The eventual keys will be a concatenation of the nested keys. Note that the `metadata` dictionary, if present,
      is not passed, as those are dealt with separately in `_setup_metadata`.

      :return: flat dictionary of parsed inputs



   .. py:method:: _flat_outputs() -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process._flat_outputs

      Return a flattened version of the registered outputs dictionary.

      The eventual keys will be a concatenation of the nested keys.

      :return: flat dictionary of parsed outputs


   .. py:method:: _flatten_inputs(port: typing.Union[None, aiida.engine.processes.ports.InputPort, aiida.engine.processes.ports.PortNamespace], port_value: typing.Any, parent_name: str = '', separator: str = PORT_NAMESPACE_SEPARATOR) -> typing.List[typing.Tuple[str, typing.Any]]
      :canonical: aiida.engine.processes.process.Process._flatten_inputs

      Function that will recursively flatten the inputs dictionary, omitting inputs for ports that
      are marked as being non database storable

      :param port: port against which to map the port value, can be InputPort or PortNamespace
      :param port_value: value for the current port, can be a Mapping
      :param parent_name: the parent key with which to prefix the keys
      :param separator: character to use for the concatenation of keys
      :return: flat list of inputs



   .. py:method:: _flatten_outputs(port: typing.Union[None, aiida.engine.processes.ports.OutputPort, aiida.engine.processes.ports.PortNamespace], port_value: typing.Any, parent_name: str = '', separator: str = PORT_NAMESPACE_SEPARATOR) -> typing.List[typing.Tuple[str, typing.Any]]
      :canonical: aiida.engine.processes.process.Process._flatten_outputs

      Function that will recursively flatten the outputs dictionary.

      :param port: port against which to map the port value, can be OutputPort or PortNamespace
      :param port_value: value for the current port, can be a Mapping
      :param parent_name: the parent key with which to prefix the keys
      :param separator: character to use for the concatenation of keys

      :return: flat list of outputs



   .. py:method:: exposed_inputs(process_class: typing.Type[aiida.engine.processes.process.Process], namespace: typing.Optional[str] = None, agglomerate: bool = True) -> aiida.common.extendeddicts.AttributeDict
      :canonical: aiida.engine.processes.process.Process.exposed_inputs

      Gather a dictionary of the inputs that were exposed for a given Process class under an optional namespace.

      :param process_class: Process class whose inputs to try and retrieve
      :param namespace: PortNamespace in which to look for the inputs
      :param agglomerate: If set to true, all parent namespaces of the given ``namespace`` will also be
          searched for inputs. Inputs in lower-lying namespaces take precedence.

      :returns: exposed inputs



   .. py:method:: exposed_outputs(node: aiida.orm.ProcessNode, process_class: typing.Type[aiida.engine.processes.process.Process], namespace: typing.Optional[str] = None, agglomerate: bool = True) -> aiida.common.extendeddicts.AttributeDict
      :canonical: aiida.engine.processes.process.Process.exposed_outputs

      Return the outputs which were exposed from the ``process_class`` and emitted by the specific ``node``

      :param node: process node whose outputs to try and retrieve
      :param namespace: Namespace in which to search for exposed outputs.
      :param agglomerate: If set to true, all parent namespaces of the given ``namespace`` will also
          be searched for outputs. Outputs in lower-lying namespaces take precedence.

      :returns: exposed outputs



   .. py:method:: _get_namespace_list(namespace: typing.Optional[str] = None, agglomerate: bool = True) -> typing.List[typing.Optional[str]]
      :canonical: aiida.engine.processes.process.Process._get_namespace_list
      :staticmethod:

      Get the list of namespaces in a given namespace.

      :param namespace: name space
      :param agglomerate: If set to true, all parent namespaces of the given ``namespace`` will also
          be searched.

      :returns: namespace list



   .. py:method:: is_valid_cache(node: aiida.orm.ProcessNode) -> bool
      :canonical: aiida.engine.processes.process.Process.is_valid_cache
      :classmethod:

      Check if the given node can be cached from.

      Overriding this method allows ``Process`` sub-classes to modify when
      corresponding process nodes are considered as a cache.

      .. warning :: When overriding this method, make sure to return ``False``
          *at least* in all cases when ``super()._node.base.caching.is_valid_cache(node)``
          returns ``False``. Otherwise, the ``invalidates_cache`` keyword on exit
          codes may have no effect.



.. py:class:: ProcessBuilder(process_class: typing.Type[aiida.engine.processes.process.Process])
   :canonical: aiida.engine.processes.builder.ProcessBuilder

   Bases: :py:obj:`aiida.engine.processes.builder.ProcessBuilderNamespace`

   A process builder that helps setting up the inputs for creating a new process.

   .. py:method:: __init__(process_class: typing.Type[aiida.engine.processes.process.Process])
      :canonical: aiida.engine.processes.builder.ProcessBuilder.__init__

      Construct a `ProcessBuilder` instance for the given `Process` class.

      :param process_class: the `Process` subclass


   .. py:property:: process_class
      :canonical: aiida.engine.processes.builder.ProcessBuilder.process_class
      :type: typing.Type[aiida.engine.processes.process.Process]

      Return the process class for which this builder is constructed.

   .. py:method:: _repr_pretty_(p, _) -> str
      :canonical: aiida.engine.processes.builder.ProcessBuilder._repr_pretty_

      Pretty representation for in the IPython console and notebooks.

.. py:class:: ProcessBuilderNamespace(port_namespace: aiida.engine.processes.ports.PortNamespace)
   :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace

   Bases: :py:obj:`collections.abc.MutableMapping`

   Input namespace for the `ProcessBuilder`.

   Dynamically generates the getters and setters for the input ports of a given PortNamespace


   .. py:method:: __init__(port_namespace: aiida.engine.processes.ports.PortNamespace) -> None
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__init__

      Dynamically construct the get and set properties for the ports of the given port namespace.

      For each port in the given port namespace a get and set property will be constructed dynamically
      and added to the ProcessBuilderNamespace. The docstring for these properties will be defined
      by calling str() on the Port, which should return the description of the Port.

      :param port_namespace: the inputs PortNamespace for which to construct the builder



   .. py:method:: __setattr__(attr: str, value: typing.Any) -> None
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__setattr__

      Assign the given value to the port with key `attr`.

      .. note:: Any attributes without a leading underscore being set correspond to inputs and should hence be
          validated with respect to the corresponding input port from the process spec



   .. py:method:: __repr__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__repr__

      Return repr(self).

   .. py:method:: __dir__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__dir__

      Default dir() implementation.

   .. py:method:: __iter__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__iter__

   .. py:method:: __len__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__len__

   .. py:method:: __getitem__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__getitem__

   .. py:method:: __setitem__(item, value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__setitem__

   .. py:method:: __delitem__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__delitem__

   .. py:method:: __delattr__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__delattr__

      Implement delattr(self, name).

   .. py:method:: _recursive_merge(dictionary, key, value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._recursive_merge

      Recursively merge the contents of ``dictionary`` setting its ``key`` to ``value``.

   .. py:method:: _merge(*args, **kwds)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._merge

      Merge the content of a dictionary or keyword arguments in .

      .. note:: This method differs in behavior from ``_update`` in that ``_merge`` will recursively update the
          existing dictionary with the one that is specified in the arguments. The ``_update`` method will merge only
          the keys on the top level, but any lower lying nested namespace will be replaced entirely.

      The method is prefixed with an underscore in order to not reserve the name for a potential port.

      :param args: a single mapping that should be mapped on the namespace.
      :param kwds: keyword value pairs that should be mapped onto the ports.


   .. py:method:: _update(*args, **kwds)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._update

      Update the values of the builder namespace passing a mapping as argument or individual keyword value pairs.

      The method functions just as `collections.abc.MutableMapping.update` and is merely prefixed with an underscore
      in order to not reserve the name for a potential port.

      :param args: a single mapping that should be mapped on the namespace.
      :param kwds: keyword value pairs that should be mapped onto the ports.


   .. py:method:: _inputs(prune: bool = False) -> dict
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._inputs

      Return the entire mapping of inputs specified for this builder.

      :param prune: boolean, when True, will prune nested namespaces that contain no actual values whatsoever
      :return: mapping of inputs ports and their input values.


   .. py:method:: _prune(value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._prune

      Prune a nested mapping from all mappings that are completely empty.

      .. note:: a nested mapping that is completely empty means it contains at most other empty mappings. Other null
          values, such as `None` or empty lists, should not be pruned.

      :param value: a nested mapping of port values
      :return: the same mapping but without any nested namespace that is completely empty.


.. py:class:: ProcessFuture(pk: int, loop: typing.Optional[asyncio.AbstractEventLoop] = None, poll_interval: typing.Union[None, int, float] = None, communicator: typing.Optional[kiwipy.Communicator] = None)
   :canonical: aiida.engine.processes.futures.ProcessFuture

   Bases: :py:obj:`asyncio.Future`

   Future that waits for a process to complete using both polling and listening for broadcast events if possible.

   .. py:attribute:: _filtered
      :canonical: aiida.engine.processes.futures.ProcessFuture._filtered
      :value: None

   .. py:method:: __init__(pk: int, loop: typing.Optional[asyncio.AbstractEventLoop] = None, poll_interval: typing.Union[None, int, float] = None, communicator: typing.Optional[kiwipy.Communicator] = None)
      :canonical: aiida.engine.processes.futures.ProcessFuture.__init__

      Construct a future for a process node being finished.

      If a None poll_interval is supplied polling will not be used.
      If a communicator is supplied it will be used to listen for broadcast messages.

      :param pk: process pk
      :param loop: An event loop
      :param poll_interval: optional polling interval, if None, polling is not activated.
      :param communicator: optional communicator, if None, will not subscribe to broadcasts.


   .. py:method:: cleanup() -> None
      :canonical: aiida.engine.processes.futures.ProcessFuture.cleanup

      Clean up the future by removing broadcast subscribers from the communicator if it still exists.

   .. py:method:: _poll_process(node: aiida.orm.Node, poll_interval: typing.Union[int, float]) -> None
      :canonical: aiida.engine.processes.futures.ProcessFuture._poll_process
      :async:

      Poll whether the process node has reached a terminal state.

.. py:class:: ProcessHandlerReport
   :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport

   Bases: :py:obj:`typing.NamedTuple`

   A namedtuple to define a process handler report for a :class:`aiida.engine.BaseRestartWorkChain`.

   This namedtuple should be returned by a process handler of a work chain instance if the condition of the handler was
   met by the completed process. If no further handling should be performed after this method the `do_break` field
   should be set to `True`.
   If the handler encountered a fatal error and the work chain needs to be terminated, an `ExitCode` with
   non-zero exit status can be set. This exit code is what will be set on the work chain itself. This works because the
   value of the `exit_code` field returned by the handler, will in turn be returned by the `inspect_process` step and
   returning a non-zero exit code from any work chain step will instruct the engine to abort the work chain.

   :param do_break: boolean, set to `True` if no further process handlers should be called, default is `False`
   :param exit_code: an instance of the :class:`~aiida.engine.processes.exit_code.ExitCode` tuple.
       If not explicitly set, the default `ExitCode` will be instantiated,
       which has status `0` meaning that the work chain step will be considered
       successful and the work chain will continue to the next step.


   .. py:attribute:: do_break
      :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport.do_break
      :type: bool
      :value: False

   .. py:attribute:: exit_code
      :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport.exit_code
      :type: aiida.engine.processes.exit_code.ExitCode
      :value: None

.. py:class:: ProcessSpec()
   :canonical: aiida.engine.processes.process_spec.ProcessSpec

   Bases: :py:obj:`plumpy.process_spec.ProcessSpec`

   Default process spec for process classes defined in `aiida-core`.

   This sub class defines custom classes for input ports and port namespaces. It also adds support for the definition
   of exit codes and retrieving them subsequently.


   .. py:attribute:: METADATA_KEY
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.METADATA_KEY
      :type: str
      :value: 'metadata'

   .. py:attribute:: METADATA_OPTIONS_KEY
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.METADATA_OPTIONS_KEY
      :type: str
      :value: 'options'

   .. py:attribute:: INPUT_PORT_TYPE
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.INPUT_PORT_TYPE
      :value: None

   .. py:attribute:: PORT_NAMESPACE_TYPE
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.PORT_NAMESPACE_TYPE
      :value: None

   .. py:method:: __init__() -> None
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.__init__

   .. py:property:: metadata_key
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.metadata_key
      :type: str

   .. py:property:: options_key
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.options_key
      :type: str

   .. py:property:: exit_codes
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.exit_codes
      :type: aiida.engine.processes.exit_code.ExitCodesNamespace

      Return the namespace of exit codes defined for this ProcessSpec

      :returns: ExitCodesNamespace of ExitCode named tuples


   .. py:method:: exit_code(status: int, label: str, message: str, invalidates_cache: bool = False) -> None
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.exit_code

      Add an exit code to the ProcessSpec

      :param status: the exit status integer
      :param label: a label by which the exit code can be addressed
      :param message: a more detailed description of the exit code
      :param invalidates_cache: when set to `True`, a process exiting
          with this exit code will not be considered for caching


   .. py:property:: ports
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.ports
      :type: aiida.engine.processes.ports.PortNamespace

   .. py:property:: inputs
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.inputs
      :type: aiida.engine.processes.ports.PortNamespace

   .. py:property:: outputs
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.outputs
      :type: aiida.engine.processes.ports.PortNamespace

.. py:class:: Runner(poll_interval: typing.Union[int, float] = 0, loop: typing.Optional[asyncio.AbstractEventLoop] = None, communicator: typing.Optional[kiwipy.Communicator] = None, rmq_submit: bool = False, persister: typing.Optional[plumpy.persistence.Persister] = None)
   :canonical: aiida.engine.runners.Runner

   Class that can launch processes by running in the current interpreter or by submitting them to the daemon.

   .. py:attribute:: _persister
      :canonical: aiida.engine.runners.Runner._persister
      :type: typing.Optional[plumpy.persistence.Persister]
      :value: None

   .. py:attribute:: _communicator
      :canonical: aiida.engine.runners.Runner._communicator
      :type: typing.Optional[kiwipy.Communicator]
      :value: None

   .. py:attribute:: _controller
      :canonical: aiida.engine.runners.Runner._controller
      :type: typing.Optional[plumpy.process_comms.RemoteProcessThreadController]
      :value: None

   .. py:attribute:: _closed
      :canonical: aiida.engine.runners.Runner._closed
      :type: bool
      :value: False

   .. py:method:: __init__(poll_interval: typing.Union[int, float] = 0, loop: typing.Optional[asyncio.AbstractEventLoop] = None, communicator: typing.Optional[kiwipy.Communicator] = None, rmq_submit: bool = False, persister: typing.Optional[plumpy.persistence.Persister] = None)
      :canonical: aiida.engine.runners.Runner.__init__

      Construct a new runner.

      :param poll_interval: interval in seconds between polling for status of active sub processes
      :param loop: an asyncio event loop, if none is suppled a new one will be created
      :param communicator: the communicator to use
      :param rmq_submit: if True, processes will be submitted to RabbitMQ, otherwise they will be scheduled here
      :param persister: the persister to use to persist processes



   .. py:method:: __enter__() -> aiida.engine.runners.Runner
      :canonical: aiida.engine.runners.Runner.__enter__

   .. py:method:: __exit__(exc_type, exc_val, exc_tb)
      :canonical: aiida.engine.runners.Runner.__exit__

   .. py:property:: loop
      :canonical: aiida.engine.runners.Runner.loop
      :type: asyncio.AbstractEventLoop

      Get the event loop of this runner.

   .. py:property:: transport
      :canonical: aiida.engine.runners.Runner.transport
      :type: aiida.engine.transports.TransportQueue

   .. py:property:: persister
      :canonical: aiida.engine.runners.Runner.persister
      :type: typing.Optional[plumpy.persistence.Persister]

      Get the persister used by this runner.

   .. py:property:: communicator
      :canonical: aiida.engine.runners.Runner.communicator
      :type: typing.Optional[kiwipy.Communicator]

      Get the communicator used by this runner.

   .. py:property:: plugin_version_provider
      :canonical: aiida.engine.runners.Runner.plugin_version_provider
      :type: aiida.plugins.utils.PluginVersionProvider

   .. py:property:: job_manager
      :canonical: aiida.engine.runners.Runner.job_manager
      :type: aiida.engine.processes.calcjobs.manager.JobManager

   .. py:property:: controller
      :canonical: aiida.engine.runners.Runner.controller
      :type: typing.Optional[plumpy.process_comms.RemoteProcessThreadController]

      Get the controller used by this runner.

   .. py:property:: is_daemon_runner
      :canonical: aiida.engine.runners.Runner.is_daemon_runner
      :type: bool

      Return whether the runner is a daemon runner, which means it submits processes over RabbitMQ.

      :return: True if the runner is a daemon runner


   .. py:method:: is_closed() -> bool
      :canonical: aiida.engine.runners.Runner.is_closed

   .. py:method:: start() -> None
      :canonical: aiida.engine.runners.Runner.start

      Start the internal event loop.

   .. py:method:: stop() -> None
      :canonical: aiida.engine.runners.Runner.stop

      Stop the internal event loop.

   .. py:method:: run_until_complete(future: asyncio.Future) -> typing.Any
      :canonical: aiida.engine.runners.Runner.run_until_complete

      Run the loop until the future has finished and return the result.

   .. py:method:: close() -> None
      :canonical: aiida.engine.runners.Runner.close

      Close the runner by stopping the loop.

   .. py:method:: instantiate_process(process: aiida.engine.runners.TYPE_RUN_PROCESS, **inputs)
      :canonical: aiida.engine.runners.Runner.instantiate_process

   .. py:method:: submit(process: aiida.engine.runners.TYPE_SUBMIT_PROCESS, **inputs: typing.Any)
      :canonical: aiida.engine.runners.Runner.submit

      Submit the process with the supplied inputs to this runner immediately returning control to
      the interpreter. The return value will be the calculation node of the submitted process

      :param process: the process class to submit
      :param inputs: the inputs to be passed to the process
      :return: the calculation node of the process


   .. py:method:: schedule(process: aiida.engine.runners.TYPE_SUBMIT_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.orm.ProcessNode
      :canonical: aiida.engine.runners.Runner.schedule

      Schedule a process to be executed by this runner

      :param process: the process class to submit
      :param inputs: the inputs to be passed to the process
      :return: the calculation node of the process


   .. py:method:: _run(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], aiida.orm.ProcessNode]
      :canonical: aiida.engine.runners.Runner._run

      Run the process with the supplied inputs in this runner that will block until the process is completed.
      The return value will be the results of the completed process

      :param process: the process class or process function to run
      :param inputs: the inputs to be passed to the process
      :return: tuple of the outputs of the process and the calculation node


   .. py:method:: run(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.runners.Runner.run

      Run the process with the supplied inputs in this runner that will block until the process is completed.
      The return value will be the results of the completed process

      :param process: the process class or process function to run
      :param inputs: the inputs to be passed to the process
      :return: the outputs of the process


   .. py:method:: run_get_node(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.engine.runners.ResultAndNode
      :canonical: aiida.engine.runners.Runner.run_get_node

      Run the process with the supplied inputs in this runner that will block until the process is completed.
      The return value will be the results of the completed process

      :param process: the process class or process function to run
      :param inputs: the inputs to be passed to the process
      :return: tuple of the outputs of the process and the calculation node


   .. py:method:: run_get_pk(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.engine.runners.ResultAndPk
      :canonical: aiida.engine.runners.Runner.run_get_pk

      Run the process with the supplied inputs in this runner that will block until the process is completed.
      The return value will be the results of the completed process

      :param process: the process class or process function to run
      :param inputs: the inputs to be passed to the process
      :return: tuple of the outputs of the process and process node pk


   .. py:method:: call_on_process_finish(pk: int, callback: typing.Callable[[], typing.Any]) -> None
      :canonical: aiida.engine.runners.Runner.call_on_process_finish

      Schedule a callback when the process of the given pk is terminated.

      This method will add a broadcast subscriber that will listen for state changes of the target process to be
      terminated. As a fail-safe, a polling-mechanism is used to check the state of the process, should the broadcast
      message be missed by the subscriber, in order to prevent the caller to wait indefinitely.

      :param pk: pk of the process
      :param callback: function to be called upon process termination


   .. py:method:: get_process_future(pk: int) -> aiida.engine.processes.futures.ProcessFuture
      :canonical: aiida.engine.runners.Runner.get_process_future

      Return a future for a process.

      The future will have the process node as the result when finished.

      :return: A future representing the completion of the process node


   .. py:method:: _poll_process(node, callback)
      :canonical: aiida.engine.runners.Runner._poll_process

      Check whether the process state of the node is terminated and call the callback or reschedule it.

      :param node: the process node
      :param callback: callback to be called when process is terminated


.. py:data:: ToContext
   :canonical: aiida.engine.processes.workchains.context.ToContext
   :value: None

.. py:class:: WithNonDb(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.WithNonDb

   A mixin that adds support to a port to flag that it should not be stored
   in the database using the non_db=True flag.

   The mixins have to go before the main port class in the superclass order
   to make sure the mixin has the chance to strip out the non_db keyword.


   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.ports.WithNonDb.__init__

   .. py:property:: non_db_explicitly_set
      :canonical: aiida.engine.processes.ports.WithNonDb.non_db_explicitly_set
      :type: bool

      Return whether the a value for `non_db` was explicitly passed in the construction of the `Port`.

      :return: boolean, True if `non_db` was explicitly defined during construction, False otherwise


   .. py:property:: non_db
      :canonical: aiida.engine.processes.ports.WithNonDb.non_db
      :type: bool

      Return whether the value of this `Port` should be stored as a `Node` in the database.

      :return: boolean, True if it should be storable as a `Node`, False otherwise


.. py:class:: WithSerialize(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.WithSerialize

   A mixin that adds support for a serialization function which is automatically applied on inputs
   that are not AiiDA data types.


   .. py:method:: __init__(*args, **kwargs) -> None
      :canonical: aiida.engine.processes.ports.WithSerialize.__init__

   .. py:method:: serialize(value: typing.Any) -> aiida.orm.Data
      :canonical: aiida.engine.processes.ports.WithSerialize.serialize

      Serialize the given value, unless it is ``None``, already a Data type, or no serializer function is defined.

      :param value: the value to be serialized
      :returns: a serialized version of the value or the unchanged value


.. py:class:: WorkChain(inputs: dict | None = None, logger: logging.Logger | None = None, runner: aiida.engine.runners.Runner | None = None, enable_persistence: bool = True)
   :canonical: aiida.engine.processes.workchains.workchain.WorkChain

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   The `WorkChain` class is the principle component to implement workflows in AiiDA.

   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._node_class
      :value: None

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._spec_class
      :value: None

   .. py:attribute:: _STEPPER_STATE
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._STEPPER_STATE
      :value: 'stepper_state'

   .. py:attribute:: _CONTEXT
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._CONTEXT
      :value: 'CONTEXT'

   .. py:method:: __init__(inputs: dict | None = None, logger: logging.Logger | None = None, runner: aiida.engine.runners.Runner | None = None, enable_persistence: bool = True) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.__init__

      Construct a WorkChain instance.

      Construct the instance only if it is a sub class of `WorkChain`, otherwise raise `InvalidOperation`.

      :param inputs: work chain inputs
      :param logger: aiida logger
      :param runner: work chain runner
      :param enable_persistence: whether to persist this work chain



   .. py:method:: spec() -> aiida.engine.processes.workchains.workchain.WorkChainSpec
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.spec
      :classmethod:

   .. py:property:: node
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.node
      :type: aiida.orm.WorkChainNode

      Return the ProcessNode used by this process to represent itself in the database.

      :return: instance of sub class of ProcessNode


   .. py:property:: ctx
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.ctx
      :type: aiida.common.extendeddicts.AttributeDict

      Get the context.

   .. py:method:: save_instance_state(out_state, save_context)
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.save_instance_state

      Save instance state.

      :param out_state: state to save in

      :param save_context:
      :type save_context: :class:`!plumpy.persistence.LoadSaveContext`



   .. py:method:: load_instance_state(saved_state, load_context)
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.load_instance_state

      Load instance state.

      :param saved_state: saved instance state
      :param load_context:



   .. py:method:: on_run()
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_run

   .. py:method:: _resolve_nested_context(key: str) -> tuple[aiida.common.extendeddicts.AttributeDict, str]
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._resolve_nested_context

      Returns a reference to a sub-dictionary of the context and the last key,
      after resolving a potentially segmented key where required sub-dictionaries are created as needed.

      :param key: A key into the context, where words before a dot are interpreted as a key for a sub-dictionary


   .. py:method:: _insert_awaitable(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._insert_awaitable

      Insert an awaitable that should be terminated before before continuing to the next step.

      :param awaitable: the thing to await


   .. py:method:: _resolve_awaitable(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable, value: typing.Any) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._resolve_awaitable

      Resolve an awaitable.

      Precondition: must be an awaitable that was previously inserted.

      :param awaitable: the awaitable to resolve


   .. py:method:: to_context(**kwargs: aiida.engine.processes.workchains.awaitable.Awaitable | aiida.orm.ProcessNode) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.to_context

      Add a dictionary of awaitables to the context.

      This is a convenience method that provides syntactic sugar, for a user to add multiple intersteps that will
      assign a certain value to the corresponding key in the context of the work chain.


   .. py:method:: _update_process_status() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._update_process_status

      Set the process status with a message accounting the current sub processes that we are waiting for.

   .. py:method:: run() -> typing.Any
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.run

   .. py:method:: _do_step() -> typing.Any
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._do_step

      Execute the next step in the outline and return the result.

      If the stepper returns a non-finished status and the return value is of type ToContext, the contents of the
      ToContext container will be turned into awaitables if necessary. If any awaitables were created, the process
      will enter in the Wait state, otherwise it will go to Continue. When the stepper returns that it is done, the
      stepper result will be converted to None and returned, unless it is an integer or instance of ExitCode.


   .. py:method:: _store_nodes(data: typing.Any) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._store_nodes

      Recurse through a data structure and store any unstored nodes that are found along the way

      :param data: a data structure potentially containing unstored nodes


   .. py:method:: on_exiting() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_exiting

      Ensure that any unstored nodes in the context are stored, before the state is exited

      After the state is exited the next state will be entered and if persistence is enabled, a checkpoint will
      be saved. If the context contains unstored nodes, the serialization necessary for checkpointing will fail.


   .. py:method:: on_wait(awaitables: typing.Sequence[aiida.engine.processes.workchains.awaitable.Awaitable])
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_wait

      Entering the WAITING state.

   .. py:method:: _action_awaitables() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._action_awaitables

      Handle the awaitables that are currently registered with the work chain.

      Depending on the class type of the awaitable's target a different callback
      function will be bound with the awaitable and the runner will be asked to
      call it when the target is completed


   .. py:method:: _on_awaitable_finished(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._on_awaitable_finished

      Callback function, for when an awaitable process instance is completed.

      The awaitable will be effectuated on the context of the work chain and removed from the internal list. If all
      awaitables have been dealt with, the work chain process is resumed.

      :param awaitable: an Awaitable instance


.. py:function:: append_(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.context.append_

   Convenience function that will construct an Awaitable for a given class instance
   with the context action set to APPEND. When the awaitable target is completed
   it will be appended to a list in the context for a key that is to be defined later

   :param target: an instance of a Process or Awaitable

   :returns: the awaitable



.. py:function:: assign_(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.context.assign_

   Convenience function that will construct an Awaitable for a given class instance
   with the context action set to ASSIGN. When the awaitable target is completed
   it will be assigned to the context for a key that is to be defined later

   :param target: an instance of a Process or Awaitable

   :returns: the awaitable



.. py:function:: calcfunction(function: aiida.engine.processes.functions.FunctionType) -> aiida.engine.processes.functions.FunctionType
   :canonical: aiida.engine.processes.functions.calcfunction

   A decorator to turn a standard python function into a calcfunction.
   Example usage:

   >>> from aiida.orm import Int
   >>>
   >>> # Define the calcfunction
   >>> @calcfunction
   >>> def sum(a, b):
   >>>    return a + b
   >>> # Run it with some input
   >>> r = sum(Int(4), Int(5))
   >>> print(r)
   9
   >>> r.base.links.get_incoming().all() # doctest: +SKIP
   [Neighbor(link_type='', link_label='result',
   node=<CalcFunctionNode: uuid: ce0c63b3-1c84-4bb8-ba64-7b70a36adf34 (pk: 3567)>)]
   >>> r.base.links.get_incoming().get_node_by_label('result').base.links.get_incoming().all_nodes()
   [4, 5]

   :param function: The function to decorate.
   :return: The decorated function.


.. py:function:: construct_awaitable(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.awaitable.construct_awaitable

   Construct an instance of the Awaitable class that will contain the information
   related to the action to be taken with respect to the context once the awaitable
   object is completed.

   The awaitable is a simple dictionary with the following keys

       * pk: the pk of the node that is being waited on
       * action: the context action to be performed upon completion
       * outputs: a boolean that toggles whether the node itself

   Currently the only awaitable classes are ProcessNode and Workflow
   The only awaitable actions are the Assign and Append operators


.. py:function:: get_object_loader() -> aiida.engine.persistence.ObjectLoader
   :canonical: aiida.engine.persistence.get_object_loader

   Return the global AiiDA object loader.

   :return: The global object loader



.. py:function:: interruptable_task(coro: typing.Callable[[aiida.engine.utils.InterruptableFuture], typing.Awaitable[typing.Any]], loop: typing.Optional[asyncio.AbstractEventLoop] = None) -> aiida.engine.utils.InterruptableFuture
   :canonical: aiida.engine.utils.interruptable_task

   Turn the given coroutine into an interruptable task by turning it into an InterruptableFuture and returning it.

   :param coro: the coroutine that should be made interruptable with object of InterutableFuture as last paramenter
   :param loop: the event loop in which to run the coroutine, by default uses asyncio.get_event_loop()
   :return: an InterruptableFuture


.. py:function:: is_process_function(function: typing.Any) -> bool
   :canonical: aiida.engine.utils.is_process_function

   Return whether the given function is a process function

   :param function: a function
   :returns: True if the function is a wrapped process function, False otherwise


.. py:function:: process_handler(wrapped: typing.Optional[types.FunctionType] = None, *, priority: int = 0, exit_codes: typing.Union[None, aiida.engine.processes.exit_code.ExitCode, typing.List[aiida.engine.processes.exit_code.ExitCode]] = None, enabled: bool = True) -> types.FunctionType
   :canonical: aiida.engine.processes.workchains.utils.process_handler

   Decorator to register a :class:`~aiida.engine.BaseRestartWorkChain` instance method as a process handler.

   The decorator will validate the `priority` and `exit_codes` optional keyword arguments and then add itself as an
   attribute to the `wrapped` instance method. This is used in the `inspect_process` to return all instance methods of
   the class that have been decorated by this function and therefore are considered to be process handlers.

   Requirements on the function signature of process handling functions. The function to which the decorator is applied
   needs to take two arguments:

       * `self`: This is the instance of the work chain itself
       * `node`: This is the process node that finished and is to be investigated

   The function body typically consists of a conditional that will check for a particular problem that might have
   occurred for the sub process. If a particular problem is handled, the process handler should return an instance of
   the :class:`aiida.engine.ProcessHandlerReport` tuple. If no other process handlers should be considered, the set
   `do_break` attribute should be set to `True`. If the work chain is to be aborted entirely, the `exit_code` of the
   report can be set to an `ExitCode` instance with a non-zero status.

   :param wrapped: the work chain method to register the process handler with
   :param priority: optional integer that defines the order in which registered handlers will be called during the
       handling of a finished process. Higher priorities will be handled first. Default value is `0`. Multiple handlers
       with the same priority is allowed, but the order of those is not well defined.
   :param exit_codes: single or list of `ExitCode` instances. If defined, the handler will return `None` if the exit
       code set on the `node` does not appear in the `exit_codes`. This is useful to have a handler called only when
       the process failed with a specific exit code.
   :param enabled: boolean, by default True, which will cause the handler to be called during `inspect_process`. When
       set to `False`, the handler will be skipped. This static value can be overridden on a per work chain instance
       basis through the input `handler_overrides`.


.. py:function:: run(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Dict[str, typing.Any]
   :canonical: aiida.engine.launch.run

   Run the process with the supplied inputs in a local runner that will block until the process is completed.

   :param process: the process class or process function to run
   :param inputs: the inputs to be passed to the process

   :return: the outputs of the process



.. py:function:: run_get_node(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], aiida.orm.ProcessNode]
   :canonical: aiida.engine.launch.run_get_node

   Run the process with the supplied inputs in a local runner that will block until the process is completed.

   :param process: the process class, instance, builder or function to run
   :param inputs: the inputs to be passed to the process

   :return: tuple of the outputs of the process and the process node



.. py:function:: run_get_pk(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], int]
   :canonical: aiida.engine.launch.run_get_pk

   Run the process with the supplied inputs in a local runner that will block until the process is completed.

   :param process: the process class, instance, builder or function to run
   :param inputs: the inputs to be passed to the process

   :return: tuple of the outputs of the process and process node pk



.. py:function:: submit(process: aiida.engine.launch.TYPE_SUBMIT_PROCESS, **inputs: typing.Any) -> aiida.orm.ProcessNode
   :canonical: aiida.engine.launch.submit

   Submit the process with the supplied inputs to the daemon immediately returning control to the interpreter.

   .. warning: this should not be used within another process. Instead, there one should use the `submit` method of
       the wrapping process itself, i.e. use `self.submit`.

   .. warning: submission of processes requires `store_provenance=True`

   :param process: the process class, instance or builder to submit
   :param inputs: the inputs to be passed to the process

   :return: the calculation node of the process



.. py:function:: workfunction(function: aiida.engine.processes.functions.FunctionType) -> aiida.engine.processes.functions.FunctionType
   :canonical: aiida.engine.processes.functions.workfunction

   A decorator to turn a standard python function into a workfunction.
   Example usage:

   >>> from aiida.orm import Int
   >>>
   >>> # Define the workfunction
   >>> @workfunction
   >>> def select(a, b):
   >>>    return a
   >>> # Run it with some input
   >>> r = select(Int(4), Int(5))
   >>> print(r)
   4
   >>> r.base.links.get_incoming().all() # doctest: +SKIP
   [Neighbor(link_type='', link_label='result',
   node=<WorkFunctionNode: uuid: ce0c63b3-1c84-4bb8-ba64-7b70a36adf34 (pk: 3567)>)]
   >>> r.base.links.get_incoming().get_node_by_label('result').base.links.get_incoming().all_nodes()
   [4, 5]

   :param function: The function to decorate.
   :return: The decorated function.

