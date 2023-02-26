:py:mod:`aiida.orm`
===================

.. py:module:: aiida.orm

.. autodoc2-docstring:: aiida.orm
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbstractCode <aiida.orm.nodes.data.code.abstract.AbstractCode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode
          :summary:
   * - :py:obj:`AbstractNodeMeta <aiida.orm.utils.node.AbstractNodeMeta>`
     - .. autodoc2-docstring:: aiida.orm.utils.node.AbstractNodeMeta
          :summary:
   * - :py:obj:`ArrayData <aiida.orm.nodes.data.array.array.ArrayData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData
          :summary:
   * - :py:obj:`AttributeManager <aiida.orm.utils.managers.AttributeManager>`
     - .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager
          :summary:
   * - :py:obj:`AuthInfo <aiida.orm.authinfos.AuthInfo>`
     - .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo
          :summary:
   * - :py:obj:`AutoGroup <aiida.orm.groups.AutoGroup>`
     - .. autodoc2-docstring:: aiida.orm.groups.AutoGroup
          :summary:
   * - :py:obj:`BandsData <aiida.orm.nodes.data.array.bands.BandsData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData
          :summary:
   * - :py:obj:`BaseType <aiida.orm.nodes.data.base.BaseType>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType
          :summary:
   * - :py:obj:`Bool <aiida.orm.nodes.data.bool.Bool>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.bool.Bool
          :summary:
   * - :py:obj:`CalcFunctionNode <aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode
          :summary:
   * - :py:obj:`CalcJobNode <aiida.orm.nodes.process.calculation.calcjob.CalcJobNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode
          :summary:
   * - :py:obj:`CalcJobResultManager <aiida.orm.utils.calcjob.CalcJobResultManager>`
     - .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager
          :summary:
   * - :py:obj:`CalculationEntityLoader <aiida.orm.utils.loaders.CalculationEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.CalculationEntityLoader
          :summary:
   * - :py:obj:`CalculationNode <aiida.orm.nodes.process.calculation.calculation.CalculationNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode
          :summary:
   * - :py:obj:`CifData <aiida.orm.nodes.data.cif.CifData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData
          :summary:
   * - :py:obj:`Code <aiida.orm.nodes.data.code.legacy.Code>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code
          :summary:
   * - :py:obj:`CodeEntityLoader <aiida.orm.utils.loaders.CodeEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.CodeEntityLoader
          :summary:
   * - :py:obj:`Collection <aiida.orm.entities.Collection>`
     - .. autodoc2-docstring:: aiida.orm.entities.Collection
          :summary:
   * - :py:obj:`Comment <aiida.orm.comments.Comment>`
     - .. autodoc2-docstring:: aiida.orm.comments.Comment
          :summary:
   * - :py:obj:`Computer <aiida.orm.computers.Computer>`
     - .. autodoc2-docstring:: aiida.orm.computers.Computer
          :summary:
   * - :py:obj:`ComputerEntityLoader <aiida.orm.utils.loaders.ComputerEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.ComputerEntityLoader
          :summary:
   * - :py:obj:`ContainerizedCode <aiida.orm.nodes.data.code.containerized.ContainerizedCode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode
          :summary:
   * - :py:obj:`Data <aiida.orm.nodes.data.data.Data>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data
          :summary:
   * - :py:obj:`Dict <aiida.orm.nodes.data.dict.Dict>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict
          :summary:
   * - :py:obj:`Entity <aiida.orm.entities.Entity>`
     - .. autodoc2-docstring:: aiida.orm.entities.Entity
          :summary:
   * - :py:obj:`EntityExtras <aiida.orm.extras.EntityExtras>`
     - .. autodoc2-docstring:: aiida.orm.extras.EntityExtras
          :summary:
   * - :py:obj:`EntityTypes <aiida.orm.entities.EntityTypes>`
     - .. autodoc2-docstring:: aiida.orm.entities.EntityTypes
          :summary:
   * - :py:obj:`EnumData <aiida.orm.nodes.data.enum.EnumData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData
          :summary:
   * - :py:obj:`Float <aiida.orm.nodes.data.float.Float>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.float.Float
          :summary:
   * - :py:obj:`FolderData <aiida.orm.nodes.data.folder.FolderData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.folder.FolderData
          :summary:
   * - :py:obj:`Group <aiida.orm.groups.Group>`
     - .. autodoc2-docstring:: aiida.orm.groups.Group
          :summary:
   * - :py:obj:`GroupEntityLoader <aiida.orm.utils.loaders.GroupEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.GroupEntityLoader
          :summary:
   * - :py:obj:`ImportGroup <aiida.orm.groups.ImportGroup>`
     - .. autodoc2-docstring:: aiida.orm.groups.ImportGroup
          :summary:
   * - :py:obj:`InstalledCode <aiida.orm.nodes.data.code.installed.InstalledCode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode
          :summary:
   * - :py:obj:`Int <aiida.orm.nodes.data.int.Int>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.int.Int
          :summary:
   * - :py:obj:`JsonableData <aiida.orm.nodes.data.jsonable.JsonableData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData
          :summary:
   * - :py:obj:`Kind <aiida.orm.nodes.data.structure.Kind>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind
          :summary:
   * - :py:obj:`KpointsData <aiida.orm.nodes.data.array.kpoints.KpointsData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData
          :summary:
   * - :py:obj:`LinkManager <aiida.orm.utils.links.LinkManager>`
     - .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager
          :summary:
   * - :py:obj:`LinkPair <aiida.orm.utils.links.LinkPair>`
     - .. autodoc2-docstring:: aiida.orm.utils.links.LinkPair
          :summary:
   * - :py:obj:`LinkTriple <aiida.orm.utils.links.LinkTriple>`
     - .. autodoc2-docstring:: aiida.orm.utils.links.LinkTriple
          :summary:
   * - :py:obj:`List <aiida.orm.nodes.data.list.List>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.list.List
          :summary:
   * - :py:obj:`Log <aiida.orm.logs.Log>`
     - .. autodoc2-docstring:: aiida.orm.logs.Log
          :summary:
   * - :py:obj:`Node <aiida.orm.nodes.node.Node>`
     - .. autodoc2-docstring:: aiida.orm.nodes.node.Node
          :summary:
   * - :py:obj:`NodeAttributes <aiida.orm.nodes.attributes.NodeAttributes>`
     - .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes
          :summary:
   * - :py:obj:`NodeEntityLoader <aiida.orm.utils.loaders.NodeEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.NodeEntityLoader
          :summary:
   * - :py:obj:`NodeLinksManager <aiida.orm.utils.managers.NodeLinksManager>`
     - .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager
          :summary:
   * - :py:obj:`NodeRepository <aiida.orm.nodes.repository.NodeRepository>`
     - .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository
          :summary:
   * - :py:obj:`NumericType <aiida.orm.nodes.data.numeric.NumericType>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType
          :summary:
   * - :py:obj:`OrbitalData <aiida.orm.nodes.data.orbital.OrbitalData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.orbital.OrbitalData
          :summary:
   * - :py:obj:`OrmEntityLoader <aiida.orm.utils.loaders.OrmEntityLoader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader
          :summary:
   * - :py:obj:`PortableCode <aiida.orm.nodes.data.code.portable.PortableCode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode
          :summary:
   * - :py:obj:`ProcessNode <aiida.orm.nodes.process.process.ProcessNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode
          :summary:
   * - :py:obj:`ProjectionData <aiida.orm.nodes.data.array.projection.ProjectionData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData
          :summary:
   * - :py:obj:`QueryBuilder <aiida.orm.querybuilder.QueryBuilder>`
     - .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder
          :summary:
   * - :py:obj:`RemoteData <aiida.orm.nodes.data.remote.base.RemoteData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData
          :summary:
   * - :py:obj:`RemoteStashData <aiida.orm.nodes.data.remote.stash.base.RemoteStashData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.base.RemoteStashData
          :summary:
   * - :py:obj:`RemoteStashFolderData <aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData
          :summary:
   * - :py:obj:`SinglefileData <aiida.orm.nodes.data.singlefile.SinglefileData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData
          :summary:
   * - :py:obj:`Site <aiida.orm.nodes.data.structure.Site>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site
          :summary:
   * - :py:obj:`Str <aiida.orm.nodes.data.str.Str>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.str.Str
          :summary:
   * - :py:obj:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData
          :summary:
   * - :py:obj:`TrajectoryData <aiida.orm.nodes.data.array.trajectory.TrajectoryData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData
          :summary:
   * - :py:obj:`UpfData <aiida.orm.nodes.data.upf.UpfData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData
          :summary:
   * - :py:obj:`UpfFamily <aiida.orm.groups.UpfFamily>`
     - .. autodoc2-docstring:: aiida.orm.groups.UpfFamily
          :summary:
   * - :py:obj:`User <aiida.orm.users.User>`
     - .. autodoc2-docstring:: aiida.orm.users.User
          :summary:
   * - :py:obj:`WorkChainNode <aiida.orm.nodes.process.workflow.workchain.WorkChainNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode
          :summary:
   * - :py:obj:`WorkFunctionNode <aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode
          :summary:
   * - :py:obj:`WorkflowNode <aiida.orm.nodes.process.workflow.workflow.WorkflowNode>`
     - .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode
          :summary:
   * - :py:obj:`XyData <aiida.orm.nodes.data.array.xy.XyData>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OrderSpecifier <aiida.orm.logs.OrderSpecifier>`
     - .. autodoc2-docstring:: aiida.orm.logs.OrderSpecifier
          :summary:
   * - :py:obj:`cif_from_ase <aiida.orm.nodes.data.cif.cif_from_ase>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.cif.cif_from_ase
          :summary:
   * - :py:obj:`find_bandgap <aiida.orm.nodes.data.array.bands.find_bandgap>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.find_bandgap
          :summary:
   * - :py:obj:`get_loader <aiida.orm.utils.loaders.get_loader>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.get_loader
          :summary:
   * - :py:obj:`get_query_type_from_type_string <aiida.orm.utils.node.get_query_type_from_type_string>`
     - .. autodoc2-docstring:: aiida.orm.utils.node.get_query_type_from_type_string
          :summary:
   * - :py:obj:`get_type_string_from_class <aiida.orm.utils.node.get_type_string_from_class>`
     - .. autodoc2-docstring:: aiida.orm.utils.node.get_type_string_from_class
          :summary:
   * - :py:obj:`has_pycifrw <aiida.orm.nodes.data.cif.has_pycifrw>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.cif.has_pycifrw
          :summary:
   * - :py:obj:`load_code <aiida.orm.utils.loaders.load_code>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.load_code
          :summary:
   * - :py:obj:`load_computer <aiida.orm.utils.loaders.load_computer>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.load_computer
          :summary:
   * - :py:obj:`load_entity <aiida.orm.utils.loaders.load_entity>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.load_entity
          :summary:
   * - :py:obj:`load_group <aiida.orm.utils.loaders.load_group>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.load_group
          :summary:
   * - :py:obj:`load_node <aiida.orm.utils.loaders.load_node>`
     - .. autodoc2-docstring:: aiida.orm.utils.loaders.load_node
          :summary:
   * - :py:obj:`load_node_class <aiida.orm.utils.node.load_node_class>`
     - .. autodoc2-docstring:: aiida.orm.utils.node.load_node_class
          :summary:
   * - :py:obj:`pycifrw_from_cif <aiida.orm.nodes.data.cif.pycifrw_from_cif>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.cif.pycifrw_from_cif
          :summary:
   * - :py:obj:`to_aiida_type <aiida.orm.nodes.data.base.to_aiida_type>`
     - .. autodoc2-docstring:: aiida.orm.nodes.data.base.to_aiida_type
          :summary:
   * - :py:obj:`validate_link <aiida.orm.utils.links.validate_link>`
     - .. autodoc2-docstring:: aiida.orm.utils.links.validate_link
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ASCENDING <aiida.orm.logs.ASCENDING>`
     - .. autodoc2-docstring:: aiida.orm.logs.ASCENDING
          :summary:
   * - :py:obj:`DESCENDING <aiida.orm.logs.DESCENDING>`
     - .. autodoc2-docstring:: aiida.orm.logs.DESCENDING
          :summary:

API
~~~

.. py:data:: ASCENDING
   :canonical: aiida.orm.logs.ASCENDING
   :value: 'asc'

   .. autodoc2-docstring:: aiida.orm.logs.ASCENDING

.. py:class:: AbstractCode(default_calc_job_plugin: str | None = None, append_text: str = '', prepend_text: str = '', use_double_quotes: bool = False, is_hidden: bool = False, **kwargs)
   :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.__init__

   .. py:attribute:: _KEY_ATTRIBUTE_DEFAULT_CALC_JOB_PLUGIN
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_DEFAULT_CALC_JOB_PLUGIN
      :type: str
      :value: 'input_plugin'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_DEFAULT_CALC_JOB_PLUGIN

   .. py:attribute:: _KEY_ATTRIBUTE_APPEND_TEXT
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_APPEND_TEXT
      :type: str
      :value: 'append_text'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_APPEND_TEXT

   .. py:attribute:: _KEY_ATTRIBUTE_PREPEND_TEXT
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_PREPEND_TEXT
      :type: str
      :value: 'prepend_text'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_PREPEND_TEXT

   .. py:attribute:: _KEY_ATTRIBUTE_USE_DOUBLE_QUOTES
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_USE_DOUBLE_QUOTES
      :type: str
      :value: 'use_double_quotes'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_USE_DOUBLE_QUOTES

   .. py:attribute:: _KEY_EXTRA_IS_HIDDEN
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_EXTRA_IS_HIDDEN
      :type: str
      :value: 'hidden'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_EXTRA_IS_HIDDEN

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.can_run_on_computer
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.can_run_on_computer

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable

   .. py:method:: get_executable_cmdline_params(cmdline_params: list[str] | None = None) -> list
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable_cmdline_params

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable_cmdline_params

   .. py:method:: get_prepend_cmdline_params(mpi_args: list[str] | None = None, extra_mpirun_params: list[str] | None = None) -> list[str]
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_prepend_cmdline_params

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.get_prepend_cmdline_params

   .. py:method:: validate_working_directory(folder: aiida.common.folders.Folder)
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.validate_working_directory

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.validate_working_directory

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.full_label
      :abstractmethod:
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.full_label

   .. py:property:: label
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.label
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.label

   .. py:property:: default_calc_job_plugin
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.default_calc_job_plugin
      :type: str | None

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.default_calc_job_plugin

   .. py:property:: append_text
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.append_text
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.append_text

   .. py:property:: prepend_text
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.prepend_text
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.prepend_text

   .. py:property:: use_double_quotes
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.use_double_quotes
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.use_double_quotes

   .. py:property:: is_hidden
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.is_hidden
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.is_hidden

   .. py:method:: get_builder() -> aiida.engine.ProcessBuilder
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_builder

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.get_builder

   .. py:method:: cli_validate_label_uniqueness(_, __, value)
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.cli_validate_label_uniqueness
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.cli_validate_label_uniqueness

   .. py:method:: get_cli_options() -> collections.OrderedDict
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_cli_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode.get_cli_options

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._get_cli_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.abstract.AbstractCode._get_cli_options

.. py:class:: AbstractNodeMeta
   :canonical: aiida.orm.utils.node.AbstractNodeMeta

   Bases: :py:obj:`abc.ABCMeta`

   .. autodoc2-docstring:: aiida.orm.utils.node.AbstractNodeMeta

   .. py:method:: __new__(name, bases, namespace, **kwargs)
      :canonical: aiida.orm.utils.node.AbstractNodeMeta.__new__

      .. autodoc2-docstring:: aiida.orm.utils.node.AbstractNodeMeta.__new__

