:py:mod:`aiida.engine`
======================

.. py:module:: aiida.engine

.. autodoc2-docstring:: aiida.engine
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AiiDAPersister <aiida.engine.persistence.AiiDAPersister>`
     - .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister
          :summary:
   * - :py:obj:`Awaitable <aiida.engine.processes.workchains.awaitable.Awaitable>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.Awaitable
          :summary:
   * - :py:obj:`AwaitableAction <aiida.engine.processes.workchains.awaitable.AwaitableAction>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableAction
          :summary:
   * - :py:obj:`AwaitableTarget <aiida.engine.processes.workchains.awaitable.AwaitableTarget>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableTarget
          :summary:
   * - :py:obj:`BaseRestartWorkChain <aiida.engine.processes.workchains.restart.BaseRestartWorkChain>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain
          :summary:
   * - :py:obj:`CalcJob <aiida.engine.processes.calcjobs.calcjob.CalcJob>`
     - .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob
          :summary:
   * - :py:obj:`CalcJobImporter <aiida.engine.processes.calcjobs.importer.CalcJobImporter>`
     - .. autodoc2-docstring:: aiida.engine.processes.calcjobs.importer.CalcJobImporter
          :summary:
   * - :py:obj:`CalcJobOutputPort <aiida.engine.processes.ports.CalcJobOutputPort>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.CalcJobOutputPort
          :summary:
   * - :py:obj:`CalcJobProcessSpec <aiida.engine.processes.process_spec.CalcJobProcessSpec>`
     - .. autodoc2-docstring:: aiida.engine.processes.process_spec.CalcJobProcessSpec
          :summary:
   * - :py:obj:`DaemonClient <aiida.engine.daemon.client.DaemonClient>`
     - .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient
          :summary:
   * - :py:obj:`ExitCode <aiida.engine.processes.exit_code.ExitCode>`
     - .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode
          :summary:
   * - :py:obj:`ExitCodesNamespace <aiida.engine.processes.exit_code.ExitCodesNamespace>`
     - .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCodesNamespace
          :summary:
   * - :py:obj:`FunctionProcess <aiida.engine.processes.functions.FunctionProcess>`
     - .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess
          :summary:
   * - :py:obj:`InputPort <aiida.engine.processes.ports.InputPort>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.InputPort
          :summary:
   * - :py:obj:`InterruptableFuture <aiida.engine.utils.InterruptableFuture>`
     - .. autodoc2-docstring:: aiida.engine.utils.InterruptableFuture
          :summary:
   * - :py:obj:`JobManager <aiida.engine.processes.calcjobs.manager.JobManager>`
     - .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobManager
          :summary:
   * - :py:obj:`JobsList <aiida.engine.processes.calcjobs.manager.JobsList>`
     - .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList
          :summary:
   * - :py:obj:`ObjectLoader <aiida.engine.persistence.ObjectLoader>`
     - .. autodoc2-docstring:: aiida.engine.persistence.ObjectLoader
          :summary:
   * - :py:obj:`PortNamespace <aiida.engine.processes.ports.PortNamespace>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace
          :summary:
   * - :py:obj:`Process <aiida.engine.processes.process.Process>`
     - .. autodoc2-docstring:: aiida.engine.processes.process.Process
          :summary:
   * - :py:obj:`ProcessBuilder <aiida.engine.processes.builder.ProcessBuilder>`
     - .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilder
          :summary:
   * - :py:obj:`ProcessBuilderNamespace <aiida.engine.processes.builder.ProcessBuilderNamespace>`
     - .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace
          :summary:
   * - :py:obj:`ProcessFuture <aiida.engine.processes.futures.ProcessFuture>`
     - .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture
          :summary:
   * - :py:obj:`ProcessHandlerReport <aiida.engine.processes.workchains.utils.ProcessHandlerReport>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.ProcessHandlerReport
          :summary:
   * - :py:obj:`ProcessSpec <aiida.engine.processes.process_spec.ProcessSpec>`
     - .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec
          :summary:
   * - :py:obj:`Runner <aiida.engine.runners.Runner>`
     - .. autodoc2-docstring:: aiida.engine.runners.Runner
          :summary:
   * - :py:obj:`WithNonDb <aiida.engine.processes.ports.WithNonDb>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.WithNonDb
          :summary:
   * - :py:obj:`WithSerialize <aiida.engine.processes.ports.WithSerialize>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.WithSerialize
          :summary:
   * - :py:obj:`WorkChain <aiida.engine.processes.workchains.workchain.WorkChain>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`append_ <aiida.engine.processes.workchains.context.append_>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.context.append_
          :summary:
   * - :py:obj:`assign_ <aiida.engine.processes.workchains.context.assign_>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.context.assign_
          :summary:
   * - :py:obj:`calcfunction <aiida.engine.processes.functions.calcfunction>`
     - .. autodoc2-docstring:: aiida.engine.processes.functions.calcfunction
          :summary:
   * - :py:obj:`construct_awaitable <aiida.engine.processes.workchains.awaitable.construct_awaitable>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.construct_awaitable
          :summary:
   * - :py:obj:`get_object_loader <aiida.engine.persistence.get_object_loader>`
     - .. autodoc2-docstring:: aiida.engine.persistence.get_object_loader
          :summary:
   * - :py:obj:`interruptable_task <aiida.engine.utils.interruptable_task>`
     - .. autodoc2-docstring:: aiida.engine.utils.interruptable_task
          :summary:
   * - :py:obj:`is_process_function <aiida.engine.utils.is_process_function>`
     - .. autodoc2-docstring:: aiida.engine.utils.is_process_function
          :summary:
   * - :py:obj:`process_handler <aiida.engine.processes.workchains.utils.process_handler>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.process_handler
          :summary:
   * - :py:obj:`run <aiida.engine.launch.run>`
     - .. autodoc2-docstring:: aiida.engine.launch.run
          :summary:
   * - :py:obj:`run_get_node <aiida.engine.launch.run_get_node>`
     - .. autodoc2-docstring:: aiida.engine.launch.run_get_node
          :summary:
   * - :py:obj:`run_get_pk <aiida.engine.launch.run_get_pk>`
     - .. autodoc2-docstring:: aiida.engine.launch.run_get_pk
          :summary:
   * - :py:obj:`submit <aiida.engine.launch.submit>`
     - .. autodoc2-docstring:: aiida.engine.launch.submit
          :summary:
   * - :py:obj:`workfunction <aiida.engine.processes.functions.workfunction>`
     - .. autodoc2-docstring:: aiida.engine.processes.functions.workfunction
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OutputPort <aiida.engine.processes.ports.OutputPort>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.OutputPort
          :summary:
   * - :py:obj:`PORT_NAMESPACE_SEPARATOR <aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR>`
     - .. autodoc2-docstring:: aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR
          :summary:
   * - :py:obj:`ToContext <aiida.engine.processes.workchains.context.ToContext>`
     - .. autodoc2-docstring:: aiida.engine.processes.workchains.context.ToContext
          :summary:

External
~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ProcessState <plumpy.process_states.ProcessState>`
     - .. autodoc2-docstring:: plumpy.process_states.ProcessState
          :summary:
   * - :py:obj:`if_ <plumpy.workchains.if_>`
     - .. autodoc2-docstring:: plumpy.workchains.if_
          :summary:
   * - :py:obj:`return_ <plumpy.workchains.return_>`
     - .. autodoc2-docstring:: plumpy.workchains.return_
          :summary:
   * - :py:obj:`while_ <plumpy.workchains.while_>`
     - .. autodoc2-docstring:: plumpy.workchains.while_
          :summary:

API
~~~

.. py:class:: AiiDAPersister
   :canonical: aiida.engine.persistence.AiiDAPersister

   Bases: :py:obj:`plumpy.persistence.Persister`

   .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister

   .. py:method:: save_checkpoint(process: aiida.engine.processes.process.Process, tag: typing.Optional[str] = None)
      :canonical: aiida.engine.persistence.AiiDAPersister.save_checkpoint

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.save_checkpoint

   .. py:method:: load_checkpoint(pid: typing.Hashable, tag: typing.Optional[str] = None) -> plumpy.persistence.Bundle
      :canonical: aiida.engine.persistence.AiiDAPersister.load_checkpoint

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.load_checkpoint

   .. py:method:: get_checkpoints()
      :canonical: aiida.engine.persistence.AiiDAPersister.get_checkpoints

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.get_checkpoints

   .. py:method:: get_process_checkpoints(pid: typing.Hashable)
      :canonical: aiida.engine.persistence.AiiDAPersister.get_process_checkpoints

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.get_process_checkpoints

   .. py:method:: delete_checkpoint(pid: typing.Hashable, tag: typing.Optional[str] = None) -> None
      :canonical: aiida.engine.persistence.AiiDAPersister.delete_checkpoint

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.delete_checkpoint

   .. py:method:: delete_process_checkpoints(pid: typing.Hashable)
      :canonical: aiida.engine.persistence.AiiDAPersister.delete_process_checkpoints

      .. autodoc2-docstring:: aiida.engine.persistence.AiiDAPersister.delete_process_checkpoints

.. py:class:: Awaitable
   :canonical: aiida.engine.processes.workchains.awaitable.Awaitable

   Bases: :py:obj:`plumpy.utils.AttributesDict`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.Awaitable

.. py:class:: AwaitableAction(*args, **kwds)
   :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableAction

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableAction.__init__

   .. py:attribute:: ASSIGN
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction.ASSIGN
      :value: 'assign'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableAction.ASSIGN

   .. py:attribute:: APPEND
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableAction.APPEND
      :value: 'append'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableAction.APPEND

.. py:class:: AwaitableTarget(*args, **kwds)
   :canonical: aiida.engine.processes.workchains.awaitable.AwaitableTarget

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableTarget

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableTarget.__init__

   .. py:attribute:: PROCESS
      :canonical: aiida.engine.processes.workchains.awaitable.AwaitableTarget.PROCESS
      :value: 'process'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.AwaitableTarget.PROCESS

.. py:class:: BaseRestartWorkChain(*args, **kwargs)
   :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain

   Bases: :py:obj:`aiida.engine.processes.workchains.workchain.WorkChain`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.__init__

   .. py:attribute:: _process_class
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._process_class
      :type: typing.Optional[typing.Type[aiida.engine.processes.Process]]
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._process_class

   .. py:attribute:: _considered_handlers_extra
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._considered_handlers_extra
      :value: 'considered_handlers'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._considered_handlers_extra

   .. py:property:: process_class
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.process_class
      :type: typing.Type[aiida.engine.processes.process.Process]

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.process_class

   .. py:method:: define(spec: aiida.engine.processes.ProcessSpec) -> None
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.define
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.define

   .. py:method:: setup() -> None
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.setup

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.setup

   .. py:method:: should_run_process() -> bool
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.should_run_process

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.should_run_process

   .. py:method:: run_process() -> aiida.engine.processes.workchains.context.ToContext
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.run_process

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.run_process

   .. py:method:: inspect_process() -> typing.Optional[aiida.engine.processes.ExitCode]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.inspect_process

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.inspect_process

   .. py:method:: get_outputs(node) -> typing.Mapping[str, aiida.orm.Node]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_outputs

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_outputs

   .. py:method:: results() -> typing.Optional[aiida.engine.processes.ExitCode]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.results

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.results

   .. py:method:: is_process_handler(process_handler_name: typing.Union[str, types.FunctionType]) -> bool
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.is_process_handler
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.is_process_handler

   .. py:method:: get_process_handlers() -> typing.List[types.FunctionType]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers

   .. py:method:: get_process_handlers_by_priority() -> typing.List[typing.Tuple[int, types.FunctionType]]
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers_by_priority

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.get_process_handlers_by_priority

   .. py:method:: on_terminated()
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.on_terminated

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain.on_terminated

   .. py:method:: _wrap_bare_dict_inputs(port_namespace: aiida.engine.processes.PortNamespace, inputs: typing.Dict[str, typing.Any]) -> aiida.common.AttributeDict
      :canonical: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._wrap_bare_dict_inputs

      .. autodoc2-docstring:: aiida.engine.processes.workchains.restart.BaseRestartWorkChain._wrap_bare_dict_inputs

.. py:class:: CalcJob(*args, **kwargs)
   :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.__init__

   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._node_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._node_class

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._spec_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._spec_class

   .. py:attribute:: link_label_retrieved
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.link_label_retrieved
      :type: str
      :value: 'retrieved'

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.link_label_retrieved

   .. py:method:: define(spec: aiida.engine.processes.process_spec.CalcJobProcessSpec) -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.define
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.define

   .. py:method:: spec_options()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.spec_options

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.spec_options

   .. py:method:: get_importer(entry_point_name: str | None = None) -> aiida.engine.processes.calcjobs.importer.CalcJobImporter
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_importer
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_importer

   .. py:property:: options
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.options
      :type: aiida.common.AttributeDict

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.options

   .. py:method:: get_state_classes() -> typing.Dict[typing.Hashable, typing.Type[plumpy.process_states.State]]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_state_classes
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.get_state_classes

   .. py:property:: node
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.node
      :type: aiida.orm.CalcJobNode

   .. py:method:: on_terminated() -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.on_terminated

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.on_terminated

   .. py:method:: run() -> typing.Union[plumpy.process_states.Stop, int, plumpy.process_states.Wait]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.run

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.run

   .. py:method:: prepare_for_submission(folder: aiida.common.folders.Folder) -> aiida.common.datastructures.CalcInfo
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.prepare_for_submission
      :abstractmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.prepare_for_submission

   .. py:method:: _setup_metadata(metadata: dict) -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_metadata

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_metadata

   .. py:method:: _setup_inputs() -> None
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_inputs

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._setup_inputs

   .. py:method:: _perform_dry_run()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_dry_run

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_dry_run

   .. py:method:: _perform_import()
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_import

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob._perform_import

   .. py:method:: parse(retrieved_temporary_folder: typing.Optional[str] = None, existing_exit_code: aiida.engine.processes.exit_code.ExitCode | None = None) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse

   .. py:method:: terminate(exit_code: aiida.engine.processes.exit_code.ExitCode) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.terminate
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.terminate

   .. py:method:: parse_scheduler_output(retrieved: aiida.orm.Node) -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_scheduler_output

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_scheduler_output

   .. py:method:: parse_retrieved_output(retrieved_temporary_folder: typing.Optional[str] = None) -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_retrieved_output

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.parse_retrieved_output

   .. py:method:: presubmit(folder: aiida.common.folders.Folder) -> aiida.common.datastructures.CalcInfo
      :canonical: aiida.engine.processes.calcjobs.calcjob.CalcJob.presubmit

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.calcjob.CalcJob.presubmit

.. py:class:: CalcJobImporter
   :canonical: aiida.engine.processes.calcjobs.importer.CalcJobImporter

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.importer.CalcJobImporter

   .. py:method:: parse_remote_data(remote_data: aiida.orm.RemoteData, **kwargs) -> typing.Dict[str, typing.Union[aiida.orm.Node, typing.Dict]]
      :canonical: aiida.engine.processes.calcjobs.importer.CalcJobImporter.parse_remote_data
      :abstractmethod:
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.importer.CalcJobImporter.parse_remote_data

.. py:class:: CalcJobOutputPort(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.CalcJobOutputPort

   Bases: :py:obj:`plumpy.ports.OutputPort`

   .. autodoc2-docstring:: aiida.engine.processes.ports.CalcJobOutputPort

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.ports.CalcJobOutputPort.__init__

   .. py:property:: pass_to_parser
      :canonical: aiida.engine.processes.ports.CalcJobOutputPort.pass_to_parser
      :type: bool

      .. autodoc2-docstring:: aiida.engine.processes.ports.CalcJobOutputPort.pass_to_parser

.. py:class:: CalcJobProcessSpec()
   :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec

   Bases: :py:obj:`aiida.engine.processes.process_spec.ProcessSpec`

   .. autodoc2-docstring:: aiida.engine.processes.process_spec.CalcJobProcessSpec

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.process_spec.CalcJobProcessSpec.__init__

   .. py:attribute:: OUTPUT_PORT_TYPE
      :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec.OUTPUT_PORT_TYPE
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.CalcJobProcessSpec.OUTPUT_PORT_TYPE

   .. py:property:: default_output_node
      :canonical: aiida.engine.processes.process_spec.CalcJobProcessSpec.default_output_node
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.CalcJobProcessSpec.default_output_node

.. py:class:: DaemonClient(profile: aiida.manage.configuration.profile.Profile)
   :canonical: aiida.engine.daemon.client.DaemonClient

   .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.__init__

   .. py:attribute:: DAEMON_ERROR_NOT_RUNNING
      :canonical: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_NOT_RUNNING
      :value: 'daemon-error-not-running'

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_NOT_RUNNING

   .. py:attribute:: DAEMON_ERROR_TIMEOUT
      :canonical: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_TIMEOUT
      :value: 'daemon-error-timeout'

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.DAEMON_ERROR_TIMEOUT

   .. py:attribute:: _DAEMON_NAME
      :canonical: aiida.engine.daemon.client.DaemonClient._DAEMON_NAME
      :value: 'aiida-{name}'

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient._DAEMON_NAME

   .. py:attribute:: _ENDPOINT_PROTOCOL
      :canonical: aiida.engine.daemon.client.DaemonClient._ENDPOINT_PROTOCOL
      :value: None

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient._ENDPOINT_PROTOCOL

   .. py:property:: profile
      :canonical: aiida.engine.daemon.client.DaemonClient.profile
      :type: aiida.manage.configuration.profile.Profile

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.profile

   .. py:property:: daemon_name
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_name
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.daemon_name

   .. py:property:: _verdi_bin
      :canonical: aiida.engine.daemon.client.DaemonClient._verdi_bin
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient._verdi_bin

   .. py:method:: cmd_start_daemon(number_workers: int = 1, foreground: bool = False) -> list[str]
      :canonical: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon

   .. py:property:: cmd_start_daemon_worker
      :canonical: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon_worker
      :type: list[str]

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.cmd_start_daemon_worker

   .. py:property:: loglevel
      :canonical: aiida.engine.daemon.client.DaemonClient.loglevel
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.loglevel

   .. py:property:: virtualenv
      :canonical: aiida.engine.daemon.client.DaemonClient.virtualenv
      :type: str | None

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.virtualenv

   .. py:property:: circus_log_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_log_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.circus_log_file

   .. py:property:: circus_pid_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_pid_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.circus_pid_file

   .. py:property:: circus_port_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_port_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.circus_port_file

   .. py:property:: circus_socket_file
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_socket_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.circus_socket_file

   .. py:property:: circus_socket_endpoints
      :canonical: aiida.engine.daemon.client.DaemonClient.circus_socket_endpoints
      :type: dict[str, str]

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.circus_socket_endpoints

   .. py:property:: daemon_log_file
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_log_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.daemon_log_file

   .. py:property:: daemon_pid_file
      :canonical: aiida.engine.daemon.client.DaemonClient.daemon_pid_file
      :type: str

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.daemon_pid_file

   .. py:method:: get_circus_port() -> int
      :canonical: aiida.engine.daemon.client.DaemonClient.get_circus_port

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_circus_port

   .. py:method:: get_env() -> dict[str, str]
      :canonical: aiida.engine.daemon.client.DaemonClient.get_env
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_env

   .. py:method:: get_circus_socket_directory() -> str
      :canonical: aiida.engine.daemon.client.DaemonClient.get_circus_socket_directory

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_circus_socket_directory

   .. py:method:: get_daemon_pid() -> int | None
      :canonical: aiida.engine.daemon.client.DaemonClient.get_daemon_pid

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_daemon_pid

   .. py:property:: is_daemon_running
      :canonical: aiida.engine.daemon.client.DaemonClient.is_daemon_running
      :type: bool

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.is_daemon_running

   .. py:method:: delete_circus_socket_directory() -> None
      :canonical: aiida.engine.daemon.client.DaemonClient.delete_circus_socket_directory

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.delete_circus_socket_directory

   .. py:method:: get_available_port()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_available_port
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_available_port

   .. py:method:: get_controller_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_controller_endpoint

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_controller_endpoint

   .. py:method:: get_pubsub_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_pubsub_endpoint

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_pubsub_endpoint

   .. py:method:: get_stats_endpoint()
      :canonical: aiida.engine.daemon.client.DaemonClient.get_stats_endpoint

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_stats_endpoint

   .. py:method:: get_ipc_endpoint(endpoint)
      :canonical: aiida.engine.daemon.client.DaemonClient.get_ipc_endpoint

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_ipc_endpoint

   .. py:method:: get_tcp_endpoint(port=None)
      :canonical: aiida.engine.daemon.client.DaemonClient.get_tcp_endpoint

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_tcp_endpoint

   .. py:method:: get_client() -> circus.client.CircusClient
      :canonical: aiida.engine.daemon.client.DaemonClient.get_client

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_client

   .. py:method:: call_client(command: aiida.engine.daemon.client.JsonDictType) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.call_client

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.call_client

   .. py:method:: get_status() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_status

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_status

   .. py:method:: get_numprocesses() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_numprocesses

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_numprocesses

   .. py:method:: get_worker_info() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_worker_info

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_worker_info

   .. py:method:: get_daemon_info() -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.get_daemon_info

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.get_daemon_info

   .. py:method:: increase_workers(number: int) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.increase_workers

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.increase_workers

   .. py:method:: decrease_workers(number: int) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.decrease_workers

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.decrease_workers

   .. py:method:: stop_daemon(wait: bool = True, timeout: int = 5) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.stop_daemon

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.stop_daemon

   .. py:method:: restart_daemon(wait: bool) -> aiida.engine.daemon.client.JsonDictType
      :canonical: aiida.engine.daemon.client.DaemonClient.restart_daemon

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.restart_daemon

   .. py:method:: start_daemon(number_workers: int = 1, foreground: bool = False, timeout: int = 5) -> None
      :canonical: aiida.engine.daemon.client.DaemonClient.start_daemon

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient.start_daemon

   .. py:method:: _await_condition(condition: typing.Callable, exception: Exception, timeout: int = 5, interval: float = 0.1)
      :canonical: aiida.engine.daemon.client.DaemonClient._await_condition
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient._await_condition

   .. py:method:: _start_daemon(number_workers: int = 1, foreground: bool = False) -> None
      :canonical: aiida.engine.daemon.client.DaemonClient._start_daemon

      .. autodoc2-docstring:: aiida.engine.daemon.client.DaemonClient._start_daemon

.. py:class:: ExitCode
   :canonical: aiida.engine.processes.exit_code.ExitCode

   Bases: :py:obj:`typing.NamedTuple`

   .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode

   .. py:attribute:: status
      :canonical: aiida.engine.processes.exit_code.ExitCode.status
      :type: int
      :value: 0

      .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode.status

   .. py:attribute:: message
      :canonical: aiida.engine.processes.exit_code.ExitCode.message
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode.message

   .. py:attribute:: invalidates_cache
      :canonical: aiida.engine.processes.exit_code.ExitCode.invalidates_cache
      :type: bool
      :value: False

      .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode.invalidates_cache

   .. py:method:: format(**kwargs: str) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.exit_code.ExitCode.format

      .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCode.format

.. py:class:: ExitCodesNamespace(dictionary=None)
   :canonical: aiida.engine.processes.exit_code.ExitCodesNamespace

   Bases: :py:obj:`aiida.common.extendeddicts.AttributeDict`

   .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCodesNamespace

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCodesNamespace.__init__

   .. py:method:: __call__(identifier: typing.Union[int, str]) -> aiida.engine.processes.exit_code.ExitCode
      :canonical: aiida.engine.processes.exit_code.ExitCodesNamespace.__call__

      .. autodoc2-docstring:: aiida.engine.processes.exit_code.ExitCodesNamespace.__call__

.. py:class:: FunctionProcess(*args, **kwargs)
   :canonical: aiida.engine.processes.functions.FunctionProcess

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.__init__

   .. py:attribute:: _func_args
      :canonical: aiida.engine.processes.functions.FunctionProcess._func_args
      :type: typing.Sequence[str]
      :value: ()

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess._func_args

   .. py:method:: _func(*_args, **_kwargs) -> dict
      :canonical: aiida.engine.processes.functions.FunctionProcess._func
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess._func

   .. py:method:: build(func: typing.Callable[..., typing.Any], node_class: typing.Type[aiida.orm.ProcessNode]) -> typing.Type[aiida.engine.processes.functions.FunctionProcess]
      :canonical: aiida.engine.processes.functions.FunctionProcess.build
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.build

   .. py:method:: validate_inputs(*args: typing.Any, **kwargs: typing.Any) -> None
      :canonical: aiida.engine.processes.functions.FunctionProcess.validate_inputs
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.validate_inputs

   .. py:method:: create_inputs(*args: typing.Any, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.functions.FunctionProcess.create_inputs
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.create_inputs

   .. py:method:: args_to_dict(*args: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.functions.FunctionProcess.args_to_dict
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.args_to_dict

   .. py:method:: get_or_create_db_record() -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.functions.FunctionProcess.get_or_create_db_record
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.get_or_create_db_record

   .. py:property:: process_class
      :canonical: aiida.engine.processes.functions.FunctionProcess.process_class
      :type: typing.Callable[..., typing.Any]

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.process_class

   .. py:method:: execute() -> typing.Optional[typing.Dict[str, typing.Any]]
      :canonical: aiida.engine.processes.functions.FunctionProcess.execute

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.execute

   .. py:method:: _setup_db_record() -> None
      :canonical: aiida.engine.processes.functions.FunctionProcess._setup_db_record

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess._setup_db_record

   .. py:method:: run() -> typing.Optional[aiida.engine.processes.exit_code.ExitCode]
      :canonical: aiida.engine.processes.functions.FunctionProcess.run

      .. autodoc2-docstring:: aiida.engine.processes.functions.FunctionProcess.run

.. py:class:: InputPort(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.InputPort

   Bases: :py:obj:`aiida.engine.processes.ports.WithSerialize`, :py:obj:`aiida.engine.processes.ports.WithNonDb`, :py:obj:`plumpy.ports.InputPort`

   .. autodoc2-docstring:: aiida.engine.processes.ports.InputPort

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.ports.InputPort.__init__

   .. py:method:: get_description() -> typing.Dict[str, str]
      :canonical: aiida.engine.processes.ports.InputPort.get_description

      .. autodoc2-docstring:: aiida.engine.processes.ports.InputPort.get_description

.. py:class:: InterruptableFuture(*, loop=None)
   :canonical: aiida.engine.utils.InterruptableFuture

   Bases: :py:obj:`asyncio.Future`

   .. autodoc2-docstring:: aiida.engine.utils.InterruptableFuture

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.utils.InterruptableFuture.__init__

   .. py:method:: interrupt(reason: Exception) -> None
      :canonical: aiida.engine.utils.InterruptableFuture.interrupt

      .. autodoc2-docstring:: aiida.engine.utils.InterruptableFuture.interrupt

   .. py:method:: with_interrupt(coro: typing.Awaitable[typing.Any]) -> typing.Any
      :canonical: aiida.engine.utils.InterruptableFuture.with_interrupt
      :async:

      .. autodoc2-docstring:: aiida.engine.utils.InterruptableFuture.with_interrupt

.. py:class:: JobManager(transport_queue: aiida.engine.transports.TransportQueue)
   :canonical: aiida.engine.processes.calcjobs.manager.JobManager

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobManager

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobManager.__init__

   .. py:method:: get_jobs_list(authinfo: aiida.orm.AuthInfo) -> aiida.engine.processes.calcjobs.manager.JobsList
      :canonical: aiida.engine.processes.calcjobs.manager.JobManager.get_jobs_list

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobManager.get_jobs_list

   .. py:method:: request_job_info_update(authinfo: aiida.orm.AuthInfo, job_id: typing.Hashable) -> typing.Iterator[asyncio.Future[JobInfo]]
      :canonical: aiida.engine.processes.calcjobs.manager.JobManager.request_job_info_update

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobManager.request_job_info_update

.. py:class:: JobsList(authinfo: aiida.orm.AuthInfo, transport_queue: aiida.engine.transports.TransportQueue, last_updated: typing.Optional[float] = None)
   :canonical: aiida.engine.processes.calcjobs.manager.JobsList

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList.__init__

   .. py:property:: logger
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.logger
      :type: logging.Logger

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList.logger

   .. py:method:: get_minimum_update_interval() -> float
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.get_minimum_update_interval

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList.get_minimum_update_interval

   .. py:property:: last_updated
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.last_updated
      :type: typing.Optional[float]

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList.last_updated

   .. py:method:: _get_jobs_from_scheduler() -> typing.Dict[typing.Hashable, aiida.schedulers.datastructures.JobInfo]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_from_scheduler
      :async:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_from_scheduler

   .. py:method:: _update_job_info() -> None
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._update_job_info
      :async:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._update_job_info

   .. py:method:: request_job_info_update(job_id: typing.Hashable) -> typing.Iterator[asyncio.Future[JobInfo]]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList.request_job_info_update

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList.request_job_info_update

   .. py:method:: _ensure_updating() -> None
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._ensure_updating

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._ensure_updating

   .. py:method:: _has_job_state_changed(old: typing.Optional[aiida.schedulers.datastructures.JobInfo], new: typing.Optional[aiida.schedulers.datastructures.JobInfo]) -> bool
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._has_job_state_changed
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._has_job_state_changed

   .. py:method:: _get_next_update_delay() -> float
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_next_update_delay

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._get_next_update_delay

   .. py:method:: _update_requests_outstanding() -> bool
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._update_requests_outstanding

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._update_requests_outstanding

   .. py:method:: _get_jobs_with_scheduler() -> typing.List[str]
      :canonical: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_with_scheduler

      .. autodoc2-docstring:: aiida.engine.processes.calcjobs.manager.JobsList._get_jobs_with_scheduler

.. py:class:: ObjectLoader
   :canonical: aiida.engine.persistence.ObjectLoader

   Bases: :py:obj:`plumpy.loaders.DefaultObjectLoader`

   .. autodoc2-docstring:: aiida.engine.persistence.ObjectLoader

   .. py:method:: load_object(identifier: str) -> typing.Any
      :canonical: aiida.engine.persistence.ObjectLoader.load_object

      .. autodoc2-docstring:: aiida.engine.persistence.ObjectLoader.load_object

.. py:data:: OutputPort
   :canonical: aiida.engine.processes.ports.OutputPort
   :value: None

   .. autodoc2-docstring:: aiida.engine.processes.ports.OutputPort

.. py:data:: PORT_NAMESPACE_SEPARATOR
   :canonical: aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR
   :value: '__'

   .. autodoc2-docstring:: aiida.engine.processes.ports.PORT_NAMESPACE_SEPARATOR

.. py:exception:: PastException()
   :canonical: aiida.engine.exceptions.PastException

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.engine.exceptions.PastException

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.exceptions.PastException.__init__

.. py:class:: PortNamespace(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.PortNamespace

   Bases: :py:obj:`aiida.engine.processes.ports.WithNonDb`, :py:obj:`plumpy.ports.PortNamespace`

   .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace.__init__

   .. py:method:: __setitem__(key: str, port: plumpy.ports.Port) -> None
      :canonical: aiida.engine.processes.ports.PortNamespace.__setitem__

      .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace.__setitem__

   .. py:method:: validate_port_name(port_name: str) -> None
      :canonical: aiida.engine.processes.ports.PortNamespace.validate_port_name
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace.validate_port_name

   .. py:method:: serialize(mapping: typing.Optional[typing.Dict[str, typing.Any]], breadcrumbs: typing.Sequence[str] = ()) -> typing.Optional[typing.Dict[str, typing.Any]]
      :canonical: aiida.engine.processes.ports.PortNamespace.serialize

      .. autodoc2-docstring:: aiida.engine.processes.ports.PortNamespace.serialize

.. py:class:: Process(inputs: typing.Optional[typing.Dict[str, typing.Any]] = None, logger: typing.Optional[logging.Logger] = None, runner: typing.Optional[aiida.engine.runners.Runner] = None, parent_pid: typing.Optional[int] = None, enable_persistence: bool = True)
   :canonical: aiida.engine.processes.process.Process

   Bases: :py:obj:`plumpy.processes.Process`

   .. autodoc2-docstring:: aiida.engine.processes.process.Process

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.process.Process.__init__

   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.process.Process._node_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._node_class

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.process.Process._spec_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._spec_class

   .. py:attribute:: SINGLE_OUTPUT_LINKNAME
      :canonical: aiida.engine.processes.process.Process.SINGLE_OUTPUT_LINKNAME
      :type: str
      :value: 'result'

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.SINGLE_OUTPUT_LINKNAME

   .. py:class:: SaveKeys(*args, **kwds)
      :canonical: aiida.engine.processes.process.Process.SaveKeys

      Bases: :py:obj:`enum.Enum`

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.SaveKeys

      .. rubric:: Initialization

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.SaveKeys.__init__

      .. py:attribute:: CALC_ID
         :canonical: aiida.engine.processes.process.Process.SaveKeys.CALC_ID
         :type: str
         :value: 'calc_id'

         .. autodoc2-docstring:: aiida.engine.processes.process.Process.SaveKeys.CALC_ID

   .. py:method:: spec() -> aiida.engine.processes.process_spec.ProcessSpec
      :canonical: aiida.engine.processes.process.Process.spec
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.spec

   .. py:method:: define(spec: aiida.engine.processes.process_spec.ProcessSpec) -> None
      :canonical: aiida.engine.processes.process.Process.define
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.define

   .. py:method:: get_builder() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.engine.processes.process.Process.get_builder
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.get_builder

   .. py:method:: get_or_create_db_record() -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.process.Process.get_or_create_db_record
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.get_or_create_db_record

   .. py:method:: init() -> None
      :canonical: aiida.engine.processes.process.Process.init

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.init

   .. py:method:: get_exit_statuses(exit_code_labels: typing.Iterable[str]) -> typing.List[int]
      :canonical: aiida.engine.processes.process.Process.get_exit_statuses
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.get_exit_statuses

   .. py:method:: exit_codes() -> aiida.engine.processes.exit_code.ExitCodesNamespace
      :canonical: aiida.engine.processes.process.Process.exit_codes

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.exit_codes

   .. py:method:: spec_metadata() -> aiida.engine.processes.ports.PortNamespace
      :canonical: aiida.engine.processes.process.Process.spec_metadata

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.spec_metadata

   .. py:property:: node
      :canonical: aiida.engine.processes.process.Process.node
      :type: aiida.orm.ProcessNode

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.node

   .. py:property:: uuid
      :canonical: aiida.engine.processes.process.Process.uuid
      :type: str

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.uuid

   .. py:property:: metadata
      :canonical: aiida.engine.processes.process.Process.metadata
      :type: aiida.common.extendeddicts.AttributeDict

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.metadata

   .. py:method:: _save_checkpoint() -> None
      :canonical: aiida.engine.processes.process.Process._save_checkpoint

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._save_checkpoint

   .. py:method:: save_instance_state(out_state: typing.MutableMapping[str, typing.Any], save_context: typing.Optional[plumpy.persistence.LoadSaveContext]) -> None
      :canonical: aiida.engine.processes.process.Process.save_instance_state

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.save_instance_state

   .. py:method:: get_provenance_inputs_iterator() -> typing.Iterator[typing.Tuple[str, typing.Union[aiida.engine.processes.ports.InputPort, aiida.engine.processes.ports.PortNamespace]]]
      :canonical: aiida.engine.processes.process.Process.get_provenance_inputs_iterator

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.get_provenance_inputs_iterator

   .. py:method:: load_instance_state(saved_state: typing.MutableMapping[str, typing.Any], load_context: plumpy.persistence.LoadSaveContext) -> None
      :canonical: aiida.engine.processes.process.Process.load_instance_state

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.load_instance_state

   .. py:method:: kill(msg: typing.Union[str, None] = None) -> typing.Union[bool, plumpy.futures.Future]
      :canonical: aiida.engine.processes.process.Process.kill

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.kill

   .. py:method:: out(output_port: str, value: typing.Any = None) -> None
      :canonical: aiida.engine.processes.process.Process.out

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.out

   .. py:method:: out_many(out_dict: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.engine.processes.process.Process.out_many

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.out_many

   .. py:method:: on_create() -> None
      :canonical: aiida.engine.processes.process.Process.on_create

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_create

   .. py:method:: on_entered(from_state: typing.Optional[plumpy.process_states.State]) -> None
      :canonical: aiida.engine.processes.process.Process.on_entered

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_entered

   .. py:method:: on_terminated() -> None
      :canonical: aiida.engine.processes.process.Process.on_terminated

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_terminated

   .. py:method:: on_except(exc_info: typing.Tuple[typing.Any, Exception, types.TracebackType]) -> None
      :canonical: aiida.engine.processes.process.Process.on_except

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_except

   .. py:method:: on_finish(result: typing.Union[int, aiida.engine.processes.exit_code.ExitCode], successful: bool) -> None
      :canonical: aiida.engine.processes.process.Process.on_finish

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_finish

   .. py:method:: on_paused(msg: typing.Optional[str] = None) -> None
      :canonical: aiida.engine.processes.process.Process.on_paused

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_paused

   .. py:method:: on_playing() -> None
      :canonical: aiida.engine.processes.process.Process.on_playing

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_playing

   .. py:method:: on_output_emitting(output_port: str, value: typing.Any) -> None
      :canonical: aiida.engine.processes.process.Process.on_output_emitting

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.on_output_emitting

   .. py:method:: set_status(status: typing.Optional[str]) -> None
      :canonical: aiida.engine.processes.process.Process.set_status

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.set_status

   .. py:method:: submit(process: typing.Type[aiida.engine.processes.process.Process], **kwargs) -> aiida.orm.ProcessNode
      :canonical: aiida.engine.processes.process.Process.submit

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.submit

   .. py:property:: runner
      :canonical: aiida.engine.processes.process.Process.runner
      :type: aiida.engine.runners.Runner

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.runner

   .. py:method:: get_parent_calc() -> typing.Optional[aiida.orm.ProcessNode]
      :canonical: aiida.engine.processes.process.Process.get_parent_calc

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.get_parent_calc

   .. py:method:: build_process_type() -> str
      :canonical: aiida.engine.processes.process.Process.build_process_type
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.build_process_type

   .. py:method:: report(msg: str, *args, **kwargs) -> None
      :canonical: aiida.engine.processes.process.Process.report

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.report

   .. py:method:: _create_and_setup_db_record() -> typing.Union[int, uuid.UUID]
      :canonical: aiida.engine.processes.process.Process._create_and_setup_db_record

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._create_and_setup_db_record

   .. py:method:: encode_input_args(inputs: typing.Dict[str, typing.Any]) -> str
      :canonical: aiida.engine.processes.process.Process.encode_input_args

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.encode_input_args

   .. py:method:: decode_input_args(encoded: str) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process.decode_input_args

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.decode_input_args

   .. py:method:: update_outputs() -> None
      :canonical: aiida.engine.processes.process.Process.update_outputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.update_outputs

   .. py:method:: _build_process_label() -> str
      :canonical: aiida.engine.processes.process.Process._build_process_label

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._build_process_label

   .. py:method:: _setup_db_record() -> None
      :canonical: aiida.engine.processes.process.Process._setup_db_record

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._setup_db_record

   .. py:method:: _setup_version_info() -> None
      :canonical: aiida.engine.processes.process.Process._setup_version_info

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._setup_version_info

   .. py:method:: _setup_metadata(metadata: dict) -> None
      :canonical: aiida.engine.processes.process.Process._setup_metadata

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._setup_metadata

   .. py:method:: _setup_inputs() -> None
      :canonical: aiida.engine.processes.process.Process._setup_inputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._setup_inputs

   .. py:method:: _flat_inputs() -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process._flat_inputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._flat_inputs

   .. py:method:: _flat_outputs() -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.processes.process.Process._flat_outputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._flat_outputs

   .. py:method:: _flatten_inputs(port: typing.Union[None, aiida.engine.processes.ports.InputPort, aiida.engine.processes.ports.PortNamespace], port_value: typing.Any, parent_name: str = '', separator: str = PORT_NAMESPACE_SEPARATOR) -> typing.List[typing.Tuple[str, typing.Any]]
      :canonical: aiida.engine.processes.process.Process._flatten_inputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._flatten_inputs

   .. py:method:: _flatten_outputs(port: typing.Union[None, aiida.engine.processes.ports.OutputPort, aiida.engine.processes.ports.PortNamespace], port_value: typing.Any, parent_name: str = '', separator: str = PORT_NAMESPACE_SEPARATOR) -> typing.List[typing.Tuple[str, typing.Any]]
      :canonical: aiida.engine.processes.process.Process._flatten_outputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._flatten_outputs

   .. py:method:: exposed_inputs(process_class: typing.Type[aiida.engine.processes.process.Process], namespace: typing.Optional[str] = None, agglomerate: bool = True) -> aiida.common.extendeddicts.AttributeDict
      :canonical: aiida.engine.processes.process.Process.exposed_inputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.exposed_inputs

   .. py:method:: exposed_outputs(node: aiida.orm.ProcessNode, process_class: typing.Type[aiida.engine.processes.process.Process], namespace: typing.Optional[str] = None, agglomerate: bool = True) -> aiida.common.extendeddicts.AttributeDict
      :canonical: aiida.engine.processes.process.Process.exposed_outputs

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.exposed_outputs

   .. py:method:: _get_namespace_list(namespace: typing.Optional[str] = None, agglomerate: bool = True) -> typing.List[typing.Optional[str]]
      :canonical: aiida.engine.processes.process.Process._get_namespace_list
      :staticmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process._get_namespace_list

   .. py:method:: is_valid_cache(node: aiida.orm.ProcessNode) -> bool
      :canonical: aiida.engine.processes.process.Process.is_valid_cache
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.process.Process.is_valid_cache

.. py:class:: ProcessBuilder(process_class: typing.Type[aiida.engine.processes.process.Process])
   :canonical: aiida.engine.processes.builder.ProcessBuilder

   Bases: :py:obj:`aiida.engine.processes.builder.ProcessBuilderNamespace`

   .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilder

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilder.__init__

   .. py:property:: process_class
      :canonical: aiida.engine.processes.builder.ProcessBuilder.process_class
      :type: typing.Type[aiida.engine.processes.process.Process]

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilder.process_class

   .. py:method:: _repr_pretty_(p, _) -> str
      :canonical: aiida.engine.processes.builder.ProcessBuilder._repr_pretty_

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilder._repr_pretty_

.. py:class:: ProcessBuilderNamespace(port_namespace: aiida.engine.processes.ports.PortNamespace)
   :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace

   Bases: :py:obj:`collections.abc.MutableMapping`

   .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__init__

   .. py:method:: __setattr__(attr: str, value: typing.Any) -> None
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__setattr__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__setattr__

   .. py:method:: __repr__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__repr__

   .. py:method:: __dir__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__dir__

   .. py:method:: __iter__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__iter__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__iter__

   .. py:method:: __len__()
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__len__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__len__

   .. py:method:: __getitem__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__getitem__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__getitem__

   .. py:method:: __setitem__(item, value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__setitem__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__setitem__

   .. py:method:: __delitem__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__delitem__

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace.__delitem__

   .. py:method:: __delattr__(item)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace.__delattr__

   .. py:method:: _recursive_merge(dictionary, key, value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._recursive_merge

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace._recursive_merge

   .. py:method:: _merge(*args, **kwds)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._merge

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace._merge

   .. py:method:: _update(*args, **kwds)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._update

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace._update

   .. py:method:: _inputs(prune: bool = False) -> dict
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._inputs

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace._inputs

   .. py:method:: _prune(value)
      :canonical: aiida.engine.processes.builder.ProcessBuilderNamespace._prune

      .. autodoc2-docstring:: aiida.engine.processes.builder.ProcessBuilderNamespace._prune

.. py:class:: ProcessFuture(pk: int, loop: typing.Optional[asyncio.AbstractEventLoop] = None, poll_interval: typing.Union[None, int, float] = None, communicator: typing.Optional[kiwipy.Communicator] = None)
   :canonical: aiida.engine.processes.futures.ProcessFuture

   Bases: :py:obj:`asyncio.Future`

   .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture.__init__

   .. py:attribute:: _filtered
      :canonical: aiida.engine.processes.futures.ProcessFuture._filtered
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture._filtered

   .. py:method:: cleanup() -> None
      :canonical: aiida.engine.processes.futures.ProcessFuture.cleanup

      .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture.cleanup

   .. py:method:: _poll_process(node: aiida.orm.Node, poll_interval: typing.Union[int, float]) -> None
      :canonical: aiida.engine.processes.futures.ProcessFuture._poll_process
      :async:

      .. autodoc2-docstring:: aiida.engine.processes.futures.ProcessFuture._poll_process

.. py:class:: ProcessHandlerReport
   :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport

   Bases: :py:obj:`typing.NamedTuple`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.ProcessHandlerReport

   .. py:attribute:: do_break
      :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport.do_break
      :type: bool
      :value: False

      .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.ProcessHandlerReport.do_break

   .. py:attribute:: exit_code
      :canonical: aiida.engine.processes.workchains.utils.ProcessHandlerReport.exit_code
      :type: aiida.engine.processes.exit_code.ExitCode
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.ProcessHandlerReport.exit_code

.. py:class:: ProcessSpec()
   :canonical: aiida.engine.processes.process_spec.ProcessSpec

   Bases: :py:obj:`plumpy.process_spec.ProcessSpec`

   .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.__init__

   .. py:attribute:: METADATA_KEY
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.METADATA_KEY
      :type: str
      :value: 'metadata'

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.METADATA_KEY

   .. py:attribute:: METADATA_OPTIONS_KEY
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.METADATA_OPTIONS_KEY
      :type: str
      :value: 'options'

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.METADATA_OPTIONS_KEY

   .. py:attribute:: INPUT_PORT_TYPE
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.INPUT_PORT_TYPE
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.INPUT_PORT_TYPE

   .. py:attribute:: PORT_NAMESPACE_TYPE
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.PORT_NAMESPACE_TYPE
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.PORT_NAMESPACE_TYPE

   .. py:property:: metadata_key
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.metadata_key
      :type: str

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.metadata_key

   .. py:property:: options_key
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.options_key
      :type: str

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.options_key

   .. py:property:: exit_codes
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.exit_codes
      :type: aiida.engine.processes.exit_code.ExitCodesNamespace

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.exit_codes

   .. py:method:: exit_code(status: int, label: str, message: str, invalidates_cache: bool = False) -> None
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.exit_code

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.exit_code

   .. py:property:: ports
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.ports
      :type: aiida.engine.processes.ports.PortNamespace

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.ports

   .. py:property:: inputs
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.inputs
      :type: aiida.engine.processes.ports.PortNamespace

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.inputs

   .. py:property:: outputs
      :canonical: aiida.engine.processes.process_spec.ProcessSpec.outputs
      :type: aiida.engine.processes.ports.PortNamespace

      .. autodoc2-docstring:: aiida.engine.processes.process_spec.ProcessSpec.outputs

.. py:class:: Runner(poll_interval: typing.Union[int, float] = 0, loop: typing.Optional[asyncio.AbstractEventLoop] = None, communicator: typing.Optional[kiwipy.Communicator] = None, rmq_submit: bool = False, persister: typing.Optional[plumpy.persistence.Persister] = None)
   :canonical: aiida.engine.runners.Runner

   .. autodoc2-docstring:: aiida.engine.runners.Runner

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.runners.Runner.__init__

   .. py:attribute:: _persister
      :canonical: aiida.engine.runners.Runner._persister
      :type: typing.Optional[plumpy.persistence.Persister]
      :value: None

      .. autodoc2-docstring:: aiida.engine.runners.Runner._persister

   .. py:attribute:: _communicator
      :canonical: aiida.engine.runners.Runner._communicator
      :type: typing.Optional[kiwipy.Communicator]
      :value: None

      .. autodoc2-docstring:: aiida.engine.runners.Runner._communicator

   .. py:attribute:: _controller
      :canonical: aiida.engine.runners.Runner._controller
      :type: typing.Optional[plumpy.process_comms.RemoteProcessThreadController]
      :value: None

      .. autodoc2-docstring:: aiida.engine.runners.Runner._controller

   .. py:attribute:: _closed
      :canonical: aiida.engine.runners.Runner._closed
      :type: bool
      :value: False

      .. autodoc2-docstring:: aiida.engine.runners.Runner._closed

   .. py:method:: __enter__() -> aiida.engine.runners.Runner
      :canonical: aiida.engine.runners.Runner.__enter__

      .. autodoc2-docstring:: aiida.engine.runners.Runner.__enter__

   .. py:method:: __exit__(exc_type, exc_val, exc_tb)
      :canonical: aiida.engine.runners.Runner.__exit__

      .. autodoc2-docstring:: aiida.engine.runners.Runner.__exit__

   .. py:property:: loop
      :canonical: aiida.engine.runners.Runner.loop
      :type: asyncio.AbstractEventLoop

      .. autodoc2-docstring:: aiida.engine.runners.Runner.loop

   .. py:property:: transport
      :canonical: aiida.engine.runners.Runner.transport
      :type: aiida.engine.transports.TransportQueue

      .. autodoc2-docstring:: aiida.engine.runners.Runner.transport

   .. py:property:: persister
      :canonical: aiida.engine.runners.Runner.persister
      :type: typing.Optional[plumpy.persistence.Persister]

      .. autodoc2-docstring:: aiida.engine.runners.Runner.persister

   .. py:property:: communicator
      :canonical: aiida.engine.runners.Runner.communicator
      :type: typing.Optional[kiwipy.Communicator]

      .. autodoc2-docstring:: aiida.engine.runners.Runner.communicator

   .. py:property:: plugin_version_provider
      :canonical: aiida.engine.runners.Runner.plugin_version_provider
      :type: aiida.plugins.utils.PluginVersionProvider

      .. autodoc2-docstring:: aiida.engine.runners.Runner.plugin_version_provider

   .. py:property:: job_manager
      :canonical: aiida.engine.runners.Runner.job_manager
      :type: aiida.engine.processes.calcjobs.manager.JobManager

      .. autodoc2-docstring:: aiida.engine.runners.Runner.job_manager

   .. py:property:: controller
      :canonical: aiida.engine.runners.Runner.controller
      :type: typing.Optional[plumpy.process_comms.RemoteProcessThreadController]

      .. autodoc2-docstring:: aiida.engine.runners.Runner.controller

   .. py:property:: is_daemon_runner
      :canonical: aiida.engine.runners.Runner.is_daemon_runner
      :type: bool

      .. autodoc2-docstring:: aiida.engine.runners.Runner.is_daemon_runner

   .. py:method:: is_closed() -> bool
      :canonical: aiida.engine.runners.Runner.is_closed

      .. autodoc2-docstring:: aiida.engine.runners.Runner.is_closed

   .. py:method:: start() -> None
      :canonical: aiida.engine.runners.Runner.start

      .. autodoc2-docstring:: aiida.engine.runners.Runner.start

   .. py:method:: stop() -> None
      :canonical: aiida.engine.runners.Runner.stop

      .. autodoc2-docstring:: aiida.engine.runners.Runner.stop

   .. py:method:: run_until_complete(future: asyncio.Future) -> typing.Any
      :canonical: aiida.engine.runners.Runner.run_until_complete

      .. autodoc2-docstring:: aiida.engine.runners.Runner.run_until_complete

   .. py:method:: close() -> None
      :canonical: aiida.engine.runners.Runner.close

      .. autodoc2-docstring:: aiida.engine.runners.Runner.close

   .. py:method:: instantiate_process(process: aiida.engine.runners.TYPE_RUN_PROCESS, **inputs)
      :canonical: aiida.engine.runners.Runner.instantiate_process

      .. autodoc2-docstring:: aiida.engine.runners.Runner.instantiate_process

   .. py:method:: submit(process: aiida.engine.runners.TYPE_SUBMIT_PROCESS, **inputs: typing.Any)
      :canonical: aiida.engine.runners.Runner.submit

      .. autodoc2-docstring:: aiida.engine.runners.Runner.submit

   .. py:method:: schedule(process: aiida.engine.runners.TYPE_SUBMIT_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.orm.ProcessNode
      :canonical: aiida.engine.runners.Runner.schedule

      .. autodoc2-docstring:: aiida.engine.runners.Runner.schedule

   .. py:method:: _run(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], aiida.orm.ProcessNode]
      :canonical: aiida.engine.runners.Runner._run

      .. autodoc2-docstring:: aiida.engine.runners.Runner._run

   .. py:method:: run(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: aiida.engine.runners.Runner.run

      .. autodoc2-docstring:: aiida.engine.runners.Runner.run

   .. py:method:: run_get_node(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.engine.runners.ResultAndNode
      :canonical: aiida.engine.runners.Runner.run_get_node

      .. autodoc2-docstring:: aiida.engine.runners.Runner.run_get_node

   .. py:method:: run_get_pk(process: aiida.engine.runners.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> aiida.engine.runners.ResultAndPk
      :canonical: aiida.engine.runners.Runner.run_get_pk

      .. autodoc2-docstring:: aiida.engine.runners.Runner.run_get_pk

   .. py:method:: call_on_process_finish(pk: int, callback: typing.Callable[[], typing.Any]) -> None
      :canonical: aiida.engine.runners.Runner.call_on_process_finish

      .. autodoc2-docstring:: aiida.engine.runners.Runner.call_on_process_finish

   .. py:method:: get_process_future(pk: int) -> aiida.engine.processes.futures.ProcessFuture
      :canonical: aiida.engine.runners.Runner.get_process_future

      .. autodoc2-docstring:: aiida.engine.runners.Runner.get_process_future

   .. py:method:: _poll_process(node, callback)
      :canonical: aiida.engine.runners.Runner._poll_process

      .. autodoc2-docstring:: aiida.engine.runners.Runner._poll_process

.. py:data:: ToContext
   :canonical: aiida.engine.processes.workchains.context.ToContext
   :value: None

   .. autodoc2-docstring:: aiida.engine.processes.workchains.context.ToContext

.. py:class:: WithNonDb(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.WithNonDb

   .. autodoc2-docstring:: aiida.engine.processes.ports.WithNonDb

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.ports.WithNonDb.__init__

   .. py:property:: non_db_explicitly_set
      :canonical: aiida.engine.processes.ports.WithNonDb.non_db_explicitly_set
      :type: bool

      .. autodoc2-docstring:: aiida.engine.processes.ports.WithNonDb.non_db_explicitly_set

   .. py:property:: non_db
      :canonical: aiida.engine.processes.ports.WithNonDb.non_db
      :type: bool

      .. autodoc2-docstring:: aiida.engine.processes.ports.WithNonDb.non_db

.. py:class:: WithSerialize(*args, **kwargs)
   :canonical: aiida.engine.processes.ports.WithSerialize

   .. autodoc2-docstring:: aiida.engine.processes.ports.WithSerialize

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.ports.WithSerialize.__init__

   .. py:method:: serialize(value: typing.Any) -> aiida.orm.Data
      :canonical: aiida.engine.processes.ports.WithSerialize.serialize

      .. autodoc2-docstring:: aiida.engine.processes.ports.WithSerialize.serialize

.. py:class:: WorkChain(inputs: dict | None = None, logger: logging.Logger | None = None, runner: aiida.engine.runners.Runner | None = None, enable_persistence: bool = True)
   :canonical: aiida.engine.processes.workchains.workchain.WorkChain

   Bases: :py:obj:`aiida.engine.processes.process.Process`

   .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.__init__

   .. py:attribute:: _node_class
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._node_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._node_class

   .. py:attribute:: _spec_class
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._spec_class
      :value: None

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._spec_class

   .. py:attribute:: _STEPPER_STATE
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._STEPPER_STATE
      :value: 'stepper_state'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._STEPPER_STATE

   .. py:attribute:: _CONTEXT
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._CONTEXT
      :value: 'CONTEXT'

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._CONTEXT

   .. py:method:: spec() -> aiida.engine.processes.workchains.workchain.WorkChainSpec
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.spec
      :classmethod:

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.spec

   .. py:property:: node
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.node
      :type: aiida.orm.WorkChainNode

   .. py:property:: ctx
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.ctx
      :type: aiida.common.extendeddicts.AttributeDict

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.ctx

   .. py:method:: save_instance_state(out_state, save_context)
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.save_instance_state

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.save_instance_state

   .. py:method:: load_instance_state(saved_state, load_context)
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.load_instance_state

   .. py:method:: on_run()
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_run

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.on_run

   .. py:method:: _resolve_nested_context(key: str) -> tuple[aiida.common.extendeddicts.AttributeDict, str]
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._resolve_nested_context

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._resolve_nested_context

   .. py:method:: _insert_awaitable(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._insert_awaitable

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._insert_awaitable

   .. py:method:: _resolve_awaitable(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable, value: typing.Any) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._resolve_awaitable

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._resolve_awaitable

   .. py:method:: to_context(**kwargs: aiida.engine.processes.workchains.awaitable.Awaitable | aiida.orm.ProcessNode) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.to_context

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.to_context

   .. py:method:: _update_process_status() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._update_process_status

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._update_process_status

   .. py:method:: run() -> typing.Any
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.run

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.run

   .. py:method:: _do_step() -> typing.Any
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._do_step

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._do_step

   .. py:method:: _store_nodes(data: typing.Any) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._store_nodes

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._store_nodes

   .. py:method:: on_exiting() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_exiting

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.on_exiting

   .. py:method:: on_wait(awaitables: typing.Sequence[aiida.engine.processes.workchains.awaitable.Awaitable])
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain.on_wait

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain.on_wait

   .. py:method:: _action_awaitables() -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._action_awaitables

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._action_awaitables

   .. py:method:: _on_awaitable_finished(awaitable: aiida.engine.processes.workchains.awaitable.Awaitable) -> None
      :canonical: aiida.engine.processes.workchains.workchain.WorkChain._on_awaitable_finished

      .. autodoc2-docstring:: aiida.engine.processes.workchains.workchain.WorkChain._on_awaitable_finished

.. py:function:: append_(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.context.append_

   .. autodoc2-docstring:: aiida.engine.processes.workchains.context.append_

.. py:function:: assign_(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.context.assign_

   .. autodoc2-docstring:: aiida.engine.processes.workchains.context.assign_

.. py:function:: calcfunction(function: aiida.engine.processes.functions.FunctionType) -> aiida.engine.processes.functions.FunctionType
   :canonical: aiida.engine.processes.functions.calcfunction

   .. autodoc2-docstring:: aiida.engine.processes.functions.calcfunction

.. py:function:: construct_awaitable(target: typing.Union[aiida.engine.processes.workchains.awaitable.Awaitable, aiida.orm.ProcessNode]) -> aiida.engine.processes.workchains.awaitable.Awaitable
   :canonical: aiida.engine.processes.workchains.awaitable.construct_awaitable

   .. autodoc2-docstring:: aiida.engine.processes.workchains.awaitable.construct_awaitable

.. py:function:: get_object_loader() -> aiida.engine.persistence.ObjectLoader
   :canonical: aiida.engine.persistence.get_object_loader

   .. autodoc2-docstring:: aiida.engine.persistence.get_object_loader

.. py:function:: interruptable_task(coro: typing.Callable[[aiida.engine.utils.InterruptableFuture], typing.Awaitable[typing.Any]], loop: typing.Optional[asyncio.AbstractEventLoop] = None) -> aiida.engine.utils.InterruptableFuture
   :canonical: aiida.engine.utils.interruptable_task

   .. autodoc2-docstring:: aiida.engine.utils.interruptable_task

.. py:function:: is_process_function(function: typing.Any) -> bool
   :canonical: aiida.engine.utils.is_process_function

   .. autodoc2-docstring:: aiida.engine.utils.is_process_function

.. py:function:: process_handler(wrapped: typing.Optional[types.FunctionType] = None, *, priority: int = 0, exit_codes: typing.Union[None, aiida.engine.processes.exit_code.ExitCode, typing.List[aiida.engine.processes.exit_code.ExitCode]] = None, enabled: bool = True) -> types.FunctionType
   :canonical: aiida.engine.processes.workchains.utils.process_handler

   .. autodoc2-docstring:: aiida.engine.processes.workchains.utils.process_handler

.. py:function:: run(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Dict[str, typing.Any]
   :canonical: aiida.engine.launch.run

   .. autodoc2-docstring:: aiida.engine.launch.run

.. py:function:: run_get_node(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], aiida.orm.ProcessNode]
   :canonical: aiida.engine.launch.run_get_node

   .. autodoc2-docstring:: aiida.engine.launch.run_get_node

.. py:function:: run_get_pk(process: aiida.engine.launch.TYPE_RUN_PROCESS, *args: typing.Any, **inputs: typing.Any) -> typing.Tuple[typing.Dict[str, typing.Any], int]
   :canonical: aiida.engine.launch.run_get_pk

   .. autodoc2-docstring:: aiida.engine.launch.run_get_pk

.. py:function:: submit(process: aiida.engine.launch.TYPE_SUBMIT_PROCESS, **inputs: typing.Any) -> aiida.orm.ProcessNode
   :canonical: aiida.engine.launch.submit

   .. autodoc2-docstring:: aiida.engine.launch.submit

.. py:function:: workfunction(function: aiida.engine.processes.functions.FunctionType) -> aiida.engine.processes.functions.FunctionType
   :canonical: aiida.engine.processes.functions.workfunction

   .. autodoc2-docstring:: aiida.engine.processes.functions.workfunction