.. py:class:: ArrayData(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.array.ArrayData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.__init__

   .. py:attribute:: array_prefix
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.array_prefix
      :value: 'array|'

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.array_prefix

   .. py:attribute:: _cached_arrays
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._cached_arrays
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._cached_arrays

   .. py:method:: initialize()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.initialize

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.initialize

   .. py:method:: delete_array(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.delete_array

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.delete_array

   .. py:method:: get_arraynames()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_arraynames

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.get_arraynames

   .. py:method:: _arraynames_from_files()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_files

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_files

   .. py:method:: _arraynames_from_properties()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_properties

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_properties

   .. py:method:: get_shape(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_shape

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.get_shape

   .. py:method:: get_iterarrays()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_iterarrays

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.get_iterarrays

   .. py:method:: get_array(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_array

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.get_array

   .. py:method:: clear_internal_cache()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.clear_internal_cache

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.clear_internal_cache

   .. py:method:: set_array(name, array)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.set_array

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData.set_array

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._validate

   .. py:method:: _get_array_entries()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._get_array_entries

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._get_array_entries

   .. py:method:: _prepare_json(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._prepare_json

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.array.ArrayData._prepare_json

.. py:class:: AttributeManager(node)
   :canonical: aiida.orm.utils.managers.AttributeManager

   .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__init__

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.managers.AttributeManager.__dir__

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__dir__

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.managers.AttributeManager.__iter__

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__iter__

   .. py:method:: _get_dict()
      :canonical: aiida.orm.utils.managers.AttributeManager._get_dict

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager._get_dict

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.managers.AttributeManager.__getattr__

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__getattr__

   .. py:method:: __setattr__(name, value)
      :canonical: aiida.orm.utils.managers.AttributeManager.__setattr__

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__setattr__

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.managers.AttributeManager.__getitem__

      .. autodoc2-docstring:: aiida.orm.utils.managers.AttributeManager.__getitem__

.. py:class:: AuthInfo(computer: aiida.orm.Computer, user: aiida.orm.User, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.authinfos.AuthInfo

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendAuthInfo`\ , :py:obj:`aiida.orm.authinfos.AuthInfoCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.authinfos.AuthInfo._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo._CLS_COLLECTION

   .. py:attribute:: PROPERTY_WORKDIR
      :canonical: aiida.orm.authinfos.AuthInfo.PROPERTY_WORKDIR
      :value: 'workdir'

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.PROPERTY_WORKDIR

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.authinfos.AuthInfo.__str__

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.__str__

   .. py:property:: enabled
      :canonical: aiida.orm.authinfos.AuthInfo.enabled
      :type: bool

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.enabled

   .. py:property:: computer
      :canonical: aiida.orm.authinfos.AuthInfo.computer
      :type: aiida.orm.Computer

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.computer

   .. py:property:: user
      :canonical: aiida.orm.authinfos.AuthInfo.user
      :type: aiida.orm.User

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.user

   .. py:method:: get_auth_params() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.authinfos.AuthInfo.get_auth_params

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.get_auth_params

   .. py:method:: set_auth_params(auth_params: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.authinfos.AuthInfo.set_auth_params

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.set_auth_params

   .. py:method:: get_metadata() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.authinfos.AuthInfo.get_metadata

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.get_metadata

   .. py:method:: set_metadata(metadata: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.authinfos.AuthInfo.set_metadata

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.set_metadata

   .. py:method:: get_workdir() -> str
      :canonical: aiida.orm.authinfos.AuthInfo.get_workdir

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.get_workdir

   .. py:method:: get_transport() -> aiida.transports.Transport
      :canonical: aiida.orm.authinfos.AuthInfo.get_transport

      .. autodoc2-docstring:: aiida.orm.authinfos.AuthInfo.get_transport

.. py:class:: AutoGroup(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.AutoGroup

   Bases: :py:obj:`aiida.orm.groups.Group`

   .. autodoc2-docstring:: aiida.orm.groups.AutoGroup

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.groups.AutoGroup.__init__

.. py:class:: BandsData
   :canonical: aiida.orm.nodes.data.array.bands.BandsData

   Bases: :py:obj:`aiida.orm.nodes.data.array.kpoints.KpointsData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData

   .. py:method:: set_kpointsdata(kpointsdata)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.set_kpointsdata

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.set_kpointsdata

   .. py:method:: _validate_bands_occupations(bands, occupations=None, labels=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._validate_bands_occupations

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._validate_bands_occupations

   .. py:method:: set_bands(bands, units=None, occupations=None, labels=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.set_bands

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.set_bands

   .. py:property:: array_labels
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.array_labels

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.array_labels

   .. py:property:: units
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.units

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.units

   .. py:method:: _set_pbc(value)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._set_pbc

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._set_pbc

   .. py:method:: get_bands(also_occupations=False, also_labels=False)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.get_bands

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.get_bands

   .. py:method:: _get_bandplot_data(cartesian, prettify_format=None, join_symbol=None, get_segments=False, y_origin=0.0)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_bandplot_data

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._get_bandplot_data

   .. py:method:: _prepare_agr_batch(main_file_name='', comments=True, prettify_format=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr_batch

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr_batch

   .. py:method:: _prepare_dat_multicolumn(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_multicolumn

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_multicolumn

   .. py:method:: _prepare_dat_blocks(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_blocks

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_blocks

   .. py:method:: _matplotlib_get_dict(main_file_name='', comments=True, title='', legend=None, legend2=None, y_max_lim=None, y_min_lim=None, y_origin=0.0, prettify_format=None, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict

   .. py:method:: _prepare_mpl_singlefile(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_singlefile

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_singlefile

   .. py:method:: _prepare_mpl_withjson(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_withjson

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_withjson

   .. py:method:: _prepare_mpl_pdf(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_pdf

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_pdf

   .. py:method:: _prepare_mpl_png(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_png

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_png

   .. py:method:: _get_mpl_body_template(paths)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_mpl_body_template
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._get_mpl_body_template

   .. py:method:: show_mpl(**kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.show_mpl

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData.show_mpl

   .. py:method:: _prepare_gnuplot(main_file_name=None, title='', comments=True, prettify_format=None, y_max_lim=None, y_min_lim=None, y_origin=0.0)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_gnuplot

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_gnuplot

   .. py:method:: _prepare_agr(main_file_name='', comments=True, setnumber_offset=0, color_number=1, color_number2=2, legend='', title='', y_max_lim=None, y_min_lim=None, y_origin=0.0, prettify_format=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr

   .. py:method:: _get_band_segments(cartesian)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_band_segments

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._get_band_segments

   .. py:method:: _prepare_json(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_json

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.BandsData._prepare_json

.. py:class:: BaseType(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.base.BaseType

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType.__init__

   .. py:property:: value
      :canonical: aiida.orm.nodes.data.base.BaseType.value

      .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType.value

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.base.BaseType.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType.__str__

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.base.BaseType.__eq__

      .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType.__eq__

   .. py:method:: new(value=None)
      :canonical: aiida.orm.nodes.data.base.BaseType.new

      .. autodoc2-docstring:: aiida.orm.nodes.data.base.BaseType.new

.. py:class:: Bool
   :canonical: aiida.orm.nodes.data.bool.Bool

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   .. autodoc2-docstring:: aiida.orm.nodes.data.bool.Bool

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.bool.Bool._type
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.bool.Bool._type

   .. py:method:: __int__()
      :canonical: aiida.orm.nodes.data.bool.Bool.__int__

      .. autodoc2-docstring:: aiida.orm.nodes.data.bool.Bool.__int__

   .. py:method:: __bool__()
      :canonical: aiida.orm.nodes.data.bool.Bool.__bool__

      .. autodoc2-docstring:: aiida.orm.nodes.data.bool.Bool.__bool__

.. py:class:: CalcFunctionNode
   :canonical: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode

   Bases: :py:obj:`aiida.orm.utils.mixins.FunctionCalculationMixin`, :py:obj:`aiida.orm.nodes.process.calculation.calculation.CalculationNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode._CLS_NODE_LINKS
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode._CLS_NODE_LINKS

.. py:class:: CalcJobNode
   :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode

   Bases: :py:obj:`aiida.orm.nodes.process.calculation.calculation.CalculationNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode

   .. py:attribute:: CALC_JOB_STATE_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.CALC_JOB_STATE_KEY
      :value: 'state'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.CALC_JOB_STATE_KEY

   .. py:attribute:: IMMIGRATED_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.IMMIGRATED_KEY
      :value: 'imported'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.IMMIGRATED_KEY

   .. py:attribute:: REMOTE_WORKDIR_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.REMOTE_WORKDIR_KEY
      :value: 'remote_workdir'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.REMOTE_WORKDIR_KEY

   .. py:attribute:: RETRIEVE_LIST_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_LIST_KEY
      :value: 'retrieve_list'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_LIST_KEY

   .. py:attribute:: RETRIEVE_TEMPORARY_LIST_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_TEMPORARY_LIST_KEY
      :value: 'retrieve_temporary_list'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_TEMPORARY_LIST_KEY

   .. py:attribute:: SCHEDULER_JOB_ID_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_JOB_ID_KEY
      :value: 'job_id'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_JOB_ID_KEY

   .. py:attribute:: SCHEDULER_STATE_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_STATE_KEY
      :value: 'scheduler_state'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_STATE_KEY

   .. py:attribute:: SCHEDULER_LAST_CHECK_TIME_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_CHECK_TIME_KEY
      :value: 'scheduler_lastchecktime'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_CHECK_TIME_KEY

   .. py:attribute:: SCHEDULER_LAST_JOB_INFO_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_JOB_INFO_KEY
      :value: 'last_job_info'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_JOB_INFO_KEY

   .. py:attribute:: SCHEDULER_DETAILED_JOB_INFO_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_DETAILED_JOB_INFO_KEY
      :value: 'detailed_job_info'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_DETAILED_JOB_INFO_KEY

   .. py:attribute:: _tools
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._tools
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._tools

   .. py:property:: tools
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.tools
      :type: aiida.tools.calculations.CalculationTools

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.tools

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._updatable_attributes

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._updatable_attributes

   .. py:method:: _hash_ignored_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._hash_ignored_attributes

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._hash_ignored_attributes

   .. py:method:: get_builder_restart() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_builder_restart

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_builder_restart

   .. py:property:: is_imported
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.is_imported
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.is_imported

   .. py:method:: get_option(name: str) -> typing.Optional[typing.Any]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_option

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_option

   .. py:method:: set_option(name: str, value: typing.Any) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_option

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_option

   .. py:method:: get_options() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_options

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_options

   .. py:method:: set_options(options: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_options

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_options

   .. py:method:: get_state() -> typing.Optional[aiida.common.datastructures.CalcJobState]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_state

   .. py:method:: set_state(state: aiida.common.datastructures.CalcJobState) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_state

   .. py:method:: delete_state() -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.delete_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.delete_state

   .. py:method:: set_remote_workdir(remote_workdir: str) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_remote_workdir

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_remote_workdir

   .. py:method:: get_remote_workdir() -> typing.Optional[str]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_remote_workdir

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_remote_workdir

   .. py:method:: _validate_retrieval_directive(directives: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._validate_retrieval_directive
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._validate_retrieval_directive

   .. py:method:: set_retrieve_list(retrieve_list: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_list

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_list

   .. py:method:: get_retrieve_list() -> typing.Optional[typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_list

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_list

   .. py:method:: set_retrieve_temporary_list(retrieve_temporary_list: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_temporary_list

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_temporary_list

   .. py:method:: get_retrieve_temporary_list() -> typing.Optional[typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_temporary_list

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_temporary_list

   .. py:method:: set_job_id(job_id: typing.Union[int, str]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_job_id

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_job_id

   .. py:method:: get_job_id() -> typing.Optional[str]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_job_id

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_job_id

   .. py:method:: set_scheduler_state(state: aiida.schedulers.datastructures.JobState) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_scheduler_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_scheduler_state

   .. py:method:: get_scheduler_state() -> typing.Optional[aiida.schedulers.datastructures.JobState]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_state

   .. py:method:: get_scheduler_lastchecktime() -> typing.Optional[datetime.datetime]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_lastchecktime

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_lastchecktime

   .. py:method:: set_detailed_job_info(detailed_job_info: typing.Optional[dict]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_detailed_job_info

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_detailed_job_info

   .. py:method:: get_detailed_job_info() -> typing.Optional[dict]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_detailed_job_info

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_detailed_job_info

   .. py:method:: set_last_job_info(last_job_info: aiida.schedulers.datastructures.JobInfo) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_last_job_info

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_last_job_info

   .. py:method:: get_last_job_info() -> typing.Optional[aiida.schedulers.datastructures.JobInfo]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_last_job_info

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_last_job_info

   .. py:method:: get_authinfo() -> aiida.orm.authinfos.AuthInfo
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_authinfo

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_authinfo

   .. py:method:: get_transport() -> aiida.transports.Transport
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_transport

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_transport

   .. py:method:: get_parser_class() -> typing.Optional[typing.Type[aiida.parsers.Parser]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_parser_class

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_parser_class

   .. py:property:: link_label_retrieved
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.link_label_retrieved
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.link_label_retrieved

   .. py:method:: get_retrieved_node() -> typing.Optional[aiida.orm.FolderData]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieved_node

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieved_node

   .. py:property:: res
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.res
      :type: aiida.orm.utils.calcjob.CalcJobResultManager

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.res

   .. py:method:: get_scheduler_stdout() -> typing.Optional[typing.AnyStr]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stdout

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stdout

   .. py:method:: get_scheduler_stderr() -> typing.Optional[typing.AnyStr]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stderr

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stderr

   .. py:method:: get_description() -> str
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_description

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_description

.. py:class:: CalcJobResultManager(node)
   :canonical: aiida.orm.utils.calcjob.CalcJobResultManager

   .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.__init__

   .. py:property:: node
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.node

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.node

   .. py:method:: _load_results()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager._load_results

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager._load_results

   .. py:method:: get_results()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.get_results

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.get_results

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__dir__

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.__dir__

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__iter__

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.__iter__

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__getattr__

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.__getattr__

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__getitem__

      .. autodoc2-docstring:: aiida.orm.utils.calcjob.CalcJobResultManager.__getitem__

.. py:class:: CalculationEntityLoader
   :canonical: aiida.orm.utils.loaders.CalculationEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   .. autodoc2-docstring:: aiida.orm.utils.loaders.CalculationEntityLoader

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.CalculationEntityLoader.orm_base_class

      .. autodoc2-docstring:: aiida.orm.utils.loaders.CalculationEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.CalculationEntityLoader._get_query_builder_label_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.CalculationEntityLoader._get_query_builder_label_identifier

.. py:class:: CalculationNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode

   Bases: :py:obj:`aiida.orm.nodes.process.process.ProcessNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode.__init__

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._storable
      :value: True

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode._storable

   .. py:attribute:: _cachable
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._cachable
      :value: True

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode._cachable

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._unstorable_message
      :value: 'storing for this node has been disabled'

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode._unstorable_message

   .. py:property:: inputs
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode.inputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode.inputs

   .. py:property:: outputs
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode.outputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      .. autodoc2-docstring:: aiida.orm.nodes.process.calculation.calculation.CalculationNode.outputs

.. py:class:: CifData(ase=None, file=None, filename=None, values=None, scan_type=None, parse_policy=None, **kwargs)
   :canonical: aiida.orm.nodes.data.cif.CifData

   Bases: :py:obj:`aiida.orm.nodes.data.singlefile.SinglefileData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.__init__

   .. py:attribute:: _SET_INCOMPATIBILITIES
      :canonical: aiida.orm.nodes.data.cif.CifData._SET_INCOMPATIBILITIES
      :value: [('ase', 'file'), ('ase', 'values'), ('file', 'values')]

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._SET_INCOMPATIBILITIES

   .. py:attribute:: _SCAN_TYPES
      :canonical: aiida.orm.nodes.data.cif.CifData._SCAN_TYPES
      :value: ('standard', 'flex')

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._SCAN_TYPES

   .. py:attribute:: _SCAN_TYPE_DEFAULT
      :canonical: aiida.orm.nodes.data.cif.CifData._SCAN_TYPE_DEFAULT
      :value: 'standard'

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._SCAN_TYPE_DEFAULT

   .. py:attribute:: _PARSE_POLICIES
      :canonical: aiida.orm.nodes.data.cif.CifData._PARSE_POLICIES
      :value: ('eager', 'lazy')

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._PARSE_POLICIES

   .. py:attribute:: _PARSE_POLICY_DEFAULT
      :canonical: aiida.orm.nodes.data.cif.CifData._PARSE_POLICY_DEFAULT
      :value: 'eager'

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._PARSE_POLICY_DEFAULT

   .. py:attribute:: _values
      :canonical: aiida.orm.nodes.data.cif.CifData._values
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._values

   .. py:attribute:: _ase
      :canonical: aiida.orm.nodes.data.cif.CifData._ase
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._ase

   .. py:method:: read_cif(fileobj, index=-1, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.read_cif
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.read_cif

   .. py:method:: from_md5(md5, backend=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.from_md5
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.from_md5

   .. py:method:: get_or_create(filename, use_first=False, store_cif=True)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_or_create
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.get_or_create

   .. py:property:: ase
      :canonical: aiida.orm.nodes.data.cif.CifData.ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.ase

   .. py:method:: get_ase(**kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.get_ase

   .. py:method:: set_ase(aseatoms)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.set_ase

   .. py:property:: values
      :canonical: aiida.orm.nodes.data.cif.CifData.values

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.values

   .. py:method:: set_values(values)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_values

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.set_values

   .. py:method:: parse(scan_type=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.parse

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.parse

   .. py:method:: store(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.store

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.store

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_file

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.set_file

   .. py:method:: set_scan_type(scan_type)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_scan_type

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.set_scan_type

   .. py:method:: set_parse_policy(parse_policy)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_parse_policy

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.set_parse_policy

   .. py:method:: get_formulae(mode='sum', custom_tags=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_formulae

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.get_formulae

   .. py:method:: get_spacegroup_numbers()
      :canonical: aiida.orm.nodes.data.cif.CifData.get_spacegroup_numbers

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.get_spacegroup_numbers

   .. py:property:: has_partial_occupancies
      :canonical: aiida.orm.nodes.data.cif.CifData.has_partial_occupancies

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.has_partial_occupancies

   .. py:property:: has_attached_hydrogens
      :canonical: aiida.orm.nodes.data.cif.CifData.has_attached_hydrogens

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.has_attached_hydrogens

   .. py:property:: has_undefined_atomic_sites
      :canonical: aiida.orm.nodes.data.cif.CifData.has_undefined_atomic_sites

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.has_undefined_atomic_sites

   .. py:property:: has_atomic_sites
      :canonical: aiida.orm.nodes.data.cif.CifData.has_atomic_sites

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.has_atomic_sites

   .. py:property:: has_unknown_species
      :canonical: aiida.orm.nodes.data.cif.CifData.has_unknown_species

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.has_unknown_species

   .. py:method:: generate_md5()
      :canonical: aiida.orm.nodes.data.cif.CifData.generate_md5

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.generate_md5

   .. py:method:: get_structure(converter='pymatgen', store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData.get_structure

   .. py:method:: _prepare_cif(**kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData._prepare_cif

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._prepare_cif

   .. py:method:: _get_object_ase()
      :canonical: aiida.orm.nodes.data.cif.CifData._get_object_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._get_object_ase

   .. py:method:: _get_object_pycifrw()
      :canonical: aiida.orm.nodes.data.cif.CifData._get_object_pycifrw

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._get_object_pycifrw

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.cif.CifData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.cif.CifData._validate

.. py:class:: Code(remote_computer_exec=None, local_executable=None, input_plugin_name=None, files=None, **kwargs)
   :canonical: aiida.orm.nodes.data.code.legacy.Code

   Bases: :py:obj:`aiida.orm.nodes.data.code.abstract.AbstractCode`

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.__init__

   .. py:attribute:: HIDDEN_KEY
      :canonical: aiida.orm.nodes.data.code.legacy.Code.HIDDEN_KEY
      :value: 'hidden'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.HIDDEN_KEY

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.legacy.Code.can_run_on_computer

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.can_run_on_computer

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_executable

   .. py:method:: hide()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.hide

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.hide

   .. py:method:: reveal()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.reveal

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.reveal

   .. py:property:: hidden
      :canonical: aiida.orm.nodes.data.code.legacy.Code.hidden

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.hidden

   .. py:method:: set_files(files)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_files

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_files

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.__str__

   .. py:method:: get_computer_label()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_computer_label

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_computer_label

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.legacy.Code.full_label

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.full_label

   .. py:method:: relabel(new_label)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.relabel

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.relabel

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_description

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_description

   .. py:method:: get_code_helper(label, machinename=None, backend=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_code_helper
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_code_helper

   .. py:method:: get(pk=None, label=None, machinename=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get

   .. py:method:: get_from_string(code_string)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_from_string
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_from_string

   .. py:method:: list_for_plugin(plugin, labels=True, backend=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.list_for_plugin
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.list_for_plugin

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code._validate

   .. py:method:: validate_remote_exec_path()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.validate_remote_exec_path

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.validate_remote_exec_path

   .. py:method:: set_prepend_text(code)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_prepend_text

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_prepend_text

   .. py:method:: get_prepend_text()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_prepend_text

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_prepend_text

   .. py:method:: set_input_plugin_name(input_plugin)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_input_plugin_name

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_input_plugin_name

   .. py:method:: get_input_plugin_name()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_input_plugin_name

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_input_plugin_name

   .. py:method:: set_use_double_quotes(use_double_quotes: bool)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_use_double_quotes

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_use_double_quotes

   .. py:method:: get_use_double_quotes() -> bool
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_use_double_quotes

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_use_double_quotes

   .. py:method:: set_append_text(code)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_append_text

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_append_text

   .. py:method:: get_append_text()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_append_text

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_append_text

   .. py:method:: set_local_executable(exec_name)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_local_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_local_executable

   .. py:method:: get_local_executable()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_local_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_local_executable

   .. py:method:: set_remote_computer_exec(remote_computer_exec)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_remote_computer_exec

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.set_remote_computer_exec

   .. py:method:: get_remote_exec_path()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_remote_exec_path

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_remote_exec_path

   .. py:method:: get_remote_computer()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_remote_computer

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_remote_computer

   .. py:method:: _set_local()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._set_local

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code._set_local

   .. py:method:: _set_remote()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._set_remote

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code._set_remote

   .. py:method:: is_local()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.is_local

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.is_local

   .. py:method:: can_run_on(computer)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.can_run_on

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.can_run_on

   .. py:method:: get_execname()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_execname

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.legacy.Code.get_execname

.. py:class:: CodeEntityLoader
   :canonical: aiida.orm.utils.loaders.CodeEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   .. autodoc2-docstring:: aiida.orm.utils.loaders.CodeEntityLoader

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.CodeEntityLoader.orm_base_class

      .. autodoc2-docstring:: aiida.orm.utils.loaders.CodeEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.CodeEntityLoader._get_query_builder_label_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.CodeEntityLoader._get_query_builder_label_identifier

.. py:class:: Collection(entity_class: typing.Type[aiida.orm.entities.EntityType], backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.entities.Collection

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`aiida.orm.entities.EntityType`\ ]

   .. autodoc2-docstring:: aiida.orm.entities.Collection

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.entities.Collection.__init__

   .. py:method:: _entity_base_cls() -> typing.Type[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection._entity_base_cls
      :abstractmethod:
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.entities.Collection._entity_base_cls

   .. py:method:: get_cached(entity_class: typing.Type[aiida.orm.entities.EntityType], backend: aiida.orm.implementation.StorageBackend)
      :canonical: aiida.orm.entities.Collection.get_cached
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.entities.Collection.get_cached

   .. py:method:: __call__(backend: aiida.orm.implementation.StorageBackend) -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Collection.__call__

      .. autodoc2-docstring:: aiida.orm.entities.Collection.__call__

   .. py:property:: entity_type
      :canonical: aiida.orm.entities.Collection.entity_type
      :type: typing.Type[aiida.orm.entities.EntityType]

      .. autodoc2-docstring:: aiida.orm.entities.Collection.entity_type

   .. py:property:: backend
      :canonical: aiida.orm.entities.Collection.backend
      :type: aiida.orm.implementation.StorageBackend

      .. autodoc2-docstring:: aiida.orm.entities.Collection.backend

   .. py:method:: query(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.entities.Collection.query

      .. autodoc2-docstring:: aiida.orm.entities.Collection.query

   .. py:method:: get(**filters: typing.Any) -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Collection.get

      .. autodoc2-docstring:: aiida.orm.entities.Collection.get

   .. py:method:: find(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, limit: typing.Optional[int] = None) -> typing.List[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection.find

      .. autodoc2-docstring:: aiida.orm.entities.Collection.find

   .. py:method:: all() -> typing.List[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection.all

      .. autodoc2-docstring:: aiida.orm.entities.Collection.all

   .. py:method:: count(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None) -> int
      :canonical: aiida.orm.entities.Collection.count

      .. autodoc2-docstring:: aiida.orm.entities.Collection.count

.. py:class:: Comment(node: aiida.orm.Node, user: aiida.orm.User, content: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.comments.Comment

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendComment`\ , :py:obj:`aiida.orm.comments.CommentCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.comments.Comment

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.comments.Comment.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.comments.Comment._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.comments.Comment._CLS_COLLECTION

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.comments.Comment.__str__

      .. autodoc2-docstring:: aiida.orm.comments.Comment.__str__

   .. py:property:: uuid
      :canonical: aiida.orm.comments.Comment.uuid
      :type: str

      .. autodoc2-docstring:: aiida.orm.comments.Comment.uuid

   .. py:property:: ctime
      :canonical: aiida.orm.comments.Comment.ctime
      :type: datetime.datetime

      .. autodoc2-docstring:: aiida.orm.comments.Comment.ctime

   .. py:property:: mtime
      :canonical: aiida.orm.comments.Comment.mtime
      :type: datetime.datetime

      .. autodoc2-docstring:: aiida.orm.comments.Comment.mtime

   .. py:method:: set_mtime(value: datetime.datetime) -> None
      :canonical: aiida.orm.comments.Comment.set_mtime

      .. autodoc2-docstring:: aiida.orm.comments.Comment.set_mtime

   .. py:property:: node
      :canonical: aiida.orm.comments.Comment.node
      :type: aiida.orm.Node

      .. autodoc2-docstring:: aiida.orm.comments.Comment.node

   .. py:property:: user
      :canonical: aiida.orm.comments.Comment.user
      :type: aiida.orm.User

      .. autodoc2-docstring:: aiida.orm.comments.Comment.user

   .. py:method:: set_user(value: aiida.orm.User) -> None
      :canonical: aiida.orm.comments.Comment.set_user

      .. autodoc2-docstring:: aiida.orm.comments.Comment.set_user

   .. py:property:: content
      :canonical: aiida.orm.comments.Comment.content
      :type: str

      .. autodoc2-docstring:: aiida.orm.comments.Comment.content

   .. py:method:: set_content(value: str) -> None
      :canonical: aiida.orm.comments.Comment.set_content

      .. autodoc2-docstring:: aiida.orm.comments.Comment.set_content

.. py:class:: Computer(label: typing.Optional[str] = None, hostname: str = '', description: str = '', transport_type: str = '', scheduler_type: str = '', workdir: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.computers.Computer

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendComputer`\ , :py:obj:`aiida.orm.computers.ComputerCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.computers.Computer

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.computers.Computer.__init__

   .. py:attribute:: _logger
      :canonical: aiida.orm.computers.Computer._logger
      :value: None

      .. autodoc2-docstring:: aiida.orm.computers.Computer._logger

   .. py:attribute:: PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL
      :canonical: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL
      :value: 'minimum_scheduler_poll_interval'

      .. autodoc2-docstring:: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL

   .. py:attribute:: PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT
      :canonical: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT
      :value: 10.0

      .. autodoc2-docstring:: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT

   .. py:attribute:: PROPERTY_WORKDIR
      :canonical: aiida.orm.computers.Computer.PROPERTY_WORKDIR
      :value: 'workdir'

      .. autodoc2-docstring:: aiida.orm.computers.Computer.PROPERTY_WORKDIR

   .. py:attribute:: PROPERTY_SHEBANG
      :canonical: aiida.orm.computers.Computer.PROPERTY_SHEBANG
      :value: 'shebang'

      .. autodoc2-docstring:: aiida.orm.computers.Computer.PROPERTY_SHEBANG

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.computers.Computer._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.computers.Computer._CLS_COLLECTION

   .. py:method:: __repr__()
      :canonical: aiida.orm.computers.Computer.__repr__

      .. autodoc2-docstring:: aiida.orm.computers.Computer.__repr__

   .. py:method:: __str__()
      :canonical: aiida.orm.computers.Computer.__str__

      .. autodoc2-docstring:: aiida.orm.computers.Computer.__str__

   .. py:property:: uuid
      :canonical: aiida.orm.computers.Computer.uuid
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.uuid

   .. py:property:: logger
      :canonical: aiida.orm.computers.Computer.logger
      :type: logging.Logger

      .. autodoc2-docstring:: aiida.orm.computers.Computer.logger

   .. py:method:: _label_validator(label: str) -> None
      :canonical: aiida.orm.computers.Computer._label_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._label_validator

   .. py:method:: _hostname_validator(hostname: str) -> None
      :canonical: aiida.orm.computers.Computer._hostname_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._hostname_validator

   .. py:method:: _description_validator(description: str) -> None
      :canonical: aiida.orm.computers.Computer._description_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._description_validator

   .. py:method:: _transport_type_validator(transport_type: str) -> None
      :canonical: aiida.orm.computers.Computer._transport_type_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._transport_type_validator

   .. py:method:: _scheduler_type_validator(scheduler_type: str) -> None
      :canonical: aiida.orm.computers.Computer._scheduler_type_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._scheduler_type_validator

   .. py:method:: _prepend_text_validator(prepend_text: str) -> None
      :canonical: aiida.orm.computers.Computer._prepend_text_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._prepend_text_validator

   .. py:method:: _append_text_validator(append_text: str) -> None
      :canonical: aiida.orm.computers.Computer._append_text_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._append_text_validator

   .. py:method:: _workdir_validator(workdir: str) -> None
      :canonical: aiida.orm.computers.Computer._workdir_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._workdir_validator

   .. py:method:: _mpirun_command_validator(mpirun_cmd: typing.Union[typing.List[str], typing.Tuple[str, ...]]) -> None
      :canonical: aiida.orm.computers.Computer._mpirun_command_validator

      .. autodoc2-docstring:: aiida.orm.computers.Computer._mpirun_command_validator

   .. py:method:: validate() -> None
      :canonical: aiida.orm.computers.Computer.validate

      .. autodoc2-docstring:: aiida.orm.computers.Computer.validate

   .. py:method:: _default_mpiprocs_per_machine_validator(def_cpus_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer._default_mpiprocs_per_machine_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer._default_mpiprocs_per_machine_validator

   .. py:method:: default_memory_per_machine_validator(def_memory_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.default_memory_per_machine_validator
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.computers.Computer.default_memory_per_machine_validator

   .. py:method:: copy() -> aiida.orm.computers.Computer
      :canonical: aiida.orm.computers.Computer.copy

      .. autodoc2-docstring:: aiida.orm.computers.Computer.copy

   .. py:method:: store() -> aiida.orm.computers.Computer
      :canonical: aiida.orm.computers.Computer.store

      .. autodoc2-docstring:: aiida.orm.computers.Computer.store

   .. py:property:: label
      :canonical: aiida.orm.computers.Computer.label
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.label

   .. py:property:: description
      :canonical: aiida.orm.computers.Computer.description
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.description

   .. py:property:: hostname
      :canonical: aiida.orm.computers.Computer.hostname
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.hostname

   .. py:property:: scheduler_type
      :canonical: aiida.orm.computers.Computer.scheduler_type
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.scheduler_type

   .. py:property:: transport_type
      :canonical: aiida.orm.computers.Computer.transport_type
      :type: str

      .. autodoc2-docstring:: aiida.orm.computers.Computer.transport_type

   .. py:property:: metadata
      :canonical: aiida.orm.computers.Computer.metadata
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.orm.computers.Computer.metadata

   .. py:method:: delete_property(name: str, raise_exception: bool = True) -> None
      :canonical: aiida.orm.computers.Computer.delete_property

      .. autodoc2-docstring:: aiida.orm.computers.Computer.delete_property

   .. py:method:: set_property(name: str, value: typing.Any) -> None
      :canonical: aiida.orm.computers.Computer.set_property

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_property

   .. py:method:: get_property(name: str, *args: typing.Any) -> typing.Any
      :canonical: aiida.orm.computers.Computer.get_property

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_property

   .. py:method:: get_prepend_text() -> str
      :canonical: aiida.orm.computers.Computer.get_prepend_text

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_prepend_text

   .. py:method:: set_prepend_text(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_prepend_text

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_prepend_text

   .. py:method:: get_append_text() -> str
      :canonical: aiida.orm.computers.Computer.get_append_text

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_append_text

   .. py:method:: set_append_text(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_append_text

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_append_text

   .. py:method:: get_use_double_quotes() -> bool
      :canonical: aiida.orm.computers.Computer.get_use_double_quotes

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_use_double_quotes

   .. py:method:: set_use_double_quotes(val: bool) -> None
      :canonical: aiida.orm.computers.Computer.set_use_double_quotes

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_use_double_quotes

   .. py:method:: get_mpirun_command() -> typing.List[str]
      :canonical: aiida.orm.computers.Computer.get_mpirun_command

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_mpirun_command

   .. py:method:: set_mpirun_command(val: typing.Union[typing.List[str], typing.Tuple[str, ...]]) -> None
      :canonical: aiida.orm.computers.Computer.set_mpirun_command

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_mpirun_command

   .. py:method:: get_default_mpiprocs_per_machine() -> typing.Optional[int]
      :canonical: aiida.orm.computers.Computer.get_default_mpiprocs_per_machine

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_default_mpiprocs_per_machine

   .. py:method:: set_default_mpiprocs_per_machine(def_cpus_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.set_default_mpiprocs_per_machine

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_default_mpiprocs_per_machine

   .. py:method:: get_default_memory_per_machine() -> typing.Optional[int]
      :canonical: aiida.orm.computers.Computer.get_default_memory_per_machine

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_default_memory_per_machine

   .. py:method:: set_default_memory_per_machine(def_memory_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.set_default_memory_per_machine

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_default_memory_per_machine

   .. py:method:: get_minimum_job_poll_interval() -> float
      :canonical: aiida.orm.computers.Computer.get_minimum_job_poll_interval

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_minimum_job_poll_interval

   .. py:method:: set_minimum_job_poll_interval(interval: float) -> None
      :canonical: aiida.orm.computers.Computer.set_minimum_job_poll_interval

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_minimum_job_poll_interval

   .. py:method:: get_workdir() -> str
      :canonical: aiida.orm.computers.Computer.get_workdir

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_workdir

   .. py:method:: set_workdir(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_workdir

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_workdir

   .. py:method:: get_shebang() -> str
      :canonical: aiida.orm.computers.Computer.get_shebang

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_shebang

   .. py:method:: set_shebang(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_shebang

      .. autodoc2-docstring:: aiida.orm.computers.Computer.set_shebang

   .. py:method:: get_authinfo(user: aiida.orm.User) -> aiida.orm.AuthInfo
      :canonical: aiida.orm.computers.Computer.get_authinfo

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_authinfo

   .. py:property:: is_configured
      :canonical: aiida.orm.computers.Computer.is_configured
      :type: bool

      .. autodoc2-docstring:: aiida.orm.computers.Computer.is_configured

   .. py:method:: is_user_configured(user: aiida.orm.User) -> bool
      :canonical: aiida.orm.computers.Computer.is_user_configured

      .. autodoc2-docstring:: aiida.orm.computers.Computer.is_user_configured

   .. py:method:: is_user_enabled(user: aiida.orm.User) -> bool
      :canonical: aiida.orm.computers.Computer.is_user_enabled

      .. autodoc2-docstring:: aiida.orm.computers.Computer.is_user_enabled

   .. py:method:: get_transport(user: typing.Optional[aiida.orm.User] = None) -> aiida.transports.Transport
      :canonical: aiida.orm.computers.Computer.get_transport

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_transport

   .. py:method:: get_transport_class() -> typing.Type[aiida.transports.Transport]
      :canonical: aiida.orm.computers.Computer.get_transport_class

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_transport_class

   .. py:method:: get_scheduler() -> aiida.schedulers.Scheduler
      :canonical: aiida.orm.computers.Computer.get_scheduler

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_scheduler

   .. py:method:: configure(user: typing.Optional[aiida.orm.User] = None, **kwargs: typing.Any) -> aiida.orm.AuthInfo
      :canonical: aiida.orm.computers.Computer.configure

      .. autodoc2-docstring:: aiida.orm.computers.Computer.configure

   .. py:method:: get_configuration(user: typing.Optional[aiida.orm.User] = None) -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.computers.Computer.get_configuration

      .. autodoc2-docstring:: aiida.orm.computers.Computer.get_configuration

.. py:class:: ComputerEntityLoader
   :canonical: aiida.orm.utils.loaders.ComputerEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   .. autodoc2-docstring:: aiida.orm.utils.loaders.ComputerEntityLoader

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.ComputerEntityLoader.orm_base_class

      .. autodoc2-docstring:: aiida.orm.utils.loaders.ComputerEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.ComputerEntityLoader._get_query_builder_label_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.ComputerEntityLoader._get_query_builder_label_identifier

.. py:class:: ContainerizedCode(engine_command: str, image_name: str, **kwargs)
   :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.installed.InstalledCode`

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode.__init__

   .. py:attribute:: _KEY_ATTRIBUTE_ENGINE_COMMAND
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_ENGINE_COMMAND
      :type: str
      :value: 'engine_command'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_ENGINE_COMMAND

   .. py:attribute:: _KEY_ATTRIBUTE_IMAGE_NAME
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_IMAGE_NAME
      :type: str
      :value: 'image_name'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_IMAGE_NAME

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.filepath_executable
      :type: pathlib.PurePosixPath

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode.filepath_executable

   .. py:property:: engine_command
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.engine_command
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode.engine_command

   .. py:property:: image_name
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.image_name
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode.image_name

   .. py:method:: get_prepend_cmdline_params(mpi_args: list[str] | None = None, extra_mpirun_params: list[str] | None = None) -> list[str]
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.get_prepend_cmdline_params

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode.get_prepend_cmdline_params

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._get_cli_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.containerized.ContainerizedCode._get_cli_options

.. py:data:: DESCENDING
   :canonical: aiida.orm.logs.DESCENDING
   :value: 'desc'

   .. autodoc2-docstring:: aiida.orm.logs.DESCENDING

.. py:class:: Data(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.data.Data

   Bases: :py:obj:`aiida.orm.nodes.node.Node`

   .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.__init__

   .. py:attribute:: _source_attributes
      :canonical: aiida.orm.nodes.data.data.Data._source_attributes
      :value: ['db_name', 'db_uri', 'uri', 'id', 'version', 'extras', 'source_md5', 'description', 'license']

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._source_attributes

   .. py:attribute:: _export_format_replacements
      :canonical: aiida.orm.nodes.data.data.Data._export_format_replacements
      :type: typing.Dict[str, str]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._export_format_replacements

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.data.Data._storable
      :value: True

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._storable

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.data.data.Data._unstorable_message
      :value: 'storing for this node has been disabled'

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._unstorable_message

   .. py:method:: __copy__()
      :canonical: aiida.orm.nodes.data.data.Data.__copy__

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.__copy__

   .. py:method:: __deepcopy__(memo)
      :canonical: aiida.orm.nodes.data.data.Data.__deepcopy__

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.__deepcopy__

   .. py:method:: clone()
      :canonical: aiida.orm.nodes.data.data.Data.clone

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.clone

   .. py:property:: source
      :canonical: aiida.orm.nodes.data.data.Data.source

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.source

   .. py:method:: set_source(source)
      :canonical: aiida.orm.nodes.data.data.Data.set_source

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.set_source

   .. py:property:: creator
      :canonical: aiida.orm.nodes.data.data.Data.creator

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.creator

   .. py:method:: _exportcontent(fileformat, main_file_name='', **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data._exportcontent

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._exportcontent

   .. py:method:: export(path, fileformat=None, overwrite=False, **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data.export

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.export

   .. py:method:: _get_exporters()
      :canonical: aiida.orm.nodes.data.data.Data._get_exporters

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._get_exporters

   .. py:method:: get_export_formats()
      :canonical: aiida.orm.nodes.data.data.Data.get_export_formats
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.get_export_formats

   .. py:method:: importstring(inputstring, fileformat, **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data.importstring

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.importstring

   .. py:method:: importfile(fname, fileformat=None)
      :canonical: aiida.orm.nodes.data.data.Data.importfile

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.importfile

   .. py:method:: _get_importers()
      :canonical: aiida.orm.nodes.data.data.Data._get_importers

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._get_importers

   .. py:method:: convert(object_format=None, *args)
      :canonical: aiida.orm.nodes.data.data.Data.convert

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data.convert

   .. py:method:: _get_converters()
      :canonical: aiida.orm.nodes.data.data.Data._get_converters

      .. autodoc2-docstring:: aiida.orm.nodes.data.data.Data._get_converters

.. py:class:: Dict(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.dict.Dict

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.__init__

   .. py:method:: __getitem__(key)
      :canonical: aiida.orm.nodes.data.dict.Dict.__getitem__

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.__getitem__

   .. py:method:: __setitem__(key, value)
      :canonical: aiida.orm.nodes.data.dict.Dict.__setitem__

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.__setitem__

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.dict.Dict.__eq__

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.__eq__

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.nodes.data.dict.Dict.__contains__

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.__contains__

   .. py:method:: set_dict(dictionary)
      :canonical: aiida.orm.nodes.data.dict.Dict.set_dict

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.set_dict

   .. py:method:: update_dict(dictionary)
      :canonical: aiida.orm.nodes.data.dict.Dict.update_dict

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.update_dict

   .. py:method:: get_dict()
      :canonical: aiida.orm.nodes.data.dict.Dict.get_dict

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.get_dict

   .. py:method:: keys()
      :canonical: aiida.orm.nodes.data.dict.Dict.keys

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.keys

   .. py:method:: items()
      :canonical: aiida.orm.nodes.data.dict.Dict.items

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.items

   .. py:property:: dict
      :canonical: aiida.orm.nodes.data.dict.Dict.dict

      .. autodoc2-docstring:: aiida.orm.nodes.data.dict.Dict.dict

.. py:class:: Entity(backend_entity: aiida.orm.entities.BackendEntityType)
   :canonical: aiida.orm.entities.Entity

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`aiida.orm.entities.BackendEntityType`\ , :py:obj:`aiida.orm.entities.CollectionType`\ ]

   .. autodoc2-docstring:: aiida.orm.entities.Entity

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.entities.Entity.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.entities.Entity._CLS_COLLECTION
      :type: typing.Type[aiida.orm.entities.CollectionType]
      :value: None

      .. autodoc2-docstring:: aiida.orm.entities.Entity._CLS_COLLECTION

   .. py:method:: objects() -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Entity.objects

      .. autodoc2-docstring:: aiida.orm.entities.Entity.objects

   .. py:method:: collection() -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Entity.collection

      .. autodoc2-docstring:: aiida.orm.entities.Entity.collection

   .. py:method:: get(**kwargs)
      :canonical: aiida.orm.entities.Entity.get
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.entities.Entity.get

   .. py:method:: from_backend_entity(backend_entity: aiida.orm.entities.BackendEntityType) -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Entity.from_backend_entity
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.entities.Entity.from_backend_entity

   .. py:method:: __getstate__()
      :canonical: aiida.orm.entities.Entity.__getstate__

      .. autodoc2-docstring:: aiida.orm.entities.Entity.__getstate__

   .. py:method:: initialize() -> None
      :canonical: aiida.orm.entities.Entity.initialize

      .. autodoc2-docstring:: aiida.orm.entities.Entity.initialize

   .. py:property:: id
      :canonical: aiida.orm.entities.Entity.id
      :type: int

      .. autodoc2-docstring:: aiida.orm.entities.Entity.id

   .. py:property:: pk
      :canonical: aiida.orm.entities.Entity.pk
      :type: int

      .. autodoc2-docstring:: aiida.orm.entities.Entity.pk

   .. py:method:: store() -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Entity.store

      .. autodoc2-docstring:: aiida.orm.entities.Entity.store

   .. py:property:: is_stored
      :canonical: aiida.orm.entities.Entity.is_stored
      :type: bool

      .. autodoc2-docstring:: aiida.orm.entities.Entity.is_stored

   .. py:property:: backend
      :canonical: aiida.orm.entities.Entity.backend
      :type: aiida.orm.implementation.StorageBackend

      .. autodoc2-docstring:: aiida.orm.entities.Entity.backend

   .. py:property:: backend_entity
      :canonical: aiida.orm.entities.Entity.backend_entity
      :type: aiida.orm.entities.BackendEntityType

      .. autodoc2-docstring:: aiida.orm.entities.Entity.backend_entity

.. py:class:: EntityExtras(entity: typing.Union[aiida.orm.nodes.node.Node, aiida.orm.groups.Group])
   :canonical: aiida.orm.extras.EntityExtras

   .. autodoc2-docstring:: aiida.orm.extras.EntityExtras

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.__init__

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.extras.EntityExtras.__contains__

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.__contains__

   .. py:property:: all
      :canonical: aiida.orm.extras.EntityExtras.all
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.all

   .. py:method:: get(key: str, default: typing.Any = _NO_DEFAULT) -> typing.Any
      :canonical: aiida.orm.extras.EntityExtras.get

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.get

   .. py:method:: get_many(keys: typing.List[str]) -> typing.List[typing.Any]
      :canonical: aiida.orm.extras.EntityExtras.get_many

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.get_many

   .. py:method:: set(key: str, value: typing.Any) -> None
      :canonical: aiida.orm.extras.EntityExtras.set

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.set

   .. py:method:: set_many(extras: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.extras.EntityExtras.set_many

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.set_many

   .. py:method:: reset(extras: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.extras.EntityExtras.reset

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.reset

   .. py:method:: delete(key: str) -> None
      :canonical: aiida.orm.extras.EntityExtras.delete

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.delete

   .. py:method:: delete_many(keys: typing.List[str]) -> None
      :canonical: aiida.orm.extras.EntityExtras.delete_many

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.delete_many

   .. py:method:: clear() -> None
      :canonical: aiida.orm.extras.EntityExtras.clear

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.clear

   .. py:method:: items() -> typing.Iterable[typing.Tuple[str, typing.Any]]
      :canonical: aiida.orm.extras.EntityExtras.items

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.items

   .. py:method:: keys() -> typing.Iterable[str]
      :canonical: aiida.orm.extras.EntityExtras.keys

      .. autodoc2-docstring:: aiida.orm.extras.EntityExtras.keys

.. py:class:: EntityTypes
   :canonical: aiida.orm.entities.EntityTypes

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.orm.entities.EntityTypes

   .. py:attribute:: AUTHINFO
      :canonical: aiida.orm.entities.EntityTypes.AUTHINFO
      :value: 'authinfo'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.AUTHINFO

   .. py:attribute:: COMMENT
      :canonical: aiida.orm.entities.EntityTypes.COMMENT
      :value: 'comment'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.COMMENT

   .. py:attribute:: COMPUTER
      :canonical: aiida.orm.entities.EntityTypes.COMPUTER
      :value: 'computer'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.COMPUTER

   .. py:attribute:: GROUP
      :canonical: aiida.orm.entities.EntityTypes.GROUP
      :value: 'group'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.GROUP

   .. py:attribute:: LOG
      :canonical: aiida.orm.entities.EntityTypes.LOG
      :value: 'log'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.LOG

   .. py:attribute:: NODE
      :canonical: aiida.orm.entities.EntityTypes.NODE
      :value: 'node'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.NODE

   .. py:attribute:: USER
      :canonical: aiida.orm.entities.EntityTypes.USER
      :value: 'user'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.USER

   .. py:attribute:: LINK
      :canonical: aiida.orm.entities.EntityTypes.LINK
      :value: 'link'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.LINK

   .. py:attribute:: GROUP_NODE
      :canonical: aiida.orm.entities.EntityTypes.GROUP_NODE
      :value: 'group_node'

      .. autodoc2-docstring:: aiida.orm.entities.EntityTypes.GROUP_NODE

.. py:class:: EnumData(member: enum.Enum, *args, **kwargs)
   :canonical: aiida.orm.nodes.data.enum.EnumData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.__init__

   .. py:attribute:: KEY_NAME
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_NAME
      :value: 'name'

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.KEY_NAME

   .. py:attribute:: KEY_VALUE
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_VALUE
      :value: 'value'

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.KEY_VALUE

   .. py:attribute:: KEY_IDENTIFIER
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_IDENTIFIER
      :value: 'identifier'

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.KEY_IDENTIFIER

   .. py:property:: name
      :canonical: aiida.orm.nodes.data.enum.EnumData.name
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.name

   .. py:property:: value
      :canonical: aiida.orm.nodes.data.enum.EnumData.value
      :type: typing.Any

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.value

   .. py:method:: get_enum() -> typing.Type[aiida.orm.nodes.data.enum.EnumType]
      :canonical: aiida.orm.nodes.data.enum.EnumData.get_enum

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.get_enum

   .. py:method:: get_member() -> aiida.orm.nodes.data.enum.EnumType
      :canonical: aiida.orm.nodes.data.enum.EnumData.get_member

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.get_member

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.orm.nodes.data.enum.EnumData.__eq__

      .. autodoc2-docstring:: aiida.orm.nodes.data.enum.EnumData.__eq__

.. py:class:: Float
   :canonical: aiida.orm.nodes.data.float.Float

   Bases: :py:obj:`aiida.orm.nodes.data.numeric.NumericType`

   .. autodoc2-docstring:: aiida.orm.nodes.data.float.Float

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.float.Float._type
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.float.Float._type

.. py:class:: FolderData(**kwargs)
   :canonical: aiida.orm.nodes.data.folder.FolderData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.folder.FolderData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.folder.FolderData.__init__

.. py:class:: Group(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.Group

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendGroup`\ , :py:obj:`aiida.orm.groups.GroupCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.groups.Group

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.groups.Group.__init__

   .. py:attribute:: _type_string
      :canonical: aiida.orm.groups.Group._type_string
      :type: typing.ClassVar[typing.Optional[str]]
      :value: None

      .. autodoc2-docstring:: aiida.orm.groups.Group._type_string

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.groups.Group._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.groups.Group._CLS_COLLECTION

   .. py:method:: base() -> aiida.orm.groups.GroupBase
      :canonical: aiida.orm.groups.Group.base

      .. autodoc2-docstring:: aiida.orm.groups.Group.base

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.groups.Group.__repr__

      .. autodoc2-docstring:: aiida.orm.groups.Group.__repr__

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.groups.Group.__str__

      .. autodoc2-docstring:: aiida.orm.groups.Group.__str__

   .. py:method:: store() -> aiida.orm.groups.SelfType
      :canonical: aiida.orm.groups.Group.store

      .. autodoc2-docstring:: aiida.orm.groups.Group.store

   .. py:method:: entry_point() -> typing.Optional[aiida.plugins.entry_point.EntryPoint]
      :canonical: aiida.orm.groups.Group.entry_point

      .. autodoc2-docstring:: aiida.orm.groups.Group.entry_point

   .. py:property:: uuid
      :canonical: aiida.orm.groups.Group.uuid
      :type: str

      .. autodoc2-docstring:: aiida.orm.groups.Group.uuid

   .. py:property:: label
      :canonical: aiida.orm.groups.Group.label
      :type: str

      .. autodoc2-docstring:: aiida.orm.groups.Group.label

   .. py:property:: description
      :canonical: aiida.orm.groups.Group.description
      :type: str

      .. autodoc2-docstring:: aiida.orm.groups.Group.description

   .. py:property:: type_string
      :canonical: aiida.orm.groups.Group.type_string
      :type: str

      .. autodoc2-docstring:: aiida.orm.groups.Group.type_string

   .. py:property:: user
      :canonical: aiida.orm.groups.Group.user
      :type: aiida.orm.User

      .. autodoc2-docstring:: aiida.orm.groups.Group.user

   .. py:method:: count() -> int
      :canonical: aiida.orm.groups.Group.count

      .. autodoc2-docstring:: aiida.orm.groups.Group.count

   .. py:property:: nodes
      :canonical: aiida.orm.groups.Group.nodes
      :type: aiida.orm.convert.ConvertIterator

      .. autodoc2-docstring:: aiida.orm.groups.Group.nodes

   .. py:property:: is_empty
      :canonical: aiida.orm.groups.Group.is_empty
      :type: bool

      .. autodoc2-docstring:: aiida.orm.groups.Group.is_empty

   .. py:method:: clear() -> None
      :canonical: aiida.orm.groups.Group.clear

      .. autodoc2-docstring:: aiida.orm.groups.Group.clear

   .. py:method:: add_nodes(nodes: typing.Union[aiida.orm.nodes.Node, typing.Sequence[aiida.orm.nodes.Node]]) -> None
      :canonical: aiida.orm.groups.Group.add_nodes

      .. autodoc2-docstring:: aiida.orm.groups.Group.add_nodes

   .. py:method:: remove_nodes(nodes: typing.Union[aiida.orm.nodes.Node, typing.Sequence[aiida.orm.nodes.Node]]) -> None
      :canonical: aiida.orm.groups.Group.remove_nodes

      .. autodoc2-docstring:: aiida.orm.groups.Group.remove_nodes

   .. py:method:: is_user_defined() -> bool
      :canonical: aiida.orm.groups.Group.is_user_defined

      .. autodoc2-docstring:: aiida.orm.groups.Group.is_user_defined

   .. py:attribute:: _deprecated_extra_methods
      :canonical: aiida.orm.groups.Group._deprecated_extra_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.groups.Group._deprecated_extra_methods

   .. py:method:: __getattr__(name: str) -> typing.Any
      :canonical: aiida.orm.groups.Group.__getattr__

      .. autodoc2-docstring:: aiida.orm.groups.Group.__getattr__

.. py:class:: GroupEntityLoader
   :canonical: aiida.orm.utils.loaders.GroupEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   .. autodoc2-docstring:: aiida.orm.utils.loaders.GroupEntityLoader

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.GroupEntityLoader.orm_base_class

      .. autodoc2-docstring:: aiida.orm.utils.loaders.GroupEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.GroupEntityLoader._get_query_builder_label_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.GroupEntityLoader._get_query_builder_label_identifier

.. py:class:: ImportGroup(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.ImportGroup

   Bases: :py:obj:`aiida.orm.groups.Group`

   .. autodoc2-docstring:: aiida.orm.groups.ImportGroup

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.groups.ImportGroup.__init__

.. py:class:: InstalledCode(computer: aiida.orm.Computer, filepath_executable: str, **kwargs)
   :canonical: aiida.orm.nodes.data.code.installed.InstalledCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.legacy.Code`

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.__init__

   .. py:attribute:: _KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :type: str
      :value: 'filepath_executable'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode._validate

   .. py:method:: validate_filepath_executable()
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.validate_filepath_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.validate_filepath_executable

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.can_run_on_computer

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.can_run_on_computer

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.get_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.get_executable

   .. py:property:: computer
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.computer
      :type: aiida.orm.Computer

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.computer

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.full_label
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.full_label

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.filepath_executable
      :type: pathlib.PurePosixPath

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.filepath_executable

   .. py:method:: cli_validate_label_uniqueness(ctx, _, value)
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.cli_validate_label_uniqueness
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode.cli_validate_label_uniqueness

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._get_cli_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.installed.InstalledCode._get_cli_options

.. py:class:: Int
   :canonical: aiida.orm.nodes.data.int.Int

   Bases: :py:obj:`aiida.orm.nodes.data.numeric.NumericType`

   .. autodoc2-docstring:: aiida.orm.nodes.data.int.Int

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.int.Int._type
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.int.Int._type

.. py:class:: JsonableData(obj: aiida.orm.nodes.data.jsonable.JsonSerializableProtocol, *args, **kwargs)
   :canonical: aiida.orm.nodes.data.jsonable.JsonableData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData.__init__

   .. py:method:: _deserialize_float_constants(data: typing.Any)
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData._deserialize_float_constants
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData._deserialize_float_constants

   .. py:method:: _get_object() -> aiida.orm.nodes.data.jsonable.JsonSerializableProtocol
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData._get_object

      .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData._get_object

   .. py:property:: obj
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData.obj
      :type: aiida.orm.nodes.data.jsonable.JsonSerializableProtocol

      .. autodoc2-docstring:: aiida.orm.nodes.data.jsonable.JsonableData.obj

.. py:class:: Kind(**kwargs)
   :canonical: aiida.orm.nodes.data.structure.Kind

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.__init__

   .. py:method:: get_raw()
      :canonical: aiida.orm.nodes.data.structure.Kind.get_raw

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.get_raw

   .. py:method:: reset_mass()
      :canonical: aiida.orm.nodes.data.structure.Kind.reset_mass

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.reset_mass

   .. py:property:: name
      :canonical: aiida.orm.nodes.data.structure.Kind.name

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.name

   .. py:method:: set_automatic_kind_name(tag=None)
      :canonical: aiida.orm.nodes.data.structure.Kind.set_automatic_kind_name

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.set_automatic_kind_name

   .. py:method:: compare_with(other_kind)
      :canonical: aiida.orm.nodes.data.structure.Kind.compare_with

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.compare_with

   .. py:property:: mass
      :canonical: aiida.orm.nodes.data.structure.Kind.mass

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.mass

   .. py:property:: weights
      :canonical: aiida.orm.nodes.data.structure.Kind.weights

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.weights

   .. py:method:: get_symbols_string()
      :canonical: aiida.orm.nodes.data.structure.Kind.get_symbols_string

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.get_symbols_string

   .. py:property:: symbol
      :canonical: aiida.orm.nodes.data.structure.Kind.symbol

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.symbol

   .. py:property:: symbols
      :canonical: aiida.orm.nodes.data.structure.Kind.symbols

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.symbols

   .. py:method:: set_symbols_and_weights(symbols, weights)
      :canonical: aiida.orm.nodes.data.structure.Kind.set_symbols_and_weights

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.set_symbols_and_weights

   .. py:property:: is_alloy
      :canonical: aiida.orm.nodes.data.structure.Kind.is_alloy

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.is_alloy

   .. py:property:: has_vacancies
      :canonical: aiida.orm.nodes.data.structure.Kind.has_vacancies

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.has_vacancies

   .. py:method:: __repr__()
      :canonical: aiida.orm.nodes.data.structure.Kind.__repr__

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.__repr__

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.structure.Kind.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Kind.__str__

.. py:class:: KpointsData
   :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_description

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.get_description

   .. py:property:: cell
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.cell

   .. py:method:: _set_cell(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._set_cell

   .. py:property:: pbc
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.pbc

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.pbc

   .. py:method:: _set_pbc(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_pbc

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._set_pbc

   .. py:property:: labels
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.labels

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.labels

   .. py:method:: _set_labels(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_labels

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._set_labels

   .. py:method:: _change_reference(kpoints, to_cartesian=True)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._change_reference

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._change_reference

   .. py:method:: set_cell_from_structure(structuredata)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell_from_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell_from_structure

   .. py:method:: set_cell(cell, pbc=None)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell

   .. py:property:: reciprocal_cell
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.reciprocal_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.reciprocal_cell

   .. py:method:: set_kpoints_mesh(mesh, offset=None)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh

   .. py:method:: get_kpoints_mesh(print_list=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints_mesh

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints_mesh

   .. py:method:: set_kpoints_mesh_from_density(distance, offset=None, force_parity=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh_from_density

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh_from_density

   .. py:property:: _dimension
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._dimension

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._dimension

   .. py:method:: _validate_kpoints_weights(kpoints, weights)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._validate_kpoints_weights

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData._validate_kpoints_weights

   .. py:method:: set_kpoints(kpoints, cartesian=False, labels=None, weights=None, fill_values=0)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints

   .. py:method:: get_kpoints(also_weights=False, cartesian=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints

.. py:class:: LinkManager(link_triples: typing.List[aiida.orm.utils.links.LinkTriple])
   :canonical: aiida.orm.utils.links.LinkManager

   .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.__init__

   .. py:method:: __iter__() -> typing.Iterator[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.__iter__

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.__iter__

   .. py:method:: __next__() -> typing.Generator[aiida.orm.utils.links.LinkTriple, None, None]
      :canonical: aiida.orm.utils.links.LinkManager.__next__

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.__next__

   .. py:method:: __bool__()
      :canonical: aiida.orm.utils.links.LinkManager.__bool__

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.__bool__

   .. py:method:: next() -> typing.Generator[aiida.orm.utils.links.LinkTriple, None, None]
      :canonical: aiida.orm.utils.links.LinkManager.next

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.next

   .. py:method:: one() -> aiida.orm.utils.links.LinkTriple
      :canonical: aiida.orm.utils.links.LinkManager.one

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.one

   .. py:method:: first() -> typing.Optional[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.first

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.first

   .. py:method:: all() -> typing.List[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.all

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.all

   .. py:method:: all_nodes() -> typing.List[aiida.orm.Node]
      :canonical: aiida.orm.utils.links.LinkManager.all_nodes

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.all_nodes

   .. py:method:: all_link_pairs() -> typing.List[aiida.orm.utils.links.LinkPair]
      :canonical: aiida.orm.utils.links.LinkManager.all_link_pairs

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.all_link_pairs

   .. py:method:: all_link_labels() -> typing.List[str]
      :canonical: aiida.orm.utils.links.LinkManager.all_link_labels

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.all_link_labels

   .. py:method:: get_node_by_label(label: str) -> aiida.orm.Node
      :canonical: aiida.orm.utils.links.LinkManager.get_node_by_label

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.get_node_by_label

   .. py:method:: nested(sort=True)
      :canonical: aiida.orm.utils.links.LinkManager.nested

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkManager.nested

.. py:class:: LinkPair
   :canonical: aiida.orm.utils.links.LinkPair

   Bases: :py:obj:`typing.NamedTuple`

   .. autodoc2-docstring:: aiida.orm.utils.links.LinkPair

   .. py:attribute:: link_type
      :canonical: aiida.orm.utils.links.LinkPair.link_type
      :type: aiida.common.links.LinkType
      :value: None

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkPair.link_type

   .. py:attribute:: link_label
      :canonical: aiida.orm.utils.links.LinkPair.link_label
      :type: str
      :value: None

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkPair.link_label

.. py:class:: LinkTriple
   :canonical: aiida.orm.utils.links.LinkTriple

   Bases: :py:obj:`typing.NamedTuple`

   .. autodoc2-docstring:: aiida.orm.utils.links.LinkTriple

   .. py:attribute:: node
      :canonical: aiida.orm.utils.links.LinkTriple.node
      :type: aiida.orm.Node
      :value: None

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkTriple.node

   .. py:attribute:: link_type
      :canonical: aiida.orm.utils.links.LinkTriple.link_type
      :type: aiida.common.links.LinkType
      :value: None

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkTriple.link_type

   .. py:attribute:: link_label
      :canonical: aiida.orm.utils.links.LinkTriple.link_label
      :type: str
      :value: None

      .. autodoc2-docstring:: aiida.orm.utils.links.LinkTriple.link_label

.. py:class:: List(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.list.List

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`, :py:obj:`collections.abc.MutableSequence`

   .. autodoc2-docstring:: aiida.orm.nodes.data.list.List

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__init__

   .. py:attribute:: _LIST_KEY
      :canonical: aiida.orm.nodes.data.list.List._LIST_KEY
      :value: 'list'

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List._LIST_KEY

   .. py:method:: __getitem__(item)
      :canonical: aiida.orm.nodes.data.list.List.__getitem__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__getitem__

   .. py:method:: __setitem__(key, value)
      :canonical: aiida.orm.nodes.data.list.List.__setitem__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__setitem__

   .. py:method:: __delitem__(key)
      :canonical: aiida.orm.nodes.data.list.List.__delitem__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__delitem__

   .. py:method:: __len__()
      :canonical: aiida.orm.nodes.data.list.List.__len__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__len__

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.list.List.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__str__

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.list.List.__eq__

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.__eq__

   .. py:method:: append(value)
      :canonical: aiida.orm.nodes.data.list.List.append

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.append

   .. py:method:: extend(value)
      :canonical: aiida.orm.nodes.data.list.List.extend

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.extend

   .. py:method:: insert(i, value)
      :canonical: aiida.orm.nodes.data.list.List.insert

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.insert

   .. py:method:: remove(value)
      :canonical: aiida.orm.nodes.data.list.List.remove

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.remove

   .. py:method:: pop(**kwargs)
      :canonical: aiida.orm.nodes.data.list.List.pop

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.pop

   .. py:method:: index(value)
      :canonical: aiida.orm.nodes.data.list.List.index

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.index

   .. py:method:: count(value)
      :canonical: aiida.orm.nodes.data.list.List.count

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.count

   .. py:method:: sort(key=None, reverse=False)
      :canonical: aiida.orm.nodes.data.list.List.sort

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.sort

   .. py:method:: reverse()
      :canonical: aiida.orm.nodes.data.list.List.reverse

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.reverse

   .. py:method:: get_list()
      :canonical: aiida.orm.nodes.data.list.List.get_list

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.get_list

   .. py:method:: set_list(data)
      :canonical: aiida.orm.nodes.data.list.List.set_list

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List.set_list

   .. py:method:: _using_list_reference()
      :canonical: aiida.orm.nodes.data.list.List._using_list_reference

      .. autodoc2-docstring:: aiida.orm.nodes.data.list.List._using_list_reference

.. py:class:: Log(time: datetime.datetime, loggername: str, levelname: str, dbnode_id: int, message: str = '', metadata: typing.Optional[typing.Dict[str, typing.Any]] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.logs.Log

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendLog`\ , :py:obj:`aiida.orm.logs.LogCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.logs.Log

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.logs.Log.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.logs.Log._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.logs.Log._CLS_COLLECTION

   .. py:property:: uuid
      :canonical: aiida.orm.logs.Log.uuid
      :type: str

      .. autodoc2-docstring:: aiida.orm.logs.Log.uuid

   .. py:property:: time
      :canonical: aiida.orm.logs.Log.time
      :type: datetime.datetime

      .. autodoc2-docstring:: aiida.orm.logs.Log.time

   .. py:property:: loggername
      :canonical: aiida.orm.logs.Log.loggername
      :type: str

      .. autodoc2-docstring:: aiida.orm.logs.Log.loggername

   .. py:property:: levelname
      :canonical: aiida.orm.logs.Log.levelname
      :type: str

      .. autodoc2-docstring:: aiida.orm.logs.Log.levelname

   .. py:property:: dbnode_id
      :canonical: aiida.orm.logs.Log.dbnode_id
      :type: int

      .. autodoc2-docstring:: aiida.orm.logs.Log.dbnode_id

   .. py:property:: message
      :canonical: aiida.orm.logs.Log.message
      :type: str

      .. autodoc2-docstring:: aiida.orm.logs.Log.message

   .. py:property:: metadata
      :canonical: aiida.orm.logs.Log.metadata
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.orm.logs.Log.metadata

.. py:class:: Node(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.node.Node

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendNode`\ , :py:obj:`aiida.orm.nodes.node.NodeCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.nodes.node.Node

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.nodes.node.Node._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._CLS_COLLECTION

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.node.Node._CLS_NODE_LINKS
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._CLS_NODE_LINKS

   .. py:attribute:: _CLS_NODE_CACHING
      :canonical: aiida.orm.nodes.node.Node._CLS_NODE_CACHING
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._CLS_NODE_CACHING

   .. py:attribute:: _plugin_type_string
      :canonical: aiida.orm.nodes.node.Node._plugin_type_string
      :type: typing.ClassVar[str]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._plugin_type_string

   .. py:attribute:: _query_type_string
      :canonical: aiida.orm.nodes.node.Node._query_type_string
      :type: typing.ClassVar[str]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._query_type_string

   .. py:attribute:: _logger
      :canonical: aiida.orm.nodes.node.Node._logger
      :type: typing.Optional[logging.Logger]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._logger

   .. py:attribute:: _updatable_attributes
      :canonical: aiida.orm.nodes.node.Node._updatable_attributes
      :type: typing.Tuple[str, ...]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._updatable_attributes

   .. py:attribute:: _hash_ignored_attributes
      :canonical: aiida.orm.nodes.node.Node._hash_ignored_attributes
      :type: typing.Tuple[str, ...]
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._hash_ignored_attributes

   .. py:attribute:: _cachable
      :canonical: aiida.orm.nodes.node.Node._cachable
      :value: False

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._cachable

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.node.Node._storable
      :value: False

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._storable

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.node.Node._unstorable_message
      :value: 'only Data, WorkflowNode, CalculationNode or their subclasses can be stored'

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._unstorable_message

   .. py:method:: base() -> aiida.orm.nodes.node.NodeBase
      :canonical: aiida.orm.nodes.node.Node.base

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.base

   .. py:method:: _check_mutability_attributes(keys: typing.Optional[typing.List[str]] = None) -> None
      :canonical: aiida.orm.nodes.node.Node._check_mutability_attributes

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._check_mutability_attributes

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.orm.nodes.node.Node.__eq__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__eq__

   .. py:method:: __hash__() -> int
      :canonical: aiida.orm.nodes.node.Node.__hash__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__hash__

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.nodes.node.Node.__repr__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__repr__

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.nodes.node.Node.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__str__

   .. py:method:: __copy__()
      :canonical: aiida.orm.nodes.node.Node.__copy__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__copy__

   .. py:method:: __deepcopy__(memo)
      :canonical: aiida.orm.nodes.node.Node.__deepcopy__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__deepcopy__

   .. py:method:: _validate() -> bool
      :canonical: aiida.orm.nodes.node.Node._validate

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._validate

   .. py:method:: _validate_storability() -> None
      :canonical: aiida.orm.nodes.node.Node._validate_storability

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._validate_storability

   .. py:method:: class_node_type() -> str
      :canonical: aiida.orm.nodes.node.Node.class_node_type

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.class_node_type

   .. py:method:: entry_point() -> typing.Optional[aiida.plugins.entry_point.EntryPoint]
      :canonical: aiida.orm.nodes.node.Node.entry_point

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.entry_point

   .. py:property:: logger
      :canonical: aiida.orm.nodes.node.Node.logger
      :type: typing.Optional[logging.Logger]

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.logger

   .. py:property:: uuid
      :canonical: aiida.orm.nodes.node.Node.uuid
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.uuid

   .. py:property:: node_type
      :canonical: aiida.orm.nodes.node.Node.node_type
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.node_type

   .. py:property:: process_type
      :canonical: aiida.orm.nodes.node.Node.process_type
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.process_type

   .. py:property:: label
      :canonical: aiida.orm.nodes.node.Node.label
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.label

   .. py:property:: description
      :canonical: aiida.orm.nodes.node.Node.description
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.description

   .. py:property:: computer
      :canonical: aiida.orm.nodes.node.Node.computer
      :type: typing.Optional[aiida.orm.computers.Computer]

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.computer

   .. py:property:: user
      :canonical: aiida.orm.nodes.node.Node.user
      :type: aiida.orm.users.User

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.user

   .. py:property:: ctime
      :canonical: aiida.orm.nodes.node.Node.ctime
      :type: datetime.datetime

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.ctime

   .. py:property:: mtime
      :canonical: aiida.orm.nodes.node.Node.mtime
      :type: datetime.datetime

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.mtime

   .. py:method:: store_all(with_transaction: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node.store_all

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.store_all

   .. py:method:: store(with_transaction: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node.store

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.store

   .. py:method:: _store(with_transaction: bool = True, clean: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node._store

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._store

   .. py:method:: _verify_are_parents_stored() -> None
      :canonical: aiida.orm.nodes.node.Node._verify_are_parents_stored

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._verify_are_parents_stored

   .. py:method:: _store_from_cache(cache_node: aiida.orm.nodes.node.Node, with_transaction: bool) -> None
      :canonical: aiida.orm.nodes.node.Node._store_from_cache

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._store_from_cache

   .. py:method:: _add_outputs_from_cache(cache_node: aiida.orm.nodes.node.Node) -> None
      :canonical: aiida.orm.nodes.node.Node._add_outputs_from_cache

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._add_outputs_from_cache

   .. py:method:: get_description() -> str
      :canonical: aiida.orm.nodes.node.Node.get_description

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.get_description

   .. py:property:: is_valid_cache
      :canonical: aiida.orm.nodes.node.Node.is_valid_cache
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.is_valid_cache

   .. py:attribute:: _deprecated_repo_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_repo_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_repo_methods

   .. py:attribute:: _deprecated_attr_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_attr_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_attr_methods

   .. py:attribute:: _deprecated_extra_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_extra_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_extra_methods

   .. py:attribute:: _deprecated_comment_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_comment_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_comment_methods

   .. py:attribute:: _deprecated_caching_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_caching_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_caching_methods

   .. py:attribute:: _deprecated_links_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_links_methods
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node._deprecated_links_methods

   .. py:method:: Collection()
      :canonical: aiida.orm.nodes.node.Node.Collection

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.Collection

   .. py:method:: __getattr__(name: str) -> typing.Any
      :canonical: aiida.orm.nodes.node.Node.__getattr__

      .. autodoc2-docstring:: aiida.orm.nodes.node.Node.__getattr__

.. py:class:: NodeAttributes(node: aiida.orm.nodes.node.Node)
   :canonical: aiida.orm.nodes.attributes.NodeAttributes

   .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.__init__

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.__contains__

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.__contains__

   .. py:property:: all
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.all
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.all

   .. py:method:: get(key: str, default=_NO_DEFAULT) -> typing.Any
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.get

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.get

   .. py:method:: get_many(keys: typing.List[str]) -> typing.List[typing.Any]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.get_many

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.get_many

   .. py:method:: set(key: str, value: typing.Any) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.set

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.set

   .. py:method:: set_many(attributes: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.set_many

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.set_many

   .. py:method:: reset(attributes: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.reset

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.reset

   .. py:method:: delete(key: str) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.delete

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.delete

   .. py:method:: delete_many(keys: typing.List[str]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.delete_many

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.delete_many

   .. py:method:: clear() -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.clear

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.clear

   .. py:method:: items() -> typing.Iterable[typing.Tuple[str, typing.Any]]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.items

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.items

   .. py:method:: keys() -> typing.Iterable[str]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.keys

      .. autodoc2-docstring:: aiida.orm.nodes.attributes.NodeAttributes.keys

.. py:class:: NodeEntityLoader
   :canonical: aiida.orm.utils.loaders.NodeEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   .. autodoc2-docstring:: aiida.orm.utils.loaders.NodeEntityLoader

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.NodeEntityLoader.orm_base_class

      .. autodoc2-docstring:: aiida.orm.utils.loaders.NodeEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.NodeEntityLoader._get_query_builder_label_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.NodeEntityLoader._get_query_builder_label_identifier

.. py:class:: NodeLinksManager(node, link_type, incoming)
   :canonical: aiida.orm.utils.managers.NodeLinksManager

   .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__init__

   .. py:attribute:: _namespace_separator
      :canonical: aiida.orm.utils.managers.NodeLinksManager._namespace_separator
      :value: '__'

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager._namespace_separator

   .. py:method:: _construct_attribute_dict(incoming)
      :canonical: aiida.orm.utils.managers.NodeLinksManager._construct_attribute_dict

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager._construct_attribute_dict

   .. py:method:: _get_keys()
      :canonical: aiida.orm.utils.managers.NodeLinksManager._get_keys

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager._get_keys

   .. py:method:: _get_node_by_link_label(label)
      :canonical: aiida.orm.utils.managers.NodeLinksManager._get_node_by_link_label

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager._get_node_by_link_label

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__dir__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__dir__

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__iter__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__iter__

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__getattr__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__getattr__

   .. py:method:: __contains__(key)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__contains__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__contains__

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__getitem__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__getitem__

   .. py:method:: __str__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__str__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__str__

   .. py:method:: __repr__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__repr__

      .. autodoc2-docstring:: aiida.orm.utils.managers.NodeLinksManager.__repr__

.. py:class:: NodeRepository(node: aiida.orm.nodes.node.Node)
   :canonical: aiida.orm.nodes.repository.NodeRepository

   .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.__init__

   .. py:property:: metadata
      :canonical: aiida.orm.nodes.repository.NodeRepository.metadata
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.metadata

   .. py:method:: _update_repository_metadata()
      :canonical: aiida.orm.nodes.repository.NodeRepository._update_repository_metadata

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._update_repository_metadata

   .. py:method:: _check_mutability()
      :canonical: aiida.orm.nodes.repository.NodeRepository._check_mutability

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._check_mutability

   .. py:property:: _repository
      :canonical: aiida.orm.nodes.repository.NodeRepository._repository
      :type: aiida.repository.Repository

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._repository

   .. py:method:: _store() -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._store

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._store

   .. py:method:: _copy(repo: aiida.orm.nodes.repository.NodeRepository) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._copy

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._copy

   .. py:method:: _clone(repo: aiida.orm.nodes.repository.NodeRepository) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._clone

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository._clone

   .. py:method:: serialize() -> typing.Dict
      :canonical: aiida.orm.nodes.repository.NodeRepository.serialize

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.serialize

   .. py:method:: hash() -> str
      :canonical: aiida.orm.nodes.repository.NodeRepository.hash

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.hash

   .. py:method:: list_objects(path: typing.Optional[str] = None) -> typing.List[aiida.repository.File]
      :canonical: aiida.orm.nodes.repository.NodeRepository.list_objects

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.list_objects

   .. py:method:: list_object_names(path: typing.Optional[str] = None) -> typing.List[str]
      :canonical: aiida.orm.nodes.repository.NodeRepository.list_object_names

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.list_object_names

   .. py:method:: open(path: str, mode='r') -> typing.Iterator[typing.Union[typing.BinaryIO, typing.TextIO]]
      :canonical: aiida.orm.nodes.repository.NodeRepository.open

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.open

   .. py:method:: get_object(path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> aiida.repository.File
      :canonical: aiida.orm.nodes.repository.NodeRepository.get_object

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.get_object

   .. py:method:: get_object_content(path: str, mode='r') -> typing.Union[str, bytes]
      :canonical: aiida.orm.nodes.repository.NodeRepository.get_object_content

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.get_object_content

   .. py:method:: put_object_from_bytes(content: bytes, path: str) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_bytes

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.put_object_from_bytes

   .. py:method:: put_object_from_filelike(handle: io.BufferedReader, path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_filelike

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.put_object_from_filelike

   .. py:method:: put_object_from_file(filepath: str, path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_file

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.put_object_from_file

   .. py:method:: put_object_from_tree(filepath: str, path: typing.Optional[str] = None)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_tree

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.put_object_from_tree

   .. py:method:: walk(path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> typing.Iterable[typing.Tuple[pathlib.PurePosixPath, typing.List[str], typing.List[str]]]
      :canonical: aiida.orm.nodes.repository.NodeRepository.walk

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.walk

   .. py:method:: glob() -> typing.Iterable[pathlib.PurePosixPath]
      :canonical: aiida.orm.nodes.repository.NodeRepository.glob

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.glob

   .. py:method:: copy_tree(target: typing.Union[str, pathlib.Path], path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository.copy_tree

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.copy_tree

   .. py:method:: delete_object(path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.delete_object

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.delete_object

   .. py:method:: erase()
      :canonical: aiida.orm.nodes.repository.NodeRepository.erase

      .. autodoc2-docstring:: aiida.orm.nodes.repository.NodeRepository.erase

.. py:class:: NumericType
   :canonical: aiida.orm.nodes.data.numeric.NumericType

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType

   .. py:method:: __add__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__add__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__add__

   .. py:method:: __radd__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__radd__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__radd__

   .. py:method:: __sub__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__sub__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__sub__

   .. py:method:: __rsub__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rsub__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rsub__

   .. py:method:: __mul__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__mul__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__mul__

   .. py:method:: __rmul__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rmul__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rmul__

   .. py:method:: __div__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__div__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__div__

   .. py:method:: __rdiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rdiv__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rdiv__

   .. py:method:: __truediv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__truediv__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__truediv__

   .. py:method:: __rtruediv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rtruediv__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rtruediv__

   .. py:method:: __floordiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__floordiv__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__floordiv__

   .. py:method:: __rfloordiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rfloordiv__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rfloordiv__

   .. py:method:: __pow__(power)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__pow__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__pow__

   .. py:method:: __lt__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__lt__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__lt__

   .. py:method:: __le__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__le__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__le__

   .. py:method:: __gt__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__gt__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__gt__

   .. py:method:: __ge__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__ge__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__ge__

   .. py:method:: __mod__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__mod__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__mod__

   .. py:method:: __rmod__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rmod__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__rmod__

   .. py:method:: __float__()
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__float__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__float__

   .. py:method:: __int__()
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__int__

      .. autodoc2-docstring:: aiida.orm.nodes.data.numeric.NumericType.__int__

.. py:class:: OrbitalData
   :canonical: aiida.orm.nodes.data.orbital.OrbitalData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.orbital.OrbitalData

   .. py:method:: clear_orbitals()
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.clear_orbitals

      .. autodoc2-docstring:: aiida.orm.nodes.data.orbital.OrbitalData.clear_orbitals

   .. py:method:: get_orbitals(**kwargs)
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.get_orbitals

      .. autodoc2-docstring:: aiida.orm.nodes.data.orbital.OrbitalData.get_orbitals

   .. py:method:: set_orbitals(orbitals)
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.set_orbitals

      .. autodoc2-docstring:: aiida.orm.nodes.data.orbital.OrbitalData.set_orbitals

.. py:function:: OrderSpecifier(field, direction)
   :canonical: aiida.orm.logs.OrderSpecifier

   .. autodoc2-docstring:: aiida.orm.logs.OrderSpecifier

.. py:class:: OrmEntityLoader
   :canonical: aiida.orm.utils.loaders.OrmEntityLoader

   .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader

   .. py:attribute:: label_ambiguity_breaker
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.label_ambiguity_breaker
      :value: '!'

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.label_ambiguity_breaker

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.orm_base_class
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.orm_base_class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_label_identifier
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_label_identifier

   .. py:method:: _get_query_builder_id_identifier(identifier, classes)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_id_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_id_identifier

   .. py:method:: _get_query_builder_uuid_identifier(identifier, classes, query_with_dashes)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_uuid_identifier
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_uuid_identifier

   .. py:method:: get_query_builder(identifier, identifier_type=None, sub_classes=None, query_with_dashes=True, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_query_builder
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.get_query_builder

   .. py:method:: get_options(incomplete, project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.get_options

   .. py:method:: load_entity(identifier, identifier_type=None, sub_classes=None, query_with_dashes=True)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.load_entity
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.load_entity

   .. py:method:: get_query_classes(sub_classes=None)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_query_classes
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.get_query_classes

   .. py:method:: infer_identifier_type(value)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.infer_identifier_type
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.utils.loaders.OrmEntityLoader.infer_identifier_type

.. py:class:: PortableCode(filepath_executable: str, filepath_files: pathlib.Path, **kwargs)
   :canonical: aiida.orm.nodes.data.code.portable.PortableCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.legacy.Code`

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.__init__

   .. py:attribute:: _KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :type: str
      :value: 'filepath_executable'

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode._validate

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.can_run_on_computer

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.can_run_on_computer

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.get_executable

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.get_executable

   .. py:method:: validate_working_directory(folder: aiida.common.folders.Folder)
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.validate_working_directory

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.validate_working_directory

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.full_label
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.full_label

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.filepath_executable
      :type: pathlib.PurePosixPath

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode.filepath_executable

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._get_cli_options
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.code.portable.PortableCode._get_cli_options

.. py:class:: ProcessNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.process.ProcessNode

   Bases: :py:obj:`aiida.orm.utils.mixins.Sealable`, :py:obj:`aiida.orm.nodes.node.Node`

   .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.__init__

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_LINKS
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_LINKS

   .. py:attribute:: _CLS_NODE_CACHING
      :canonical: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_CACHING
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_CACHING

   .. py:attribute:: CHECKPOINT_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.CHECKPOINT_KEY
      :value: 'checkpoints'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.CHECKPOINT_KEY

   .. py:attribute:: EXCEPTION_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXCEPTION_KEY
      :value: 'exception'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.EXCEPTION_KEY

   .. py:attribute:: EXIT_MESSAGE_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXIT_MESSAGE_KEY
      :value: 'exit_message'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.EXIT_MESSAGE_KEY

   .. py:attribute:: EXIT_STATUS_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXIT_STATUS_KEY
      :value: 'exit_status'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.EXIT_STATUS_KEY

   .. py:attribute:: PROCESS_PAUSED_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_PAUSED_KEY
      :value: 'paused'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.PROCESS_PAUSED_KEY

   .. py:attribute:: PROCESS_LABEL_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_LABEL_KEY
      :value: 'process_label'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.PROCESS_LABEL_KEY

   .. py:attribute:: PROCESS_STATE_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATE_KEY
      :value: 'process_state'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATE_KEY

   .. py:attribute:: PROCESS_STATUS_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATUS_KEY
      :value: 'process_status'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATUS_KEY

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.process.ProcessNode._unstorable_message
      :value: 'only Data, WorkflowNode, CalculationNode or their subclasses can be stored'

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode._unstorable_message

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.nodes.process.process.ProcessNode.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.__str__

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.process.ProcessNode._updatable_attributes

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode._updatable_attributes

   .. py:property:: logger
      :canonical: aiida.orm.nodes.process.process.ProcessNode.logger

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.logger

   .. py:method:: get_builder_restart() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.orm.nodes.process.process.ProcessNode.get_builder_restart

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.get_builder_restart

   .. py:property:: process_class
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_class
      :type: typing.Type[aiida.engine.processes.Process]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.process_class

   .. py:method:: set_process_type(process_type_string: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_type

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_process_type

   .. py:property:: process_label
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_label
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.process_label

   .. py:method:: set_process_label(label: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_label

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_process_label

   .. py:property:: process_state
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_state
      :type: typing.Optional[plumpy.process_states.ProcessState]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.process_state

   .. py:method:: set_process_state(state: typing.Union[str, plumpy.process_states.ProcessState, None])
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_state

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_process_state

   .. py:property:: process_status
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_status
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.process_status

   .. py:method:: set_process_status(status: typing.Optional[str]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_status

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_process_status

   .. py:property:: is_terminated
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_terminated
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_terminated

   .. py:property:: is_excepted
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_excepted
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_excepted

   .. py:property:: is_killed
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_killed
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_killed

   .. py:property:: is_finished
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_finished
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_finished

   .. py:property:: is_finished_ok
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_finished_ok
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_finished_ok

   .. py:property:: is_failed
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_failed
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.is_failed

   .. py:property:: exit_status
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exit_status
      :type: typing.Optional[int]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.exit_status

   .. py:method:: set_exit_status(status: typing.Union[None, enum.Enum, int]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exit_status

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_exit_status

   .. py:property:: exit_message
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exit_message
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.exit_message

   .. py:method:: set_exit_message(message: typing.Optional[str]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exit_message

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_exit_message

   .. py:property:: exception
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exception
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.exception

   .. py:method:: set_exception(exception: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exception

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_exception

   .. py:property:: checkpoint
      :canonical: aiida.orm.nodes.process.process.ProcessNode.checkpoint
      :type: typing.Optional[typing.Dict[str, typing.Any]]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.checkpoint

   .. py:method:: set_checkpoint(checkpoint: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_checkpoint

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.set_checkpoint

   .. py:method:: delete_checkpoint() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.delete_checkpoint

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.delete_checkpoint

   .. py:property:: paused
      :canonical: aiida.orm.nodes.process.process.ProcessNode.paused
      :type: bool

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.paused

   .. py:method:: pause() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.pause

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.pause

   .. py:method:: unpause() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.unpause

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.unpause

   .. py:property:: called
      :canonical: aiida.orm.nodes.process.process.ProcessNode.called
      :type: typing.List[aiida.orm.nodes.process.process.ProcessNode]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.called

   .. py:property:: called_descendants
      :canonical: aiida.orm.nodes.process.process.ProcessNode.called_descendants
      :type: typing.List[aiida.orm.nodes.process.process.ProcessNode]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.called_descendants

   .. py:property:: caller
      :canonical: aiida.orm.nodes.process.process.ProcessNode.caller
      :type: typing.Optional[aiida.orm.nodes.process.process.ProcessNode]

      .. autodoc2-docstring:: aiida.orm.nodes.process.process.ProcessNode.caller

.. py:class:: ProjectionData(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.projection.ProjectionData

   Bases: :py:obj:`aiida.orm.nodes.data.orbital.OrbitalData`, :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.__init__

   .. py:method:: _check_projections_bands(projection_array)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._check_projections_bands

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData._check_projections_bands

   .. py:method:: set_reference_bandsdata(value)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_reference_bandsdata

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.set_reference_bandsdata

   .. py:method:: get_reference_bandsdata()
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_reference_bandsdata

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.get_reference_bandsdata

   .. py:method:: _find_orbitals_and_indices(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._find_orbitals_and_indices

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData._find_orbitals_and_indices

   .. py:method:: get_pdos(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_pdos

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.get_pdos

   .. py:method:: get_projections(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_projections

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.get_projections

   .. py:method:: _from_index_to_arrayname(index)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._from_index_to_arrayname
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData._from_index_to_arrayname

   .. py:method:: set_projectiondata(list_of_orbitals, list_of_projections=None, list_of_energy=None, list_of_pdos=None, tags=None, bands_check=True)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_projectiondata

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.set_projectiondata

   .. py:method:: set_orbitals(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_orbitals
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.projection.ProjectionData.set_orbitals

.. py:class:: QueryBuilder(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, *, debug: bool = False, path: typing.Optional[typing.Sequence[typing.Union[str, typing.Dict[str, typing.Any], aiida.orm.querybuilder.EntityClsType]]] = (), filters: typing.Optional[typing.Dict[str, aiida.orm.querybuilder.FilterType]] = None, project: typing.Optional[typing.Dict[str, aiida.orm.querybuilder.ProjectType]] = None, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, distinct: bool = False)
   :canonical: aiida.orm.querybuilder.QueryBuilder

   .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.__init__

   .. py:attribute:: _EDGE_TAG_DELIM
      :canonical: aiida.orm.querybuilder.QueryBuilder._EDGE_TAG_DELIM
      :value: '--'

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._EDGE_TAG_DELIM

   .. py:attribute:: _VALID_PROJECTION_KEYS
      :canonical: aiida.orm.querybuilder.QueryBuilder._VALID_PROJECTION_KEYS
      :value: ('func', 'cast')

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._VALID_PROJECTION_KEYS

   .. py:property:: backend
      :canonical: aiida.orm.querybuilder.QueryBuilder.backend
      :type: aiida.orm.implementation.StorageBackend

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.backend

   .. py:method:: as_dict(copy: bool = True) -> aiida.orm.implementation.querybuilder.QueryDictType
      :canonical: aiida.orm.querybuilder.QueryBuilder.as_dict

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.as_dict

   .. py:property:: queryhelp
      :canonical: aiida.orm.querybuilder.QueryBuilder.queryhelp
      :type: aiida.orm.implementation.querybuilder.QueryDictType

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.queryhelp

   .. py:method:: from_dict(dct: typing.Dict[str, typing.Any]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.from_dict
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.from_dict

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.__repr__

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.__repr__

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.__str__

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.__str__

   .. py:method:: __deepcopy__(memo) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.__deepcopy__

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.__deepcopy__

   .. py:method:: get_used_tags(vertices: bool = True, edges: bool = True) -> typing.List[str]
      :canonical: aiida.orm.querybuilder.QueryBuilder.get_used_tags

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.get_used_tags

   .. py:method:: _get_unique_tag(classifiers: typing.List[aiida.orm.querybuilder.Classifier]) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder._get_unique_tag

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._get_unique_tag

   .. py:method:: append(cls: typing.Optional[typing.Union[aiida.orm.querybuilder.EntityClsType, typing.Sequence[aiida.orm.querybuilder.EntityClsType]]] = None, entity_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None, tag: typing.Optional[str] = None, filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, project: typing.Optional[aiida.orm.querybuilder.ProjectType] = None, subclassing: bool = True, edge_tag: typing.Optional[str] = None, edge_filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, edge_project: typing.Optional[aiida.orm.querybuilder.ProjectType] = None, outerjoin: bool = False, joining_keyword: typing.Optional[str] = None, joining_value: typing.Optional[typing.Any] = None, orm_base: typing.Optional[str] = None, **kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.append

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.append

   .. py:method:: order_by(order_by: aiida.orm.querybuilder.OrderByType) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.order_by

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.order_by

   .. py:method:: add_filter(tagspec: typing.Union[str, aiida.orm.querybuilder.EntityClsType], filter_spec: aiida.orm.querybuilder.FilterType) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.add_filter

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.add_filter

   .. py:method:: _process_filters(filters: aiida.orm.querybuilder.FilterType) -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder._process_filters
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._process_filters

   .. py:method:: _add_node_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool)
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_node_type_filter

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._add_node_type_filter

   .. py:method:: _add_process_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_process_type_filter

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._add_process_type_filter

   .. py:method:: _add_group_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_group_type_filter

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._add_group_type_filter

   .. py:method:: add_projection(tag_spec: typing.Union[str, aiida.orm.querybuilder.EntityClsType], projection_spec: aiida.orm.querybuilder.ProjectType) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder.add_projection

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.add_projection

   .. py:method:: set_debug(debug: bool) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.set_debug

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.set_debug

   .. py:method:: debug(msg: str, *objects: typing.Any) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder.debug

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.debug

   .. py:method:: limit(limit: typing.Optional[int]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.limit

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.limit

   .. py:method:: offset(offset: typing.Optional[int]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.offset

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.offset

   .. py:method:: distinct(value: bool = True) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.distinct

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.distinct

   .. py:method:: inputs(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.inputs

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.inputs

   .. py:method:: outputs(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.outputs

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.outputs

   .. py:method:: children(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.children

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.children

   .. py:method:: parents(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.parents

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.parents

   .. py:method:: as_sql(inline: bool = False) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.as_sql

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.as_sql

   .. py:method:: analyze_query(execute: bool = True, verbose: bool = False) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.analyze_query

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.analyze_query

   .. py:method:: _get_aiida_entity_res(value) -> typing.Any
      :canonical: aiida.orm.querybuilder.QueryBuilder._get_aiida_entity_res
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder._get_aiida_entity_res

   .. py:method:: first(flat: bool = False) -> typing.Optional[list[typing.Any] | typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder.first

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.first

   .. py:method:: count() -> int
      :canonical: aiida.orm.querybuilder.QueryBuilder.count

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.count

   .. py:method:: iterall(batch_size: typing.Optional[int] = 100) -> typing.Iterable[typing.List[typing.Any]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.iterall

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.iterall

   .. py:method:: iterdict(batch_size: typing.Optional[int] = 100) -> typing.Iterable[typing.Dict[str, typing.Dict[str, typing.Any]]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.iterdict

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.iterdict

   .. py:method:: all(batch_size: typing.Optional[int] = None, flat: bool = False) -> typing.Union[typing.List[typing.List[typing.Any]], typing.List[typing.Any]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.all

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.all

   .. py:method:: one() -> typing.List[typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder.one

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.one

   .. py:method:: dict(batch_size: typing.Optional[int] = None) -> typing.List[typing.Dict[str, typing.Dict[str, typing.Any]]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.dict

      .. autodoc2-docstring:: aiida.orm.querybuilder.QueryBuilder.dict

.. py:class:: RemoteData(remote_path=None, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.base.RemoteData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.__init__

   .. py:attribute:: KEY_EXTRA_CLEANED
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.KEY_EXTRA_CLEANED
      :value: 'cleaned'

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.KEY_EXTRA_CLEANED

   .. py:method:: get_remote_path()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.get_remote_path

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.get_remote_path

   .. py:method:: set_remote_path(val)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.set_remote_path

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.set_remote_path

   .. py:property:: is_empty
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.is_empty

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.is_empty

   .. py:method:: getfile(relpath, destpath)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.getfile

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.getfile

   .. py:method:: listdir(relpath='.')
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.listdir

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.listdir

   .. py:method:: listdir_withattributes(path='.')
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.listdir_withattributes

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.listdir_withattributes

   .. py:method:: _clean(transport=None)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData._clean

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData._clean

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData._validate

   .. py:method:: get_authinfo()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.get_authinfo

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.base.RemoteData.get_authinfo

.. py:class:: RemoteStashData(stash_mode: aiida.common.datastructures.StashMode, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.base.RemoteStashData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.base.RemoteStashData.__init__

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData._storable
      :value: False

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.base.RemoteStashData._storable

   .. py:property:: stash_mode
      :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData.stash_mode
      :type: aiida.common.datastructures.StashMode

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.base.RemoteStashData.stash_mode

.. py:class:: RemoteStashFolderData(stash_mode: aiida.common.datastructures.StashMode, target_basepath: str, source_list: typing.List, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData

   Bases: :py:obj:`aiida.orm.nodes.data.remote.stash.base.RemoteStashData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.__init__

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData._storable
      :value: True

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData._storable

   .. py:property:: target_basepath
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.target_basepath
      :type: str

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.target_basepath

   .. py:property:: source_list
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.source_list
      :type: typing.Union[typing.List, typing.Tuple]

      .. autodoc2-docstring:: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.source_list

.. py:class:: SinglefileData(file, filename=None, **kwargs)
   :canonical: aiida.orm.nodes.data.singlefile.SinglefileData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.__init__

   .. py:attribute:: DEFAULT_FILENAME
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.DEFAULT_FILENAME
      :value: 'file.txt'

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.DEFAULT_FILENAME

   .. py:property:: filename
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.filename

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.filename

   .. py:method:: open(path=None, mode='r')
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.open

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.open

   .. py:method:: get_content()
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.get_content

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.get_content

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.set_file

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData.set_file

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.singlefile.SinglefileData._validate

.. py:class:: Site(**kwargs)
   :canonical: aiida.orm.nodes.data.structure.Site

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.__init__

   .. py:method:: get_raw()
      :canonical: aiida.orm.nodes.data.structure.Site.get_raw

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.get_raw

   .. py:method:: get_ase(kinds)
      :canonical: aiida.orm.nodes.data.structure.Site.get_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.get_ase

   .. py:property:: kind_name
      :canonical: aiida.orm.nodes.data.structure.Site.kind_name

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.kind_name

   .. py:property:: position
      :canonical: aiida.orm.nodes.data.structure.Site.position

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.position

   .. py:method:: __repr__()
      :canonical: aiida.orm.nodes.data.structure.Site.__repr__

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.__repr__

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.structure.Site.__str__

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.Site.__str__

.. py:class:: Str
   :canonical: aiida.orm.nodes.data.str.Str

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   .. autodoc2-docstring:: aiida.orm.nodes.data.str.Str

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.str.Str._type
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.str.Str._type

.. py:class:: StructureData(cell=None, pbc=None, ase=None, pymatgen=None, pymatgen_structure=None, pymatgen_molecule=None, **kwargs)
   :canonical: aiida.orm.nodes.data.structure.StructureData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.__init__

   .. py:attribute:: _set_incompatibilities
      :canonical: aiida.orm.nodes.data.structure.StructureData._set_incompatibilities
      :value: [('ase', 'cell'), ('ase', 'pbc'), ('ase', 'pymatgen'), ('ase', 'pymatgen_molecule'), ('ase', 'pymatg...

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._set_incompatibilities

   .. py:attribute:: _dimensionality_label
      :canonical: aiida.orm.nodes.data.structure.StructureData._dimensionality_label
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._dimensionality_label

   .. py:attribute:: _internal_kind_tags
      :canonical: aiida.orm.nodes.data.structure.StructureData._internal_kind_tags
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._internal_kind_tags

   .. py:method:: get_dimensionality()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_dimensionality

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_dimensionality

   .. py:method:: set_ase(aseatoms)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_ase

   .. py:method:: set_pymatgen(obj, **kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_pymatgen

   .. py:method:: set_pymatgen_molecule(mol, margin=5)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_molecule

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_molecule

   .. py:method:: set_pymatgen_structure(struct)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_structure

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.structure.StructureData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._validate

   .. py:method:: _prepare_xsf(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_xsf

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._prepare_xsf

   .. py:method:: _prepare_cif(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_cif

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._prepare_cif

   .. py:method:: _prepare_chemdoodle(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_chemdoodle

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._prepare_chemdoodle

   .. py:method:: _prepare_xyz(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_xyz

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._prepare_xyz

   .. py:method:: _parse_xyz(inputstring)
      :canonical: aiida.orm.nodes.data.structure.StructureData._parse_xyz

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._parse_xyz

   .. py:method:: _adjust_default_cell(vacuum_factor=1.0, vacuum_addition=10.0, pbc=(False, False, False))
      :canonical: aiida.orm.nodes.data.structure.StructureData._adjust_default_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._adjust_default_cell

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_description

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_description

   .. py:method:: get_symbols_set()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_symbols_set

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_symbols_set

   .. py:method:: get_formula(mode='hill', separator='')
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_formula

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_formula

   .. py:method:: get_site_kindnames()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_site_kindnames

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_site_kindnames

   .. py:method:: get_composition()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_composition

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_composition

   .. py:method:: get_ase()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_ase

   .. py:method:: get_pymatgen(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_pymatgen

   .. py:method:: get_pymatgen_structure(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_structure

   .. py:method:: get_pymatgen_molecule()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_molecule

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_molecule

   .. py:method:: append_kind(kind)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_kind

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.append_kind

   .. py:method:: append_site(site)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_site

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.append_site

   .. py:method:: append_atom(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_atom

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.append_atom

   .. py:method:: clear_kinds()
      :canonical: aiida.orm.nodes.data.structure.StructureData.clear_kinds

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.clear_kinds

   .. py:method:: clear_sites()
      :canonical: aiida.orm.nodes.data.structure.StructureData.clear_sites

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.clear_sites

   .. py:property:: sites
      :canonical: aiida.orm.nodes.data.structure.StructureData.sites

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.sites

   .. py:property:: kinds
      :canonical: aiida.orm.nodes.data.structure.StructureData.kinds

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.kinds

   .. py:method:: get_kind(kind_name)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_kind

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_kind

   .. py:method:: get_kind_names()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_kind_names

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_kind_names

   .. py:property:: cell
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.cell

   .. py:method:: set_cell(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_cell

   .. py:method:: reset_cell(new_cell)
      :canonical: aiida.orm.nodes.data.structure.StructureData.reset_cell

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.reset_cell

   .. py:method:: reset_sites_positions(new_positions, conserve_particle=True)
      :canonical: aiida.orm.nodes.data.structure.StructureData.reset_sites_positions

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.reset_sites_positions

   .. py:property:: pbc
      :canonical: aiida.orm.nodes.data.structure.StructureData.pbc

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.pbc

   .. py:method:: set_pbc(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pbc

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_pbc

   .. py:property:: cell_lengths
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell_lengths

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.cell_lengths

   .. py:method:: set_cell_lengths(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell_lengths
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_cell_lengths

   .. py:property:: cell_angles
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell_angles

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.cell_angles

   .. py:method:: set_cell_angles(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell_angles
      :abstractmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.set_cell_angles

   .. py:property:: is_alloy
      :canonical: aiida.orm.nodes.data.structure.StructureData.is_alloy

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.is_alloy

   .. py:property:: has_vacancies
      :canonical: aiida.orm.nodes.data.structure.StructureData.has_vacancies

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.has_vacancies

   .. py:method:: get_cell_volume()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_cell_volume

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_cell_volume

   .. py:method:: get_cif(converter='ase', store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_cif

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData.get_cif

   .. py:method:: _get_object_phonopyatoms()
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_phonopyatoms

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._get_object_phonopyatoms

   .. py:method:: _get_object_ase()
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_ase

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._get_object_ase

   .. py:method:: _get_object_pymatgen(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen

   .. py:method:: _get_object_pymatgen_structure(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_structure

   .. py:method:: _get_object_pymatgen_molecule(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_molecule

      .. autodoc2-docstring:: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_molecule

.. py:class:: TrajectoryData(structurelist=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.__init__

   .. py:method:: _internal_validate(stepids, cells, symbols, positions, times, velocities)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._internal_validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._internal_validate

   .. py:method:: set_trajectory(symbols, positions, stepids=None, cells=None, times=None, velocities=None)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_trajectory

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_trajectory

   .. py:method:: set_structurelist(structurelist)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_structurelist

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_structurelist

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._validate

   .. py:property:: numsteps
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsteps

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsteps

   .. py:property:: numsites
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsites

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsites

   .. py:method:: get_stepids()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_stepids

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_stepids

   .. py:method:: get_times()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_times

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_times

   .. py:method:: get_cells()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cells

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cells

   .. py:property:: symbols
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.symbols

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.symbols

   .. py:method:: get_positions()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_positions

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_positions

   .. py:method:: get_velocities()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_velocities

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_velocities

   .. py:method:: get_index_from_stepid(stepid)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_index_from_stepid

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_index_from_stepid

   .. py:method:: get_step_data(index)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_data

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_data

   .. py:method:: get_step_structure(index, custom_kinds=None)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_structure

   .. py:method:: _prepare_xsf(index=None, main_file_name='')
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_xsf

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_xsf

   .. py:method:: _prepare_cif(trajectory_index=None, main_file_name='')
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_cif

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_cif

   .. py:method:: get_structure(store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_structure

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_structure

   .. py:method:: get_cif(index=None, **kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cif

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cif

   .. py:method:: _parse_xyz_pos(inputstring)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_pos

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_pos

   .. py:method:: _parse_xyz_vel(inputstring)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_vel

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_vel

   .. py:method:: show_mpl_pos(**kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_pos

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_pos

   .. py:method:: show_mpl_heatmap(**kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_heatmap

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_heatmap

.. py:class:: UpfData(file, filename=None, **kwargs)
   :canonical: aiida.orm.nodes.data.upf.UpfData

   Bases: :py:obj:`aiida.orm.nodes.data.singlefile.SinglefileData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.__init__

   .. py:method:: get_or_create(filepath, use_first=False, store_upf=True)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_or_create
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.get_or_create

   .. py:method:: store(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.upf.UpfData.store

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.store

   .. py:method:: from_md5(md5, backend=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.from_md5
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.from_md5

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.set_file

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.set_file

   .. py:method:: get_upf_family_names()
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_family_names

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.get_upf_family_names

   .. py:property:: element
      :canonical: aiida.orm.nodes.data.upf.UpfData.element

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.element

   .. py:property:: md5sum
      :canonical: aiida.orm.nodes.data.upf.UpfData.md5sum

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.md5sum

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.upf.UpfData._validate

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData._validate

   .. py:method:: _prepare_upf(main_file_name='')
      :canonical: aiida.orm.nodes.data.upf.UpfData._prepare_upf

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData._prepare_upf

   .. py:method:: get_upf_group(group_label)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_group
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.get_upf_group

   .. py:method:: get_upf_groups(filter_elements=None, user=None, backend=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_groups
      :classmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData.get_upf_groups

   .. py:method:: _prepare_json(main_file_name='')
      :canonical: aiida.orm.nodes.data.upf.UpfData._prepare_json

      .. autodoc2-docstring:: aiida.orm.nodes.data.upf.UpfData._prepare_json

.. py:class:: UpfFamily(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.UpfFamily

   Bases: :py:obj:`aiida.orm.groups.Group`

   .. autodoc2-docstring:: aiida.orm.groups.UpfFamily

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.groups.UpfFamily.__init__

.. py:class:: User(email: str, first_name: str = '', last_name: str = '', institution: str = '', backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.users.User

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendUser`\ , :py:obj:`aiida.orm.users.UserCollection`\ ]

   .. autodoc2-docstring:: aiida.orm.users.User

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.users.User.__init__

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.users.User._CLS_COLLECTION
      :value: None

      .. autodoc2-docstring:: aiida.orm.users.User._CLS_COLLECTION

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.users.User.__str__

      .. autodoc2-docstring:: aiida.orm.users.User.__str__

   .. py:method:: normalize_email(email: str) -> str
      :canonical: aiida.orm.users.User.normalize_email
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.users.User.normalize_email

   .. py:property:: email
      :canonical: aiida.orm.users.User.email
      :type: str

      .. autodoc2-docstring:: aiida.orm.users.User.email

   .. py:property:: first_name
      :canonical: aiida.orm.users.User.first_name
      :type: str

      .. autodoc2-docstring:: aiida.orm.users.User.first_name

   .. py:property:: last_name
      :canonical: aiida.orm.users.User.last_name
      :type: str

      .. autodoc2-docstring:: aiida.orm.users.User.last_name

   .. py:property:: institution
      :canonical: aiida.orm.users.User.institution
      :type: str

      .. autodoc2-docstring:: aiida.orm.users.User.institution

   .. py:method:: get_full_name() -> str
      :canonical: aiida.orm.users.User.get_full_name

      .. autodoc2-docstring:: aiida.orm.users.User.get_full_name

   .. py:method:: get_short_name() -> str
      :canonical: aiida.orm.users.User.get_short_name

      .. autodoc2-docstring:: aiida.orm.users.User.get_short_name

   .. py:property:: uuid
      :canonical: aiida.orm.users.User.uuid
      :type: None

      .. autodoc2-docstring:: aiida.orm.users.User.uuid

.. py:class:: WorkChainNode
   :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode

   Bases: :py:obj:`aiida.orm.nodes.process.workflow.workflow.WorkflowNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode

   .. py:attribute:: STEPPER_STATE_INFO_KEY
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.STEPPER_STATE_INFO_KEY
      :value: 'stepper_state_info'

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.STEPPER_STATE_INFO_KEY

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode._updatable_attributes

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode._updatable_attributes

   .. py:property:: stepper_state_info
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.stepper_state_info
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.stepper_state_info

   .. py:method:: set_stepper_state_info(stepper_state_info: str) -> None
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.set_stepper_state_info

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.set_stepper_state_info

.. py:class:: WorkFunctionNode
   :canonical: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode

   Bases: :py:obj:`aiida.orm.utils.mixins.FunctionCalculationMixin`, :py:obj:`aiida.orm.nodes.process.workflow.workflow.WorkflowNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode._CLS_NODE_LINKS
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode._CLS_NODE_LINKS

.. py:class:: WorkflowNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode

   Bases: :py:obj:`aiida.orm.nodes.process.process.ProcessNode`

   .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.__init__

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._CLS_NODE_LINKS
      :value: None

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._CLS_NODE_LINKS

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._storable
      :value: True

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._storable

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._unstorable_message
      :value: 'storing for this node has been disabled'

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._unstorable_message

   .. py:property:: inputs
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.inputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.inputs

   .. py:property:: outputs
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.outputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      .. autodoc2-docstring:: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.outputs

.. py:class:: XyData
   :canonical: aiida.orm.nodes.data.array.xy.XyData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData

   .. py:method:: _arrayandname_validator(array, name, units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData._arrayandname_validator
      :staticmethod:

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData._arrayandname_validator

   .. py:method:: set_x(x_array, x_name, x_units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData.set_x

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData.set_x

   .. py:method:: set_y(y_arrays, y_names, y_units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData.set_y

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData.set_y

   .. py:method:: get_x()
      :canonical: aiida.orm.nodes.data.array.xy.XyData.get_x

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData.get_x

   .. py:method:: get_y()
      :canonical: aiida.orm.nodes.data.array.xy.XyData.get_y

      .. autodoc2-docstring:: aiida.orm.nodes.data.array.xy.XyData.get_y

.. py:function:: cif_from_ase(ase, full_occupancies=False, add_fake_biso=False)
   :canonical: aiida.orm.nodes.data.cif.cif_from_ase

   .. autodoc2-docstring:: aiida.orm.nodes.data.cif.cif_from_ase

.. py:function:: find_bandgap(bandsdata, number_electrons=None, fermi_energy=None)
   :canonical: aiida.orm.nodes.data.array.bands.find_bandgap

   .. autodoc2-docstring:: aiida.orm.nodes.data.array.bands.find_bandgap

.. py:function:: get_loader(orm_class)
   :canonical: aiida.orm.utils.loaders.get_loader

   .. autodoc2-docstring:: aiida.orm.utils.loaders.get_loader

.. py:function:: get_query_type_from_type_string(type_string)
   :canonical: aiida.orm.utils.node.get_query_type_from_type_string

   .. autodoc2-docstring:: aiida.orm.utils.node.get_query_type_from_type_string

.. py:function:: get_type_string_from_class(class_module, class_name)
   :canonical: aiida.orm.utils.node.get_type_string_from_class

   .. autodoc2-docstring:: aiida.orm.utils.node.get_type_string_from_class

.. py:function:: has_pycifrw()
   :canonical: aiida.orm.nodes.data.cif.has_pycifrw

   .. autodoc2-docstring:: aiida.orm.nodes.data.cif.has_pycifrw

.. py:function:: load_code(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Code
   :canonical: aiida.orm.utils.loaders.load_code

   .. autodoc2-docstring:: aiida.orm.utils.loaders.load_code

.. py:function:: load_computer(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Computer
   :canonical: aiida.orm.utils.loaders.load_computer

   .. autodoc2-docstring:: aiida.orm.utils.loaders.load_computer

.. py:function:: load_entity(entity_loader=None, identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True)
   :canonical: aiida.orm.utils.loaders.load_entity

   .. autodoc2-docstring:: aiida.orm.utils.loaders.load_entity

.. py:function:: load_group(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Group
   :canonical: aiida.orm.utils.loaders.load_group

   .. autodoc2-docstring:: aiida.orm.utils.loaders.load_group

.. py:function:: load_node(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Node
   :canonical: aiida.orm.utils.loaders.load_node

   .. autodoc2-docstring:: aiida.orm.utils.loaders.load_node

.. py:function:: load_node_class(type_string)
   :canonical: aiida.orm.utils.node.load_node_class

   .. autodoc2-docstring:: aiida.orm.utils.node.load_node_class

.. py:function:: pycifrw_from_cif(datablocks, loops=None, names=None)
   :canonical: aiida.orm.nodes.data.cif.pycifrw_from_cif

   .. autodoc2-docstring:: aiida.orm.nodes.data.cif.pycifrw_from_cif

.. py:function:: to_aiida_type(value)
   :canonical: aiida.orm.nodes.data.base.to_aiida_type

   .. autodoc2-docstring:: aiida.orm.nodes.data.base.to_aiida_type

.. py:function:: validate_link(source: aiida.orm.Node, target: aiida.orm.Node, link_type: aiida.common.links.LinkType, link_label: str, backend: typing.Optional[aiida.orm.implementation.storage_backend.StorageBackend] = None) -> None
   :canonical: aiida.orm.utils.links.validate_link

   .. autodoc2-docstring:: aiida.orm.utils.links.validate_link
