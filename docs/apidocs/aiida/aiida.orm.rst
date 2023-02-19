:py:mod:`aiida.orm`
===================

.. py:module:: aiida.orm


Description
-----------

Main module to expose all orm classes and methods

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbstractCode <aiida.orm.nodes.data.code.abstract.AbstractCode>`
     - Abstract data plugin representing an executable code.
   * - :py:obj:`AbstractNodeMeta <aiida.orm.utils.node.AbstractNodeMeta>`
     - Some python black magic to set correctly the logger also in subclasses.
   * - :py:obj:`ArrayData <aiida.orm.nodes.data.array.array.ArrayData>`
     - Store a set of arrays on disk (rather than on the database) in an efficient way using numpy.save() (therefore, this class requires numpy to be installed).
   * - :py:obj:`AttributeManager <aiida.orm.utils.managers.AttributeManager>`
     - An object used internally to return the attributes as a dictionary. This is currently used in :py:class:`~aiida.orm.nodes.data.dict.Dict`, for instance.
   * - :py:obj:`AuthInfo <aiida.orm.authinfos.AuthInfo>`
     - ORM class that models the authorization information that allows a `User` to connect to a `Computer`.
   * - :py:obj:`AutoGroup <aiida.orm.groups.AutoGroup>`
     - Group to be used to contain selected nodes generated, whilst autogrouping is enabled.
   * - :py:obj:`BandsData <aiida.orm.nodes.data.array.bands.BandsData>`
     - Class to handle bands data
   * - :py:obj:`BaseType <aiida.orm.nodes.data.base.BaseType>`
     - `Data` sub class to be used as a base for data containers that represent base python data types.
   * - :py:obj:`Bool <aiida.orm.nodes.data.bool.Bool>`
     - `Data` sub class to represent a boolean value.
   * - :py:obj:`CalcFunctionNode <aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode>`
     - ORM class for all nodes representing the execution of a calcfunction.
   * - :py:obj:`CalcJobNode <aiida.orm.nodes.process.calculation.calcjob.CalcJobNode>`
     - ORM class for all nodes representing the execution of a CalcJob.
   * - :py:obj:`CalcJobResultManager <aiida.orm.utils.calcjob.CalcJobResultManager>`
     - Utility class to easily access the contents of the 'default output' node of a `CalcJobNode`.
   * - :py:obj:`CalculationEntityLoader <aiida.orm.utils.loaders.CalculationEntityLoader>`
     - Loader for the `Calculation` entity and sub classes.
   * - :py:obj:`CalculationNode <aiida.orm.nodes.process.calculation.calculation.CalculationNode>`
     - Base class for all nodes representing the execution of a calculation process.
   * - :py:obj:`CifData <aiida.orm.nodes.data.cif.CifData>`
     - Wrapper for Crystallographic Interchange File (CIF)
   * - :py:obj:`Code <aiida.orm.nodes.data.code.legacy.Code>`
     - A code entity. It can either be 'local', or 'remote'.
   * - :py:obj:`CodeEntityLoader <aiida.orm.utils.loaders.CodeEntityLoader>`
     - Loader for the `Code` entity and sub classes.
   * - :py:obj:`Collection <aiida.orm.entities.Collection>`
     - Container class that represents the collection of objects of a particular entity type.
   * - :py:obj:`Comment <aiida.orm.comments.Comment>`
     - Base class to map a DbComment that represents a comment attached to a certain Node.
   * - :py:obj:`Computer <aiida.orm.computers.Computer>`
     - Computer entity.
   * - :py:obj:`ComputerEntityLoader <aiida.orm.utils.loaders.ComputerEntityLoader>`
     - Loader for the `Computer` entity and sub classes.
   * - :py:obj:`ContainerizedCode <aiida.orm.nodes.data.code.containerized.ContainerizedCode>`
     - Data plugin representing an executable code in container on a remote computer.
   * - :py:obj:`Data <aiida.orm.nodes.data.data.Data>`
     - The base class for all Data nodes.
   * - :py:obj:`Dict <aiida.orm.nodes.data.dict.Dict>`
     - `Data` sub class to represent a dictionary.
   * - :py:obj:`Entity <aiida.orm.entities.Entity>`
     - An AiiDA entity
   * - :py:obj:`EntityExtras <aiida.orm.extras.EntityExtras>`
     - Interface to the extras of a node or group instance.
   * - :py:obj:`EntityTypes <aiida.orm.entities.EntityTypes>`
     - Enum for referring to ORM entities in a backend-agnostic manner.
   * - :py:obj:`EnumData <aiida.orm.nodes.data.enum.EnumData>`
     - Data plugin that allows to easily wrap an :class:`enum.Enum` member.
   * - :py:obj:`Float <aiida.orm.nodes.data.float.Float>`
     - `Data` sub class to represent a float value.
   * - :py:obj:`FolderData <aiida.orm.nodes.data.folder.FolderData>`
     - `Data` sub class to represent a folder on a file system.
   * - :py:obj:`Group <aiida.orm.groups.Group>`
     - An AiiDA ORM implementation of group of nodes.
   * - :py:obj:`GroupEntityLoader <aiida.orm.utils.loaders.GroupEntityLoader>`
     - Loader for the `Group` entity and sub classes.
   * - :py:obj:`ImportGroup <aiida.orm.groups.ImportGroup>`
     - Group to be used to contain all nodes from an export archive that has been imported.
   * - :py:obj:`InstalledCode <aiida.orm.nodes.data.code.installed.InstalledCode>`
     - Data plugin representing an executable code on a remote computer.
   * - :py:obj:`Int <aiida.orm.nodes.data.int.Int>`
     - `Data` sub class to represent an integer value.
   * - :py:obj:`JsonableData <aiida.orm.nodes.data.jsonable.JsonableData>`
     - Data plugin that allows to easily wrap objects that are JSON-able.
   * - :py:obj:`Kind <aiida.orm.nodes.data.structure.Kind>`
     - This class contains the information about the species (kinds) of the system.
   * - :py:obj:`KpointsData <aiida.orm.nodes.data.array.kpoints.KpointsData>`
     - Class to handle array of kpoints in the Brillouin zone. Provide methods to generate either user-defined k-points or path of k-points along symmetry lines. Internally, all k-points are defined in terms of crystal (fractional) coordinates. Cell and lattice vector coordinates are in Angstroms, reciprocal lattice vectors in Angstrom^-1 . :note: The methods setting and using the Bravais lattice info assume the PRIMITIVE unit cell is provided in input to the set_cell or set_cell_from_structure methods.
   * - :py:obj:`LinkManager <aiida.orm.utils.links.LinkManager>`
     - Class to convert a list of LinkTriple tuples into an iterator.
   * - :py:obj:`LinkPair <aiida.orm.utils.links.LinkPair>`
     - 
   * - :py:obj:`LinkTriple <aiida.orm.utils.links.LinkTriple>`
     - 
   * - :py:obj:`List <aiida.orm.nodes.data.list.List>`
     - `Data` sub class to represent a list.
   * - :py:obj:`Log <aiida.orm.logs.Log>`
     - An AiiDA Log entity.  Corresponds to a logged message against a particular AiiDA node.
   * - :py:obj:`Node <aiida.orm.nodes.node.Node>`
     - Base class for all nodes in AiiDA.
   * - :py:obj:`NodeAttributes <aiida.orm.nodes.attributes.NodeAttributes>`
     - Interface to the attributes of a node instance.
   * - :py:obj:`NodeEntityLoader <aiida.orm.utils.loaders.NodeEntityLoader>`
     - Loader for the `Node` entity and sub classes.
   * - :py:obj:`NodeLinksManager <aiida.orm.utils.managers.NodeLinksManager>`
     - A manager that allows to inspect, with tab-completion, nodes linked to a given one. See an example of its use in `CalculationNode.inputs`.
   * - :py:obj:`NodeRepository <aiida.orm.nodes.repository.NodeRepository>`
     - Interface to the file repository of a node instance.
   * - :py:obj:`NumericType <aiida.orm.nodes.data.numeric.NumericType>`
     - Sub class of Data to store numbers, overloading common operators (``+``, ``*``, ...).
   * - :py:obj:`OrbitalData <aiida.orm.nodes.data.orbital.OrbitalData>`
     - Used for storing collections of orbitals, as well as providing methods for accessing them internally.
   * - :py:obj:`OrmEntityLoader <aiida.orm.utils.loaders.OrmEntityLoader>`
     - Base class for entity loaders.
   * - :py:obj:`PortableCode <aiida.orm.nodes.data.code.portable.PortableCode>`
     - Data plugin representing an executable code stored in AiiDA's storage.
   * - :py:obj:`ProcessNode <aiida.orm.nodes.process.process.ProcessNode>`
     - Base class for all nodes representing the execution of a process
   * - :py:obj:`ProjectionData <aiida.orm.nodes.data.array.projection.ProjectionData>`
     - A class to handle arrays of projected wavefunction data. That is projections of a orbitals, usually an atomic-hydrogen orbital, onto a given bloch wavefunction, the bloch wavefunction being indexed by s, n, and k. E.g. the elements are the projections described as < orbital | Bloch wavefunction (s,n,k) >
   * - :py:obj:`QueryBuilder <aiida.orm.querybuilder.QueryBuilder>`
     - The class to query the AiiDA database.
   * - :py:obj:`RemoteData <aiida.orm.nodes.data.remote.base.RemoteData>`
     - Store a link to a file or folder on a remote machine.
   * - :py:obj:`RemoteStashData <aiida.orm.nodes.data.remote.stash.base.RemoteStashData>`
     - Data plugin that models an archived folder on a remote computer.
   * - :py:obj:`RemoteStashFolderData <aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData>`
     - Data plugin that models a folder with files of a completed calculation job that has been stashed through a copy.
   * - :py:obj:`SinglefileData <aiida.orm.nodes.data.singlefile.SinglefileData>`
     - Data class that can be used to store a single file in its repository.
   * - :py:obj:`Site <aiida.orm.nodes.data.structure.Site>`
     - This class contains the information about a given site of the system.
   * - :py:obj:`Str <aiida.orm.nodes.data.str.Str>`
     - `Data` sub class to represent a string value.
   * - :py:obj:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
     - This class contains the information about a given structure, i.e. a collection of sites together with a cell, the boundary conditions (whether they are periodic or not) and other related useful information.
   * - :py:obj:`TrajectoryData <aiida.orm.nodes.data.array.trajectory.TrajectoryData>`
     - Stores a trajectory (a sequence of crystal structures with timestamps, and possibly with velocities).
   * - :py:obj:`UpfData <aiida.orm.nodes.data.upf.UpfData>`
     - `Data` sub class to represent a pseudopotential single file in UPF format.
   * - :py:obj:`UpfFamily <aiida.orm.groups.UpfFamily>`
     - Group that represents a pseudo potential family containing `UpfData` nodes.
   * - :py:obj:`User <aiida.orm.users.User>`
     - AiiDA User
   * - :py:obj:`WorkChainNode <aiida.orm.nodes.process.workflow.workchain.WorkChainNode>`
     - ORM class for all nodes representing the execution of a WorkChain.
   * - :py:obj:`WorkFunctionNode <aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode>`
     - ORM class for all nodes representing the execution of a workfunction.
   * - :py:obj:`WorkflowNode <aiida.orm.nodes.process.workflow.workflow.WorkflowNode>`
     - Base class for all nodes representing the execution of a workflow process.
   * - :py:obj:`XyData <aiida.orm.nodes.data.array.xy.XyData>`
     - A subclass designed to handle arrays that have an "XY" relationship to each other. That is there is one array, the X array, and there are several Y arrays, which can be considered functions of X.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OrderSpecifier <aiida.orm.logs.OrderSpecifier>`
     - 
   * - :py:obj:`cif_from_ase <aiida.orm.nodes.data.cif.cif_from_ase>`
     - Construct a CIF datablock from the ASE structure. The code is taken from https://wiki.fysik.dtu.dk/ase/ase/io/formatoptions.html#ase.io.cif.write_cif, as the original ASE code contains a bug in printing the Hermann-Mauguin symmetry space group symbol.
   * - :py:obj:`find_bandgap <aiida.orm.nodes.data.array.bands.find_bandgap>`
     - Tries to guess whether the bandsdata represent an insulator. This method is meant to be used only for electronic bands (not phonons) By default, it will try to use the occupations to guess the number of electrons and find the Fermi Energy, otherwise, it can be provided explicitely. Also, there is an implicit assumption that the kpoints grid is "sufficiently" dense, so that the bandsdata are not missing the intersection between valence and conduction band if present. Use this function with care!
   * - :py:obj:`get_loader <aiida.orm.utils.loaders.get_loader>`
     - Return the correct OrmEntityLoader for the given orm class.
   * - :py:obj:`get_query_type_from_type_string <aiida.orm.utils.node.get_query_type_from_type_string>`
     - Take the type string of a Node and create the queryable type string
   * - :py:obj:`get_type_string_from_class <aiida.orm.utils.node.get_type_string_from_class>`
     - Given the module and name of a class, determine the orm_class_type string, which codifies the orm class that is to be used. The returned string will always have a terminating period, which is required to query for the string in the database
   * - :py:obj:`has_pycifrw <aiida.orm.nodes.data.cif.has_pycifrw>`
     - :return: True if the PyCifRW module can be imported, False otherwise.
   * - :py:obj:`load_code <aiida.orm.utils.loaders.load_code>`
     - Load a Code instance by one of its identifiers: pk, uuid or label
   * - :py:obj:`load_computer <aiida.orm.utils.loaders.load_computer>`
     - Load a Computer instance by one of its identifiers: pk, uuid or label
   * - :py:obj:`load_entity <aiida.orm.utils.loaders.load_entity>`
     - Load an entity instance by one of its identifiers: pk, uuid or label
   * - :py:obj:`load_group <aiida.orm.utils.loaders.load_group>`
     - Load a Group instance by one of its identifiers: pk, uuid or label
   * - :py:obj:`load_node <aiida.orm.utils.loaders.load_node>`
     - Load a node by one of its identifiers: pk or uuid. If the type of the identifier is unknown simply pass it without a keyword and the loader will attempt to infer the type
   * - :py:obj:`load_node_class <aiida.orm.utils.node.load_node_class>`
     - Return the `Node` sub class that corresponds to the given type string.
   * - :py:obj:`pycifrw_from_cif <aiida.orm.nodes.data.cif.pycifrw_from_cif>`
     - Constructs PyCifRW's CifFile from an array of CIF datablocks.
   * - :py:obj:`to_aiida_type <aiida.orm.nodes.data.base.to_aiida_type>`
     - Turns basic Python types (str, int, float, bool) into the corresponding AiiDA types.
   * - :py:obj:`validate_link <aiida.orm.utils.links.validate_link>`
     - Validate adding a link of the given type and label from a given node to ourself.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ASCENDING <aiida.orm.logs.ASCENDING>`
     - 
   * - :py:obj:`DESCENDING <aiida.orm.logs.DESCENDING>`
     - 

API
~~~

.. py:data:: ASCENDING
   :canonical: aiida.orm.logs.ASCENDING
   :value: 'asc'

.. py:class:: AbstractCode(default_calc_job_plugin: str | None = None, append_text: str = '', prepend_text: str = '', use_double_quotes: bool = False, is_hidden: bool = False, **kwargs)
   :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Abstract data plugin representing an executable code.

   .. rubric:: Initialization

   Construct a new instance.

   :param default_calc_job_plugin: The entry point name of the default ``CalcJob`` plugin to use.
   :param append_text: The text that should be appended to the run line in the job script.
   :param prepend_text: The text that should be prepended to the run line in the job script.
   :param use_double_quotes: Whether the command line invocation of this code should be escaped with double quotes.
   :param is_hidden: Whether the code is hidden.

   .. py:attribute:: _KEY_ATTRIBUTE_DEFAULT_CALC_JOB_PLUGIN
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_DEFAULT_CALC_JOB_PLUGIN
      :type: str
      :value: 'input_plugin'

   .. py:attribute:: _KEY_ATTRIBUTE_APPEND_TEXT
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_APPEND_TEXT
      :type: str
      :value: 'append_text'

   .. py:attribute:: _KEY_ATTRIBUTE_PREPEND_TEXT
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_PREPEND_TEXT
      :type: str
      :value: 'prepend_text'

   .. py:attribute:: _KEY_ATTRIBUTE_USE_DOUBLE_QUOTES
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_ATTRIBUTE_USE_DOUBLE_QUOTES
      :type: str
      :value: 'use_double_quotes'

   .. py:attribute:: _KEY_EXTRA_IS_HIDDEN
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._KEY_EXTRA_IS_HIDDEN
      :type: str
      :value: 'hidden'

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.can_run_on_computer
      :abstractmethod:

      Return whether the code can run on a given computer.

      :param computer: The computer.
      :return: ``True`` if the code can run on ``computer``, ``False`` otherwise.

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable
      :abstractmethod:

      Return the executable that the submission script should execute to run the code.

      :return: The executable to be called in the submission script.

   .. py:method:: get_executable_cmdline_params(cmdline_params: list[str] | None = None) -> list
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_executable_cmdline_params

      Return the list of executable with its command line parameters.

      :param cmdline_params: List of command line parameters provided by the ``CalcJob`` plugin.
      :return: List of the executable followed by its command line parameters.

   .. py:method:: get_prepend_cmdline_params(mpi_args: list[str] | None = None, extra_mpirun_params: list[str] | None = None) -> list[str]
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_prepend_cmdline_params

      Return List of command line parameters to be prepended to the executable in submission line.
      These command line parameters are typically parameters related to MPI invocations.

      :param mpi_args: List of MPI parameters provided by the ``Computer.get_mpirun_command`` method.
      :param extra_mpiruns_params: List of MPI parameters provided by the ``metadata.options.extra_mpirun_params``
          input of the ``CalcJob``.
      :return: List of command line parameters to be prepended to the executable in submission line.

   .. py:method:: validate_working_directory(folder: aiida.common.folders.Folder)
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.validate_working_directory

      Validate content of the working directory created by the :class:`~aiida.engine.CalcJob` plugin.

      This method will be called by :meth:`~aiida.engine.processes.calcjobs.calcjob.CalcJob.presubmit` when a new
      calculation job is launched, passing the :class:`~aiida.common.folders.Folder` that was used by the plugin used
      for the calculation to create the input files for the working directory. This method can be overridden by
      implementations of the ``AbstractCode`` class that need to validate the contents of that folder.

      :param folder: A sandbox folder that the ``CalcJob`` plugin wrote input files to that will be copied to the
          working directory for the corresponding calculation job instance.
      :raises PluginInternalError: If the content of the sandbox folder is not valid.

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.full_label
      :abstractmethod:
      :type: str

      Return the full label of this code.

      The full label can be just the label itself but it can be something else. However, it at the very least has to
      include the label of the code.

      :return: The full label of the code.

   .. py:property:: label
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.label
      :type: str

      Return the label.

      :return: The label.

   .. py:property:: default_calc_job_plugin
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.default_calc_job_plugin
      :type: str | None

      Return the optional default ``CalcJob`` plugin.

      :return: The entry point name of the default ``CalcJob`` plugin to use.

   .. py:property:: append_text
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.append_text
      :type: str

      Return the text that should be appended to the run line in the job script.

      :return: The text that should be appended to the run line in the job script.

   .. py:property:: prepend_text
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.prepend_text
      :type: str

      Return the text that should be prepended to the run line in the job script.

      :return: The text that should be prepended to the run line in the job script.

   .. py:property:: use_double_quotes
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.use_double_quotes
      :type: bool

      Return whether the command line invocation of this code should be escaped with double quotes.

      :return: ``True`` if to escape with double quotes, ``False`` otherwise.

   .. py:property:: is_hidden
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.is_hidden
      :type: bool

      Return whether the code is hidden.

      :return: ``True`` if the code is hidden, ``False`` otherwise, which is also the default.

   .. py:method:: get_builder() -> aiida.engine.ProcessBuilder
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_builder

      Create and return a new ``ProcessBuilder`` for the ``CalcJob`` class of the plugin configured for this code.

      The configured calculation plugin class is defined by the ``default_calc_job_plugin`` property.

      .. note:: it also sets the ``builder.code`` value.

      :return: a ``ProcessBuilder`` instance with the ``code`` input already populated with ourselves
      :raise aiida.common.EntryPointError: if the specified plugin does not exist.
      :raise ValueError: if no default plugin was specified.

   .. py:method:: cli_validate_label_uniqueness(_, __, value)
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.cli_validate_label_uniqueness
      :staticmethod:

      Validate the uniqueness of the label of the code.

   .. py:method:: get_cli_options() -> collections.OrderedDict
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode.get_cli_options
      :classmethod:

      Return the CLI options that would allow to create an instance of this class.

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.abstract.AbstractCode._get_cli_options
      :classmethod:

      Return the CLI options that would allow to create an instance of this class.

.. py:class:: AbstractNodeMeta
   :canonical: aiida.orm.utils.node.AbstractNodeMeta

   Bases: :py:obj:`abc.ABCMeta`

   Some python black magic to set correctly the logger also in subclasses.

   .. py:method:: __new__(name, bases, namespace, **kwargs)
      :canonical: aiida.orm.utils.node.AbstractNodeMeta.__new__

.. py:class:: ArrayData(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.array.ArrayData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Store a set of arrays on disk (rather than on the database) in an efficient
   way using numpy.save() (therefore, this class requires numpy to be
   installed).

   Each array is stored within the Node folder as a different .npy file.

   :note: Before storing, no caching is done: if you perform a
     :py:meth:`.get_array` call, the array will be re-read from disk.
     If instead the ArrayData node has already been stored,
     the array is cached in memory after the first read, and the cached array
     is used thereafter.
     If too much RAM memory is used, you can clear the
     cache with the :py:meth:`.clear_internal_cache` method.

   .. rubric:: Initialization

   Construct a new instance, setting the ``source`` attribute if provided as a keyword argument.

   .. py:attribute:: array_prefix
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.array_prefix
      :value: 'array|'

   .. py:attribute:: _cached_arrays
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._cached_arrays
      :value: None

   .. py:method:: initialize()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.initialize

      Initialize instance attributes.

      This will be called after the constructor is called or an entity is created from an existing backend entity.

   .. py:method:: delete_array(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.delete_array

      Delete an array from the node. Can only be called before storing.

      :param name: The name of the array to delete from the node.

   .. py:method:: get_arraynames()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_arraynames

      Return a list of all arrays stored in the node, listing the files (and
      not relying on the properties).

      .. versionadded:: 0.7
         Renamed from arraynames

   .. py:method:: _arraynames_from_files()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_files

      Return a list of all arrays stored in the node, listing the files (and
      not relying on the properties).

   .. py:method:: _arraynames_from_properties()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._arraynames_from_properties

      Return a list of all arrays stored in the node, listing the attributes
      starting with the correct prefix.

   .. py:method:: get_shape(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_shape

      Return the shape of an array (read from the value cached in the
      properties for efficiency reasons).

      :param name: The name of the array.

   .. py:method:: get_iterarrays()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_iterarrays

      Iterator that returns tuples (name, array) for each array stored in the node.

      .. versionadded:: 1.0
          Renamed from iterarrays

   .. py:method:: get_array(name)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.get_array

      Return an array stored in the node

      :param name: The name of the array to return.

   .. py:method:: clear_internal_cache()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.clear_internal_cache

      Clear the internal memory cache where the arrays are stored after being
      read from disk (used in order to reduce at minimum the readings from
      disk).
      This function is useful if you want to keep the node in memory, but you
      do not want to waste memory to cache the arrays in RAM.

   .. py:method:: set_array(name, array)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData.set_array

      Store a new numpy array inside the node. Possibly overwrite the array
      if it already existed.

      Internally, it stores a name.npy file in numpy format.

      :param name: The name of the array.
      :param array: The numpy array to store.

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._validate

      Check if the list of .npy files stored inside the node and the
      list of properties match. Just a name check, no check on the size
      since this would require to reload all arrays and this may take time
      and memory.

   .. py:method:: _get_array_entries()
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._get_array_entries

      Return a dictionary with the different array entries.

      The idea is that this dictionary contains the array name as a key and
      the value is the numpy array transformed into a list. This is so that
      it can be transformed into a json object.

   .. py:method:: _prepare_json(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.array.ArrayData._prepare_json

      Dump the content of the arrays stored in this node into JSON format.

      :param comments: if True, includes comments (if it makes sense for the given format)

.. py:class:: AttributeManager(node)
   :canonical: aiida.orm.utils.managers.AttributeManager

   An object used internally to return the attributes as a dictionary.
   This is currently used in :py:class:`~aiida.orm.nodes.data.dict.Dict`,
   for instance.

   :note: Important! It cannot be used to change variables, just to read
     them. To change values (of unstored nodes), use the proper Node methods.

   .. rubric:: Initialization

   :param node: the node object.

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.managers.AttributeManager.__dir__

      Allow to list the keys of the dictionary

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.managers.AttributeManager.__iter__

      Return the keys as an iterator

   .. py:method:: _get_dict()
      :canonical: aiida.orm.utils.managers.AttributeManager._get_dict

      Return the internal dictionary

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.managers.AttributeManager.__getattr__

      Interface to get to dictionary values, using the key as an attribute.

      :note: it works only for attributes that only contain letters, numbers
        and underscores, and do not start with a number.

      :param name: name of the key whose value is required.

   .. py:method:: __setattr__(name, value)
      :canonical: aiida.orm.utils.managers.AttributeManager.__setattr__

      Implement setattr(self, name, value).

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.managers.AttributeManager.__getitem__

      Interface to get to dictionary values as a dictionary.

      :param name: name of the key whose value is required.

.. py:class:: AuthInfo(computer: aiida.orm.Computer, user: aiida.orm.User, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.authinfos.AuthInfo

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendAuthInfo`\ , :py:obj:`aiida.orm.authinfos.AuthInfoCollection`\ ]

   ORM class that models the authorization information that allows a `User` to connect to a `Computer`.

   .. rubric:: Initialization

   Create an `AuthInfo` instance for the given computer and user.

   :param computer: a `Computer` instance
   :param user: a `User` instance
   :param backend: the backend to use for the instance, or use the default backend if None

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.authinfos.AuthInfo._CLS_COLLECTION
      :value: None

   .. py:attribute:: PROPERTY_WORKDIR
      :canonical: aiida.orm.authinfos.AuthInfo.PROPERTY_WORKDIR
      :value: 'workdir'

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.authinfos.AuthInfo.__str__

   .. py:property:: enabled
      :canonical: aiida.orm.authinfos.AuthInfo.enabled
      :type: bool

      Return whether this instance is enabled.

      :return: True if enabled, False otherwise

   .. py:property:: computer
      :canonical: aiida.orm.authinfos.AuthInfo.computer
      :type: aiida.orm.Computer

      Return the computer associated with this instance.

   .. py:property:: user
      :canonical: aiida.orm.authinfos.AuthInfo.user
      :type: aiida.orm.User

      Return the user associated with this instance.

   .. py:method:: get_auth_params() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.authinfos.AuthInfo.get_auth_params

      Return the dictionary of authentication parameters

      :return: a dictionary with authentication parameters

   .. py:method:: set_auth_params(auth_params: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.authinfos.AuthInfo.set_auth_params

      Set the dictionary of authentication parameters

      :param auth_params: a dictionary with authentication parameters

   .. py:method:: get_metadata() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.authinfos.AuthInfo.get_metadata

      Return the dictionary of metadata

      :return: a dictionary with metadata

   .. py:method:: set_metadata(metadata: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.authinfos.AuthInfo.set_metadata

      Set the dictionary of metadata

      :param metadata: a dictionary with metadata

   .. py:method:: get_workdir() -> str
      :canonical: aiida.orm.authinfos.AuthInfo.get_workdir

      Return the working directory.

      If no explicit work directory is set for this instance, the working directory of the computer will be returned.

      :return: the working directory

   .. py:method:: get_transport() -> aiida.transports.Transport
      :canonical: aiida.orm.authinfos.AuthInfo.get_transport

      Return a fully configured transport that can be used to connect to the computer set for this instance.

.. py:class:: AutoGroup(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.AutoGroup

   Bases: :py:obj:`aiida.orm.groups.Group`

   Group to be used to contain selected nodes generated, whilst autogrouping is enabled.

   .. rubric:: Initialization

   Create a new group. Either pass a dbgroup parameter, to reload
   a group from the DB (and then, no further parameters are allowed),
   or pass the parameters for the Group creation.

   :param label: The group label, required on creation
   :param description: The group description (by default, an empty string)
   :param user: The owner of the group (by default, the automatic user)
   :param type_string: a string identifying the type of group (by default,
       an empty string, indicating an user-defined group.

.. py:class:: BandsData
   :canonical: aiida.orm.nodes.data.array.bands.BandsData

   Bases: :py:obj:`aiida.orm.nodes.data.array.kpoints.KpointsData`

   Class to handle bands data

   .. py:method:: set_kpointsdata(kpointsdata)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.set_kpointsdata

      Load the kpoints from a kpoint object.
      :param kpointsdata: an instance of KpointsData class

   .. py:method:: _validate_bands_occupations(bands, occupations=None, labels=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._validate_bands_occupations

      Validate the list of bands and of occupations before storage.
      Kpoints must be set in advance.
      Bands and occupations must be convertible into arrays of
      Nkpoints x Nbands floats or Nspins x Nkpoints x Nbands; Nkpoints must
      correspond to the number of kpoints.

   .. py:method:: set_bands(bands, units=None, occupations=None, labels=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.set_bands

      Set an array of band energies of dimension (nkpoints x nbands).
      Kpoints must be set in advance. Can contain floats or None.
      :param bands: a list of nkpoints lists of nbands bands, or a 2D array
      of shape (nkpoints x nbands), with band energies for each kpoint
      :param units: optional, energy units
      :param occupations: optional, a 2D list or array of floats of same
      shape as bands, with the occupation associated to each band

   .. py:property:: array_labels
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.array_labels

      Get the labels associated with the band arrays

   .. py:property:: units
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.units

      Units in which the data in bands were stored. A string

   .. py:method:: _set_pbc(value)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._set_pbc

      validate the pbc, then store them

   .. py:method:: get_bands(also_occupations=False, also_labels=False)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.get_bands

      Returns an array (nkpoints x num_bands or nspins x nkpoints x num_bands)
      of energies.
      :param also_occupations: if True, returns also the occupations array.
      Default = False

   .. py:method:: _get_bandplot_data(cartesian, prettify_format=None, join_symbol=None, get_segments=False, y_origin=0.0)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_bandplot_data

      Get data to plot a band structure

      :param cartesian: if True, distances (for the x-axis) are computed in
              cartesian coordinates, otherwise they are computed in reciprocal
              coordinates. cartesian=True will fail if no cell has been set.
      :param prettify_format: by default, strings are not prettified. If you want
           to prettify them, pass a valid prettify_format string (see valid options
           in the docstring of :py:func:prettify_labels).
      :param join_symbols: by default, strings are not joined. If you pass a string,
           this is used to join strings that are much closer than a given threshold.
           The most typical string is the pipe symbol: ``|``.
      :param get_segments: if True, also computes the band split into segments
      :param y_origin: if present, shift bands so to set the value specified at ``y=0``
      :return: a plot_info dictiorary, whose keys are ``x`` (array of distances
         for the x axis of the plot); ``y`` (array of bands), ``labels`` (list
         of tuples in the format (float x value of the label, label string),
         ``band_type_idx`` (array containing an index for each band: if there is only
         one spin, then it's an array of zeros, of length equal to the number of bands
         at each point; if there are two spins, then it's an array of zeros or ones
         depending on the type of spin; the length is always equalt to the total
         number of bands per kpoint).

   .. py:method:: _prepare_agr_batch(main_file_name='', comments=True, prettify_format=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr_batch

      Prepare two files, data and batch, to be plot with xmgrace as:
      xmgrace -batch file.dat

      :param main_file_name: if the user asks to write the main content on a
           file, this contains the filename. This should be used to infer a
           good filename for the additional files.
           In this case, we remove the extension, and add '_data.dat'
      :param comments: if True, print comments (if it makes sense for the given
          format)
      :param prettify_format: if None, use the default prettify format. Otherwise
          specify a string with the prettifier to use.

   .. py:method:: _prepare_dat_multicolumn(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_multicolumn

      Write an N x M matrix. First column is the distance between kpoints,
      The other columns are the bands. Header contains number of kpoints and
      the number of bands (commented).

      :param comments: if True, print comments (if it makes sense for the given
          format)

   .. py:method:: _prepare_dat_blocks(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_dat_blocks

      Format suitable for gnuplot using blocks.
      Columns with x and y (path and band energy). Several blocks, separated
      by two empty lines, one per energy band.

      :param comments: if True, print comments (if it makes sense for the given
          format)

   .. py:method:: _matplotlib_get_dict(main_file_name='', comments=True, title='', legend=None, legend2=None, y_max_lim=None, y_min_lim=None, y_origin=0.0, prettify_format=None, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict

      Prepare the data to send to the python-matplotlib plotting script.

      :param comments: if True, print comments (if it makes sense for the given
          format)
      :param plot_info: a dictionary
      :param setnumber_offset: an offset to be applied to all set numbers
          (i.e. s0 is replaced by s[offset], s1 by s[offset+1], etc.)
      :param color_number: the color number for lines, symbols, error bars
          and filling (should be less than the parameter MAX_NUM_AGR_COLORS
          defined below)
      :param title: the title
      :param legend: the legend (applied only to the first of the set)
      :param legend2: the legend for second-type spins
          (applied only to the first of the set)
      :param y_max_lim: the maximum on the y axis (if None, put the
          maximum of the bands)
      :param y_min_lim: the minimum on the y axis (if None, put the
          minimum of the bands)
      :param y_origin: the new origin of the y axis -> all bands are replaced
          by bands-y_origin
      :param prettify_format: if None, use the default prettify format. Otherwise
          specify a string with the prettifier to use.
      :param kwargs: additional customization variables; only a subset is
          accepted, see internal variable 'valid_additional_keywords

   .. py:method:: _prepare_mpl_singlefile(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_singlefile

      Prepare a python script using matplotlib to plot the bands

      For the possible parameters, see documentation of
      :py:meth:`~aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict`

   .. py:method:: _prepare_mpl_withjson(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_withjson

      Prepare a python script using matplotlib to plot the bands, with the JSON
      returned as an independent file.

      For the possible parameters, see documentation of
      :py:meth:`~aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict`

   .. py:method:: _prepare_mpl_pdf(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_pdf

      Prepare a python script using matplotlib to plot the bands, with the JSON
      returned as an independent file.

      For the possible parameters, see documentation of
      :py:meth:`~aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict`

   .. py:method:: _prepare_mpl_png(main_file_name='', *args, **kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_mpl_png

      Prepare a python script using matplotlib to plot the bands, with the JSON
      returned as an independent file.

      For the possible parameters, see documentation of
      :py:meth:`~aiida.orm.nodes.data.array.bands.BandsData._matplotlib_get_dict`

   .. py:method:: _get_mpl_body_template(paths)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_mpl_body_template
      :staticmethod:

      :param paths: paths of k-points

   .. py:method:: show_mpl(**kwargs)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData.show_mpl

      Call a show() command for the band structure using matplotlib.
      This uses internally the 'mpl_singlefile' format, with empty
      main_file_name.

      Other kwargs are passed to self._exportcontent.

   .. py:method:: _prepare_gnuplot(main_file_name=None, title='', comments=True, prettify_format=None, y_max_lim=None, y_min_lim=None, y_origin=0.0)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_gnuplot

      Prepare an gnuplot script to plot the bands, with the .dat file
      returned as an independent file.

      :param main_file_name: if the user asks to write the main content on a
           file, this contains the filename. This should be used to infer a
           good filename for the additional files.
           In this case, we remove the extension, and add '_data.dat'
      :param title: if specified, add a title to the plot
      :param comments: if True, print comments (if it makes sense for the given
          format)
      :param prettify_format: if None, use the default prettify format. Otherwise
          specify a string with the prettifier to use.

   .. py:method:: _prepare_agr(main_file_name='', comments=True, setnumber_offset=0, color_number=1, color_number2=2, legend='', title='', y_max_lim=None, y_min_lim=None, y_origin=0.0, prettify_format=None)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_agr

      Prepare an xmgrace agr file.

      :param comments: if True, print comments
          (if it makes sense for the given format)
      :param plot_info: a dictionary
      :param setnumber_offset: an offset to be applied to all set numbers
          (i.e. s0 is replaced by s[offset], s1 by s[offset+1], etc.)
      :param color_number: the color number for lines, symbols, error bars
          and filling (should be less than the parameter MAX_NUM_AGR_COLORS
          defined below)
      :param color_number2: the color number for lines, symbols, error bars
          and filling for the second-type spins (should be less than the
          parameter MAX_NUM_AGR_COLORS defined below)
      :param legend: the legend (applied only to the first set)
      :param title: the title
      :param y_max_lim: the maximum on the y axis (if None, put the
          maximum of the bands); applied *after* shifting the origin
          by ``y_origin``
      :param y_min_lim: the minimum on the y axis (if None, put the
          minimum of the bands); applied *after* shifting the origin
          by ``y_origin``
      :param y_origin: the new origin of the y axis -> all bands are replaced
          by bands-y_origin
      :param prettify_format: if None, use the default prettify format. Otherwise
          specify a string with the prettifier to use.

   .. py:method:: _get_band_segments(cartesian)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._get_band_segments

      Return the band segments.

   .. py:method:: _prepare_json(main_file_name='', comments=True)
      :canonical: aiida.orm.nodes.data.array.bands.BandsData._prepare_json

      Prepare a json file in a format compatible with the AiiDA band visualizer

      :param comments: if True, print comments (if it makes sense for the given
          format)

.. py:class:: BaseType(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.base.BaseType

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   `Data` sub class to be used as a base for data containers that represent base python data types.

   .. py:property:: value
      :canonical: aiida.orm.nodes.data.base.BaseType.value

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.base.BaseType.__str__

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.base.BaseType.__eq__

   .. py:method:: new(value=None)
      :canonical: aiida.orm.nodes.data.base.BaseType.new

.. py:class:: Bool
   :canonical: aiida.orm.nodes.data.bool.Bool

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   `Data` sub class to represent a boolean value.

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.bool.Bool._type
      :value: None

   .. py:method:: __int__()
      :canonical: aiida.orm.nodes.data.bool.Bool.__int__

   .. py:method:: __bool__()
      :canonical: aiida.orm.nodes.data.bool.Bool.__bool__

.. py:class:: CalcFunctionNode
   :canonical: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode

   Bases: :py:obj:`aiida.orm.utils.mixins.FunctionCalculationMixin`, :py:obj:`aiida.orm.nodes.process.calculation.calculation.CalculationNode`

   ORM class for all nodes representing the execution of a calcfunction.

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.calculation.calcfunction.CalcFunctionNode._CLS_NODE_LINKS
      :value: None

.. py:class:: CalcJobNode
   :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode

   Bases: :py:obj:`aiida.orm.nodes.process.calculation.calculation.CalculationNode`

   ORM class for all nodes representing the execution of a CalcJob.

   .. py:attribute:: CALC_JOB_STATE_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.CALC_JOB_STATE_KEY
      :value: 'state'

   .. py:attribute:: IMMIGRATED_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.IMMIGRATED_KEY
      :value: 'imported'

   .. py:attribute:: REMOTE_WORKDIR_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.REMOTE_WORKDIR_KEY
      :value: 'remote_workdir'

   .. py:attribute:: RETRIEVE_LIST_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_LIST_KEY
      :value: 'retrieve_list'

   .. py:attribute:: RETRIEVE_TEMPORARY_LIST_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.RETRIEVE_TEMPORARY_LIST_KEY
      :value: 'retrieve_temporary_list'

   .. py:attribute:: SCHEDULER_JOB_ID_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_JOB_ID_KEY
      :value: 'job_id'

   .. py:attribute:: SCHEDULER_STATE_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_STATE_KEY
      :value: 'scheduler_state'

   .. py:attribute:: SCHEDULER_LAST_CHECK_TIME_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_CHECK_TIME_KEY
      :value: 'scheduler_lastchecktime'

   .. py:attribute:: SCHEDULER_LAST_JOB_INFO_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_LAST_JOB_INFO_KEY
      :value: 'last_job_info'

   .. py:attribute:: SCHEDULER_DETAILED_JOB_INFO_KEY
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.SCHEDULER_DETAILED_JOB_INFO_KEY
      :value: 'detailed_job_info'

   .. py:attribute:: _tools
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._tools
      :value: None

   .. py:property:: tools
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.tools
      :type: aiida.tools.calculations.CalculationTools

      Return the calculation tools that are registered for the process type associated with this calculation.

      If the entry point name stored in the `process_type` of the CalcJobNode has an accompanying entry point in the
      `aiida.tools.calculations` entry point category, it will attempt to load the entry point and instantiate it
      passing the node to the constructor. If the entry point does not exist, cannot be resolved or loaded, a warning
      will be logged and the base CalculationTools class will be instantiated and returned.

      :return: CalculationTools instance

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._updatable_attributes

   .. py:method:: _hash_ignored_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._hash_ignored_attributes

   .. py:method:: get_builder_restart() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_builder_restart

      Return a `ProcessBuilder` that is ready to relaunch the same `CalcJob` that created this node.

      The process class will be set based on the `process_type` of this node and the inputs of the builder will be
      prepopulated with the inputs registered for this node. This functionality is very useful if a process has
      completed and you want to relaunch it with slightly different inputs.

      In addition to prepopulating the input nodes, which is implemented by the base `ProcessNode` class, here we
      also add the `options` that were passed in the `metadata` input of the `CalcJob` process.


   .. py:property:: is_imported
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.is_imported
      :type: bool

      Return whether the calculation job was imported instead of being an actual run.

   .. py:method:: get_option(name: str) -> typing.Optional[typing.Any]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_option

      Retun the value of an option that was set for this CalcJobNode

      :param name: the option name
      :return: the option value or None
      :raises: ValueError for unknown option

   .. py:method:: set_option(name: str, value: typing.Any) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_option

      Set an option to the given value

      :param name: the option name
      :param value: the value to set
      :raises: ValueError for unknown option
      :raises: TypeError for values with invalid type

   .. py:method:: get_options() -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_options

      Return the dictionary of options set for this CalcJobNode

      :return: dictionary of the options and their values

   .. py:method:: set_options(options: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_options

      Set the options for this CalcJobNode

      :param options: dictionary of option and their values to set

   .. py:method:: get_state() -> typing.Optional[aiida.common.datastructures.CalcJobState]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_state

      Return the calculation job active sub state.

      The calculation job state serves to give more granular state information to `CalcJobs`, in addition to the
      generic process state, while the calculation job is active. The state can take values from the enumeration
      defined in `aiida.common.datastructures.CalcJobState` and can be used to query for calculation jobs in specific
      active states.

      :return: instance of `aiida.common.datastructures.CalcJobState` or `None` if invalid value, or not set

   .. py:method:: set_state(state: aiida.common.datastructures.CalcJobState) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_state

      Set the calculation active job state.

      :raise: ValueError if state is invalid

   .. py:method:: delete_state() -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.delete_state

      Delete the calculation job state attribute if it exists.

   .. py:method:: set_remote_workdir(remote_workdir: str) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_remote_workdir

      Set the absolute path to the working directory on the remote computer where the calculation is run.

      :param remote_workdir: absolute filepath to the remote working directory

   .. py:method:: get_remote_workdir() -> typing.Optional[str]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_remote_workdir

      Return the path to the remote (on cluster) scratch folder of the calculation.

      :return: a string with the remote path

   .. py:method:: _validate_retrieval_directive(directives: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode._validate_retrieval_directive
      :staticmethod:

      Validate a list or tuple of file retrieval directives.

      :param directives: a list or tuple of file retrieval directives
      :raise ValueError: if the format of the directives is invalid

   .. py:method:: set_retrieve_list(retrieve_list: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_list

      Set the retrieve list.

      This list of directives will instruct the daemon what files to retrieve after the calculation has completed.
      list or tuple of files or paths that should be retrieved by the daemon.

      :param retrieve_list: list or tuple of with filepath directives

   .. py:method:: get_retrieve_list() -> typing.Optional[typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_list

      Return the list of files/directories to be retrieved on the cluster after the calculation has completed.

      :return: a list of file directives

   .. py:method:: set_retrieve_temporary_list(retrieve_temporary_list: typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_retrieve_temporary_list

      Set the retrieve temporary list.

      The retrieve temporary list stores files that are retrieved after completion and made available during parsing
      and are deleted as soon as the parsing has been completed.

      :param retrieve_temporary_list: list or tuple of with filepath directives

   .. py:method:: get_retrieve_temporary_list() -> typing.Optional[typing.Sequence[typing.Union[str, typing.Tuple[str, str, str]]]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieve_temporary_list

      Return list of files to be retrieved from the cluster which will be available during parsing.

      :return: a list of file directives

   .. py:method:: set_job_id(job_id: typing.Union[int, str]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_job_id

      Set the job id that was assigned to the calculation by the scheduler.

      .. note:: the id will always be stored as a string

      :param job_id: the id assigned by the scheduler after submission

   .. py:method:: get_job_id() -> typing.Optional[str]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_job_id

      Return job id that was assigned to the calculation by the scheduler.

      :return: the string representation of the scheduler job id

   .. py:method:: set_scheduler_state(state: aiida.schedulers.datastructures.JobState) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_scheduler_state

      Set the scheduler state.

      :param state: an instance of `JobState`

   .. py:method:: get_scheduler_state() -> typing.Optional[aiida.schedulers.datastructures.JobState]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_state

      Return the status of the calculation according to the cluster scheduler.

      :return: a JobState enum instance.

   .. py:method:: get_scheduler_lastchecktime() -> typing.Optional[datetime.datetime]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_lastchecktime

      Return the time of the last update of the scheduler state by the daemon or None if it was never set.

      :return: a datetime object or None

   .. py:method:: set_detailed_job_info(detailed_job_info: typing.Optional[dict]) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_detailed_job_info

      Set the detailed job info dictionary.

      :param detailed_job_info: a dictionary with metadata with the accounting of a completed job

   .. py:method:: get_detailed_job_info() -> typing.Optional[dict]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_detailed_job_info

      Return the detailed job info dictionary.

      The scheduler is polled for the detailed job info after the job is completed and ready to be retrieved.

      :return: the dictionary with detailed job info if defined or None

   .. py:method:: set_last_job_info(last_job_info: aiida.schedulers.datastructures.JobInfo) -> None
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.set_last_job_info

      Set the last job info.

      :param last_job_info: a `JobInfo` object

   .. py:method:: get_last_job_info() -> typing.Optional[aiida.schedulers.datastructures.JobInfo]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_last_job_info

      Return the last information asked to the scheduler about the status of the job.

      The last job info is updated on every poll of the scheduler, except for the final poll when the job drops from
      the scheduler's job queue.
      For completed jobs, the last job info therefore contains the "second-to-last" job info that still shows the job
      as running. Please use :meth:`~aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_detailed_job_info`
      instead.

      :return: a `JobInfo` object (that closely resembles a dictionary) or None.

   .. py:method:: get_authinfo() -> aiida.orm.authinfos.AuthInfo
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_authinfo

      Return the `AuthInfo` that is configured for the `Computer` set for this node.

      :return: `AuthInfo`

   .. py:method:: get_transport() -> aiida.transports.Transport
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_transport

      Return the transport for this calculation.

      :return: `Transport` configured with the `AuthInfo` associated to the computer of this node

   .. py:method:: get_parser_class() -> typing.Optional[typing.Type[aiida.parsers.Parser]]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_parser_class

      Return the output parser object for this calculation or None if no parser is set.

      :return: a `Parser` class.
      :raises `aiida.common.exceptions.EntryPointError`: if the parser entry point can not be resolved.

   .. py:property:: link_label_retrieved
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.link_label_retrieved
      :type: str

      Return the link label used for the retrieved FolderData node.

   .. py:method:: get_retrieved_node() -> typing.Optional[aiida.orm.FolderData]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_retrieved_node

      Return the retrieved data folder.

      :return: the retrieved FolderData node or None if not found

   .. py:property:: res
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.res
      :type: aiida.orm.utils.calcjob.CalcJobResultManager

      To be used to get direct access to the parsed parameters.

      :return: an instance of the CalcJobResultManager.

      :note: a practical example on how it is meant to be used: let's say that there is a key 'energy'
          in the dictionary of the parsed results which contains a list of floats.
          The command `calc.res.energy` will return such a list.

   .. py:method:: get_scheduler_stdout() -> typing.Optional[typing.AnyStr]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stdout

      Return the scheduler stderr output if the calculation has finished and been retrieved, None otherwise.

      :return: scheduler stderr output or None

   .. py:method:: get_scheduler_stderr() -> typing.Optional[typing.AnyStr]
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_scheduler_stderr

      Return the scheduler stdout output if the calculation has finished and been retrieved, None otherwise.

      :return: scheduler stdout output or None

   .. py:method:: get_description() -> str
      :canonical: aiida.orm.nodes.process.calculation.calcjob.CalcJobNode.get_description

      Return a description of the node based on its properties.

.. py:class:: CalcJobResultManager(node)
   :canonical: aiida.orm.utils.calcjob.CalcJobResultManager

   Utility class to easily access the contents of the 'default output' node of a `CalcJobNode`.

   A `CalcJob` process can mark one of its outputs as the 'default output'. The default output node will always be
   returned by the `CalcJob` and will always be a `Dict` node.

   If a `CalcJob` defines such a default output node, this utility class will simplify retrieving the result of said
   node through the `CalcJobNode` instance produced by the execution of the `CalcJob`.

   The default results are only defined if the `CalcJobNode` has a `process_type` that can be successfully used
   to load the corresponding `CalcJob` process class *and* if its process spec defines a `default_output_node`.
   If both these conditions are met, the results are defined as the dictionary contained within the default
   output node.

   .. rubric:: Initialization

   Construct an instance of the `CalcJobResultManager`.

   :param calc: the `CalcJobNode` instance.

   .. py:property:: node
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.node

      Return the `CalcJobNode` associated with this result manager instance.

   .. py:method:: _load_results()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager._load_results

      Try to load the results for the `CalcJobNode` of this result manager.

      :raises ValueError: if no default output node could be loaded

   .. py:method:: get_results()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.get_results

      Return the results dictionary of the default results node of the calculation node.

      This property will lazily load the dictionary.

      :return: the dictionary of the default result node

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__dir__

      Add the keys of the results dictionary such that they can be autocompleted.

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__iter__

      Return an iterator over the keys of the result dictionary.

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__getattr__

      Return an attribute from the results dictionary.

      :param name: name of the result return
      :return: value of the attribute
      :raises AttributeError: if the results node cannot be retrieved or it does not contain the `name` attribute

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.calcjob.CalcJobResultManager.__getitem__

      Return an attribute from the results dictionary.

      :param name: name of the result return
      :return: value of the attribute
      :raises KeyError: if the results node cannot be retrieved or it does not contain the `name` attribute

.. py:class:: CalculationEntityLoader
   :canonical: aiida.orm.utils.loaders.CalculationEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   Loader for the `Calculation` entity and sub classes.

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.CalculationEntityLoader.orm_base_class

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.CalculationEntityLoader._get_query_builder_label_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance that should retrieve the entity corresponding to the identifier
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

.. py:class:: CalculationNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode

   Bases: :py:obj:`aiida.orm.nodes.process.process.ProcessNode`

   Base class for all nodes representing the execution of a calculation process.

   .. rubric:: Initialization

   :param backend_entity: the backend model supporting this entity

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._storable
      :value: True

   .. py:attribute:: _cachable
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._cachable
      :value: True

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode._unstorable_message
      :value: 'storing for this node has been disabled'

   .. py:property:: inputs
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode.inputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      Return an instance of `NodeLinksManager` to manage incoming INPUT_CALC links

      The returned Manager allows you to easily explore the nodes connected to this node
      via an incoming INPUT_CALC link.
      The incoming nodes are reachable by their link labels which are attributes of the manager.


   .. py:property:: outputs
      :canonical: aiida.orm.nodes.process.calculation.calculation.CalculationNode.outputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      Return an instance of `NodeLinksManager` to manage outgoing CREATE links

      The returned Manager allows you to easily explore the nodes connected to this node
      via an outgoing CREATE link.
      The outgoing nodes are reachable by their link labels which are attributes of the manager.


.. py:class:: CifData(ase=None, file=None, filename=None, values=None, scan_type=None, parse_policy=None, **kwargs)
   :canonical: aiida.orm.nodes.data.cif.CifData

   Bases: :py:obj:`aiida.orm.nodes.data.singlefile.SinglefileData`

   Wrapper for Crystallographic Interchange File (CIF)

   .. note:: the file (physical) is held as the authoritative source of
       information, so all conversions are done through the physical file:
       when setting ``ase`` or ``values``, a physical CIF file is generated
       first, the values are updated from the physical CIF file.

   .. rubric:: Initialization

   Construct a new instance and set the contents to that of the file.

   :param file: an absolute filepath or filelike object for CIF.
       Hint: Pass io.BytesIO(b"my string") to construct the SinglefileData directly from a string.
   :param filename: specify filename to use (defaults to name of provided file).
   :param ase: ASE Atoms object to construct the CifData instance from.
   :param values: PyCifRW CifFile object to construct the CifData instance from.
   :param scan_type: scan type string for parsing with PyCIFRW ('standard' or 'flex'). See CifFile.ReadCif
   :param parse_policy: 'eager' (parse CIF file on set_file) or 'lazy' (defer parsing until needed)

   .. py:attribute:: _SET_INCOMPATIBILITIES
      :canonical: aiida.orm.nodes.data.cif.CifData._SET_INCOMPATIBILITIES
      :value: [('ase', 'file'), ('ase', 'values'), ('file', 'values')]

   .. py:attribute:: _SCAN_TYPES
      :canonical: aiida.orm.nodes.data.cif.CifData._SCAN_TYPES
      :value: ('standard', 'flex')

   .. py:attribute:: _SCAN_TYPE_DEFAULT
      :canonical: aiida.orm.nodes.data.cif.CifData._SCAN_TYPE_DEFAULT
      :value: 'standard'

   .. py:attribute:: _PARSE_POLICIES
      :canonical: aiida.orm.nodes.data.cif.CifData._PARSE_POLICIES
      :value: ('eager', 'lazy')

   .. py:attribute:: _PARSE_POLICY_DEFAULT
      :canonical: aiida.orm.nodes.data.cif.CifData._PARSE_POLICY_DEFAULT
      :value: 'eager'

   .. py:attribute:: _values
      :canonical: aiida.orm.nodes.data.cif.CifData._values
      :value: None

   .. py:attribute:: _ase
      :canonical: aiida.orm.nodes.data.cif.CifData._ase
      :value: None

   .. py:method:: read_cif(fileobj, index=-1, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.read_cif
      :staticmethod:

      A wrapper method that simulates the behavior of the old
      function ase.io.cif.read_cif by using the new generic ase.io.read
      function.

      Somewhere from 3.12 to 3.17 the tag concept was bundled with each Atom object. When
      reading a CIF file, this is incremented and signifies the atomic species, even though
      the CIF file do not have specific tags embedded. On reading CIF files we thus force the
      ASE tag to zero for all Atom elements.


   .. py:method:: from_md5(md5, backend=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.from_md5
      :classmethod:

      Return a list of all CIF files that match a given MD5 hash.

      .. note:: the hash has to be stored in a ``_md5`` attribute,
          otherwise the CIF file will not be found.

   .. py:method:: get_or_create(filename, use_first=False, store_cif=True)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_or_create
      :classmethod:

      Pass the same parameter of the init; if a file with the same md5
      is found, that CifData is returned.

      :param filename: an absolute filename on disk
      :param use_first: if False (default), raise an exception if more than                 one CIF file is found.                If it is True, instead, use the first available CIF file.
      :param bool store_cif: If false, the CifData objects are not stored in
              the database. default=True.
      :return (cif, created): where cif is the CifData object, and create is either            True if the object was created, or False if the object was retrieved            from the DB.

   .. py:property:: ase
      :canonical: aiida.orm.nodes.data.cif.CifData.ase

      ASE object, representing the CIF.

      .. note:: requires ASE module.

   .. py:method:: get_ase(**kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_ase

      Returns ASE object, representing the CIF. This function differs
      from the property ``ase`` by the possibility to pass the keyworded
      arguments (kwargs) to ase.io.cif.read_cif().

      .. note:: requires ASE module.

   .. py:method:: set_ase(aseatoms)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_ase

      Set the contents of the CifData starting from an ASE atoms object

      :param aseatoms: the ASE atoms object

   .. py:property:: values
      :canonical: aiida.orm.nodes.data.cif.CifData.values

      PyCifRW structure, representing the CIF datablocks.

      .. note:: requires PyCifRW module.

   .. py:method:: set_values(values)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_values

      Set internal representation to `values`.

      Warning: This also writes a new CIF file.

      :param values: PyCifRW CifFile object

      .. note:: requires PyCifRW module.

   .. py:method:: parse(scan_type=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.parse

      Parses CIF file and sets attributes.

      :param scan_type:  See set_scan_type

   .. py:method:: store(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.store

      Store the node.

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_file

      Set the file.

      If the source is set and the MD5 checksum of new file
      is different from the source, the source has to be deleted.

      :param file: filepath or filelike object of the CIF file to store.
          Hint: Pass io.BytesIO(b"my string") to construct the file directly from a string.
      :param filename: specify filename to use (defaults to name of provided file).

   .. py:method:: set_scan_type(scan_type)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_scan_type

      Set the scan_type for PyCifRW.

      The 'flex' scan_type of PyCifRW is faster for large CIF files but
      does not yet support the CIF2 format as of 02/2018.
      See the CifFile.ReadCif function

      :param scan_type: Either 'standard' or 'flex' (see _scan_types)

   .. py:method:: set_parse_policy(parse_policy)
      :canonical: aiida.orm.nodes.data.cif.CifData.set_parse_policy

      Set the parse policy.

      :param parse_policy: Either 'eager' (parse CIF file on set_file)
          or 'lazy' (defer parsing until needed)

   .. py:method:: get_formulae(mode='sum', custom_tags=None)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_formulae

      Return chemical formulae specified in CIF file.

      Note: This does not compute the formula, it only reads it from the
      appropriate tag. Use refine_inline to compute formulae.

   .. py:method:: get_spacegroup_numbers()
      :canonical: aiida.orm.nodes.data.cif.CifData.get_spacegroup_numbers

      Get the spacegroup international number.

   .. py:property:: has_partial_occupancies
      :canonical: aiida.orm.nodes.data.cif.CifData.has_partial_occupancies

      Return if the cif data contains partial occupancies

      A partial occupancy is defined as site with an occupancy that differs from unity, within a precision of 1E-6

      .. note: occupancies that cannot be parsed into a float are ignored

      :return: True if there are partial occupancies, False otherwise

   .. py:property:: has_attached_hydrogens
      :canonical: aiida.orm.nodes.data.cif.CifData.has_attached_hydrogens

      Check if there are hydrogens without coordinates, specified as attached
      to the atoms of the structure.

      :returns: True if there are attached hydrogens, False otherwise.

   .. py:property:: has_undefined_atomic_sites
      :canonical: aiida.orm.nodes.data.cif.CifData.has_undefined_atomic_sites

      Return whether the cif data contains any undefined atomic sites.

      An undefined atomic site is defined as a site where at least one of the fractional coordinates specified in the
      `_atom_site_fract_*` tags, cannot be successfully interpreted as a float. If the cif data contains any site that
      matches this description, or it does not contain any atomic site tags at all, the cif data is said to have
      undefined atomic sites.

      :return: boolean, True if no atomic sites are defined or if any of the defined sites contain undefined positions
          and False otherwise

   .. py:property:: has_atomic_sites
      :canonical: aiida.orm.nodes.data.cif.CifData.has_atomic_sites

      Returns whether there are any atomic sites defined in the cif data. That
      is to say, it will check all the values for the `_atom_site_fract_*` tags
      and if they are all equal to `?` that means there are no relevant atomic
      sites defined and the function will return False. In all other cases the
      function will return True

      :returns: False when at least one atomic site fractional coordinate is not
          equal to `?` and True otherwise

   .. py:property:: has_unknown_species
      :canonical: aiida.orm.nodes.data.cif.CifData.has_unknown_species

      Returns whether the cif contains atomic species that are not recognized by AiiDA.

      The known species are taken from the elements dictionary in `aiida.common.constants`, with the exception of
      the "unknown" placeholder element with symbol 'X', as this could not be used to construct a real structure.
      If any of the formula of the cif data contain species that are not in that elements dictionary, the function
      will return True and False in all other cases. If there is no formulae to be found, it will return None

      :returns: True when there are unknown species in any of the formulae, False if not, None if no formula found

   .. py:method:: generate_md5()
      :canonical: aiida.orm.nodes.data.cif.CifData.generate_md5

      Computes and returns MD5 hash of the CIF file.

   .. py:method:: get_structure(converter='pymatgen', store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData.get_structure

      Creates :py:class:`aiida.orm.nodes.data.structure.StructureData`.

      .. versionadded:: 1.0
         Renamed from _get_aiida_structure

      :param converter: specify the converter. Default 'pymatgen'.
      :param store: if True, intermediate calculation gets stored in the
          AiiDA database for record. Default False.
      :param primitive_cell: if True, primitive cell is returned,
          conventional cell if False. Default False.
      :param occupancy_tolerance: If total occupancy of a site is between 1 and occupancy_tolerance,
          the occupancies will be scaled down to 1. (pymatgen only)
      :param site_tolerance: This tolerance is used to determine if two sites are sitting in the same position,
          in which case they will be combined to a single disordered site. Defaults to 1e-4. (pymatgen only)
      :return: :py:class:`aiida.orm.nodes.data.structure.StructureData` node.

   .. py:method:: _prepare_cif(**kwargs)
      :canonical: aiida.orm.nodes.data.cif.CifData._prepare_cif

      Return CIF string of CifData object.

      If parsed values are present, a CIF string is created and written to file. If no parsed values are present, the
      CIF string is read from file.

   .. py:method:: _get_object_ase()
      :canonical: aiida.orm.nodes.data.cif.CifData._get_object_ase

      Converts CifData to ase.Atoms

      :return: an ase.Atoms object

   .. py:method:: _get_object_pycifrw()
      :canonical: aiida.orm.nodes.data.cif.CifData._get_object_pycifrw

      Converts CifData to PyCIFRW.CifFile

      :return: a PyCIFRW.CifFile object

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.cif.CifData._validate

      Validates MD5 hash of CIF file.

.. py:class:: Code(remote_computer_exec=None, local_executable=None, input_plugin_name=None, files=None, **kwargs)
   :canonical: aiida.orm.nodes.data.code.legacy.Code

   Bases: :py:obj:`aiida.orm.nodes.data.code.abstract.AbstractCode`

   A code entity.
   It can either be 'local', or 'remote'.

   * Local code: it is a collection of files/dirs (added using the add_path() method), where one     file is flagged as executable (using the set_local_executable() method).

   * Remote code: it is a pair (remotecomputer, remotepath_of_executable) set using the     set_remote_computer_exec() method.

   For both codes, one can set some code to be executed right before or right after
   the execution of the code, using the set_preexec_code() and set_postexec_code()
   methods (e.g., the set_preexec_code() can be used to load specific modules required
   for the code to be run).

   .. rubric:: Initialization

   Construct a new instance.

   :param default_calc_job_plugin: The entry point name of the default ``CalcJob`` plugin to use.
   :param append_text: The text that should be appended to the run line in the job script.
   :param prepend_text: The text that should be prepended to the run line in the job script.
   :param use_double_quotes: Whether the command line invocation of this code should be escaped with double quotes.
   :param is_hidden: Whether the code is hidden.

   .. py:attribute:: HIDDEN_KEY
      :canonical: aiida.orm.nodes.data.code.legacy.Code.HIDDEN_KEY
      :value: 'hidden'

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.legacy.Code.can_run_on_computer

      Return whether the code can run on a given computer.

      :param computer: The computer.
      :return: ``True`` if the code can run on ``computer``, ``False`` otherwise.

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_executable

      Return the executable that the submission script should execute to run the code.

      :return: The executable to be called in the submission script.

   .. py:method:: hide()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.hide

      Hide the code (prevents from showing it in the verdi code list)

   .. py:method:: reveal()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.reveal

      Reveal the code (allows to show it in the verdi code list)
      By default, it is revealed

   .. py:property:: hidden
      :canonical: aiida.orm.nodes.data.code.legacy.Code.hidden

      Determines whether the Code is hidden or not

   .. py:method:: set_files(files)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_files

      Given a list of filenames (or a single filename string),
      add it to the path (all at level zero, i.e. without folders).
      Therefore, be careful for files with the same name!

      :todo: decide whether to check if the Code must be a local executable
           to be able to call this function.

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.__str__

      Return str(self).

   .. py:method:: get_computer_label()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_computer_label

      Get label of this code's computer.

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.legacy.Code.full_label

      Get full label of this code.

      Returns label of the form <code-label>@<computer-name>.

   .. py:method:: relabel(new_label)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.relabel

      Relabel this code.

      :param new_label: new code label

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_description

      Return a string description of this Code instance.

      :return: string description of this Code instance

   .. py:method:: get_code_helper(label, machinename=None, backend=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_code_helper
      :classmethod:

      :param label: the code label identifying the code to load
      :param machinename: the machine name where code is setup

      :raise aiida.common.NotExistent: if no code identified by the given string is found
      :raise aiida.common.MultipleObjectsError: if the string cannot identify uniquely
          a code

   .. py:method:: get(pk=None, label=None, machinename=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get
      :classmethod:

      Get a Computer object with given identifier string, that can either be
      the numeric ID (pk), or the label (and computername) (if unique).

      :param pk: the numeric ID (pk) for code
      :param label: the code label identifying the code to load
      :param machinename: the machine name where code is setup

      :raise aiida.common.NotExistent: if no code identified by the given string is found
      :raise aiida.common.MultipleObjectsError: if the string cannot identify uniquely a code
      :raise ValueError: if neither a pk nor a label was passed in

   .. py:method:: get_from_string(code_string)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_from_string
      :classmethod:

      Get a Computer object with given identifier string in the format
      label@machinename. See the note below for details on the string
      detection algorithm.

      .. note:: the (leftmost) '@' symbol is always used to split code
          and computername. Therefore do not use
          '@' in the code name if you want to use this function
          ('@' in the computer name are instead valid).

      :param code_string: the code string identifying the code to load

      :raise aiida.common.NotExistent: if no code identified by the given string is found
      :raise aiida.common.MultipleObjectsError: if the string cannot identify uniquely
          a code
      :raise TypeError: if code_string is not of string type


   .. py:method:: list_for_plugin(plugin, labels=True, backend=None)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.list_for_plugin
      :classmethod:

      Return a list of valid code strings for a given plugin.

      :param plugin: The string of the plugin.
      :param labels: if True, return a list of code names, otherwise
        return the code PKs (integers).
      :return: a list of string, with the code names if labels is True,
        otherwise a list of integers with the code PKs.

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._validate

      Validate information stored in Node object.

      For the :py:class:`~aiida.orm.Node` base class, this check is always valid.
      Subclasses can override this method to perform additional checks
      and should usually call ``super()._validate()`` first!

      This method is called automatically before storing the node in the DB.
      Therefore, use :py:meth:`~aiida.orm.nodes.attributes.NodeAttributes.get()` and similar methods that
      automatically read either from the DB or from the internal attribute cache.

   .. py:method:: validate_remote_exec_path()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.validate_remote_exec_path

      Validate the ``remote_exec_path`` attribute.

      Checks whether the executable exists on the remote computer if a transport can be opened to it. This method
      is intentionally not called in ``_validate`` as to allow the creation of ``Code`` instances whose computers can
      not yet be connected to and as to not require the overhead of opening transports in storing a new code.

      :raises `~aiida.common.exceptions.ValidationError`: if no transport could be opened or if the defined executable
          does not exist on the remote computer.

   .. py:method:: set_prepend_text(code)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_prepend_text

      Pass a string of code that will be put in the scheduler script before the
      execution of the code.

   .. py:method:: get_prepend_text()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_prepend_text

      Return the code that will be put in the scheduler script before the
      execution, or an empty string if no pre-exec code was defined.

   .. py:method:: set_input_plugin_name(input_plugin)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_input_plugin_name

      Set the name of the default input plugin, to be used for the automatic
      generation of a new calculation.

   .. py:method:: get_input_plugin_name()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_input_plugin_name

      Return the name of the default input plugin (or None if no input plugin
      was set.

   .. py:method:: set_use_double_quotes(use_double_quotes: bool)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_use_double_quotes

      Set whether the command line invocation of this code should be escaped with double quotes.

      :param use_double_quotes: True if to escape with double quotes, False otherwise.

   .. py:method:: get_use_double_quotes() -> bool
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_use_double_quotes

      Return whether the command line invocation of this code should be escaped with double quotes.

      :returns: True if to escape with double quotes, False otherwise which is also the default.

   .. py:method:: set_append_text(code)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_append_text

      Pass a string of code that will be put in the scheduler script after the
      execution of the code.

   .. py:method:: get_append_text()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_append_text

      Return the postexec_code, or an empty string if no post-exec code was defined.

   .. py:method:: set_local_executable(exec_name)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_local_executable

      Set the filename of the local executable.
      Implicitly set the code as local.

   .. py:method:: get_local_executable()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_local_executable

   .. py:method:: set_remote_computer_exec(remote_computer_exec)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.set_remote_computer_exec

      Set the code as remote, and pass the computer on which it resides
      and the absolute path on that computer.

      :param remote_computer_exec: a tuple (computer, remote_exec_path), where computer is a aiida.orm.Computer and
          remote_exec_path is the absolute path of the main executable on remote computer.

   .. py:method:: get_remote_exec_path()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_remote_exec_path

   .. py:method:: get_remote_computer()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_remote_computer

      Return the remote computer associated with this code.

   .. py:method:: _set_local()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._set_local

      Set the code as a 'local' code, meaning that all the files belonging to the code
      will be copied to the cluster, and the file set with set_exec_filename will be
      run.

      It also deletes the flags related to the local case (if any)

   .. py:method:: _set_remote()
      :canonical: aiida.orm.nodes.data.code.legacy.Code._set_remote

      Set the code as a 'remote' code, meaning that the code itself has no files attached,
      but only a location on a remote computer (with an absolute path of the executable on
      the remote computer).

      It also deletes the flags related to the local case (if any)

   .. py:method:: is_local()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.is_local

      Return True if the code is 'local', False if it is 'remote' (see also documentation
      of the set_local and set_remote functions).

   .. py:method:: can_run_on(computer)
      :canonical: aiida.orm.nodes.data.code.legacy.Code.can_run_on

      Return True if this code can run on the given computer, False otherwise.

      Local codes can run on any machine; remote codes can run only on the machine
      on which they reside.

      TODO: add filters to mask the remote machines on which a local code can run.

   .. py:method:: get_execname()
      :canonical: aiida.orm.nodes.data.code.legacy.Code.get_execname

      Return the executable string to be put in the script.
      For local codes, it is ./LOCAL_EXECUTABLE_NAME
      For remote codes, it is the absolute path to the executable.

.. py:class:: CodeEntityLoader
   :canonical: aiida.orm.utils.loaders.CodeEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   Loader for the `Code` entity and sub classes.

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.CodeEntityLoader.orm_base_class

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.CodeEntityLoader._get_query_builder_label_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance that should retrieve the entity corresponding to the identifier
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

.. py:class:: Collection(entity_class: typing.Type[aiida.orm.entities.EntityType], backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.entities.Collection

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`aiida.orm.entities.EntityType`\ ]

   Container class that represents the collection of objects of a particular entity type.

   .. rubric:: Initialization

   Construct a new entity collection.

   :param entity_class: the entity type e.g. User, Computer, etc
   :param backend: the backend instance to get the collection for, or use the default

   .. py:method:: _entity_base_cls() -> typing.Type[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection._entity_base_cls
      :abstractmethod:
      :staticmethod:

      The allowed entity class or subclasses thereof.

   .. py:method:: get_cached(entity_class: typing.Type[aiida.orm.entities.EntityType], backend: aiida.orm.implementation.StorageBackend)
      :canonical: aiida.orm.entities.Collection.get_cached
      :classmethod:

      Get the cached collection instance for the given entity class and backend.

      :param backend: the backend instance to get the collection for

   .. py:method:: __call__(backend: aiida.orm.implementation.StorageBackend) -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Collection.__call__

      Get or create a cached collection using a new backend.

   .. py:property:: entity_type
      :canonical: aiida.orm.entities.Collection.entity_type
      :type: typing.Type[aiida.orm.entities.EntityType]

      The entity type for this instance.

   .. py:property:: backend
      :canonical: aiida.orm.entities.Collection.backend
      :type: aiida.orm.implementation.StorageBackend

      Return the backend.

   .. py:method:: query(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.entities.Collection.query

      Get a query builder for the objects of this collection.

      :param filters: the keyword value pair filters to match
      :param order_by: a list of (key, direction) pairs specifying the sort order
      :param limit: the maximum number of results to return
      :param offset: number of initial results to be skipped

   .. py:method:: get(**filters: typing.Any) -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Collection.get

      Get a single collection entry that matches the filter criteria.

      :param filters: the filters identifying the object to get

      :return: the entry

   .. py:method:: find(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, limit: typing.Optional[int] = None) -> typing.List[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection.find

      Find collection entries matching the filter criteria.

      :param filters: the keyword value pair filters to match
      :param order_by: a list of (key, direction) pairs specifying the sort order
      :param limit: the maximum number of results to return

      :return: a list of resulting matches

   .. py:method:: all() -> typing.List[aiida.orm.entities.EntityType]
      :canonical: aiida.orm.entities.Collection.all

      Get all entities in this collection.

      :return: A list of all entities

   .. py:method:: count(filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None) -> int
      :canonical: aiida.orm.entities.Collection.count

      Count entities in this collection according to criteria.

      :param filters: the keyword value pair filters to match

      :return: The number of entities found using the supplied criteria

.. py:class:: Comment(node: aiida.orm.Node, user: aiida.orm.User, content: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.comments.Comment

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendComment`\ , :py:obj:`aiida.orm.comments.CommentCollection`\ ]

   Base class to map a DbComment that represents a comment attached to a certain Node.

   .. rubric:: Initialization

   Create a Comment for a given node and user

   :param node: a Node instance
   :param user: a User instance
   :param content: the comment content
   :param backend: the backend to use for the instance, or use the default backend if None

   :return: a Comment object associated to the given node and user

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.comments.Comment._CLS_COLLECTION
      :value: None

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.comments.Comment.__str__

   .. py:property:: uuid
      :canonical: aiida.orm.comments.Comment.uuid
      :type: str

      Return the UUID for this comment.

      This identifier is unique across all entities types and backend instances.

      :return: the entity uuid

   .. py:property:: ctime
      :canonical: aiida.orm.comments.Comment.ctime
      :type: datetime.datetime

   .. py:property:: mtime
      :canonical: aiida.orm.comments.Comment.mtime
      :type: datetime.datetime

   .. py:method:: set_mtime(value: datetime.datetime) -> None
      :canonical: aiida.orm.comments.Comment.set_mtime

   .. py:property:: node
      :canonical: aiida.orm.comments.Comment.node
      :type: aiida.orm.Node

   .. py:property:: user
      :canonical: aiida.orm.comments.Comment.user
      :type: aiida.orm.User

   .. py:method:: set_user(value: aiida.orm.User) -> None
      :canonical: aiida.orm.comments.Comment.set_user

   .. py:property:: content
      :canonical: aiida.orm.comments.Comment.content
      :type: str

   .. py:method:: set_content(value: str) -> None
      :canonical: aiida.orm.comments.Comment.set_content

.. py:class:: Computer(label: typing.Optional[str] = None, hostname: str = '', description: str = '', transport_type: str = '', scheduler_type: str = '', workdir: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.computers.Computer

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendComputer`\ , :py:obj:`aiida.orm.computers.ComputerCollection`\ ]

   Computer entity.

   .. rubric:: Initialization

   Construct a new computer.

   .. py:attribute:: _logger
      :canonical: aiida.orm.computers.Computer._logger
      :value: None

   .. py:attribute:: PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL
      :canonical: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL
      :value: 'minimum_scheduler_poll_interval'

   .. py:attribute:: PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT
      :canonical: aiida.orm.computers.Computer.PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT
      :value: 10.0

   .. py:attribute:: PROPERTY_WORKDIR
      :canonical: aiida.orm.computers.Computer.PROPERTY_WORKDIR
      :value: 'workdir'

   .. py:attribute:: PROPERTY_SHEBANG
      :canonical: aiida.orm.computers.Computer.PROPERTY_SHEBANG
      :value: 'shebang'

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.computers.Computer._CLS_COLLECTION
      :value: None

   .. py:method:: __repr__()
      :canonical: aiida.orm.computers.Computer.__repr__

   .. py:method:: __str__()
      :canonical: aiida.orm.computers.Computer.__str__

   .. py:property:: uuid
      :canonical: aiida.orm.computers.Computer.uuid
      :type: str

      Return the UUID for this computer.

      This identifier is unique across all entities types and backend instances.

      :return: the entity uuid

   .. py:property:: logger
      :canonical: aiida.orm.computers.Computer.logger
      :type: logging.Logger

   .. py:method:: _label_validator(label: str) -> None
      :canonical: aiida.orm.computers.Computer._label_validator
      :classmethod:

      Validates the label.

   .. py:method:: _hostname_validator(hostname: str) -> None
      :canonical: aiida.orm.computers.Computer._hostname_validator
      :classmethod:

      Validates the hostname.

   .. py:method:: _description_validator(description: str) -> None
      :canonical: aiida.orm.computers.Computer._description_validator
      :classmethod:

      Validates the description.

   .. py:method:: _transport_type_validator(transport_type: str) -> None
      :canonical: aiida.orm.computers.Computer._transport_type_validator
      :classmethod:

      Validates the transport string.

   .. py:method:: _scheduler_type_validator(scheduler_type: str) -> None
      :canonical: aiida.orm.computers.Computer._scheduler_type_validator
      :classmethod:

      Validates the transport string.

   .. py:method:: _prepend_text_validator(prepend_text: str) -> None
      :canonical: aiida.orm.computers.Computer._prepend_text_validator
      :classmethod:

      Validates the prepend text string.

   .. py:method:: _append_text_validator(append_text: str) -> None
      :canonical: aiida.orm.computers.Computer._append_text_validator
      :classmethod:

      Validates the append text string.

   .. py:method:: _workdir_validator(workdir: str) -> None
      :canonical: aiida.orm.computers.Computer._workdir_validator
      :classmethod:

      Validates the transport string.

   .. py:method:: _mpirun_command_validator(mpirun_cmd: typing.Union[typing.List[str], typing.Tuple[str, ...]]) -> None
      :canonical: aiida.orm.computers.Computer._mpirun_command_validator

      Validates the mpirun_command variable. MUST be called after properly
      checking for a valid scheduler.

   .. py:method:: validate() -> None
      :canonical: aiida.orm.computers.Computer.validate

      Check if the attributes and files retrieved from the DB are valid.
      Raise a ValidationError if something is wrong.

      Must be able to work even before storing: therefore, use the get_attr and similar methods
      that automatically read either from the DB or from the internal attribute cache.

      For the base class, this is always valid. Subclasses will reimplement this.
      In the subclass, always call the super().validate() method first!

   .. py:method:: _default_mpiprocs_per_machine_validator(def_cpus_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer._default_mpiprocs_per_machine_validator
      :classmethod:

      Validates the default number of CPUs per machine (node)

   .. py:method:: default_memory_per_machine_validator(def_memory_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.default_memory_per_machine_validator
      :classmethod:

      Validates the default amount of memory (kB) per machine (node)

   .. py:method:: copy() -> aiida.orm.computers.Computer
      :canonical: aiida.orm.computers.Computer.copy

      Return a copy of the current object to work with, not stored yet.

   .. py:method:: store() -> aiida.orm.computers.Computer
      :canonical: aiida.orm.computers.Computer.store

      Store the computer in the DB.

      Differently from Nodes, a computer can be re-stored if its properties
      are to be changed (e.g. a new mpirun command, etc.)

   .. py:property:: label
      :canonical: aiida.orm.computers.Computer.label
      :type: str

      Return the computer label.

      :return: the label.

   .. py:property:: description
      :canonical: aiida.orm.computers.Computer.description
      :type: str

      Return the computer computer.

      :return: the description.

   .. py:property:: hostname
      :canonical: aiida.orm.computers.Computer.hostname
      :type: str

      Return the computer hostname.

      :return: the hostname.

   .. py:property:: scheduler_type
      :canonical: aiida.orm.computers.Computer.scheduler_type
      :type: str

      Return the computer scheduler type.

      :return: the scheduler type.

   .. py:property:: transport_type
      :canonical: aiida.orm.computers.Computer.transport_type
      :type: str

      Return the computer transport type.

      :return: the transport_type.

   .. py:property:: metadata
      :canonical: aiida.orm.computers.Computer.metadata
      :type: typing.Dict[str, typing.Any]

      Return the computer metadata.

      :return: the metadata.

   .. py:method:: delete_property(name: str, raise_exception: bool = True) -> None
      :canonical: aiida.orm.computers.Computer.delete_property

      Delete a property from this computer

      :param name: the name of the property
      :param raise_exception: if True raise if the property does not exist, otherwise return None

   .. py:method:: set_property(name: str, value: typing.Any) -> None
      :canonical: aiida.orm.computers.Computer.set_property

      Set a property on this computer

      :param name: the property name
      :param value: the new value

   .. py:method:: get_property(name: str, *args: typing.Any) -> typing.Any
      :canonical: aiida.orm.computers.Computer.get_property

      Get a property of this computer

      :param name: the property name
      :param args: additional arguments

      :return: the property value

   .. py:method:: get_prepend_text() -> str
      :canonical: aiida.orm.computers.Computer.get_prepend_text

   .. py:method:: set_prepend_text(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_prepend_text

   .. py:method:: get_append_text() -> str
      :canonical: aiida.orm.computers.Computer.get_append_text

   .. py:method:: set_append_text(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_append_text

   .. py:method:: get_use_double_quotes() -> bool
      :canonical: aiida.orm.computers.Computer.get_use_double_quotes

      Return whether the command line parameters of this computer should be escaped with double quotes.

      :returns: True if to escape with double quotes, False otherwise which is also the default.

   .. py:method:: set_use_double_quotes(val: bool) -> None
      :canonical: aiida.orm.computers.Computer.set_use_double_quotes

      Set whether the command line parameters of this computer should be escaped with double quotes.

      :param use_double_quotes: True if to escape with double quotes, False otherwise.

   .. py:method:: get_mpirun_command() -> typing.List[str]
      :canonical: aiida.orm.computers.Computer.get_mpirun_command

      Return the mpirun command. Must be a list of strings, that will be
      then joined with spaces when submitting.

      I also provide a sensible default that may be ok in many cases.

   .. py:method:: set_mpirun_command(val: typing.Union[typing.List[str], typing.Tuple[str, ...]]) -> None
      :canonical: aiida.orm.computers.Computer.set_mpirun_command

      Set the mpirun command. It must be a list of strings (you can use
      string.split() if you have a single, space-separated string).

   .. py:method:: get_default_mpiprocs_per_machine() -> typing.Optional[int]
      :canonical: aiida.orm.computers.Computer.get_default_mpiprocs_per_machine

      Return the default number of CPUs per machine (node) for this computer,
      or None if it was not set.

   .. py:method:: set_default_mpiprocs_per_machine(def_cpus_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.set_default_mpiprocs_per_machine

      Set the default number of CPUs per machine (node) for this computer.
      Accepts None if you do not want to set this value.

   .. py:method:: get_default_memory_per_machine() -> typing.Optional[int]
      :canonical: aiida.orm.computers.Computer.get_default_memory_per_machine

      Return the default amount of memory (kB) per machine (node) for this computer,
      or None if it was not set.

   .. py:method:: set_default_memory_per_machine(def_memory_per_machine: typing.Optional[int]) -> None
      :canonical: aiida.orm.computers.Computer.set_default_memory_per_machine

      Set the default amount of memory (kB) per machine (node) for this computer.
      Accepts None if you do not want to set this value.

   .. py:method:: get_minimum_job_poll_interval() -> float
      :canonical: aiida.orm.computers.Computer.get_minimum_job_poll_interval

      Get the minimum interval between subsequent requests to poll the scheduler for job status.

      .. note:: If no value was ever set for this computer it will fall back on the default provided by the associated
          transport class in the ``DEFAULT_MINIMUM_JOB_POLL_INTERVAL`` attribute. If the computer doesn't have a
          transport class, or it cannot be loaded, or it doesn't provide a job poll interval default, then this will
          fall back on the ``PROPERTY_MINIMUM_SCHEDULER_POLL_INTERVAL__DEFAULT`` attribute of this class.

      :return: The minimum interval (in seconds).

   .. py:method:: set_minimum_job_poll_interval(interval: float) -> None
      :canonical: aiida.orm.computers.Computer.set_minimum_job_poll_interval

      Set the minimum interval between subsequent requests to update the list
      of jobs currently running on this computer.

      :param interval: The minimum interval in seconds

   .. py:method:: get_workdir() -> str
      :canonical: aiida.orm.computers.Computer.get_workdir

      Get the working directory for this computer
      :return: The currently configured working directory

   .. py:method:: set_workdir(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_workdir

   .. py:method:: get_shebang() -> str
      :canonical: aiida.orm.computers.Computer.get_shebang

   .. py:method:: set_shebang(val: str) -> None
      :canonical: aiida.orm.computers.Computer.set_shebang

      :param str val: A valid shebang line

   .. py:method:: get_authinfo(user: aiida.orm.User) -> aiida.orm.AuthInfo
      :canonical: aiida.orm.computers.Computer.get_authinfo

      Return the aiida.orm.authinfo.AuthInfo instance for the
      given user on this computer, if the computer
      is configured for the given user.

      :param user: a User instance.
      :return: a AuthInfo instance
      :raise aiida.common.NotExistent: if the computer is not configured for the given
          user.

   .. py:property:: is_configured
      :canonical: aiida.orm.computers.Computer.is_configured
      :type: bool

      Return whether the computer is configured for the current default user.

      :return: Boolean, ``True`` if the computer is configured for the current default user, ``False`` otherwise.

   .. py:method:: is_user_configured(user: aiida.orm.User) -> bool
      :canonical: aiida.orm.computers.Computer.is_user_configured

      Is the user configured on this computer?

      :param user: the user to check
      :return: True if configured, False otherwise

   .. py:method:: is_user_enabled(user: aiida.orm.User) -> bool
      :canonical: aiida.orm.computers.Computer.is_user_enabled

      Is the given user enabled to run on this computer?

      :param user: the user to check
      :return: True if enabled, False otherwise

   .. py:method:: get_transport(user: typing.Optional[aiida.orm.User] = None) -> aiida.transports.Transport
      :canonical: aiida.orm.computers.Computer.get_transport

      Return a Transport class, configured with all correct parameters.
      The Transport is closed (meaning that if you want to run any operation with
      it, you have to open it first (i.e., e.g. for a SSH transport, you have
      to open a connection). To do this you can call ``transports.open()``, or simply
      run within a ``with`` statement::

         transport = Computer.get_transport()
         with transport:
             print(transports.whoami())

      :param user: if None, try to obtain a transport for the default user.
          Otherwise, pass a valid User.

      :return: a (closed) Transport, already configured with the connection
          parameters to the supercomputer, as configured with ``verdi computer configure``
          for the user specified as a parameter ``user``.

   .. py:method:: get_transport_class() -> typing.Type[aiida.transports.Transport]
      :canonical: aiida.orm.computers.Computer.get_transport_class

      Get the transport class for this computer.  Can be used to instantiate a transport instance.

   .. py:method:: get_scheduler() -> aiida.schedulers.Scheduler
      :canonical: aiida.orm.computers.Computer.get_scheduler

      Get a scheduler instance for this computer

   .. py:method:: configure(user: typing.Optional[aiida.orm.User] = None, **kwargs: typing.Any) -> aiida.orm.AuthInfo
      :canonical: aiida.orm.computers.Computer.configure

      Configure a computer for a user with valid auth params passed via kwargs

      :param user: the user to configure the computer for
      :kwargs: the configuration keywords with corresponding values
      :return: the authinfo object for the configured user

   .. py:method:: get_configuration(user: typing.Optional[aiida.orm.User] = None) -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.computers.Computer.get_configuration

      Get the configuration of computer for the given user as a dictionary

      :param user: the user to to get the configuration for, otherwise default user

.. py:class:: ComputerEntityLoader
   :canonical: aiida.orm.utils.loaders.ComputerEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   Loader for the `Computer` entity and sub classes.

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.ComputerEntityLoader.orm_base_class

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.ComputerEntityLoader._get_query_builder_label_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance that should retrieve the entity corresponding to the identifier
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

.. py:class:: ContainerizedCode(engine_command: str, image_name: str, **kwargs)
   :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.installed.InstalledCode`

   Data plugin representing an executable code in container on a remote computer.

   .. py:attribute:: _KEY_ATTRIBUTE_ENGINE_COMMAND
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_ENGINE_COMMAND
      :type: str
      :value: 'engine_command'

   .. py:attribute:: _KEY_ATTRIBUTE_IMAGE_NAME
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._KEY_ATTRIBUTE_IMAGE_NAME
      :type: str
      :value: 'image_name'

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.filepath_executable
      :type: pathlib.PurePosixPath

      Return the filepath of the executable that this code represents.

      .. note:: This is overridden from the base class since the path does not have to be absolute.

      :return: The filepath of the executable.

   .. py:property:: engine_command
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.engine_command
      :type: str

      Return the engine command with image as template field of the containerized code

      :return: The engine command of the containerized code

   .. py:property:: image_name
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.image_name
      :type: str

      The image name of container

      :return: The image name of container.

   .. py:method:: get_prepend_cmdline_params(mpi_args: list[str] | None = None, extra_mpirun_params: list[str] | None = None) -> list[str]
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode.get_prepend_cmdline_params

      Return the list of prepend cmdline params for mpi seeting

      :return: list of prepend cmdline parameters.

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.containerized.ContainerizedCode._get_cli_options
      :classmethod:

      Return the CLI options that would allow to create an instance of this class.

.. py:data:: DESCENDING
   :canonical: aiida.orm.logs.DESCENDING
   :value: 'desc'

.. py:class:: Data(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.data.Data

   Bases: :py:obj:`aiida.orm.nodes.node.Node`

   The base class for all Data nodes.

   AiiDA Data classes are subclasses of Node and must support multiple inheritance.

   Architecture note:
   Calculation plugins are responsible for converting raw output data from simulation codes to Data nodes.
   Nodes are responsible for validating their content (see _validate method).

   .. rubric:: Initialization

   Construct a new instance, setting the ``source`` attribute if provided as a keyword argument.

   .. py:attribute:: _source_attributes
      :canonical: aiida.orm.nodes.data.data.Data._source_attributes
      :value: ['db_name', 'db_uri', 'uri', 'id', 'version', 'extras', 'source_md5', 'description', 'license']

   .. py:attribute:: _export_format_replacements
      :canonical: aiida.orm.nodes.data.data.Data._export_format_replacements
      :type: typing.Dict[str, str]
      :value: None

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.data.Data._storable
      :value: True

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.data.data.Data._unstorable_message
      :value: 'storing for this node has been disabled'

   .. py:method:: __copy__()
      :canonical: aiida.orm.nodes.data.data.Data.__copy__

      Copying a Data node is not supported, use copy.deepcopy or call Data.clone().

   .. py:method:: __deepcopy__(memo)
      :canonical: aiida.orm.nodes.data.data.Data.__deepcopy__

      Create a clone of the Data node by piping through to the clone method and return the result.

      :returns: an unstored clone of this Data node

   .. py:method:: clone()
      :canonical: aiida.orm.nodes.data.data.Data.clone

      Create a clone of the Data node.

      :returns: an unstored clone of this Data node

   .. py:property:: source
      :canonical: aiida.orm.nodes.data.data.Data.source

      Gets the dictionary describing the source of Data object. Possible fields:

      * **db_name**: name of the source database.
      * **db_uri**: URI of the source database.
      * **uri**: URI of the object's source. Should be a permanent link.
      * **id**: object's source identifier in the source database.
      * **version**: version of the object's source.
      * **extras**: a dictionary with other fields for source description.
      * **source_md5**: MD5 checksum of object's source.
      * **description**: human-readable free form description of the object's source.
      * **license**: a string with a type of license.

      .. note:: some limitations for setting the data source exist, see ``_validate`` method.

      :return: dictionary describing the source of Data object.

   .. py:method:: set_source(source)
      :canonical: aiida.orm.nodes.data.data.Data.set_source

      Sets the dictionary describing the source of Data object.

   .. py:property:: creator
      :canonical: aiida.orm.nodes.data.data.Data.creator

      Return the creator of this node or None if it does not exist.

      :return: the creating node or None

   .. py:method:: _exportcontent(fileformat, main_file_name='', **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data._exportcontent

      Converts a Data node to one (or multiple) files.

      Note: Export plugins should return utf8-encoded **bytes**, which can be
      directly dumped to file.

      :param fileformat: the extension, uniquely specifying the file format.
      :type fileformat: str
      :param main_file_name: (empty by default) Can be used by plugin to
          infer sensible names for additional files, if necessary.  E.g. if the
          main file is '../myplot.gnu', the plugin may decide to store the dat
          file under '../myplot_data.dat'.
      :type main_file_name: str
      :param kwargs: other parameters are passed down to the plugin
      :returns: a tuple of length 2. The first element is the content of the
          otuput file. The second is a dictionary (possibly empty) in the format
          {filename: filecontent} for any additional file that should be produced.
      :rtype: (bytes, dict)

   .. py:method:: export(path, fileformat=None, overwrite=False, **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data.export

      Save a Data object to a file.

      :param fname: string with file name. Can be an absolute or relative path.
      :param fileformat: kind of format to use for the export. If not present,
          it will try to use the extension of the file name.
      :param overwrite: if set to True, overwrites file found at path. Default=False
      :param kwargs: additional parameters to be passed to the
          _exportcontent method
      :return: the list of files created

   .. py:method:: _get_exporters()
      :canonical: aiida.orm.nodes.data.data.Data._get_exporters

      Get all implemented export formats.
      The convention is to find all _prepare_... methods.
      Returns a dictionary of method_name: method_function

   .. py:method:: get_export_formats()
      :canonical: aiida.orm.nodes.data.data.Data.get_export_formats
      :classmethod:

      Get the list of valid export format strings

      :return: a list of valid formats

   .. py:method:: importstring(inputstring, fileformat, **kwargs)
      :canonical: aiida.orm.nodes.data.data.Data.importstring

      Converts a Data object to other text format.

      :param fileformat: a string (the extension) to describe the file format.
      :returns: a string with the structure description.

   .. py:method:: importfile(fname, fileformat=None)
      :canonical: aiida.orm.nodes.data.data.Data.importfile

      Populate a Data object from a file.

      :param fname: string with file name. Can be an absolute or relative path.
      :param fileformat: kind of format to use for the export. If not present,
          it will try to use the extension of the file name.

   .. py:method:: _get_importers()
      :canonical: aiida.orm.nodes.data.data.Data._get_importers

      Get all implemented import formats.
      The convention is to find all _parse_... methods.
      Returns a list of strings.

   .. py:method:: convert(object_format=None, *args)
      :canonical: aiida.orm.nodes.data.data.Data.convert

      Convert the AiiDA StructureData into another python object

      :param object_format: Specify the output format

   .. py:method:: _get_converters()
      :canonical: aiida.orm.nodes.data.data.Data._get_converters

      Get all implemented converter formats.
      The convention is to find all _get_object_... methods.
      Returns a list of strings.

.. py:class:: Dict(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.dict.Dict

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   `Data` sub class to represent a dictionary.

   The dictionary contents of a `Dict` node are stored in the database as attributes. The dictionary
   can be initialized through the `dict` argument in the constructor. After construction, values can
   be retrieved and updated through the item getters and setters, respectively:

       node['key'] = 'value'

   Alternatively, the `dict` property returns an instance of the `AttributeManager` that can be used
   to get and set values through attribute notation:

       node.dict.key = 'value'

   Note that trying to set dictionary values directly on the node, e.g. `node.key = value`, will not
   work as intended. It will merely set the `key` attribute on the node instance, but will not be
   stored in the database. As soon as the node goes out of scope, the value will be lost.

   It is also relevant to note here the difference in something being an "attribute of a node" (in
   the sense that it is stored in the "attribute" column of the database when the node is stored)
   and something being an "attribute of a python object" (in the sense of being able to modify and
   access it as if it was a property of the variable, e.g. `node.key = value`). This is true of all
   types of nodes, but it becomes more relevant for `Dict` nodes where one is constantly manipulating
   these attributes.

   Finally, all dictionary mutations will be forbidden once the node is stored.

   .. rubric:: Initialization

   Initialise a ``Dict`` node instance.

   Usual rules for attribute names apply, in particular, keys cannot start with an underscore, or a ``ValueError``
   will be raised.

   Initial attributes can be changed, deleted or added as long as the node is not stored.

   :param value: dictionary to initialise the ``Dict`` node from

   .. py:method:: __getitem__(key)
      :canonical: aiida.orm.nodes.data.dict.Dict.__getitem__

   .. py:method:: __setitem__(key, value)
      :canonical: aiida.orm.nodes.data.dict.Dict.__setitem__

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.dict.Dict.__eq__

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.nodes.data.dict.Dict.__contains__

      Return whether the node contains a key.

   .. py:method:: set_dict(dictionary)
      :canonical: aiida.orm.nodes.data.dict.Dict.set_dict

      Replace the current dictionary with another one.

      :param dictionary: dictionary to set

   .. py:method:: update_dict(dictionary)
      :canonical: aiida.orm.nodes.data.dict.Dict.update_dict

      Update the current dictionary with the keys provided in the dictionary.

      .. note:: works exactly as `dict.update()` where new keys are simply added and existing keys are overwritten.

      :param dictionary: a dictionary with the keys to substitute

   .. py:method:: get_dict()
      :canonical: aiida.orm.nodes.data.dict.Dict.get_dict

      Return a dictionary with the parameters currently set.

      :return: dictionary

   .. py:method:: keys()
      :canonical: aiida.orm.nodes.data.dict.Dict.keys

      Iterator of valid keys stored in the Dict object.

      :return: iterator over the keys of the current dictionary

   .. py:method:: items()
      :canonical: aiida.orm.nodes.data.dict.Dict.items

      Iterator of all items stored in the Dict node.

   .. py:property:: dict
      :canonical: aiida.orm.nodes.data.dict.Dict.dict

      Return an instance of `AttributeManager` that transforms the dictionary into an attribute dict.

      .. note:: this will allow one to do `node.dict.key` as well as `node.dict[key]`.

      :return: an instance of the `AttributeResultManager`.

.. py:class:: Entity(backend_entity: aiida.orm.entities.BackendEntityType)
   :canonical: aiida.orm.entities.Entity

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`aiida.orm.entities.BackendEntityType`\ , :py:obj:`aiida.orm.entities.CollectionType`\ ]

   An AiiDA entity

   .. rubric:: Initialization

   :param backend_entity: the backend model supporting this entity

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.entities.Entity._CLS_COLLECTION
      :type: typing.Type[aiida.orm.entities.CollectionType]
      :value: None

   .. py:method:: objects() -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Entity.objects

      Get a collection for objects of this type, with the default backend.

      .. deprecated:: This will be removed in v3, use ``collection`` instead.

      :return: an object that can be used to access entities of this type

   .. py:method:: collection() -> aiida.orm.entities.CollectionType
      :canonical: aiida.orm.entities.Entity.collection

      Get a collection for objects of this type, with the default backend.

      :return: an object that can be used to access entities of this type

   .. py:method:: get(**kwargs)
      :canonical: aiida.orm.entities.Entity.get
      :classmethod:

      Get an entity of the collection matching the given filters.

      .. deprecated: Will be removed in v3, use `Entity.collection.get` instead.


   .. py:method:: from_backend_entity(backend_entity: aiida.orm.entities.BackendEntityType) -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Entity.from_backend_entity
      :classmethod:

      Construct an entity from a backend entity instance

      :param backend_entity: the backend entity

      :return: an AiiDA entity instance

   .. py:method:: __getstate__()
      :canonical: aiida.orm.entities.Entity.__getstate__

      Prevent an ORM entity instance from being pickled.

   .. py:method:: initialize() -> None
      :canonical: aiida.orm.entities.Entity.initialize

      Initialize instance attributes.

      This will be called after the constructor is called or an entity is created from an existing backend entity.

   .. py:property:: id
      :canonical: aiida.orm.entities.Entity.id
      :type: int

      Return the id for this entity.

      This identifier is guaranteed to be unique amongst entities of the same type for a single backend instance.

      .. deprecated: Will be removed in v3, use `pk` instead.

      :return: the entity's id

   .. py:property:: pk
      :canonical: aiida.orm.entities.Entity.pk
      :type: int

      Return the primary key for this entity.

      This identifier is guaranteed to be unique amongst entities of the same type for a single backend instance.

      :return: the entity's principal key

   .. py:method:: store() -> aiida.orm.entities.EntityType
      :canonical: aiida.orm.entities.Entity.store

      Store the entity.

   .. py:property:: is_stored
      :canonical: aiida.orm.entities.Entity.is_stored
      :type: bool

      Return whether the entity is stored.

   .. py:property:: backend
      :canonical: aiida.orm.entities.Entity.backend
      :type: aiida.orm.implementation.StorageBackend

      Get the backend for this entity

   .. py:property:: backend_entity
      :canonical: aiida.orm.entities.Entity.backend_entity
      :type: aiida.orm.entities.BackendEntityType

      Get the implementing class for this object

.. py:class:: EntityExtras(entity: typing.Union[aiida.orm.nodes.node.Node, aiida.orm.groups.Group])
   :canonical: aiida.orm.extras.EntityExtras

   Interface to the extras of a node or group instance.

   Extras are a JSONable dictionary, stored on each entity,
   allowing for arbitrary data to be stored by users.

   Extras are mutable, even after storing the entity,
   and as such are not deemed a core part of the provenance graph.

   .. rubric:: Initialization

   Initialize the interface.

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.extras.EntityExtras.__contains__

      Check if the extras contain the given key.

   .. py:property:: all
      :canonical: aiida.orm.extras.EntityExtras.all
      :type: typing.Dict[str, typing.Any]

      Return the complete extras dictionary.

      .. warning:: While the entity is unstored, this will return references of the extras on the database model,
          meaning that changes on the returned values (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          extras will be a deep copy and mutations of the database extras will have to go through the appropriate set
          methods. Therefore, once stored, retrieving a deep copy can be a heavy operation. If you only need the keys
          or some values, use the iterators `extras_keys` and `extras_items`, or the getters `get_extra` and
          `get_extra_many` instead.

      :return: the extras as a dictionary

   .. py:method:: get(key: str, default: typing.Any = _NO_DEFAULT) -> typing.Any
      :canonical: aiida.orm.extras.EntityExtras.get

      Return the value of an extra.

      .. warning:: While the entity is unstored, this will return a reference of the extra on the database model,
          meaning that changes on the returned value (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          extra will be a deep copy and mutations of the database extras will have to go through the appropriate set
          methods.

      :param key: name of the extra
      :param default: return this value instead of raising if the attribute does not exist
      :return: the value of the extra
      :raises AttributeError: if the extra does not exist and no default is specified

   .. py:method:: get_many(keys: typing.List[str]) -> typing.List[typing.Any]
      :canonical: aiida.orm.extras.EntityExtras.get_many

      Return the values of multiple extras.

      .. warning:: While the entity is unstored, this will return references of the extras on the database model,
          meaning that changes on the returned values (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          extras will be a deep copy and mutations of the database extras will have to go through the appropriate set
          methods. Therefore, once stored, retrieving a deep copy can be a heavy operation. If you only need the keys
          or some values, use the iterators `extras_keys` and `extras_items`, or the getters `get_extra` and
          `get_extra_many` instead.

      :param keys: a list of extra names
      :return: a list of extra values
      :raises AttributeError: if at least one extra does not exist

   .. py:method:: set(key: str, value: typing.Any) -> None
      :canonical: aiida.orm.extras.EntityExtras.set

      Set an extra to the given value.

      :param key: name of the extra
      :param value: value of the extra
      :raise aiida.common.ValidationError: if the key is invalid, i.e. contains periods

   .. py:method:: set_many(extras: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.extras.EntityExtras.set_many

      Set multiple extras.

      .. note:: This will override any existing extras that are present in the new dictionary.

      :param extras: a dictionary with the extras to set
      :raise aiida.common.ValidationError: if any of the keys are invalid, i.e. contain periods

   .. py:method:: reset(extras: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.extras.EntityExtras.reset

      Reset the extras.

      .. note:: This will completely clear any existing extras and replace them with the new dictionary.

      :param extras: a dictionary with the extras to set
      :raise aiida.common.ValidationError: if any of the keys are invalid, i.e. contain periods

   .. py:method:: delete(key: str) -> None
      :canonical: aiida.orm.extras.EntityExtras.delete

      Delete an extra.

      :param key: name of the extra
      :raises AttributeError: if the extra does not exist

   .. py:method:: delete_many(keys: typing.List[str]) -> None
      :canonical: aiida.orm.extras.EntityExtras.delete_many

      Delete multiple extras.

      :param keys: names of the extras to delete
      :raises AttributeError: if at least one of the extra does not exist

   .. py:method:: clear() -> None
      :canonical: aiida.orm.extras.EntityExtras.clear

      Delete all extras.

   .. py:method:: items() -> typing.Iterable[typing.Tuple[str, typing.Any]]
      :canonical: aiida.orm.extras.EntityExtras.items

      Return an iterator over the extras.

      :return: an iterator with extra key value pairs

   .. py:method:: keys() -> typing.Iterable[str]
      :canonical: aiida.orm.extras.EntityExtras.keys

      Return an iterator over the extra keys.

      :return: an iterator with extra keys

.. py:class:: EntityTypes
   :canonical: aiida.orm.entities.EntityTypes

   Bases: :py:obj:`enum.Enum`

   Enum for referring to ORM entities in a backend-agnostic manner.

   .. py:attribute:: AUTHINFO
      :canonical: aiida.orm.entities.EntityTypes.AUTHINFO
      :value: 'authinfo'

   .. py:attribute:: COMMENT
      :canonical: aiida.orm.entities.EntityTypes.COMMENT
      :value: 'comment'

   .. py:attribute:: COMPUTER
      :canonical: aiida.orm.entities.EntityTypes.COMPUTER
      :value: 'computer'

   .. py:attribute:: GROUP
      :canonical: aiida.orm.entities.EntityTypes.GROUP
      :value: 'group'

   .. py:attribute:: LOG
      :canonical: aiida.orm.entities.EntityTypes.LOG
      :value: 'log'

   .. py:attribute:: NODE
      :canonical: aiida.orm.entities.EntityTypes.NODE
      :value: 'node'

   .. py:attribute:: USER
      :canonical: aiida.orm.entities.EntityTypes.USER
      :value: 'user'

   .. py:attribute:: LINK
      :canonical: aiida.orm.entities.EntityTypes.LINK
      :value: 'link'

   .. py:attribute:: GROUP_NODE
      :canonical: aiida.orm.entities.EntityTypes.GROUP_NODE
      :value: 'group_node'

.. py:class:: EnumData(member: enum.Enum, *args, **kwargs)
   :canonical: aiida.orm.nodes.data.enum.EnumData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Data plugin that allows to easily wrap an :class:`enum.Enum` member.

   The enum member is stored in the database by storing the value, name and the identifier (string that represents the
   class of the enumeration) in the ``KEY_NAME``, ``KEY_VALUE`` and ``KEY_IDENTIFIER`` attribute, respectively. The
   original enum member can be reconstructured from the (loaded) node through the ``get_member`` method. The enum
   itself can be retrieved from the ``get_enum`` method. Like a normal enum member, the ``EnumData`` plugin provides
   the ``name`` and ``value`` properties which return the name and value of the enum member, respectively.

   .. rubric:: Initialization

   Construct the node for the to enum member that is to be wrapped.

   .. py:attribute:: KEY_NAME
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_NAME
      :value: 'name'

   .. py:attribute:: KEY_VALUE
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_VALUE
      :value: 'value'

   .. py:attribute:: KEY_IDENTIFIER
      :canonical: aiida.orm.nodes.data.enum.EnumData.KEY_IDENTIFIER
      :value: 'identifier'

   .. py:property:: name
      :canonical: aiida.orm.nodes.data.enum.EnumData.name
      :type: str

      Return the name of the enum member.

   .. py:property:: value
      :canonical: aiida.orm.nodes.data.enum.EnumData.value
      :type: typing.Any

      Return the value of the enum member.

   .. py:method:: get_enum() -> typing.Type[aiida.orm.nodes.data.enum.EnumType]
      :canonical: aiida.orm.nodes.data.enum.EnumData.get_enum

      Return the enum class reconstructed from the serialized identifier stored in the database.

      :raises `ImportError`: if the enum class represented by the stored identifier cannot be imported.

   .. py:method:: get_member() -> aiida.orm.nodes.data.enum.EnumType
      :canonical: aiida.orm.nodes.data.enum.EnumData.get_member

      Return the enum member reconstructed from the serialized data stored in the database.

      For the enum member to be successfully reconstructed, the class of course has to still be importable and its
      implementation should not have changed since the node was stored. That is to say, the value of the member when
      it was stored, should still be a valid value for the enum class now.

      :raises `ImportError`: if the enum class represented by the stored identifier cannot be imported.
      :raises `ValueError`: if the stored enum member value is no longer valid for the imported enum class.

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.orm.nodes.data.enum.EnumData.__eq__

      Return whether the other object is equivalent to ourselves.

.. py:class:: Float
   :canonical: aiida.orm.nodes.data.float.Float

   Bases: :py:obj:`aiida.orm.nodes.data.numeric.NumericType`

   `Data` sub class to represent a float value.

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.float.Float._type
      :value: None

.. py:class:: FolderData(**kwargs)
   :canonical: aiida.orm.nodes.data.folder.FolderData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   `Data` sub class to represent a folder on a file system.

   .. rubric:: Initialization

   Construct a new `FolderData` to which any files and folders can be added.

   Use the `tree` keyword to simply wrap a directory:

       folder = FolderData(tree='/absolute/path/to/directory')

   Alternatively, one can construct the node first and then use the various repository methods to add objects:

       folder = FolderData()
       folder.put_object_from_tree('/absolute/path/to/directory')
       folder.put_object_from_filepath('/absolute/path/to/file.txt')
       folder.put_object_from_filelike(filelike_object)

   :param tree: absolute path to a folder to wrap
   :type tree: str

.. py:class:: Group(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.Group

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendGroup`\ , :py:obj:`aiida.orm.groups.GroupCollection`\ ]

   An AiiDA ORM implementation of group of nodes.

   .. rubric:: Initialization

   Create a new group. Either pass a dbgroup parameter, to reload
   a group from the DB (and then, no further parameters are allowed),
   or pass the parameters for the Group creation.

   :param label: The group label, required on creation
   :param description: The group description (by default, an empty string)
   :param user: The owner of the group (by default, the automatic user)
   :param type_string: a string identifying the type of group (by default,
       an empty string, indicating an user-defined group.

   .. py:attribute:: _type_string
      :canonical: aiida.orm.groups.Group._type_string
      :type: typing.ClassVar[typing.Optional[str]]
      :value: None

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.groups.Group._CLS_COLLECTION
      :value: None

   .. py:method:: base() -> aiida.orm.groups.GroupBase
      :canonical: aiida.orm.groups.Group.base

      Return the group base namespace.

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.groups.Group.__repr__

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.groups.Group.__str__

   .. py:method:: store() -> aiida.orm.groups.SelfType
      :canonical: aiida.orm.groups.Group.store

      Verify that the group is allowed to be stored, which is the case along as `type_string` is set.

   .. py:method:: entry_point() -> typing.Optional[aiida.plugins.entry_point.EntryPoint]
      :canonical: aiida.orm.groups.Group.entry_point

      Return the entry point associated this group type.

      :return: the associated entry point or ``None`` if it isn't known.

   .. py:property:: uuid
      :canonical: aiida.orm.groups.Group.uuid
      :type: str

      Return the UUID for this group.

      This identifier is unique across all entities types and backend instances.

      :return: the entity uuid

   .. py:property:: label
      :canonical: aiida.orm.groups.Group.label
      :type: str

      :return: the label of the group as a string

   .. py:property:: description
      :canonical: aiida.orm.groups.Group.description
      :type: str

      :return: the description of the group as a string

   .. py:property:: type_string
      :canonical: aiida.orm.groups.Group.type_string
      :type: str

      :return: the string defining the type of the group

   .. py:property:: user
      :canonical: aiida.orm.groups.Group.user
      :type: aiida.orm.User

      :return: the user associated with this group

   .. py:method:: count() -> int
      :canonical: aiida.orm.groups.Group.count

      Return the number of entities in this group.

      :return: integer number of entities contained within the group

   .. py:property:: nodes
      :canonical: aiida.orm.groups.Group.nodes
      :type: aiida.orm.convert.ConvertIterator

      Return a generator/iterator that iterates over all nodes and returns
      the respective AiiDA subclasses of Node, and also allows to ask for
      the number of nodes in the group using len().

   .. py:property:: is_empty
      :canonical: aiida.orm.groups.Group.is_empty
      :type: bool

      Return whether the group is empty, i.e. it does not contain any nodes.

      :return: True if it contains no nodes, False otherwise

   .. py:method:: clear() -> None
      :canonical: aiida.orm.groups.Group.clear

      Remove all the nodes from this group.

   .. py:method:: add_nodes(nodes: typing.Union[aiida.orm.nodes.Node, typing.Sequence[aiida.orm.nodes.Node]]) -> None
      :canonical: aiida.orm.groups.Group.add_nodes

      Add a node or a set of nodes to the group.

      :note: all the nodes *and* the group itself have to be stored.

      :param nodes: a single `Node` or a list of `Nodes`

   .. py:method:: remove_nodes(nodes: typing.Union[aiida.orm.nodes.Node, typing.Sequence[aiida.orm.nodes.Node]]) -> None
      :canonical: aiida.orm.groups.Group.remove_nodes

      Remove a node or a set of nodes to the group.

      :note: all the nodes *and* the group itself have to be stored.

      :param nodes: a single `Node` or a list of `Nodes`

   .. py:method:: is_user_defined() -> bool
      :canonical: aiida.orm.groups.Group.is_user_defined

      :return: True if the group is user defined, False otherwise

   .. py:attribute:: _deprecated_extra_methods
      :canonical: aiida.orm.groups.Group._deprecated_extra_methods
      :value: None

   .. py:method:: __getattr__(name: str) -> typing.Any
      :canonical: aiida.orm.groups.Group.__getattr__

      This method is called when an extras is not found in the instance.

      It allows for the handling of deprecated mixin methods.

.. py:class:: GroupEntityLoader
   :canonical: aiida.orm.utils.loaders.GroupEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   Loader for the `Group` entity and sub classes.

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.GroupEntityLoader.orm_base_class

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.GroupEntityLoader._get_query_builder_label_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance that should retrieve the entity corresponding to the identifier
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

.. py:class:: ImportGroup(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.ImportGroup

   Bases: :py:obj:`aiida.orm.groups.Group`

   Group to be used to contain all nodes from an export archive that has been imported.

   .. rubric:: Initialization

   Create a new group. Either pass a dbgroup parameter, to reload
   a group from the DB (and then, no further parameters are allowed),
   or pass the parameters for the Group creation.

   :param label: The group label, required on creation
   :param description: The group description (by default, an empty string)
   :param user: The owner of the group (by default, the automatic user)
   :param type_string: a string identifying the type of group (by default,
       an empty string, indicating an user-defined group.

.. py:class:: InstalledCode(computer: aiida.orm.Computer, filepath_executable: str, **kwargs)
   :canonical: aiida.orm.nodes.data.code.installed.InstalledCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.legacy.Code`

   Data plugin representing an executable code on a remote computer.

   .. rubric:: Initialization

   Construct a new instance.

   :param computer: The remote computer on which the executable is located.
   :param filepath_executable: The absolute filepath of the executable on the remote computer.

   .. py:attribute:: _KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :type: str
      :value: 'filepath_executable'

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._validate

      Validate the instance by checking that a computer has been defined.

      :raises :class:`aiida.common.exceptions.ValidationError`: If the state of the node is invalid.

   .. py:method:: validate_filepath_executable()
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.validate_filepath_executable

      Validate the ``filepath_executable`` attribute.

      Checks whether the executable exists on the remote computer if a transport can be opened to it. This method
      is intentionally not called in ``_validate`` as to allow the creation of ``Code`` instances whose computers can
      not yet be connected to and as to not require the overhead of opening transports in storing a new code.

      :raises `~aiida.common.exceptions.ValidationError`: if no transport could be opened or if the defined executable
          does not exist on the remote computer.

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.can_run_on_computer

      Return whether the code can run on a given computer.

      :param computer: The computer.
      :return: ``True`` if the provided computer is the same as the one configured for this code.

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.get_executable

      Return the executable that the submission script should execute to run the code.

      :return: The executable to be called in the submission script.

   .. py:property:: computer
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.computer
      :type: aiida.orm.Computer

      Return the computer of this code.

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.full_label
      :type: str

      Return the full label of this code.

      The full label can be just the label itself but it can be something else. However, it at the very least has to
      include the label of the code.

      :return: The full label of the code.

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.filepath_executable
      :type: pathlib.PurePosixPath

      Return the absolute filepath of the executable that this code represents.

      :return: The absolute filepath of the executable.

   .. py:method:: cli_validate_label_uniqueness(ctx, _, value)
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode.cli_validate_label_uniqueness
      :staticmethod:

      Validate the uniqueness of the label of the code.

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.installed.InstalledCode._get_cli_options
      :classmethod:

      Return the CLI options that would allow to create an instance of this class.

.. py:class:: Int
   :canonical: aiida.orm.nodes.data.int.Int

   Bases: :py:obj:`aiida.orm.nodes.data.numeric.NumericType`

   `Data` sub class to represent an integer value.

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.int.Int._type
      :value: None

.. py:class:: JsonableData(obj: aiida.orm.nodes.data.jsonable.JsonSerializableProtocol, *args, **kwargs)
   :canonical: aiida.orm.nodes.data.jsonable.JsonableData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Data plugin that allows to easily wrap objects that are JSON-able.

   Any class that implements the ``as_dict`` method, returning a dictionary that is a JSON serializable representation
   of the object, can be wrapped and stored by this data plugin.

   As an example, take the ``Molecule`` class of the ``pymatgen`` library, which respects the spec described above. To
   store an instance as a ``JsonableData`` simply pass an instance as an argument to the constructor as follows::

       from pymatgen.core import Molecule
       molecule = Molecule(['H']. [0, 0, 0])
       node = JsonableData(molecule)
       node.store()

   Since ``Molecule.as_dict`` returns a dictionary that is JSON-serializable, the data plugin will call it and store
   the dictionary as the attributes of the ``JsonableData`` node in the database.

   .. note:: A JSON-serializable dictionary means a dictionary that when passed to ``json.dumps`` does not except but
       produces a valid JSON string representation of the dictionary.

   If the wrapped class implements a class-method ``from_dict``, the wrapped instance can easily be recovered from a
   previously stored node that was optionally loaded from the database. The ``from_dict`` method should simply accept
   a single argument which is the dictionary that is returned by the ``as_dict`` method. If this criteria is satisfied,
   an instance wrapped and stored in a ``JsonableData`` node can be recovered through the ``obj`` property::

       loaded = load_node(node.pk)
       molecule = loaded.obj

   Of course, this requires that the class of the originally wrapped instance can be imported in the current
   environment, or an ``ImportError`` will be raised.

   .. rubric:: Initialization

   Construct the node for the to be wrapped object.

   .. py:method:: _deserialize_float_constants(data: typing.Any)
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData._deserialize_float_constants
      :classmethod:

      Deserialize the contents of a dictionary ``data`` deserializing infinity and NaN string constants.

      The ``data`` dictionary is recursively checked for the ``Infinity``, ``-Infinity`` and ``NaN`` strings, which
      are the Javascript string equivalents to the Python ``float('inf')``, ``-float('inf')`` and ``float('nan')``
      float constants. If one of the strings is encountered, the Python float constant is returned and otherwise the
      original value is returned.

   .. py:method:: _get_object() -> aiida.orm.nodes.data.jsonable.JsonSerializableProtocol
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData._get_object

      Return the cached wrapped object.

      .. note:: If the object is not yet present in memory, for example if the node was loaded from the database,
          the object will first be reconstructed from the state stored in the node attributes.


   .. py:property:: obj
      :canonical: aiida.orm.nodes.data.jsonable.JsonableData.obj
      :type: aiida.orm.nodes.data.jsonable.JsonSerializableProtocol

      Return the wrapped object.

      .. note:: This property caches the deserialized object, this means that when the node is loaded from the
          database, the object is deserialized only once and stored in memory as an attribute. Subsequent calls will
          simply return this cached object and not reload it from the database. This is fine, since nodes that are
          loaded from the database are by definition stored and therefore immutable, making it safe to assume that the
          object that is represented can not change. Note, however, that the caching also applies to unstored nodes.
          That means that manually changing the attributes of an unstored ``JsonableData`` can lead to inconsistencies
          with the object returned by this property.


.. py:class:: Kind(**kwargs)
   :canonical: aiida.orm.nodes.data.structure.Kind

   This class contains the information about the species (kinds) of the system.

   It can be a single atom, or an alloy, or even contain vacancies.

   .. rubric:: Initialization

   Create a site.
   One can either pass:

   :param raw: the raw python dictionary that will be converted to a
          Kind object.
   :param ase: an ase Atom object
   :param kind: a Kind object (to get a copy)

   Or alternatively the following parameters:

   :param symbols: a single string for the symbol of this site, or a list
              of symbol strings
   :param weights: (optional) the weights for each atomic species of
              this site.
              If only a single symbol is provided, then this value is
              optional and the weight is set to 1.
   :param mass: (optional) the mass for this site in atomic mass units.
              If not provided, the mass is set by the
              self.reset_mass() function.
   :param name: a string that uniquely identifies the kind, and that
              is used to identify the sites.

   .. py:method:: get_raw()
      :canonical: aiida.orm.nodes.data.structure.Kind.get_raw

      Return the raw version of the site, mapped to a suitable dictionary.
      This is the format that is actually used to store each kind of the
      structure in the DB.

      :return: a python dictionary with the kind.

   .. py:method:: reset_mass()
      :canonical: aiida.orm.nodes.data.structure.Kind.reset_mass

      Reset the mass to the automatic calculated value.

      The mass can be set manually; by default, if not provided,
      it is the mass of the constituent atoms, weighted with their
      weight (after the weight has been normalized to one to take
      correctly into account vacancies).

      This function uses the internal _symbols and _weights values and
      thus assumes that the values are validated.

      It sets the mass to None if the sum of weights is zero.

   .. py:property:: name
      :canonical: aiida.orm.nodes.data.structure.Kind.name

      Return the name of this kind.
      The name of a kind is used to identify the species of a site.

      :return: a string

   .. py:method:: set_automatic_kind_name(tag=None)
      :canonical: aiida.orm.nodes.data.structure.Kind.set_automatic_kind_name

      Set the type to a string obtained with the symbols appended one
      after the other, without spaces, in alphabetical order;
      if the site has a vacancy, a X is appended at the end too.

   .. py:method:: compare_with(other_kind)
      :canonical: aiida.orm.nodes.data.structure.Kind.compare_with

      Compare with another Kind object to check if they are different.

      .. note:: This does NOT check the 'type' attribute. Instead, it compares
          (with reasonable thresholds, where applicable): the mass, and the list
          of symbols and of weights. Moreover, it compares the
          ``_internal_tag``, if defined (at the moment, defined automatically
          only when importing the Kind from ASE, if the atom has a non-zero tag).
          Note that the _internal_tag is only used while the class is loaded,
          but is not persisted on the database.

      :return: A tuple with two elements. The first one is True if the two sites
          are 'equivalent' (same mass, symbols and weights), False otherwise.
          The second element of the tuple is a string,
          which is either None (if the first element was True), or contains
          a 'human-readable' description of the first difference encountered
          between the two sites.

   .. py:property:: mass
      :canonical: aiida.orm.nodes.data.structure.Kind.mass

      The mass of this species kind.

      :return: a float

   .. py:property:: weights
      :canonical: aiida.orm.nodes.data.structure.Kind.weights

      Weights for this species kind. Refer also to
      :func:validate_symbols_tuple for the validation rules on the weights.

   .. py:method:: get_symbols_string()
      :canonical: aiida.orm.nodes.data.structure.Kind.get_symbols_string

      Return a string that tries to match as good as possible the symbols
      of this kind. If there is only one symbol (no alloy) with 100%
      occupancy, just returns the symbol name. Otherwise, groups the full
      string in curly brackets, and try to write also the composition
      (with 2 precision only).

      .. note:: If there is a vacancy (sum of weights<1), we indicate it
          with the X symbol followed by 1-sum(weights) (still with 2
          digits precision, so it can be 0.00)

      .. note:: Note the difference with respect to the symbols and the
          symbol properties!

   .. py:property:: symbol
      :canonical: aiida.orm.nodes.data.structure.Kind.symbol

      If the kind has only one symbol, return it; otherwise, raise a
      ValueError.

   .. py:property:: symbols
      :canonical: aiida.orm.nodes.data.structure.Kind.symbols

      List of symbols for this site. If the site is a single atom,
      pass a list of one element only, or simply the string for that atom.
      For alloys, a list of elements.

      .. note:: Note that if you change the list of symbols, the kind
          name remains unchanged.

   .. py:method:: set_symbols_and_weights(symbols, weights)
      :canonical: aiida.orm.nodes.data.structure.Kind.set_symbols_and_weights

      Set the chemical symbols and the weights for the site.

      .. note:: Note that the kind name remains unchanged.

   .. py:property:: is_alloy
      :canonical: aiida.orm.nodes.data.structure.Kind.is_alloy

      Return whether the Kind is an alloy, i.e. contains more than one element

      :return: boolean, True if the kind has more than one element, False otherwise.

   .. py:property:: has_vacancies
      :canonical: aiida.orm.nodes.data.structure.Kind.has_vacancies

      Return whether the Kind contains vacancies, i.e. when the sum of the weights is less than one.

      .. note:: the property uses the internal variable `_SUM_THRESHOLD` as a threshold.

      :return: boolean, True if the sum of the weights is less than one, False otherwise

   .. py:method:: __repr__()
      :canonical: aiida.orm.nodes.data.structure.Kind.__repr__

      Return repr(self).

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.structure.Kind.__str__

      Return str(self).

.. py:class:: KpointsData
   :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   Class to handle array of kpoints in the Brillouin zone. Provide methods to
   generate either user-defined k-points or path of k-points along symmetry
   lines.
   Internally, all k-points are defined in terms of crystal (fractional)
   coordinates.
   Cell and lattice vector coordinates are in Angstroms, reciprocal lattice
   vectors in Angstrom^-1 .
   :note: The methods setting and using the Bravais lattice info assume the
   PRIMITIVE unit cell is provided in input to the set_cell or
   set_cell_from_structure methods.

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_description

      Returns a string with infos retrieved from  kpoints node's properties.
      :param node:
      :return: retstr

   .. py:property:: cell
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.cell

      The crystal unit cell. Rows are the crystal vectors in Angstroms.
      :return: a 3x3 numpy.array

   .. py:method:: _set_cell(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_cell

      Validate if 'value' is a allowed crystal unit cell
      :param value: something compatible with a 3x3 tuple of floats

   .. py:property:: pbc
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.pbc

      The periodic boundary conditions along the vectors a1,a2,a3.

      :return: a tuple of three booleans, each one tells if there are periodic
          boundary conditions for the i-th real-space direction (i=1,2,3)

   .. py:method:: _set_pbc(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_pbc

      validate the pbc, then store them

   .. py:property:: labels
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.labels

      Labels associated with the list of kpoints.
      List of tuples with kpoint index and kpoint name: ``[(0,'G'),(13,'M'),...]``

   .. py:method:: _set_labels(value)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._set_labels

      set label names. Must pass in input a list like: ``[[0,'X'],[34,'L'],... ]``

   .. py:method:: _change_reference(kpoints, to_cartesian=True)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._change_reference

      Change reference system, from cartesian to crystal coordinates (units of b1,b2,b3) or viceversa.
      :param kpoints: a list of (3) point coordinates
      :return kpoints: a list of (3) point coordinates in the new reference

   .. py:method:: set_cell_from_structure(structuredata)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell_from_structure

      Set a cell to be used for symmetry analysis from an AiiDA structure.
      Inherits both the cell and the pbc's.
      To set manually a cell, use "set_cell"

      :param structuredata: an instance of StructureData

   .. py:method:: set_cell(cell, pbc=None)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_cell

      Set a cell to be used for symmetry analysis.
      To set a cell from an AiiDA structure, use "set_cell_from_structure".

      :param cell: 3x3 matrix of cell vectors. Orientation: each row
                   represent a lattice vector. Units are Angstroms.
      :param pbc: list of 3 booleans, True if in the nth crystal direction the
                  structure is periodic. Default = [True,True,True]

   .. py:property:: reciprocal_cell
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.reciprocal_cell

      Compute reciprocal cell from the internally set cell.

      :returns: reciprocal cell in units of 1/Angstrom with cell vectors stored as rows.
          Use e.g. reciprocal_cell[0] to access the first reciprocal cell vector.

   .. py:method:: set_kpoints_mesh(mesh, offset=None)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh

      Set KpointsData to represent a uniformily spaced mesh of kpoints in the
      Brillouin zone. This excludes the possibility of set/get kpoints

      :param mesh: a list of three integers, representing the size of the
          kpoint mesh along b1,b2,b3.
      :param offset: (optional) a list of three floats between 0 and 1.
          [0.,0.,0.] is Gamma centered mesh
          [0.5,0.5,0.5] is half shifted
          [1.,1.,1.] by periodicity should be equivalent to [0.,0.,0.]
          Default = [0.,0.,0.].

   .. py:method:: get_kpoints_mesh(print_list=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints_mesh

      Get the mesh of kpoints.

      :param print_list: default=False. If True, prints the mesh of kpoints as a list

      :raise AttributeError: if no mesh has been set
      :return mesh,offset: (if print_list=False) a list of 3 integers and a list of three
              floats 0<x<1, representing the mesh and the offset of kpoints
      :return kpoints: (if print_list = True) an explicit list of kpoints coordinates,
              similar to what returned by get_kpoints()

   .. py:method:: set_kpoints_mesh_from_density(distance, offset=None, force_parity=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints_mesh_from_density

      Set a kpoints mesh using a kpoints density, expressed as the maximum
      distance between adjacent points along a reciprocal axis

      :param distance: distance (in 1/Angstrom) between adjacent
          kpoints, i.e. the number of kpoints along each reciprocal
          axis i is :math:`|b_i|/distance`
          where :math:`|b_i|` is the norm of the reciprocal cell vector.
      :param offset: (optional) a list of three floats between 0 and 1.
          [0.,0.,0.] is Gamma centered mesh
          [0.5,0.5,0.5] is half shifted
          Default = [0.,0.,0.].
      :param force_parity: (optional) if True, force each integer in the mesh
          to be even (except for the non-periodic directions).

      :note: a cell should be defined first.
      :note: the number of kpoints along non-periodic axes is always 1.

   .. py:property:: _dimension
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._dimension

      Dimensionality of the structure, found from its pbc (i.e. 1 if it's a 1D
      structure, 2 if its 2D, 3 if it's 3D ...).
      :return dimensionality: 0, 1, 2 or 3
      :note: will return 3 if pbc has not been set beforehand

   .. py:method:: _validate_kpoints_weights(kpoints, weights)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData._validate_kpoints_weights

      Validate the list of kpoints and of weights before storage.
      Kpoints and weights must be convertible respectively to an array of
      N x dimension and N floats

   .. py:method:: set_kpoints(kpoints, cartesian=False, labels=None, weights=None, fill_values=0)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.set_kpoints

      Set the list of kpoints. If a mesh has already been stored, raise a
      ModificationNotAllowed

      :param kpoints: a list of kpoints, each kpoint being a list of one, two
          or three coordinates, depending on self.pbc: if structure is 1D
          (only one True in self.pbc) one allows singletons or scalars for
          each k-point, if it's 2D it can be a length-2 list, and in all
          cases it can be a length-3 list.
          Examples:

              * [[0.,0.,0.],[0.1,0.1,0.1],...] for 1D, 2D or 3D
              * [[0.,0.],[0.1,0.1,],...] for 1D or 2D
              * [[0.],[0.1],...] for 1D
              * [0., 0.1, ...] for 1D (list of scalars)

          For 0D (all pbc are False), the list can be any of the above
          or empty - then only Gamma point is set.
          The value of k for the non-periodic dimension(s) is set by
          fill_values
      :param cartesian: if True, the coordinates given in input are treated
          as in cartesian units. If False, the coordinates are crystal,
          i.e. in units of b1,b2,b3. Default = False
      :param labels: optional, the list of labels to be set for some of the
          kpoints. See labels for more info
      :param weights: optional, a list of floats with the weight associated
          to the kpoint list
      :param fill_values: scalar to be set to all
          non-periodic dimensions (indicated by False in self.pbc), or list of
          values for each of the non-periodic dimensions.

   .. py:method:: get_kpoints(also_weights=False, cartesian=False)
      :canonical: aiida.orm.nodes.data.array.kpoints.KpointsData.get_kpoints

      Return the list of kpoints

      :param also_weights: if True, returns also the list of weights.
          Default = False
      :param cartesian: if True, returns points in cartesian coordinates,
          otherwise, returns in crystal coordinates. Default = False.

.. py:class:: LinkManager(link_triples: typing.List[aiida.orm.utils.links.LinkTriple])
   :canonical: aiida.orm.utils.links.LinkManager

   Class to convert a list of LinkTriple tuples into an iterator.

   It defines convenience methods to retrieve certain subsets of LinkTriple while checking for consistency.
   For example::

       LinkManager.one(): returns the only entry in the list or it raises an exception
       LinkManager.first(): returns the first entry from the list
       LinkManager.all(): returns all entries from list

   The methods `all_nodes` and `all_link_labels` are syntactic sugar wrappers around `all` to get a list of only the
   incoming nodes or link labels, respectively.

   .. rubric:: Initialization

   Initialise the collection.

   .. py:method:: __iter__() -> typing.Iterator[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.__iter__

      Return an iterator of LinkTriple instances.

      :return: iterator of LinkTriple instances

   .. py:method:: __next__() -> typing.Generator[aiida.orm.utils.links.LinkTriple, None, None]
      :canonical: aiida.orm.utils.links.LinkManager.__next__

      Return the next element in the iterator.

      :return: LinkTriple

   .. py:method:: __bool__()
      :canonical: aiida.orm.utils.links.LinkManager.__bool__

   .. py:method:: next() -> typing.Generator[aiida.orm.utils.links.LinkTriple, None, None]
      :canonical: aiida.orm.utils.links.LinkManager.next

      Return the next element in the iterator.

      :return: LinkTriple

   .. py:method:: one() -> aiida.orm.utils.links.LinkTriple
      :canonical: aiida.orm.utils.links.LinkManager.one

      Return a single entry from the iterator.

      If the iterator contains no or more than one entry, an exception will be raised
      :return: LinkTriple instance
      :raises ValueError: if the iterator contains anything but one entry

   .. py:method:: first() -> typing.Optional[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.first

      Return the first entry from the iterator.

      :return: LinkTriple instance or None if no entries were matched

   .. py:method:: all() -> typing.List[aiida.orm.utils.links.LinkTriple]
      :canonical: aiida.orm.utils.links.LinkManager.all

      Return all entries from the list.

      :return: list of LinkTriple instances

   .. py:method:: all_nodes() -> typing.List[aiida.orm.Node]
      :canonical: aiida.orm.utils.links.LinkManager.all_nodes

      Return a list of all nodes.

      :return: list of nodes

   .. py:method:: all_link_pairs() -> typing.List[aiida.orm.utils.links.LinkPair]
      :canonical: aiida.orm.utils.links.LinkManager.all_link_pairs

      Return a list of all link pairs.

      :return: list of LinkPair instances

   .. py:method:: all_link_labels() -> typing.List[str]
      :canonical: aiida.orm.utils.links.LinkManager.all_link_labels

      Return a list of all link labels.

      :return: list of link labels

   .. py:method:: get_node_by_label(label: str) -> aiida.orm.Node
      :canonical: aiida.orm.utils.links.LinkManager.get_node_by_label

      Return the node from list for given label.

      :return: node that corresponds to the given label
      :raises aiida.common.NotExistent: if the label is not present among the link_triples

   .. py:method:: nested(sort=True)
      :canonical: aiida.orm.utils.links.LinkManager.nested

      Construct (nested) dictionary of matched nodes that mirrors the original nesting of link namespaces.

      Process input and output namespaces can be nested, however the link labels that represent them in the database
      have a flat hierarchy, and so the link labels are flattened representations of the nested namespaces.
      This function reconstructs the original node nesting based on the flattened links.

      :return: dictionary of nested namespaces
      :raises KeyError: if there are duplicate link labels in a namespace

.. py:class:: LinkPair
   :canonical: aiida.orm.utils.links.LinkPair

   Bases: :py:obj:`typing.NamedTuple`

   .. py:attribute:: link_type
      :canonical: aiida.orm.utils.links.LinkPair.link_type
      :type: aiida.common.links.LinkType
      :value: None

   .. py:attribute:: link_label
      :canonical: aiida.orm.utils.links.LinkPair.link_label
      :type: str
      :value: None

.. py:class:: LinkTriple
   :canonical: aiida.orm.utils.links.LinkTriple

   Bases: :py:obj:`typing.NamedTuple`

   .. py:attribute:: node
      :canonical: aiida.orm.utils.links.LinkTriple.node
      :type: aiida.orm.Node
      :value: None

   .. py:attribute:: link_type
      :canonical: aiida.orm.utils.links.LinkTriple.link_type
      :type: aiida.common.links.LinkType
      :value: None

   .. py:attribute:: link_label
      :canonical: aiida.orm.utils.links.LinkTriple.link_label
      :type: str
      :value: None

.. py:class:: List(value=None, **kwargs)
   :canonical: aiida.orm.nodes.data.list.List

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`, :py:obj:`collections.abc.MutableSequence`

   `Data` sub class to represent a list.

   .. rubric:: Initialization

   Initialise a ``List`` node instance.

   :param value: list to initialise the ``List`` node from

   .. py:attribute:: _LIST_KEY
      :canonical: aiida.orm.nodes.data.list.List._LIST_KEY
      :value: 'list'

   .. py:method:: __getitem__(item)
      :canonical: aiida.orm.nodes.data.list.List.__getitem__

   .. py:method:: __setitem__(key, value)
      :canonical: aiida.orm.nodes.data.list.List.__setitem__

   .. py:method:: __delitem__(key)
      :canonical: aiida.orm.nodes.data.list.List.__delitem__

   .. py:method:: __len__()
      :canonical: aiida.orm.nodes.data.list.List.__len__

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.list.List.__str__

      Return str(self).

   .. py:method:: __eq__(other)
      :canonical: aiida.orm.nodes.data.list.List.__eq__

      Return self==value.

   .. py:method:: append(value)
      :canonical: aiida.orm.nodes.data.list.List.append

      S.append(value) -- append value to the end of the sequence

   .. py:method:: extend(value)
      :canonical: aiida.orm.nodes.data.list.List.extend

      S.extend(iterable) -- extend sequence by appending elements from the iterable

   .. py:method:: insert(i, value)
      :canonical: aiida.orm.nodes.data.list.List.insert

      S.insert(index, value) -- insert value before index

   .. py:method:: remove(value)
      :canonical: aiida.orm.nodes.data.list.List.remove

      S.remove(value) -- remove first occurrence of value.
      Raise ValueError if the value is not present.

   .. py:method:: pop(**kwargs)
      :canonical: aiida.orm.nodes.data.list.List.pop

      Remove and return item at index (default last).

   .. py:method:: index(value)
      :canonical: aiida.orm.nodes.data.list.List.index

      Return first index of value..

   .. py:method:: count(value)
      :canonical: aiida.orm.nodes.data.list.List.count

      Return number of occurrences of value.

   .. py:method:: sort(key=None, reverse=False)
      :canonical: aiida.orm.nodes.data.list.List.sort

   .. py:method:: reverse()
      :canonical: aiida.orm.nodes.data.list.List.reverse

      S.reverse() -- reverse *IN PLACE*

   .. py:method:: get_list()
      :canonical: aiida.orm.nodes.data.list.List.get_list

      Return the contents of this node.

      :return: a list

   .. py:method:: set_list(data)
      :canonical: aiida.orm.nodes.data.list.List.set_list

      Set the contents of this node.

      :param data: the list to set

   .. py:method:: _using_list_reference()
      :canonical: aiida.orm.nodes.data.list.List._using_list_reference

      This function tells the class if we are using a list reference.  This
      means that calls to self.get_list return a reference rather than a copy
      of the underlying list and therefore self.set_list need not be called.
      This knwoledge is essential to make sure this class is performant.

      Currently the implementation assumes that if the node needs to be
      stored then it is using the attributes cache which is a reference.

      :return: True if using self.get_list returns a reference to the
          underlying sequence.  False otherwise.
      :rtype: bool

.. py:class:: Log(time: datetime.datetime, loggername: str, levelname: str, dbnode_id: int, message: str = '', metadata: typing.Optional[typing.Dict[str, typing.Any]] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.logs.Log

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendLog`\ , :py:obj:`aiida.orm.logs.LogCollection`\ ]

   An AiiDA Log entity.  Corresponds to a logged message against a particular AiiDA node.

   .. rubric:: Initialization

   Construct a new log

   :param time: time
   :param loggername: name of logger
   :param levelname: name of log level
   :param dbnode_id: id of database node
   :param message: log message
   :param metadata: metadata
   :param backend: database backend

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.logs.Log._CLS_COLLECTION
      :value: None

   .. py:property:: uuid
      :canonical: aiida.orm.logs.Log.uuid
      :type: str

      Return the UUID for this log.

      This identifier is unique across all entities types and backend instances.

      :return: the entity uuid

   .. py:property:: time
      :canonical: aiida.orm.logs.Log.time
      :type: datetime.datetime

      Get the time corresponding to the entry

      :return: The entry timestamp

   .. py:property:: loggername
      :canonical: aiida.orm.logs.Log.loggername
      :type: str

      The name of the logger that created this entry

      :return: The entry loggername

   .. py:property:: levelname
      :canonical: aiida.orm.logs.Log.levelname
      :type: str

      The name of the log level

      :return: The entry log level name

   .. py:property:: dbnode_id
      :canonical: aiida.orm.logs.Log.dbnode_id
      :type: int

      Get the id of the object that created the log entry

      :return: The id of the object that created the log entry

   .. py:property:: message
      :canonical: aiida.orm.logs.Log.message
      :type: str

      Get the message corresponding to the entry

      :return: The entry message

   .. py:property:: metadata
      :canonical: aiida.orm.logs.Log.metadata
      :type: typing.Dict[str, typing.Any]

      Get the metadata corresponding to the entry

      :return: The entry metadata

.. py:class:: Node(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.node.Node

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendNode`\ , :py:obj:`aiida.orm.nodes.node.NodeCollection`\ ]

   Base class for all nodes in AiiDA.

   Stores attributes starting with an underscore.

   Caches files and attributes before the first save, and saves everything
   only on store(). After the call to store(), attributes cannot be changed.

   Only after storing (or upon loading from uuid) extras can be modified
   and in this case they are directly set on the db.

   In the plugin, also set the _plugin_type_string, to be set in the DB in
   the 'type' field.

   .. rubric:: Initialization

   :param backend_entity: the backend model supporting this entity

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.nodes.node.Node._CLS_COLLECTION
      :value: None

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.node.Node._CLS_NODE_LINKS
      :value: None

   .. py:attribute:: _CLS_NODE_CACHING
      :canonical: aiida.orm.nodes.node.Node._CLS_NODE_CACHING
      :value: None

   .. py:attribute:: _plugin_type_string
      :canonical: aiida.orm.nodes.node.Node._plugin_type_string
      :type: typing.ClassVar[str]
      :value: None

   .. py:attribute:: _query_type_string
      :canonical: aiida.orm.nodes.node.Node._query_type_string
      :type: typing.ClassVar[str]
      :value: None

   .. py:attribute:: _logger
      :canonical: aiida.orm.nodes.node.Node._logger
      :type: typing.Optional[logging.Logger]
      :value: None

   .. py:attribute:: _updatable_attributes
      :canonical: aiida.orm.nodes.node.Node._updatable_attributes
      :type: typing.Tuple[str, ...]
      :value: None

   .. py:attribute:: _hash_ignored_attributes
      :canonical: aiida.orm.nodes.node.Node._hash_ignored_attributes
      :type: typing.Tuple[str, ...]
      :value: None

   .. py:attribute:: _cachable
      :canonical: aiida.orm.nodes.node.Node._cachable
      :value: False

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.node.Node._storable
      :value: False

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.node.Node._unstorable_message
      :value: 'only Data, WorkflowNode, CalculationNode or their subclasses can be stored'

   .. py:method:: base() -> aiida.orm.nodes.node.NodeBase
      :canonical: aiida.orm.nodes.node.Node.base

      Return the node base namespace.

   .. py:method:: _check_mutability_attributes(keys: typing.Optional[typing.List[str]] = None) -> None
      :canonical: aiida.orm.nodes.node.Node._check_mutability_attributes

      Check if the entity is mutable and raise an exception if not.

      This is called from `NodeAttributes` methods that modify the attributes.

      :param keys: the keys that will be mutated, or all if None

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.orm.nodes.node.Node.__eq__

      Fallback equality comparison by uuid (can be overwritten by specific types)

   .. py:method:: __hash__() -> int
      :canonical: aiida.orm.nodes.node.Node.__hash__

      Python-Hash: Implementation that is compatible with __eq__

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.nodes.node.Node.__repr__

      Return repr(self).

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.nodes.node.Node.__str__

      Return str(self).

   .. py:method:: __copy__()
      :canonical: aiida.orm.nodes.node.Node.__copy__

      Copying a Node is not supported in general, but only for the Data sub class.

   .. py:method:: __deepcopy__(memo)
      :canonical: aiida.orm.nodes.node.Node.__deepcopy__

      Deep copying a Node is not supported in general, but only for the Data sub class.

   .. py:method:: _validate() -> bool
      :canonical: aiida.orm.nodes.node.Node._validate

      Validate information stored in Node object.

      For the :py:class:`~aiida.orm.Node` base class, this check is always valid.
      Subclasses can override this method to perform additional checks
      and should usually call ``super()._validate()`` first!

      This method is called automatically before storing the node in the DB.
      Therefore, use :py:meth:`~aiida.orm.nodes.attributes.NodeAttributes.get()` and similar methods that
      automatically read either from the DB or from the internal attribute cache.

   .. py:method:: _validate_storability() -> None
      :canonical: aiida.orm.nodes.node.Node._validate_storability

      Verify that the current node is allowed to be stored.

      :raises `aiida.common.exceptions.StoringNotAllowed`: if the node does not match all requirements for storing

   .. py:method:: class_node_type() -> str
      :canonical: aiida.orm.nodes.node.Node.class_node_type

      Returns the node type of this node (sub) class.

   .. py:method:: entry_point() -> typing.Optional[aiida.plugins.entry_point.EntryPoint]
      :canonical: aiida.orm.nodes.node.Node.entry_point

      Return the entry point associated this node class.

      :return: the associated entry point or ``None`` if it isn't known.

   .. py:property:: logger
      :canonical: aiida.orm.nodes.node.Node.logger
      :type: typing.Optional[logging.Logger]

      Return the logger configured for this Node.

      :return: Logger object

   .. py:property:: uuid
      :canonical: aiida.orm.nodes.node.Node.uuid
      :type: str

      Return the node UUID.

      :return: the string representation of the UUID

   .. py:property:: node_type
      :canonical: aiida.orm.nodes.node.Node.node_type
      :type: str

      Return the node type.

      :return: the node type

   .. py:property:: process_type
      :canonical: aiida.orm.nodes.node.Node.process_type
      :type: typing.Optional[str]

      Return the node process type.

      :return: the process type

   .. py:property:: label
      :canonical: aiida.orm.nodes.node.Node.label
      :type: str

      Return the node label.

      :return: the label

   .. py:property:: description
      :canonical: aiida.orm.nodes.node.Node.description
      :type: str

      Return the node description.

      :return: the description

   .. py:property:: computer
      :canonical: aiida.orm.nodes.node.Node.computer
      :type: typing.Optional[aiida.orm.computers.Computer]

      Return the computer of this node.

   .. py:property:: user
      :canonical: aiida.orm.nodes.node.Node.user
      :type: aiida.orm.users.User

      Return the user of this node.

   .. py:property:: ctime
      :canonical: aiida.orm.nodes.node.Node.ctime
      :type: datetime.datetime

      Return the node ctime.

      :return: the ctime

   .. py:property:: mtime
      :canonical: aiida.orm.nodes.node.Node.mtime
      :type: datetime.datetime

      Return the node mtime.

      :return: the mtime

   .. py:method:: store_all(with_transaction: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node.store_all

      Store the node, together with all input links.

      Unstored nodes from cached incoming linkswill also be stored.

      :parameter with_transaction: if False, do not use a transaction because the caller will already have opened one.

   .. py:method:: store(with_transaction: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node.store

      Store the node in the database while saving its attributes and repository directory.

      After being called attributes cannot be changed anymore! Instead, extras can be changed only AFTER calling
      this store() function.

      :note: After successful storage, those links that are in the cache, and for which also the parent node is
          already stored, will be automatically stored. The others will remain unstored.

      :parameter with_transaction: if False, do not use a transaction because the caller will already have opened one.

   .. py:method:: _store(with_transaction: bool = True, clean: bool = True) -> aiida.orm.nodes.node.Node
      :canonical: aiida.orm.nodes.node.Node._store

      Store the node in the database while saving its attributes and repository directory.

      :param with_transaction: if False, do not use a transaction because the caller will already have opened one.
      :param clean: boolean, if True, will clean the attributes and extras before attempting to store

   .. py:method:: _verify_are_parents_stored() -> None
      :canonical: aiida.orm.nodes.node.Node._verify_are_parents_stored

      Verify that all `parent` nodes are already stored.

      :raise aiida.common.ModificationNotAllowed: if one of the source nodes of incoming links is not stored.

   .. py:method:: _store_from_cache(cache_node: aiida.orm.nodes.node.Node, with_transaction: bool) -> None
      :canonical: aiida.orm.nodes.node.Node._store_from_cache

      Store this node from an existing cache node.

      .. note::

          With the current implementation of the backend repository, which automatically deduplicates the content that
          it contains, we do not have to copy the contents of the source node. Since the content should be exactly
          equal, the repository will already contain it and there is nothing to copy. We simply replace the current
          ``repository`` instance with a clone of that of the source node, which does not actually copy any files.


   .. py:method:: _add_outputs_from_cache(cache_node: aiida.orm.nodes.node.Node) -> None
      :canonical: aiida.orm.nodes.node.Node._add_outputs_from_cache

      Replicate the output links and nodes from the cached node onto this node.

   .. py:method:: get_description() -> str
      :canonical: aiida.orm.nodes.node.Node.get_description

      Return a string with a description of the node.

      :return: a description string

   .. py:property:: is_valid_cache
      :canonical: aiida.orm.nodes.node.Node.is_valid_cache
      :type: bool

      Hook to exclude certain ``Node`` classes from being considered a valid cache.

      The base class assumes that all node instances are valid to cache from, unless the ``_VALID_CACHE_KEY`` extra
      has been set to ``False`` explicitly. Subclasses can override this property with more specific logic, but should
      probably also consider the value returned by this base class.

   .. py:attribute:: _deprecated_repo_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_repo_methods
      :value: None

   .. py:attribute:: _deprecated_attr_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_attr_methods
      :value: None

   .. py:attribute:: _deprecated_extra_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_extra_methods
      :value: None

   .. py:attribute:: _deprecated_comment_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_comment_methods
      :value: None

   .. py:attribute:: _deprecated_caching_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_caching_methods
      :value: None

   .. py:attribute:: _deprecated_links_methods
      :canonical: aiida.orm.nodes.node.Node._deprecated_links_methods
      :value: None

   .. py:method:: Collection()
      :canonical: aiida.orm.nodes.node.Node.Collection

      Return the collection type for this class.

      This used to be a class argument with the value ``NodeCollection``. The argument is deprecated and this property
      is here for backwards compatibility to print the deprecation warning.

   .. py:method:: __getattr__(name: str) -> typing.Any
      :canonical: aiida.orm.nodes.node.Node.__getattr__

      This method is called when an attribute is not found in the instance.

      It allows for the handling of deprecated mixin methods.

.. py:class:: NodeAttributes(node: aiida.orm.nodes.node.Node)
   :canonical: aiida.orm.nodes.attributes.NodeAttributes

   Interface to the attributes of a node instance.

   Attributes are a JSONable dictionary, stored on each node,
   allowing for arbitrary data to be stored by node subclasses (and thus data plugins).

   Once the node is stored, the attributes are generally deemed immutable
   (except for some updatable keys on process nodes, which can be mutated whilst the node is not "sealed").

   .. rubric:: Initialization

   Initialize the interface.

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.__contains__

      Check if the node contains an attribute with the given key.

   .. py:property:: all
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.all
      :type: typing.Dict[str, typing.Any]

      Return the complete attributes dictionary.

      .. warning:: While the entity is unstored, this will return references of the attributes on the database model,
          meaning that changes on the returned values (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          attributes will be a deep copy and mutations of the database attributes will have to go through the
          appropriate set methods. Therefore, once stored, retrieving a deep copy can be a heavy operation. If you
          only need the keys or some values, use the iterators `keys` and `items`, or the
          getters `get` and `get_many` instead.

      :return: the attributes as a dictionary

   .. py:method:: get(key: str, default=_NO_DEFAULT) -> typing.Any
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.get

      Return the value of an attribute.

      .. warning:: While the entity is unstored, this will return a reference of the attribute on the database model,
          meaning that changes on the returned value (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          attribute will be a deep copy and mutations of the database attributes will have to go through the
          appropriate set methods.

      :param key: name of the attribute
      :param default: return this value instead of raising if the attribute does not exist
      :return: the value of the attribute
      :raises AttributeError: if the attribute does not exist and no default is specified

   .. py:method:: get_many(keys: typing.List[str]) -> typing.List[typing.Any]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.get_many

      Return the values of multiple attributes.

      .. warning:: While the entity is unstored, this will return references of the attributes on the database model,
          meaning that changes on the returned values (if they are mutable themselves, e.g. a list or dictionary) will
          automatically be reflected on the database model as well. As soon as the entity is stored, the returned
          attributes will be a deep copy and mutations of the database attributes will have to go through the
          appropriate set methods. Therefore, once stored, retrieving a deep copy can be a heavy operation. If you
          only need the keys or some values, use the iterators `keys` and `items`, or the
          getters `get` and `get_many` instead.

      :param keys: a list of attribute names
      :return: a list of attribute values
      :raises AttributeError: if at least one attribute does not exist

   .. py:method:: set(key: str, value: typing.Any) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.set

      Set an attribute to the given value.

      :param key: name of the attribute
      :param value: value of the attribute
      :raise aiida.common.ValidationError: if the key is invalid, i.e. contains periods
      :raise aiida.common.ModificationNotAllowed: if the entity is stored

   .. py:method:: set_many(attributes: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.set_many

      Set multiple attributes.

      .. note:: This will override any existing attributes that are present in the new dictionary.

      :param attributes: a dictionary with the attributes to set
      :raise aiida.common.ValidationError: if any of the keys are invalid, i.e. contain periods
      :raise aiida.common.ModificationNotAllowed: if the entity is stored

   .. py:method:: reset(attributes: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.reset

      Reset the attributes.

      .. note:: This will completely clear any existing attributes and replace them with the new dictionary.

      :param attributes: a dictionary with the attributes to set
      :raise aiida.common.ValidationError: if any of the keys are invalid, i.e. contain periods
      :raise aiida.common.ModificationNotAllowed: if the entity is stored

   .. py:method:: delete(key: str) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.delete

      Delete an attribute.

      :param key: name of the attribute
      :raises AttributeError: if the attribute does not exist
      :raise aiida.common.ModificationNotAllowed: if the entity is stored

   .. py:method:: delete_many(keys: typing.List[str]) -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.delete_many

      Delete multiple attributes.

      :param keys: names of the attributes to delete
      :raises AttributeError: if at least one of the attribute does not exist
      :raise aiida.common.ModificationNotAllowed: if the entity is stored

   .. py:method:: clear() -> None
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.clear

      Delete all attributes.

   .. py:method:: items() -> typing.Iterable[typing.Tuple[str, typing.Any]]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.items

      Return an iterator over the attributes.

      :return: an iterator with attribute key value pairs

   .. py:method:: keys() -> typing.Iterable[str]
      :canonical: aiida.orm.nodes.attributes.NodeAttributes.keys

      Return an iterator over the attribute keys.

      :return: an iterator with attribute keys

.. py:class:: NodeEntityLoader
   :canonical: aiida.orm.utils.loaders.NodeEntityLoader

   Bases: :py:obj:`aiida.orm.utils.loaders.OrmEntityLoader`

   Loader for the `Node` entity and sub classes.

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.NodeEntityLoader.orm_base_class

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.NodeEntityLoader._get_query_builder_label_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance that should retrieve the entity corresponding to the identifier
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

.. py:class:: NodeLinksManager(node, link_type, incoming)
   :canonical: aiida.orm.utils.managers.NodeLinksManager

   A manager that allows to inspect, with tab-completion, nodes linked to a given one.
   See an example of its use in `CalculationNode.inputs`.

   .. rubric:: Initialization

   Initialise the link manager.

   :param node: the reference node object
   :param link_type: the link_type to inspect
   :param incoming: if True, inspect incoming links, otherwise inspect
       outgoing links

   .. py:attribute:: _namespace_separator
      :canonical: aiida.orm.utils.managers.NodeLinksManager._namespace_separator
      :value: '__'

   .. py:method:: _construct_attribute_dict(incoming)
      :canonical: aiida.orm.utils.managers.NodeLinksManager._construct_attribute_dict

      Construct an attribute dict from all links of the node, recreating nested namespaces from flat link labels.

      :param incoming: if True, inspect incoming links, otherwise inspect outgoing links.

   .. py:method:: _get_keys()
      :canonical: aiida.orm.utils.managers.NodeLinksManager._get_keys

      Return the valid link labels, used e.g. to make getattr() work

   .. py:method:: _get_node_by_link_label(label)
      :canonical: aiida.orm.utils.managers.NodeLinksManager._get_node_by_link_label

      Return the linked node with a given link label.

      Nested namespaces in link labels get represented by double underscores in the database. Up until now, the link
      manager didn't automatically unroll these again into nested namespaces and so a user was forced to pass the link
      with double underscores to dereference the corresponding node. For example, when used with the ``inputs``
      attribute of a ``ProcessNode`` one had to do:

          node.inputs.nested__sub__namespace

      Now it is possible to do

          node.inputs.nested.sub.namespace

      which is more intuitive since the double underscore replacement is just for the database and the user shouldn't
      even have to know about it. For compatibility we support the old version a bit longer and it will emit a
      deprecation warning.

      :param label: the link label connecting the current node to the node to get.

   .. py:method:: __dir__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__dir__

      Allow to list all valid input links

   .. py:method:: __iter__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__iter__

   .. py:method:: __getattr__(name)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__getattr__

      :param name: name of the attribute to be asked to the parser results.

   .. py:method:: __contains__(key)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__contains__

      Override the operator of the base class to emit deprecation warning if double underscore is used in key.

   .. py:method:: __getitem__(name)
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__getitem__

      interface to get to the parser results as a dictionary.

      :param name: name of the attribute to be asked to the parser results.

   .. py:method:: __str__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__str__

      Return a string representation of the manager

   .. py:method:: __repr__()
      :canonical: aiida.orm.utils.managers.NodeLinksManager.__repr__

      Return repr(self).

.. py:class:: NodeRepository(node: aiida.orm.nodes.node.Node)
   :canonical: aiida.orm.nodes.repository.NodeRepository

   Interface to the file repository of a node instance.

   This is the compatibility layer between the `Node` class and the `Repository` class. The repository in principle has
   no concept of immutability, so it is implemented here. Any mutating operations will raise a `ModificationNotAllowed`
   exception if the node is stored. Otherwise the operation is just forwarded to the repository instance.

   The repository instance keeps an internal mapping of the file hierarchy that it maintains, starting from an empty
   hierarchy if the instance was constructed normally, or from a specific hierarchy if reconstructred through the
   ``Repository.from_serialized`` classmethod. This is only the case for stored nodes, because unstored nodes do not
   have any files yet when they are constructed. Once the node get's stored, the repository is asked to serialize its
   metadata contents which is then stored in the ``repository_metadata`` field of the backend node.
   This layer explicitly does not update the metadata of the node on a mutation action.
   The reason is that for stored nodes these actions are anyway forbidden and for unstored nodes,
   the final metadata will be stored in one go, once the node is stored,
   so there is no need to keep updating the node metadata intermediately.
   Note that this does mean that ``repository_metadata`` does not give accurate information,
   as long as the node is not yet stored.

   .. rubric:: Initialization

   Construct a new instance of the repository interface.

   .. py:property:: metadata
      :canonical: aiida.orm.nodes.repository.NodeRepository.metadata
      :type: typing.Dict[str, typing.Any]

      Return the repository metadata, representing the virtual file hierarchy.

      Note, this is only accurate if the node is stored.

      :return: the repository metadata

   .. py:method:: _update_repository_metadata()
      :canonical: aiida.orm.nodes.repository.NodeRepository._update_repository_metadata

      Refresh the repository metadata of the node if it is stored.

   .. py:method:: _check_mutability()
      :canonical: aiida.orm.nodes.repository.NodeRepository._check_mutability

      Check if the node is mutable.

      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

   .. py:property:: _repository
      :canonical: aiida.orm.nodes.repository.NodeRepository._repository
      :type: aiida.repository.Repository

      Return the repository instance, lazily constructing it if necessary.

      .. note:: this property is protected because a node's repository should not be accessed outside of its scope.

      :return: the file repository instance.

   .. py:method:: _store() -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._store

      Store the repository in the backend.

   .. py:method:: _copy(repo: aiida.orm.nodes.repository.NodeRepository) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._copy

      Copy a repository from another instance.

      This is used when storing cached nodes.

      :param repo: the repository to clone.

   .. py:method:: _clone(repo: aiida.orm.nodes.repository.NodeRepository) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository._clone

      Clone the repository from another instance.

      This is used when cloning a node.

      :param repo: the repository to clone.

   .. py:method:: serialize() -> typing.Dict
      :canonical: aiida.orm.nodes.repository.NodeRepository.serialize

      Serialize the metadata of the repository content into a JSON-serializable format.

      :return: dictionary with the content metadata.

   .. py:method:: hash() -> str
      :canonical: aiida.orm.nodes.repository.NodeRepository.hash

      Generate a hash of the repository's contents.

      :return: the hash representing the contents of the repository.

   .. py:method:: list_objects(path: typing.Optional[str] = None) -> typing.List[aiida.repository.File]
      :canonical: aiida.orm.nodes.repository.NodeRepository.list_objects

      Return a list of the objects contained in this repository sorted by name, optionally in given sub directory.

      :param path: the relative path where to store the object in the repository.
      :return: a list of `File` named tuples representing the objects present in directory with the given key.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises NotADirectoryError: if the object at the given path is not a directory.

   .. py:method:: list_object_names(path: typing.Optional[str] = None) -> typing.List[str]
      :canonical: aiida.orm.nodes.repository.NodeRepository.list_object_names

      Return a sorted list of the object names contained in this repository, optionally in the given sub directory.

      :param path: the relative path where to store the object in the repository.
      :return: a list of `File` named tuples representing the objects present in directory with the given key.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises NotADirectoryError: if the object at the given path is not a directory.

   .. py:method:: open(path: str, mode='r') -> typing.Iterator[typing.Union[typing.BinaryIO, typing.TextIO]]
      :canonical: aiida.orm.nodes.repository.NodeRepository.open

      Open a file handle to an object stored under the given key.

      .. note:: this should only be used to open a handle to read an existing file. To write a new file use the method
          ``put_object_from_filelike`` instead.

      :param path: the relative path of the object within the repository.
      :return: yield a byte stream object.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be opened.

   .. py:method:: get_object(path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> aiida.repository.File
      :canonical: aiida.orm.nodes.repository.NodeRepository.get_object

      Return the object at the given path.

      :param path: the relative path where to store the object in the repository.
      :return: the `File` representing the object located at the given relative path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.

   .. py:method:: get_object_content(path: str, mode='r') -> typing.Union[str, bytes]
      :canonical: aiida.orm.nodes.repository.NodeRepository.get_object_content

      Return the content of a object identified by key.

      :param key: fully qualified identifier for the object within the repository.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be opened.

   .. py:method:: put_object_from_bytes(content: bytes, path: str) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_bytes

      Store the given content in the repository at the given path.

      :param path: the relative path where to store the object in the repository.
      :param content: the content to store.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileExistsError: if an object already exists at the given path.

   .. py:method:: put_object_from_filelike(handle: io.BufferedReader, path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_filelike

      Store the byte contents of a file in the repository.

      :param handle: filelike object with the byte content to be stored.
      :param path: the relative path where to store the object in the repository.
      :raises TypeError: if the path is not a string and relative path.
      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

   .. py:method:: put_object_from_file(filepath: str, path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_file

      Store a new object under `path` with contents of the file located at `filepath` on the local file system.

      :param filepath: absolute path of file whose contents to copy to the repository
      :param path: the relative path where to store the object in the repository.
      :raises TypeError: if the path is not a string and relative path, or the handle is not a byte stream.
      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

   .. py:method:: put_object_from_tree(filepath: str, path: typing.Optional[str] = None)
      :canonical: aiida.orm.nodes.repository.NodeRepository.put_object_from_tree

      Store the entire contents of `filepath` on the local file system in the repository with under given `path`.

      :param filepath: absolute path of the directory whose contents to copy to the repository.
      :param path: the relative path where to store the objects in the repository.
      :raises TypeError: if the path is not a string and relative path.
      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

   .. py:method:: walk(path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> typing.Iterable[typing.Tuple[pathlib.PurePosixPath, typing.List[str], typing.List[str]]]
      :canonical: aiida.orm.nodes.repository.NodeRepository.walk

      Walk over the directories and files contained within this repository.

      .. note:: the order of the dirname and filename lists that are returned is not necessarily sorted. This is in
          line with the ``os.walk`` implementation where the order depends on the underlying file system used.

      :param path: the relative path of the directory within the repository whose contents to walk.
      :return: tuples of root, dirnames and filenames just like ``os.walk``, with the exception that the root path is
          always relative with respect to the repository root, instead of an absolute path and it is an instance of
          ``pathlib.PurePosixPath`` instead of a normal string

   .. py:method:: glob() -> typing.Iterable[pathlib.PurePosixPath]
      :canonical: aiida.orm.nodes.repository.NodeRepository.glob

      Yield a recursive list of all paths (files and directories).

   .. py:method:: copy_tree(target: typing.Union[str, pathlib.Path], path: typing.Optional[aiida.orm.nodes.repository.FilePath] = None) -> None
      :canonical: aiida.orm.nodes.repository.NodeRepository.copy_tree

      Copy the contents of the entire node repository to another location on the local file system.

      :param target: absolute path of the directory where to copy the contents to.
      :param path: optional relative path whose contents to copy.

   .. py:method:: delete_object(path: str)
      :canonical: aiida.orm.nodes.repository.NodeRepository.delete_object

      Delete the object from the repository.

      :param key: fully qualified identifier for the object within the repository.
      :raises TypeError: if the path is not a string and relative path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be deleted.
      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

   .. py:method:: erase()
      :canonical: aiida.orm.nodes.repository.NodeRepository.erase

      Delete all objects from the repository.

      :raises `~aiida.common.exceptions.ModificationNotAllowed`: when the node is stored and therefore immutable.

.. py:class:: NumericType
   :canonical: aiida.orm.nodes.data.numeric.NumericType

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   Sub class of Data to store numbers, overloading common operators (``+``, ``*``, ...).

   .. py:method:: __add__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__add__

   .. py:method:: __radd__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__radd__

   .. py:method:: __sub__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__sub__

   .. py:method:: __rsub__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rsub__

   .. py:method:: __mul__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__mul__

   .. py:method:: __rmul__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rmul__

   .. py:method:: __div__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__div__

   .. py:method:: __rdiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rdiv__

   .. py:method:: __truediv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__truediv__

   .. py:method:: __rtruediv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rtruediv__

   .. py:method:: __floordiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__floordiv__

   .. py:method:: __rfloordiv__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rfloordiv__

   .. py:method:: __pow__(power)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__pow__

   .. py:method:: __lt__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__lt__

   .. py:method:: __le__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__le__

   .. py:method:: __gt__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__gt__

   .. py:method:: __ge__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__ge__

   .. py:method:: __mod__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__mod__

   .. py:method:: __rmod__(other)
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__rmod__

   .. py:method:: __float__()
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__float__

   .. py:method:: __int__()
      :canonical: aiida.orm.nodes.data.numeric.NumericType.__int__

.. py:class:: OrbitalData
   :canonical: aiida.orm.nodes.data.orbital.OrbitalData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Used for storing collections of orbitals, as well as
   providing methods for accessing them internally.

   .. py:method:: clear_orbitals()
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.clear_orbitals

      Remove all orbitals that were added to the class
      Cannot work if OrbitalData has been already stored

   .. py:method:: get_orbitals(**kwargs)
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.get_orbitals

      Returns all orbitals by default. If a site is provided, returns
      all orbitals cooresponding to the location of that site, additional
      arguments may be provided, which act as filters on the retrieved
      orbitals.

      :param site: if provided, returns all orbitals with position of site
      :kwargs: attributes than can filter the set of returned orbitals
      :return list_of_outputs: a list of orbitals

   .. py:method:: set_orbitals(orbitals)
      :canonical: aiida.orm.nodes.data.orbital.OrbitalData.set_orbitals

      Sets the orbitals into the database. Uses the orbital's inherent
      set_orbital_dict method to generate a orbital dict string.

      :param orbital: an orbital or list of orbitals to be set

.. py:function:: OrderSpecifier(field, direction)
   :canonical: aiida.orm.logs.OrderSpecifier

.. py:class:: OrmEntityLoader
   :canonical: aiida.orm.utils.loaders.OrmEntityLoader

   Base class for entity loaders.

   .. py:attribute:: label_ambiguity_breaker
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.label_ambiguity_breaker
      :value: '!'

   .. py:method:: orm_base_class()
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.orm_base_class
      :abstractmethod:

      Return the orm base class to which loaded entities should be mapped. Actual queries to load an entity
      may further narrow the query set by defining a more specific set of orm classes, as long as each of
      those is a strict sub class of the orm base class.

      :returns: the orm base class

   .. py:method:: _get_query_builder_label_identifier(identifier, classes, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_label_identifier
      :abstractmethod:
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a LABEL like identifier

      :param identifier: the LABEL identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance
      :raises ValueError: if the identifier is invalid
      :raises aiida.common.NotExistent: if the orm base class does not support a LABEL like identifier

   .. py:method:: _get_query_builder_id_identifier(identifier, classes)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_id_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as an ID like identifier

      :param identifier: the ID identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :returns: the query builder instance

   .. py:method:: _get_query_builder_uuid_identifier(identifier, classes, query_with_dashes)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader._get_query_builder_uuid_identifier
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, interpreting the identifier as a UUID like identifier

      :param identifier: the UUID identifier
      :param classes: a tuple of orm classes to which the identifier should be mapped
      :returns: the query builder instance

   .. py:method:: get_query_builder(identifier, identifier_type=None, sub_classes=None, query_with_dashes=True, operator='==', project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_query_builder
      :classmethod:

      Return the query builder instance that attempts to map the identifier onto an entity of the orm class,
      defined for this loader class, inferring the identifier type if it is not defined.

      :param identifier: the identifier
      :param identifier_type: the type of the identifier
      :param sub_classes: an optional tuple of orm classes, that should each be strict sub classes of the
          base orm class of the loader, that will narrow the queryset
      :param operator: the operator to use in the query
      :param project: the property or properties to project for entities matching the query
      :returns: the query builder instance and a dictionary of used query parameters

   .. py:method:: get_options(incomplete, project='*')
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_options
      :classmethod:

      Return the list of entities that match the `incomplete` identifier.

      .. note:: For the time being only `LABEL` auto-completion is supported so the identifier type is not inferred
          but hard-coded to be `IdentifierType.LABEL`

      :param incomplete: the incomplete identifier
      :param project: the field(s) to project for each entity that matches the incomplete identifier
      :return: list of entities matching the incomplete identifier

   .. py:method:: load_entity(identifier, identifier_type=None, sub_classes=None, query_with_dashes=True)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.load_entity
      :classmethod:

      Load an entity that uniquely corresponds to the provided identifier of the identifier type.

      :param identifier: the identifier
      :param identifier_type: the type of the identifier
      :param sub_classes: an optional tuple of orm classes, that should each be strict sub classes of the
          base orm class of the loader, that will narrow the queryset
      :returns: the loaded entity
      :raises aiida.common.MultipleObjectsError: if the identifier maps onto multiple entities
      :raises aiida.common.NotExistent: if the identifier maps onto not a single entity

   .. py:method:: get_query_classes(sub_classes=None)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.get_query_classes
      :classmethod:

      Get the tuple of classes to be used for the entity query. If sub_classes is defined, each class will be
      validated by verifying that it is a sub class of the loader's orm base class.
      Validate a tuple of classes if a user passes in a specific one when attempting to load an entity. Each class
      should be a sub class of the entity loader's orm base class

      :param sub_classes: an optional tuple of orm classes, that should each be strict sub classes of the
          base orm class of the loader, that will narrow the queryset
      :returns: the tuple of orm classes to be used for the entity query
      :raises ValueError: if any of the classes are not a sub class of the entity loader's orm base class

   .. py:method:: infer_identifier_type(value)
      :canonical: aiida.orm.utils.loaders.OrmEntityLoader.infer_identifier_type
      :classmethod:

      This method will attempt to automatically distinguish which identifier type is implied for the given value, if
      the value itself has no type from which it can be inferred.

      The strategy is to first attempt to convert the value to an integer. If successful, it is assumed that the value
      represents an ID. If that fails, we attempt to interpret the value as a base 16 encoded integer, after having
      removed any dashes from the string. If that succeeds, it is most likely a UUID. If it seems to be neither an ID
      nor a UUID, it is assumed to be a LABEL like identifier.

      With this approach there is the possibility for ambiguity. Since it is allowed to pass a partial UUID, it is
      possible that the partial UUID is also a valid ID. Likewise, a LABEL identifier might also be a valid ID, or a
      valid (partial) UUID. Fortunately, these ambiguities can be solved though:

       * ID/UUID: can always be solved by passing a partial UUID with at least one dash
       * ID/LABEL: appending an exclamation point ! to the identifier, will force LABEL interpretation
       * UUID/LABEL: appending an exclamation point ! to the identifier, will force LABEL interpretation

      As one can see, the user will always be able to include at least one dash of the UUID identifier to prevent it
      from being interpreted as an ID. For the potential ambiguities in LABEL identifiers, we had to introduce a
      special marker to provide a surefire way of breaking any ambiguity that may arise. Adding an exclamation point
      will break the normal strategy and the identifier will directly be interpreted as a LABEL identifier.

      :param value: the value of the identifier
      :returns: the identifier and identifier type
      :raises ValueError: if the value is an invalid identifier

.. py:class:: PortableCode(filepath_executable: str, filepath_files: pathlib.Path, **kwargs)
   :canonical: aiida.orm.nodes.data.code.portable.PortableCode

   Bases: :py:obj:`aiida.orm.nodes.data.code.legacy.Code`

   Data plugin representing an executable code stored in AiiDA's storage.

   .. rubric:: Initialization

   Construct a new instance.

   .. note:: If the files necessary for this code are not all located in a single directory or the directory
       contains files that should not be uploaded, and so the ``filepath_files`` cannot be used. One can use the
       methods of the :class:`aiida.orm.nodes.repository.NodeRepository` class. This can be accessed through the
       ``base.repository`` attribute of the instance after it has been constructed. For example::

           code = PortableCode(filepath_executable='some_name.exe')
           code.put_object_from_file()
           code.put_object_from_filelike()
           code.put_object_from_tree()

   :param filepath_executable: The relative filepath of the executable within the directory of uploaded files.
   :param filepath_files: The filepath to the directory containing all the files of the code.

   .. py:attribute:: _KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._KEY_ATTRIBUTE_FILEPATH_EXECUTABLE
      :type: str
      :value: 'filepath_executable'

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._validate

      Validate the instance by checking that an executable is defined and it is part of the repository files.

      :raises :class:`aiida.common.exceptions.ValidationError`: If the state of the node is invalid.

   .. py:method:: can_run_on_computer(computer: aiida.orm.Computer) -> bool
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.can_run_on_computer

      Return whether the code can run on a given computer.

      A ``PortableCode`` should be able to be run on any computer in principle.

      :param computer: The computer.
      :return: ``True`` if the provided computer is the same as the one configured for this code.

   .. py:method:: get_executable() -> pathlib.PurePosixPath
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.get_executable

      Return the executable that the submission script should execute to run the code.

      :return: The executable to be called in the submission script.

   .. py:method:: validate_working_directory(folder: aiida.common.folders.Folder)
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.validate_working_directory

      Validate content of the working directory created by the :class:`~aiida.engine.CalcJob` plugin.

      This method will be called by :meth:`~aiida.engine.processes.calcjobs.calcjob.CalcJob.presubmit` when a new
      calculation job is launched, passing the :class:`~aiida.common.folders.Folder` that was used by the plugin used
      for the calculation to create the input files for the working directory. This method can be overridden by
      implementations of the ``AbstractCode`` class that need to validate the contents of that folder.

      :param folder: A sandbox folder that the ``CalcJob`` plugin wrote input files to that will be copied to the
          working directory for the corresponding calculation job instance.
      :raises PluginInternalError: The ``CalcJob`` plugin created a file that has the same relative filepath as the
          executable for this portable code.

   .. py:property:: full_label
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.full_label
      :type: str

      Return the full label of this code.

      The full label can be just the label itself but it can be something else. However, it at the very least has to
      include the label of the code.

      :return: The full label of the code.

   .. py:property:: filepath_executable
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode.filepath_executable
      :type: pathlib.PurePosixPath

      Return the relative filepath of the executable that this code represents.

      :return: The relative filepath of the executable.

   .. py:method:: _get_cli_options() -> dict
      :canonical: aiida.orm.nodes.data.code.portable.PortableCode._get_cli_options
      :classmethod:

      Return the CLI options that would allow to create an instance of this class.

.. py:class:: ProcessNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.process.ProcessNode

   Bases: :py:obj:`aiida.orm.utils.mixins.Sealable`, :py:obj:`aiida.orm.nodes.node.Node`

   Base class for all nodes representing the execution of a process

   This class and its subclasses serve as proxies in the database, for actual `Process` instances being run. The
   `Process` instance in memory will leverage an instance of this class (the exact sub class depends on the sub class
   of `Process`) to persist important information of its state to the database. This serves as a way for the user to
   inspect the state of the `Process` during its execution as well as a permanent record of its execution in the
   provenance graph, after the execution has terminated.

   .. rubric:: Initialization

   :param backend_entity: the backend model supporting this entity

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_LINKS
      :value: None

   .. py:attribute:: _CLS_NODE_CACHING
      :canonical: aiida.orm.nodes.process.process.ProcessNode._CLS_NODE_CACHING
      :value: None

   .. py:attribute:: CHECKPOINT_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.CHECKPOINT_KEY
      :value: 'checkpoints'

   .. py:attribute:: EXCEPTION_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXCEPTION_KEY
      :value: 'exception'

   .. py:attribute:: EXIT_MESSAGE_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXIT_MESSAGE_KEY
      :value: 'exit_message'

   .. py:attribute:: EXIT_STATUS_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.EXIT_STATUS_KEY
      :value: 'exit_status'

   .. py:attribute:: PROCESS_PAUSED_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_PAUSED_KEY
      :value: 'paused'

   .. py:attribute:: PROCESS_LABEL_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_LABEL_KEY
      :value: 'process_label'

   .. py:attribute:: PROCESS_STATE_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATE_KEY
      :value: 'process_state'

   .. py:attribute:: PROCESS_STATUS_KEY
      :canonical: aiida.orm.nodes.process.process.ProcessNode.PROCESS_STATUS_KEY
      :value: 'process_status'

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.process.ProcessNode._unstorable_message
      :value: 'only Data, WorkflowNode, CalculationNode or their subclasses can be stored'

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.nodes.process.process.ProcessNode.__str__

      Return str(self).

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.process.ProcessNode._updatable_attributes

   .. py:property:: logger
      :canonical: aiida.orm.nodes.process.process.ProcessNode.logger

      Get the logger of the Calculation object, so that it also logs to the DB.

      :return: LoggerAdapter object, that works like a logger, but also has the 'extra' embedded

   .. py:method:: get_builder_restart() -> aiida.engine.processes.builder.ProcessBuilder
      :canonical: aiida.orm.nodes.process.process.ProcessNode.get_builder_restart

      Return a `ProcessBuilder` that is ready to relaunch the process that created this node.

      The process class will be set based on the `process_type` of this node and the inputs of the builder will be
      prepopulated with the inputs registered for this node. This functionality is very useful if a process has
      completed and you want to relaunch it with slightly different inputs.

      :return: `~aiida.engine.processes.builder.ProcessBuilder` instance

   .. py:property:: process_class
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_class
      :type: typing.Type[aiida.engine.processes.Process]

      Return the process class that was used to create this node.

      :return: `Process` class
      :raises ValueError: if no process type is defined, it is an invalid process type string or cannot be resolved
          to load the corresponding class

   .. py:method:: set_process_type(process_type_string: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_type

      Set the process type string.

      :param process_type: the process type string identifying the class using this process node as storage.

   .. py:property:: process_label
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_label
      :type: typing.Optional[str]

      Return the process label

      :returns: the process label

   .. py:method:: set_process_label(label: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_label

      Set the process label

      :param label: process label string

   .. py:property:: process_state
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_state
      :type: typing.Optional[plumpy.process_states.ProcessState]

      Return the process state

      :returns: the process state instance of ProcessState enum

   .. py:method:: set_process_state(state: typing.Union[str, plumpy.process_states.ProcessState, None])
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_state

      Set the process state

      :param state: value or instance of ProcessState enum

   .. py:property:: process_status
      :canonical: aiida.orm.nodes.process.process.ProcessNode.process_status
      :type: typing.Optional[str]

      Return the process status

      The process status is a generic status message e.g. the reason it might be paused or when it is being killed

      :returns: the process status

   .. py:method:: set_process_status(status: typing.Optional[str]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_process_status

      Set the process status

      The process status is a generic status message e.g. the reason it might be paused or when it is being killed.
      If status is None, the corresponding attribute will be deleted.

      :param status: string process status

   .. py:property:: is_terminated
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_terminated
      :type: bool

      Return whether the process has terminated

      Terminated means that the process has reached any terminal state.

      :return: True if the process has terminated, False otherwise
      :rtype: bool

   .. py:property:: is_excepted
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_excepted
      :type: bool

      Return whether the process has excepted

      Excepted means that during execution of the process, an exception was raised that was not caught.

      :return: True if during execution of the process an exception occurred, False otherwise
      :rtype: bool

   .. py:property:: is_killed
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_killed
      :type: bool

      Return whether the process was killed

      Killed means the process was killed directly by the user or by the calling process being killed.

      :return: True if the process was killed, False otherwise
      :rtype: bool

   .. py:property:: is_finished
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_finished
      :type: bool

      Return whether the process has finished

      Finished means that the process reached a terminal state nominally.
      Note that this does not necessarily mean successfully, but there were no exceptions and it was not killed.

      :return: True if the process has finished, False otherwise
      :rtype: bool

   .. py:property:: is_finished_ok
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_finished_ok
      :type: bool

      Return whether the process has finished successfully

      Finished successfully means that it terminated nominally and had a zero exit status.

      :return: True if the process has finished successfully, False otherwise
      :rtype: bool

   .. py:property:: is_failed
      :canonical: aiida.orm.nodes.process.process.ProcessNode.is_failed
      :type: bool

      Return whether the process has failed

      Failed means that the process terminated nominally but it had a non-zero exit status.

      :return: True if the process has failed, False otherwise
      :rtype: bool

   .. py:property:: exit_status
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exit_status
      :type: typing.Optional[int]

      Return the exit status of the process

      :returns: the exit status, an integer exit code or None

   .. py:method:: set_exit_status(status: typing.Union[None, enum.Enum, int]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exit_status

      Set the exit status of the process

      :param state: an integer exit code or None, which will be interpreted as zero

   .. py:property:: exit_message
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exit_message
      :type: typing.Optional[str]

      Return the exit message of the process

      :returns: the exit message

   .. py:method:: set_exit_message(message: typing.Optional[str]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exit_message

      Set the exit message of the process, if None nothing will be done

      :param message: a string message

   .. py:property:: exception
      :canonical: aiida.orm.nodes.process.process.ProcessNode.exception
      :type: typing.Optional[str]

      Return the exception of the process or None if the process is not excepted.

      If the process is marked as excepted yet there is no exception attribute, an empty string will be returned.

      :returns: the exception message or None

   .. py:method:: set_exception(exception: str) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_exception

      Set the exception of the process

      :param exception: the exception message

   .. py:property:: checkpoint
      :canonical: aiida.orm.nodes.process.process.ProcessNode.checkpoint
      :type: typing.Optional[typing.Dict[str, typing.Any]]

      Return the checkpoint bundle set for the process

      :returns: checkpoint bundle if it exists, None otherwise

   .. py:method:: set_checkpoint(checkpoint: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.set_checkpoint

      Set the checkpoint bundle set for the process

      :param state: string representation of the stepper state info

   .. py:method:: delete_checkpoint() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.delete_checkpoint

      Delete the checkpoint bundle set for the process

   .. py:property:: paused
      :canonical: aiida.orm.nodes.process.process.ProcessNode.paused
      :type: bool

      Return whether the process is paused

      :returns: True if the Calculation is marked as paused, False otherwise

   .. py:method:: pause() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.pause

      Mark the process as paused by setting the corresponding attribute.

      This serves only to reflect that the corresponding Process is paused and so this method should not be called
      by anyone but the Process instance itself.

   .. py:method:: unpause() -> None
      :canonical: aiida.orm.nodes.process.process.ProcessNode.unpause

      Mark the process as unpaused by removing the corresponding attribute.

      This serves only to reflect that the corresponding Process is unpaused and so this method should not be called
      by anyone but the Process instance itself.

   .. py:property:: called
      :canonical: aiida.orm.nodes.process.process.ProcessNode.called
      :type: typing.List[aiida.orm.nodes.process.process.ProcessNode]

      Return a list of nodes that the process called

      :returns: list of process nodes called by this process

   .. py:property:: called_descendants
      :canonical: aiida.orm.nodes.process.process.ProcessNode.called_descendants
      :type: typing.List[aiida.orm.nodes.process.process.ProcessNode]

      Return a list of all nodes that have been called downstream of this process

      This will recursively find all the called processes for this process and its children.

   .. py:property:: caller
      :canonical: aiida.orm.nodes.process.process.ProcessNode.caller
      :type: typing.Optional[aiida.orm.nodes.process.process.ProcessNode]

      Return the process node that called this process node, or None if it does not have a caller

      :returns: process node that called this process node instance or None

.. py:class:: ProjectionData(*args, source=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.projection.ProjectionData

   Bases: :py:obj:`aiida.orm.nodes.data.orbital.OrbitalData`, :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   A class to handle arrays of projected wavefunction data. That is projections
   of a orbitals, usually an atomic-hydrogen orbital, onto a
   given bloch wavefunction, the bloch wavefunction being indexed by
   s, n, and k. E.g. the elements are the projections described as
   < orbital | Bloch wavefunction (s,n,k) >

   .. rubric:: Initialization

   Construct a new instance, setting the ``source`` attribute if provided as a keyword argument.

   .. py:method:: _check_projections_bands(projection_array)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._check_projections_bands

      Checks to make sure that a reference bandsdata is already set, and that
      projection_array is of the same shape of the bands data

      :param projwfc_arrays: nk x nb x nwfc array, to be
                             checked against bands

      :raise: AttributeError if energy is not already set
      :raise: AttributeError if input_array is not of same shape as
              dos_energy

   .. py:method:: set_reference_bandsdata(value)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_reference_bandsdata

      Sets a reference bandsdata, creates a uuid link between this data
      object and a bandsdata object, must be set before any projection arrays

      :param value: a BandsData instance, a uuid or a pk
      :raise: exceptions.NotExistent if there was no BandsData associated with uuid or pk

   .. py:method:: get_reference_bandsdata()
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_reference_bandsdata

      Returns the reference BandsData, using the set uuid via
      set_reference_bandsdata

      :return: a BandsData instance
      :raise AttributeError: if the bandsdata has not been set yet
      :raise exceptions.NotExistent: if the bandsdata uuid did not retrieve bandsdata

   .. py:method:: _find_orbitals_and_indices(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._find_orbitals_and_indices

      Finds all the orbitals and their indicies associated with kwargs
      essential for retrieving the other indexed array parameters

      :param kwargs: kwargs that can call orbitals as in get_orbitals()
      :return: retrieve_indexes, list of indicicies of orbitals corresponding
               to the kwargs
      :return: all_orbitals, list of orbitals to which the indexes correspond

   .. py:method:: get_pdos(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_pdos

      Retrieves all the pdos arrays corresponding to the input kwargs

      :param kwargs: inputs describing the orbitals associated with the pdos
                     arrays
      :return: a list of tuples containing the orbital, energy array and pdos
               array associated with all orbitals that correspond to kwargs


   .. py:method:: get_projections(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.get_projections

      Retrieves all the pdos arrays corresponding to the input kwargs

      :param kwargs: inputs describing the orbitals associated with the pdos
                     arrays
      :return: a list of tuples containing the orbital, and projection arrays
               associated with all orbitals that correspond to kwargs


   .. py:method:: _from_index_to_arrayname(index)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData._from_index_to_arrayname
      :staticmethod:

      Used internally to determine the array names.

   .. py:method:: set_projectiondata(list_of_orbitals, list_of_projections=None, list_of_energy=None, list_of_pdos=None, tags=None, bands_check=True)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_projectiondata

      Stores the projwfc_array using the projwfc_label, after validating both.

      :param list_of_orbitals: list of orbitals, of class orbital data.
                               They should be the ones up on which the
                               projection array corresponds with.

      :param list_of_projections: list of arrays of projections of a atomic
                            wavefunctions onto bloch wavefunctions. Since the
                            projection is for every bloch wavefunction which
                            can be specified by its spin (if used), band, and
                            kpoint the dimensions must be
                            nspin x nbands x nkpoints for the projwfc array.
                            Or nbands x nkpoints if spin is not used.

      :param energy_axis: list of energy axis for the list_of_pdos

      :param list_of_pdos: a list of projected density of states for the
                           atomic wavefunctions, units in states/eV

      :param tags: A list of tags, not supported currently.

      :param bands_check: if false, skips checks of whether the bands has
                          been already set, and whether the sizes match. For
                          use in parsers, where the BandsData has not yet
                          been stored and therefore get_reference_bandsdata
                          cannot be called

   .. py:method:: set_orbitals(**kwargs)
      :canonical: aiida.orm.nodes.data.array.projection.ProjectionData.set_orbitals
      :abstractmethod:

      This method is inherited from OrbitalData, but is blocked here.
      If used will raise a NotImplementedError

.. py:class:: QueryBuilder(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, *, debug: bool = False, path: typing.Optional[typing.Sequence[typing.Union[str, typing.Dict[str, typing.Any], aiida.orm.querybuilder.EntityClsType]]] = (), filters: typing.Optional[typing.Dict[str, aiida.orm.querybuilder.FilterType]] = None, project: typing.Optional[typing.Dict[str, aiida.orm.querybuilder.ProjectType]] = None, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, order_by: typing.Optional[aiida.orm.querybuilder.OrderByType] = None, distinct: bool = False)
   :canonical: aiida.orm.querybuilder.QueryBuilder

   The class to query the AiiDA database.

   Usage::

       from aiida.orm.querybuilder import QueryBuilder
       qb = QueryBuilder()
       # Querying nodes:
       qb.append(Node)
       # retrieving the results:
       results = qb.all()


   .. rubric:: Initialization

   Instantiates a QueryBuilder instance.

   Which backend is used decided here based on backend-settings (taken from the user profile).
   This cannot be overridden so far by the user.

   :param debug:
       Turn on debug mode. This feature prints information on the screen about the stages
       of the QueryBuilder. Does not affect results.
   :param path:
       A list of the vertices to traverse. Leave empty if you plan on using the method
       :func:`QueryBuilder.append`.
   :param filters:
       The filters to apply. You can specify the filters here, when appending to the query
       using :func:`QueryBuilder.append` or even later using :func:`QueryBuilder.add_filter`.
       Check latter gives API-details.
   :param project:
       The projections to apply. You can specify the projections here, when appending to the query
       using :func:`QueryBuilder.append` or even later using :func:`QueryBuilder.add_projection`.
       Latter gives you API-details.
   :param limit:
       Limit the number of rows to this number. Check :func:`QueryBuilder.limit`
       for more information.
   :param offset:
       Set an offset for the results returned. Details in :func:`QueryBuilder.offset`.
   :param order_by:
       How to order the results. As the 2 above, can be set also at later stage,
       check :func:`QueryBuilder.order_by` for more information.
   :param distinct: Whether to return de-duplicated rows


   .. py:attribute:: _EDGE_TAG_DELIM
      :canonical: aiida.orm.querybuilder.QueryBuilder._EDGE_TAG_DELIM
      :value: '--'

   .. py:attribute:: _VALID_PROJECTION_KEYS
      :canonical: aiida.orm.querybuilder.QueryBuilder._VALID_PROJECTION_KEYS
      :value: ('func', 'cast')

   .. py:property:: backend
      :canonical: aiida.orm.querybuilder.QueryBuilder.backend
      :type: aiida.orm.implementation.StorageBackend

      Return the backend used by the QueryBuilder.

   .. py:method:: as_dict(copy: bool = True) -> aiida.orm.implementation.querybuilder.QueryDictType
      :canonical: aiida.orm.querybuilder.QueryBuilder.as_dict

      Convert to a JSON serialisable dictionary representation of the query.

   .. py:property:: queryhelp
      :canonical: aiida.orm.querybuilder.QueryBuilder.queryhelp
      :type: aiida.orm.implementation.querybuilder.QueryDictType

      "Legacy name for ``as_dict`` method.

   .. py:method:: from_dict(dct: typing.Dict[str, typing.Any]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.from_dict
      :classmethod:

      Create an instance from a dictionary representation of the query.

   .. py:method:: __repr__() -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.__repr__

      Return an unambiguous string representation of the instance.

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.__str__

      Return a readable string representation of the instance.

   .. py:method:: __deepcopy__(memo) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.__deepcopy__

      Create deep copy of the instance.

   .. py:method:: get_used_tags(vertices: bool = True, edges: bool = True) -> typing.List[str]
      :canonical: aiida.orm.querybuilder.QueryBuilder.get_used_tags

      Returns a list of all the vertices that are being used.

      :param vertices: If True, adds the tags of vertices to the returned list
      :param edges: If True, adds the tags of edges to the returnend list.

      :returns: A list of tags

   .. py:method:: _get_unique_tag(classifiers: typing.List[aiida.orm.querybuilder.Classifier]) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder._get_unique_tag

      Using the function get_tag_from_type, I get a tag.
      I increment an index that is appended to that tag until I have an unused tag.
      This function is called in :func:`QueryBuilder.append` when no tag is given.

      :param dict classifiers:
          Classifiers, containing the string that defines the type of the AiiDA ORM class.
          For subclasses of Node, this is the Node._plugin_type_string, for other they are
          as defined as returned by :func:`QueryBuilder._get_ormclass`.

          Can also be a list of dictionaries, when multiple classes are passed to QueryBuilder.append

      :returns: A tag as a string (it is a single string also when passing multiple classes).

   .. py:method:: append(cls: typing.Optional[typing.Union[aiida.orm.querybuilder.EntityClsType, typing.Sequence[aiida.orm.querybuilder.EntityClsType]]] = None, entity_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None, tag: typing.Optional[str] = None, filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, project: typing.Optional[aiida.orm.querybuilder.ProjectType] = None, subclassing: bool = True, edge_tag: typing.Optional[str] = None, edge_filters: typing.Optional[aiida.orm.querybuilder.FilterType] = None, edge_project: typing.Optional[aiida.orm.querybuilder.ProjectType] = None, outerjoin: bool = False, joining_keyword: typing.Optional[str] = None, joining_value: typing.Optional[typing.Any] = None, orm_base: typing.Optional[str] = None, **kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.append

      Any iterative procedure to build the path for a graph query
      needs to invoke this method to append to the path.

      :param cls:
          The Aiida-class (or backend-class) defining the appended vertice.
          Also supports a tuple/list of classes. This results in an all instances of
          this class being accepted in a query. However the classes have to have the same orm-class
          for the joining to work. I.e. both have to subclasses of Node. Valid is::

              cls=(StructureData, Dict)

          This is invalid:

              cls=(Group, Node)

      :param entity_type: The node type of the class, if cls is not given. Also here, a tuple or list is accepted.
      :param tag:
          A unique tag. If none is given, I will create a unique tag myself.
      :param filters:
          Filters to apply for this vertex.
          See :meth:`.add_filter`, the method invoked in the background, or usage examples for details.
      :param project:
          Projections to apply. See usage examples for details.
          More information also in :meth:`.add_projection`.
      :param subclassing:
          Whether to include subclasses of the given class (default **True**).
          E.g. Specifying a ProcessNode as cls will include CalcJobNode, WorkChainNode, CalcFunctionNode, etc..
      :param edge_tag:
          The tag that the edge will get. If nothing is specified
          (and there is a meaningful edge) the default is tag1--tag2 with tag1 being the entity joining
          from and tag2 being the entity joining to (this entity).
      :param edge_filters:
          The filters to apply on the edge. Also here, details in :meth:`.add_filter`.
      :param edge_project:
          The project from the edges. API-details in :meth:`.add_projection`.
      :param outerjoin:
          If True, (default is False), will do a left outerjoin
          instead of an inner join

      Joining can be specified in two ways:

          - Specifying the 'joining_keyword' and 'joining_value' arguments
          - Specify a single keyword argument

      The joining keyword wil be ``with_*`` or ``direction``, depending on the joining entity type.
      The joining value is the tag name or class of the entity to join to.

      A small usage example how this can be invoked::

          qb = QueryBuilder()             # Instantiating empty querybuilder instance
          qb.append(cls=StructureData)    # First item is StructureData node
          # The
          # next node in the path is a PwCalculation, with
          # the structure joined as an input
          qb.append(
              cls=PwCalculation,
              with_incoming=StructureData
          )

      :return: self

   .. py:method:: order_by(order_by: aiida.orm.querybuilder.OrderByType) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.order_by

      Set the entity to order by

      :param order_by:
          This is a list of items, where each item is a dictionary specifies
          what to sort for an entity

      In each dictionary in that list, keys represent valid tags of
      entities (tables), and values are list of columns.

      Usage::

          #Sorting by id (ascending):
          qb = QueryBuilder()
          qb.append(Node, tag='node')
          qb.order_by({'node':['id']})

          # or
          #Sorting by id (ascending):
          qb = QueryBuilder()
          qb.append(Node, tag='node')
          qb.order_by({'node':[{'id':{'order':'asc'}}]})

          # for descending order:
          qb = QueryBuilder()
          qb.append(Node, tag='node')
          qb.order_by({'node':[{'id':{'order':'desc'}}]})

          # or (shorter)
          qb = QueryBuilder()
          qb.append(Node, tag='node')
          qb.order_by({'node':[{'id':'desc'}]})

   .. py:method:: add_filter(tagspec: typing.Union[str, aiida.orm.querybuilder.EntityClsType], filter_spec: aiida.orm.querybuilder.FilterType) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.add_filter

      Adding a filter to my filters.

      :param tagspec: A tag string or an ORM class which maps to an existing tag
      :param filter_spec: The specifications for the filter, has to be a dictionary

      Usage::

          qb = QueryBuilder()         # Instantiating the QueryBuilder instance
          qb.append(Node, tag='node') # Appending a Node
          #let's put some filters:
          qb.add_filter('node',{'id':{'>':12}})
          # 2 filters together:
          qb.add_filter('node',{'label':'foo', 'uuid':{'like':'ab%'}})
          # Now I am overriding the first filter I set:
          qb.add_filter('node',{'id':13})

   .. py:method:: _process_filters(filters: aiida.orm.querybuilder.FilterType) -> typing.Dict[str, typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder._process_filters
      :staticmethod:

      Process filters.

   .. py:method:: _add_node_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool)
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_node_type_filter

      Add a filter based on node type.

      :param tagspec: The tag, which has to exist already as a key in self._filters
      :param classifiers: a dictionary with classifiers
      :param subclassing: if True, allow for subclasses of the ormclass

   .. py:method:: _add_process_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_process_type_filter

      Add a filter based on process type.

      :param tagspec: The tag, which has to exist already as a key in self._filters
      :param classifiers: a dictionary with classifiers
      :param subclassing: if True, allow for subclasses of the process type

      Note: This function handles the case when process_type_string is None.

   .. py:method:: _add_group_type_filter(tagspec: str, classifiers: typing.List[aiida.orm.querybuilder.Classifier], subclassing: bool) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder._add_group_type_filter

      Add a filter based on group type.

      :param tagspec: The tag, which has to exist already as a key in self._filters
      :param classifiers: a dictionary with classifiers
      :param subclassing: if True, allow for subclasses of the ormclass

   .. py:method:: add_projection(tag_spec: typing.Union[str, aiida.orm.querybuilder.EntityClsType], projection_spec: aiida.orm.querybuilder.ProjectType) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder.add_projection

      Adds a projection

      :param tag_spec: A tag string or an ORM class which maps to an existing tag
      :param projection_spec:
          The specification for the projection.
          A projection is a list of dictionaries, with each dictionary
          containing key-value pairs where the key is database entity
          (e.g. a column / an attribute) and the value is (optional)
          additional information on how to process this database entity.

      If the given *projection_spec* is not a list, it will be expanded to
      a list.
      If the listitems are not dictionaries, but strings (No additional
      processing of the projected results desired), they will be expanded to
      dictionaries.

      Usage::

          qb = QueryBuilder()
          qb.append(StructureData, tag='struc')

          # Will project the uuid and the kinds
          qb.add_projection('struc', ['uuid', 'attributes.kinds'])

      The above example will project the uuid and the kinds-attribute of all matching structures.
      There are 2 (so far) special keys.

      The single star *\** will project the *ORM-instance*::

          qb = QueryBuilder()
          qb.append(StructureData, tag='struc')
          # Will project the ORM instance
          qb.add_projection('struc', '*')
          print type(qb.first()[0])
          # >>> aiida.orm.nodes.data.structure.StructureData

      The double star ``**`` projects all possible projections of this entity:

          QueryBuilder().append(StructureData,tag='s', project='**').limit(1).dict()[0]['s'].keys()

          # >>> 'user_id, description, ctime, label, extras, mtime, id, attributes, dbcomputer_id, type, uuid'

      Be aware that the result of ``**`` depends on the backend implementation.


   .. py:method:: set_debug(debug: bool) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.set_debug

      Run in debug mode. This does not affect functionality, but prints intermediate stages
      when creating a query on screen.

      :param debug: Turn debug on or off

   .. py:method:: debug(msg: str, *objects: typing.Any) -> None
      :canonical: aiida.orm.querybuilder.QueryBuilder.debug

      Log debug message.

      objects will passed to the format string, e.g. ``msg % objects``

   .. py:method:: limit(limit: typing.Optional[int]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.limit

      Set the limit (nr of rows to return)

      :param limit: integers of number of rows of rows to return

   .. py:method:: offset(offset: typing.Optional[int]) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.offset

      Set the offset. If offset is set, that many rows are skipped before returning.
      *offset* = 0 is the same as omitting setting the offset.
      If both offset and limit appear,
      then *offset* rows are skipped before starting to count the *limit* rows
      that are returned.

      :param offset: integers of nr of rows to skip

   .. py:method:: distinct(value: bool = True) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.distinct

      Asks for distinct rows, which is the same as asking the backend to remove
      duplicates.
      Does not execute the query!

      If you want a distinct query::

          qb = QueryBuilder()
          # append stuff!
          qb.append(...)
          qb.append(...)
          ...
          qb.distinct().all() #or
          qb.distinct().dict()

      :returns: self

   .. py:method:: inputs(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.inputs

      Join to inputs of previous vertice in path.

      :returns: self

   .. py:method:: outputs(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.outputs

      Join to outputs of previous vertice in path.

      :returns: self

   .. py:method:: children(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.children

      Join to children/descendants of previous vertice in path.

      :returns: self

   .. py:method:: parents(**kwargs: typing.Any) -> aiida.orm.querybuilder.QueryBuilder
      :canonical: aiida.orm.querybuilder.QueryBuilder.parents

      Join to parents/ancestors of previous vertice in path.

      :returns: self

   .. py:method:: as_sql(inline: bool = False) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.as_sql

      Convert the query to an SQL string representation.

      .. warning::

          This method should be used for debugging purposes only,
          since normally sqlalchemy will handle this process internally.

      :params inline: Inline bound parameters (this is normally handled by the Python DB-API).

   .. py:method:: analyze_query(execute: bool = True, verbose: bool = False) -> str
      :canonical: aiida.orm.querybuilder.QueryBuilder.analyze_query

      Return the query plan, i.e. a list of SQL statements that will be executed.

      See: https://www.postgresql.org/docs/11/sql-explain.html

      :params execute: Carry out the command and show actual run times and other statistics.
      :params verbose: Display additional information regarding the plan.

   .. py:method:: _get_aiida_entity_res(value) -> typing.Any
      :canonical: aiida.orm.querybuilder.QueryBuilder._get_aiida_entity_res
      :staticmethod:

      Convert a projected query result to front end class if it is an instance of a `BackendEntity`.

      Values that are not an `BackendEntity` instance will be returned unaltered

      :param value: a projected query result to convert
      :return: the converted value

   .. py:method:: first(flat: bool = False) -> typing.Optional[list[typing.Any] | typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder.first

      Return the first result of the query.

      Calling ``first`` results in an execution of the underlying query.

      Note, this may change if several rows are valid for the query, as persistent ordering is not guaranteed unless
      explicitly specified.

      :param flat: if True, return just the projected quantity if there is just a single projection.
      :returns: One row of results as a list, or None if no result returned.

   .. py:method:: count() -> int
      :canonical: aiida.orm.querybuilder.QueryBuilder.count

      Counts the number of rows returned by the backend.

      :returns: the number of rows as an integer

   .. py:method:: iterall(batch_size: typing.Optional[int] = 100) -> typing.Iterable[typing.List[typing.Any]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.iterall

      Same as :meth:`.all`, but returns a generator.
      Be aware that this is only safe if no commit will take place during this
      transaction. You might also want to read the SQLAlchemy documentation on
      https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.yield_per

      :param batch_size:
          The size of the batches to ask the backend to batch results in subcollections.
          You can optimize the speed of the query by tuning this parameter.

      :returns: a generator of lists

   .. py:method:: iterdict(batch_size: typing.Optional[int] = 100) -> typing.Iterable[typing.Dict[str, typing.Dict[str, typing.Any]]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.iterdict

      Same as :meth:`.dict`, but returns a generator.
      Be aware that this is only safe if no commit will take place during this
      transaction. You might also want to read the SQLAlchemy documentation on
      https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.yield_per

      :param batch_size:
          The size of the batches to ask the backend to batch results in subcollections.
          You can optimize the speed of the query by tuning this parameter.

      :returns: a generator of dictionaries

   .. py:method:: all(batch_size: typing.Optional[int] = None, flat: bool = False) -> typing.Union[typing.List[typing.List[typing.Any]], typing.List[typing.Any]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.all

      Executes the full query with the order of the rows as returned by the backend.

      The order inside each row is given by the order of the vertices in the path and the order of the projections for
      each vertex in the path.

      :param batch_size: the size of the batches to ask the backend to batch results in subcollections. You can
          optimize the speed of the query by tuning this parameter. Leave the default `None` if speed is not critical
          or if you don't know what you're doing.
      :param flat: return the result as a flat list of projected entities without sub lists.
      :returns: a list of lists of all projected entities.

   .. py:method:: one() -> typing.List[typing.Any]
      :canonical: aiida.orm.querybuilder.QueryBuilder.one

      Executes the query asking for exactly one results.

      Will raise an exception if this is not the case:

      :raises: MultipleObjectsError if more then one row can be returned
      :raises: NotExistent if no result was found

   .. py:method:: dict(batch_size: typing.Optional[int] = None) -> typing.List[typing.Dict[str, typing.Dict[str, typing.Any]]]
      :canonical: aiida.orm.querybuilder.QueryBuilder.dict

      Executes the full query with the order of the rows as returned by the backend.
      the order inside each row is given by the order of the vertices in the path
      and the order of the projections for each vertice in the path.

      :param batch_size:
          The size of the batches to ask the backend to batch results in subcollections.
          You can optimize the speed of the query by tuning this parameter.
          Leave the default (*None*) if speed is not critical or if you don't know what you're doing!

      :returns: A list of dictionaries of all projected entities: tag -> field -> value

      Usage::

          qb = QueryBuilder()
          qb.append(
              StructureData,
              tag='structure',
              filters={'uuid':{'==':myuuid}},
          )
          qb.append(
              Node,
              with_ancestors='structure',
              project=['entity_type', 'id'],  # returns entity_type (string) and id (string)
              tag='descendant'
          )

          # Return the dictionaries:
          print "qb.iterdict()"
          for d in qb.iterdict():
              print '>>>', d

      results in the following output::

          qb.iterdict()
          >>> {'descendant': {
                  'entity_type': 'calculation.job.quantumespresso.pw.PwCalculation.',
                  'id': 7716}
              }
          >>> {'descendant': {
                  'entity_type': 'data.remote.RemoteData.',
                  'id': 8510}
              }


.. py:class:: RemoteData(remote_path=None, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.base.RemoteData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Store a link to a file or folder on a remote machine.

   Remember to pass a computer!

   .. rubric:: Initialization

   Construct a new instance, setting the ``source`` attribute if provided as a keyword argument.

   .. py:attribute:: KEY_EXTRA_CLEANED
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.KEY_EXTRA_CLEANED
      :value: 'cleaned'

   .. py:method:: get_remote_path()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.get_remote_path

   .. py:method:: set_remote_path(val)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.set_remote_path

   .. py:property:: is_empty
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.is_empty

      Check if remote folder is empty

   .. py:method:: getfile(relpath, destpath)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.getfile

      Connects to the remote folder and retrieves the content of a file.

      :param relpath:  The relative path of the file on the remote to retrieve.
      :param destpath: The absolute path of where to store the file on the local machine.

   .. py:method:: listdir(relpath='.')
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.listdir

      Connects to the remote folder and lists the directory content.

      :param relpath: If 'relpath' is specified, lists the content of the given subfolder.
      :return: a flat list of file/directory names (as strings).

   .. py:method:: listdir_withattributes(path='.')
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.listdir_withattributes

      Connects to the remote folder and lists the directory content.

      :param relpath: If 'relpath' is specified, lists the content of the given subfolder.
      :return: a list of dictionaries, where the documentation is in :py:class:Transport.listdir_withattributes.

   .. py:method:: _clean(transport=None)
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData._clean

      Remove all content of the remote folder on the remote computer.

      When the cleaning operation is successful, the extra with the key ``RemoteData.KEY_EXTRA_CLEANED`` is set.

      :param transport: Provide an optional transport that is already open. If not provided, a transport will be
          automatically opened, based on the current default user and the computer of this data node. Passing in the
          transport can be used for efficiency if a great number of nodes need to be cleaned for the same computer.
          Note that the user should take care that the correct transport is passed.
      :raises ValueError: If the hostname of the provided transport does not match that of the node's computer.

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData._validate

      Validate information stored in Node object.

      For the :py:class:`~aiida.orm.Node` base class, this check is always valid.
      Subclasses can override this method to perform additional checks
      and should usually call ``super()._validate()`` first!

      This method is called automatically before storing the node in the DB.
      Therefore, use :py:meth:`~aiida.orm.nodes.attributes.NodeAttributes.get()` and similar methods that
      automatically read either from the DB or from the internal attribute cache.

   .. py:method:: get_authinfo()
      :canonical: aiida.orm.nodes.data.remote.base.RemoteData.get_authinfo

.. py:class:: RemoteStashData(stash_mode: aiida.common.datastructures.StashMode, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Data plugin that models an archived folder on a remote computer.

   A stashed folder is essentially an instance of ``RemoteData`` that has been archived. Archiving in this context can
   simply mean copying the content of the folder to another location on the same or another filesystem as long as it is
   on the same machine. In addition, the folder may have been compressed into a single file for efficiency or even
   written to tape. The ``stash_mode`` attribute will distinguish how the folder was stashed which will allow the
   implementation to also `unstash` it and transform it back into a ``RemoteData`` such that it can be used as an input
   for new ``CalcJobs``.

   This class is a non-storable base class that merely registers the ``stash_mode`` attribute. Only its subclasses,
   that actually implement a certain stash mode, can be instantiated and therefore stored. The reason for this design
   is that because the behavior of the class can change significantly based on the mode employed to stash the files and
   implementing all these variants in the same class will lead to an unintuitive interface where certain properties or
   methods of the class will only be available or function properly based on the ``stash_mode``.

   .. rubric:: Initialization

   Construct a new instance

   :param stash_mode: the stashing mode with which the data was stashed on the remote.

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData._storable
      :value: False

   .. py:property:: stash_mode
      :canonical: aiida.orm.nodes.data.remote.stash.base.RemoteStashData.stash_mode
      :type: aiida.common.datastructures.StashMode

      Return the mode with which the data was stashed on the remote.

      :return: the stash mode.

.. py:class:: RemoteStashFolderData(stash_mode: aiida.common.datastructures.StashMode, target_basepath: str, source_list: typing.List, **kwargs)
   :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData

   Bases: :py:obj:`aiida.orm.nodes.data.remote.stash.base.RemoteStashData`

   Data plugin that models a folder with files of a completed calculation job that has been stashed through a copy.

   This data plugin can and should be used to stash files if and only if the stash mode is `StashMode.COPY`.

   .. rubric:: Initialization

   Construct a new instance

   :param stash_mode: the stashing mode with which the data was stashed on the remote.
   :param target_basepath: the target basepath.
   :param source_list: the list of source files.

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData._storable
      :value: True

   .. py:property:: target_basepath
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.target_basepath
      :type: str

      Return the target basepath.

      :return: the target basepath.

   .. py:property:: source_list
      :canonical: aiida.orm.nodes.data.remote.stash.folder.RemoteStashFolderData.source_list
      :type: typing.Union[typing.List, typing.Tuple]

      Return the list of source files that were stashed.

      :return: the list of source files.

.. py:class:: SinglefileData(file, filename=None, **kwargs)
   :canonical: aiida.orm.nodes.data.singlefile.SinglefileData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   Data class that can be used to store a single file in its repository.

   .. rubric:: Initialization

   Construct a new instance and set the contents to that of the file.

   :param file: an absolute filepath or filelike object whose contents to copy.
       Hint: Pass io.BytesIO(b"my string") to construct the SinglefileData directly from a string.
   :param filename: specify filename to use (defaults to name of provided file).

   .. py:attribute:: DEFAULT_FILENAME
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.DEFAULT_FILENAME
      :value: 'file.txt'

   .. py:property:: filename
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.filename

      Return the name of the file stored.

      :return: the filename under which the file is stored in the repository

   .. py:method:: open(path=None, mode='r')
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.open

      Return an open file handle to the content of this data node.

      :param path: the relative path of the object within the repository.
      :param mode: the mode with which to open the file handle (default: read mode)
      :return: a file handle

   .. py:method:: get_content()
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.get_content

      Return the content of the single file stored for this data node.

      :return: the content of the file as a string

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData.set_file

      Store the content of the file in the node's repository, deleting any other existing objects.

      :param file: an absolute filepath or filelike object whose contents to copy
          Hint: Pass io.BytesIO(b"my string") to construct the file directly from a string.
      :param filename: specify filename to use (defaults to name of provided file).

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.singlefile.SinglefileData._validate

      Ensure that there is one object stored in the repository, whose key matches value set for `filename` attr.

.. py:class:: Site(**kwargs)
   :canonical: aiida.orm.nodes.data.structure.Site

   This class contains the information about a given site of the system.

   It can be a single atom, or an alloy, or even contain vacancies.

   .. rubric:: Initialization

   Create a site.

   :param kind_name: a string that identifies the kind (species) of this site.
           This has to be found in the list of kinds of the StructureData
           object.
           Validation will be done at the StructureData level.
   :param position: the absolute position (three floats) in angstrom

   .. py:method:: get_raw()
      :canonical: aiida.orm.nodes.data.structure.Site.get_raw

      Return the raw version of the site, mapped to a suitable dictionary.
      This is the format that is actually used to store each site of the
      structure in the DB.

      :return: a python dictionary with the site.

   .. py:method:: get_ase(kinds)
      :canonical: aiida.orm.nodes.data.structure.Site.get_ase

      Return a ase.Atom object for this site.

      :param kinds: the list of kinds from the StructureData object.

      .. note:: If any site is an alloy or has vacancies, a ValueError
          is raised (from the site.get_ase() routine).

   .. py:property:: kind_name
      :canonical: aiida.orm.nodes.data.structure.Site.kind_name

      Return the kind name of this site (a string).

      The type of a site is used to decide whether two sites are identical
      (same mass, symbols, weights, ...) or not.

   .. py:property:: position
      :canonical: aiida.orm.nodes.data.structure.Site.position

      Return the position of this site in absolute coordinates,
      in angstrom.

   .. py:method:: __repr__()
      :canonical: aiida.orm.nodes.data.structure.Site.__repr__

      Return repr(self).

   .. py:method:: __str__()
      :canonical: aiida.orm.nodes.data.structure.Site.__str__

      Return str(self).

.. py:class:: Str
   :canonical: aiida.orm.nodes.data.str.Str

   Bases: :py:obj:`aiida.orm.nodes.data.base.BaseType`

   `Data` sub class to represent a string value.

   .. py:attribute:: _type
      :canonical: aiida.orm.nodes.data.str.Str._type
      :value: None

.. py:class:: StructureData(cell=None, pbc=None, ase=None, pymatgen=None, pymatgen_structure=None, pymatgen_molecule=None, **kwargs)
   :canonical: aiida.orm.nodes.data.structure.StructureData

   Bases: :py:obj:`aiida.orm.nodes.data.data.Data`

   This class contains the information about a given structure, i.e. a
   collection of sites together with a cell, the
   boundary conditions (whether they are periodic or not) and other
   related useful information.

   .. py:attribute:: _set_incompatibilities
      :canonical: aiida.orm.nodes.data.structure.StructureData._set_incompatibilities
      :value: [('ase', 'cell'), ('ase', 'pbc'), ('ase', 'pymatgen'), ('ase', 'pymatgen_molecule'), ('ase', 'pymatg...

   .. py:attribute:: _dimensionality_label
      :canonical: aiida.orm.nodes.data.structure.StructureData._dimensionality_label
      :value: None

   .. py:attribute:: _internal_kind_tags
      :canonical: aiida.orm.nodes.data.structure.StructureData._internal_kind_tags
      :value: None

   .. py:method:: get_dimensionality()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_dimensionality

      Return the dimensionality of the structure and its length/surface/volume.

      Zero-dimensional structures are assigned "volume" 0.

      :return: returns a dictionary with keys "dim" (dimensionality integer), "label" (dimensionality label)
          and "value" (numerical length/surface/volume).

   .. py:method:: set_ase(aseatoms)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_ase

      Load the structure from a ASE object

   .. py:method:: set_pymatgen(obj, **kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen

      Load the structure from a pymatgen object.

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

   .. py:method:: set_pymatgen_molecule(mol, margin=5)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_molecule

      Load the structure from a pymatgen Molecule object.

      :param margin: the margin to be added in all directions of the
          bounding box of the molecule.

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

   .. py:method:: set_pymatgen_structure(struct)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pymatgen_structure

      Load the structure from a pymatgen Structure object.

      .. note:: periodic boundary conditions are set to True in all
          three directions.
      .. note:: Requires the pymatgen module (version >= 3.3.5, usage
          of earlier versions may cause errors).

      :raise ValueError: if there are partial occupancies together with spins.

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.structure.StructureData._validate

      Performs some standard validation tests.

   .. py:method:: _prepare_xsf(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_xsf

      Write the given structure to a string of format XSF (for XCrySDen).

   .. py:method:: _prepare_cif(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_cif

      Write the given structure to a string of format CIF.

   .. py:method:: _prepare_chemdoodle(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_chemdoodle

      Write the given structure to a string of format required by ChemDoodle.

   .. py:method:: _prepare_xyz(main_file_name='')
      :canonical: aiida.orm.nodes.data.structure.StructureData._prepare_xyz

      Write the given structure to a string of format XYZ.

   .. py:method:: _parse_xyz(inputstring)
      :canonical: aiida.orm.nodes.data.structure.StructureData._parse_xyz

      Read the structure from a string of format XYZ.

   .. py:method:: _adjust_default_cell(vacuum_factor=1.0, vacuum_addition=10.0, pbc=(False, False, False))
      :canonical: aiida.orm.nodes.data.structure.StructureData._adjust_default_cell

      If the structure was imported from an xyz file, it lacks a cell.
      This method will adjust the cell

   .. py:method:: get_description()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_description

      Returns a string with infos retrieved from StructureData node's properties

      :param self: the StructureData node
      :return: retsrt: the description string

   .. py:method:: get_symbols_set()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_symbols_set

      Return a set containing the names of all elements involved in
      this structure (i.e., for it joins the list of symbols for each
      kind k in the structure).

      :returns: a set of strings of element names.

   .. py:method:: get_formula(mode='hill', separator='')
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_formula

      Return a string with the chemical formula.

      :param mode: a string to specify how to generate the formula, can
          assume one of the following values:

          * 'hill' (default): count the number of atoms of each species,
            then use Hill notation, i.e. alphabetical order with C and H
            first if one or several C atom(s) is (are) present, e.g.
            ``['C','H','H','H','O','C','H','H','H']`` will return ``'C2H6O'``
            ``['S','O','O','H','O','H','O']``  will return ``'H2O4S'``
            From E. A. Hill, J. Am. Chem. Soc., 22 (8), pp 478–494 (1900)

          * 'hill_compact': same as hill but the number of atoms for each
            species is divided by the greatest common divisor of all of them, e.g.
            ``['C','H','H','H','O','C','H','H','H','O','O','O']``
            will return ``'CH3O2'``

          * 'reduce': group repeated symbols e.g.
            ``['Ba', 'Ti', 'O', 'O', 'O', 'Ba', 'Ti', 'O', 'O', 'O',
            'Ba', 'Ti', 'Ti', 'O', 'O', 'O']`` will return ``'BaTiO3BaTiO3BaTi2O3'``

          * 'group': will try to group as much as possible parts of the formula
            e.g.
            ``['Ba', 'Ti', 'O', 'O', 'O', 'Ba', 'Ti', 'O', 'O', 'O',
            'Ba', 'Ti', 'Ti', 'O', 'O', 'O']`` will return ``'(BaTiO3)2BaTi2O3'``

          * 'count': same as hill (i.e. one just counts the number
            of atoms of each species) without the re-ordering (take the
            order of the atomic sites), e.g.
            ``['Ba', 'Ti', 'O', 'O', 'O','Ba', 'Ti', 'O', 'O', 'O']``
            will return ``'Ba2Ti2O6'``

          * 'count_compact': same as count but the number of atoms
            for each species is divided by the greatest common divisor of
            all of them, e.g.
            ``['Ba', 'Ti', 'O', 'O', 'O','Ba', 'Ti', 'O', 'O', 'O']``
            will return ``'BaTiO3'``

      :param separator: a string used to concatenate symbols. Default empty.

      :return: a string with the formula

      .. note:: in modes reduce, group, count and count_compact, the
          initial order in which the atoms were appended by the user is
          used to group and/or order the symbols in the formula

   .. py:method:: get_site_kindnames()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_site_kindnames

      Return a list with length equal to the number of sites of this structure,
      where each element of the list is the kind name of the corresponding site.

      .. note:: This is NOT necessarily a list of chemical symbols! Use
          ``[ self.get_kind(s.kind_name).get_symbols_string() for s in self.sites]``
          for chemical symbols

      :return: a list of strings

   .. py:method:: get_composition()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_composition

      Returns the chemical composition of this structure as a dictionary,
      where each key is the kind symbol (e.g. H, Li, Ba),
      and each value is the number of occurences of that element in this
      structure. For BaZrO3 it would return {'Ba':1, 'Zr':1, 'O':3}.
      No reduction with smallest common divisor!

      :returns: a dictionary with the composition

   .. py:method:: get_ase()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_ase

      Get the ASE object.
      Requires to be able to import ase.

      :return: an ASE object corresponding to this
        :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
        object.

      .. note:: If any site is an alloy or has vacancies, a ValueError
          is raised (from the site.get_ase() routine).

   .. py:method:: get_pymatgen(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen

      Get pymatgen object. Returns Structure for structures with
      periodic boundary conditions (in three dimensions) and Molecule
      otherwise.
      :param add_spin: True to add the spins to the pymatgen structure.
      Default is False (no spin added).

      .. note:: The spins are set according to the following rule:

          * if the kind name ends with 1 -> spin=+1

          * if the kind name ends with 2 -> spin=-1

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

   .. py:method:: get_pymatgen_structure(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_structure

      Get the pymatgen Structure object.
      :param add_spin: True to add the spins to the pymatgen structure.
      Default is False (no spin added).

      .. note:: The spins are set according to the following rule:

          * if the kind name ends with 1 -> spin=+1

          * if the kind name ends with 2 -> spin=-1

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

      :return: a pymatgen Structure object corresponding to this
        :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
        object.
      :raise ValueError: if periodic boundary conditions do not hold
        in at least one dimension of real space.

   .. py:method:: get_pymatgen_molecule()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_pymatgen_molecule

      Get the pymatgen Molecule object.

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

      :return: a pymatgen Molecule object corresponding to this
        :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
        object.

   .. py:method:: append_kind(kind)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_kind

      Append a kind to the
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`.
      It makes a copy of the kind.

      :param kind: the site to append, must be a Kind object.

   .. py:method:: append_site(site)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_site

      Append a site to the
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`.
      It makes a copy of the site.

      :param site: the site to append. It must be a Site object.

   .. py:method:: append_atom(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.append_atom

      Append an atom to the Structure, taking care of creating the
      corresponding kind.

      :param ase: the ase Atom object from which we want to create a new atom
              (if present, this must be the only parameter)
      :param position: the position of the atom (three numbers in angstrom)
      :param symbols: passed to the constructor of the Kind object.
      :param weights: passed to the constructor of the Kind object.
      :param name: passed to the constructor of the Kind object. See also the note below.

      .. note :: Note on the 'name' parameter (that is, the name of the kind):

          * if specified, no checks are done on existing species. Simply,
            a new kind with that name is created. If there is a name
            clash, a check is done: if the kinds are identical, no error
            is issued; otherwise, an error is issued because you are trying
            to store two different kinds with the same name.

          * if not specified, the name is automatically generated. Before
            adding the kind, a check is done. If other species with the
            same properties already exist, no new kinds are created, but
            the site is added to the existing (identical) kind.
            (Actually, the first kind that is encountered).
            Otherwise, the name is made unique first, by adding to the string
            containing the list of chemical symbols a number starting from 1,
            until an unique name is found

      .. note :: checks of equality of species are done using
        the :py:meth:`~aiida.orm.nodes.data.structure.Kind.compare_with` method.

   .. py:method:: clear_kinds()
      :canonical: aiida.orm.nodes.data.structure.StructureData.clear_kinds

      Removes all kinds for the StructureData object.

      .. note:: Also clear all sites!

   .. py:method:: clear_sites()
      :canonical: aiida.orm.nodes.data.structure.StructureData.clear_sites

      Removes all sites for the StructureData object.

   .. py:property:: sites
      :canonical: aiida.orm.nodes.data.structure.StructureData.sites

      Returns a list of sites.

   .. py:property:: kinds
      :canonical: aiida.orm.nodes.data.structure.StructureData.kinds

      Returns a list of kinds.

   .. py:method:: get_kind(kind_name)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_kind

      Return the kind object associated with the given kind name.

      :param kind_name: String, the name of the kind you want to get

      :return: The Kind object associated with the given kind_name, if
         a Kind with the given name is present in the structure.

      :raise: ValueError if the kind_name is not present.

   .. py:method:: get_kind_names()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_kind_names

      Return a list of kind names (in the same order of the ``self.kinds``
      property, but return the names rather than Kind objects)

      .. note:: This is NOT necessarily a list of chemical symbols! Use
          get_symbols_set for chemical symbols

      :return: a list of strings.

   .. py:property:: cell
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell

      Returns the cell shape.

      :return: a 3x3 list of lists.

   .. py:method:: set_cell(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell

      Set the cell.

   .. py:method:: reset_cell(new_cell)
      :canonical: aiida.orm.nodes.data.structure.StructureData.reset_cell

      Reset the cell of a structure not yet stored to a new value.

      :param new_cell: list specifying the cell vectors

      :raises:
          ModificationNotAllowed: if object is already stored

   .. py:method:: reset_sites_positions(new_positions, conserve_particle=True)
      :canonical: aiida.orm.nodes.data.structure.StructureData.reset_sites_positions

      Replace all the Site positions attached to the Structure

      :param new_positions: list of (3D) positions for every sites.

      :param conserve_particle: if True, allows the possibility of removing a site.
          currently not implemented.

      :raises aiida.common.ModificationNotAllowed: if object is stored already
      :raises ValueError: if positions are invalid

      .. note:: it is assumed that the order of the new_positions is
          given in the same order of the one it's substituting, i.e. the
          kind of the site will not be checked.

   .. py:property:: pbc
      :canonical: aiida.orm.nodes.data.structure.StructureData.pbc

      Get the periodic boundary conditions.

      :return: a tuple of three booleans, each one tells if there are periodic
          boundary conditions for the i-th real-space direction (i=1,2,3)

   .. py:method:: set_pbc(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_pbc

      Set the periodic boundary conditions.

   .. py:property:: cell_lengths
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell_lengths

      Get the lengths of cell lattice vectors in angstroms.

   .. py:method:: set_cell_lengths(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell_lengths
      :abstractmethod:

   .. py:property:: cell_angles
      :canonical: aiida.orm.nodes.data.structure.StructureData.cell_angles

      Get the angles between the cell lattice vectors in degrees.

   .. py:method:: set_cell_angles(value)
      :canonical: aiida.orm.nodes.data.structure.StructureData.set_cell_angles
      :abstractmethod:

   .. py:property:: is_alloy
      :canonical: aiida.orm.nodes.data.structure.StructureData.is_alloy

      Return whether the structure contains any alloy kinds.

      :return: a boolean, True if at least one kind is an alloy

   .. py:property:: has_vacancies
      :canonical: aiida.orm.nodes.data.structure.StructureData.has_vacancies

      Return whether the structure has vacancies in the structure.

      :return: a boolean, True if at least one kind has a vacancy

   .. py:method:: get_cell_volume()
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_cell_volume

      Returns the three-dimensional cell volume in Angstrom^3.

      Use the `get_dimensionality` method in order to get the area/length of lower-dimensional cells.

      :return: a float.

   .. py:method:: get_cif(converter='ase', store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData.get_cif

      Creates :py:class:`aiida.orm.nodes.data.cif.CifData`.

      .. versionadded:: 1.0
         Renamed from _get_cif

      :param converter: specify the converter. Default 'ase'.
      :param store: If True, intermediate calculation gets stored in the
          AiiDA database for record. Default False.
      :return: :py:class:`aiida.orm.nodes.data.cif.CifData` node.

   .. py:method:: _get_object_phonopyatoms()
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_phonopyatoms

      Converts StructureData to PhonopyAtoms

      :return: a PhonopyAtoms object

   .. py:method:: _get_object_ase()
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_ase

      Converts
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
      to ase.Atoms

      :return: an ase.Atoms object

   .. py:method:: _get_object_pymatgen(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen

      Converts
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
      to pymatgen object

      :return: a pymatgen Structure for structures with periodic boundary
          conditions (in three dimensions) and Molecule otherwise

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors).

   .. py:method:: _get_object_pymatgen_structure(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_structure

      Converts
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
      to pymatgen Structure object
      :param add_spin: True to add the spins to the pymatgen structure.
      Default is False (no spin added).

      .. note:: The spins are set according to the following rule:

          * if the kind name ends with 1 -> spin=+1

          * if the kind name ends with 2 -> spin=-1

      :return: a pymatgen Structure object corresponding to this
        :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
        object
      :raise ValueError: if periodic boundary conditions does not hold
        in at least one dimension of real space; if there are partial occupancies
        together with spins (defined by kind names ending with '1' or '2').

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors)

   .. py:method:: _get_object_pymatgen_molecule(**kwargs)
      :canonical: aiida.orm.nodes.data.structure.StructureData._get_object_pymatgen_molecule

      Converts
      :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
      to pymatgen Molecule object

      :return: a pymatgen Molecule object corresponding to this
        :py:class:`StructureData <aiida.orm.nodes.data.structure.StructureData>`
        object.

      .. note:: Requires the pymatgen module (version >= 3.0.13, usage
          of earlier versions may cause errors)

.. py:class:: TrajectoryData(structurelist=None, **kwargs)
   :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   Stores a trajectory (a sequence of crystal structures with timestamps, and
   possibly with velocities).

   .. py:method:: _internal_validate(stepids, cells, symbols, positions, times, velocities)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._internal_validate

      Internal function to validate the type and shape of the arrays. See
      the documentation of py:meth:`.set_trajectory` for a description of the
      valid shape and type of the parameters.

   .. py:method:: set_trajectory(symbols, positions, stepids=None, cells=None, times=None, velocities=None)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_trajectory

      Store the whole trajectory, after checking that types and dimensions
      are correct.

      Parameters ``stepids``, ``cells`` and ``velocities`` are optional
      variables. If nothing is passed for ``cells`` or ``velocities``
      nothing will be stored. However, if no input is given for ``stepids``
      a consecutive sequence [0,1,2,...,len(positions)-1] will be assumed.


      :param symbols: string list with dimension ``n``, where ``n`` is the
                    number of atoms (i.e., sites) in the structure.
                    The same list is used for each step. Normally, the string
                    should be a valid chemical symbol, but actually any unique
                    string works and can be used as the name of the atomic kind
                    (see also the :py:meth:`.get_step_structure()` method).
      :param positions: float array with dimension :math:`s \times n \times 3`,
                    where ``s`` is the
                    length of the ``stepids`` array and ``n`` is the length
                    of the ``symbols`` array. Units are angstrom.
                    In particular,
                    ``positions[i,j,k]`` is the ``k``-th component of the
                    ``j``-th atom (or site) in the structure at the time step
                    with index ``i`` (identified
                    by step number ``step[i]`` and with timestamp ``times[i]``).
      :param stepids: integer array with dimension ``s``, where ``s`` is the
                    number of steps. Typically represents an internal counter
                    within the code. For instance, if you want to store a
                    trajectory with one step every 10, starting from step 65,
                    the array will be ``[65,75,85,...]``.
                    No checks are done on duplicate elements
                    or on the ordering, but anyway this array should be
                    sorted in ascending order, without duplicate elements.
                    (If not specified, stepids will be set to ``numpy.arange(s)``
                    by default) It is internally stored as an array named 'steps'.
      :param cells: if specified float array with dimension
                    :math:`s \times 3 \times 3`, where ``s`` is the
                    length of the ``stepids`` array. Units are angstrom.
                    In particular, ``cells[i,j,k]`` is the ``k``-th component
                    of the ``j``-th cell vector at the time step with index
                    ``i`` (identified by step number ``stepid[i]`` and with
                    timestamp ``times[i]``).
      :param times: if specified, float array with dimension ``s``, where
                    ``s`` is the length of the ``stepids`` array. Contains the
                    timestamp of each step in picoseconds (ps).
      :param velocities: if specified, must be a float array with the same
                    dimensions of the ``positions`` array.
                    The array contains the velocities in the atoms.

      .. todo :: Choose suitable units for velocities

   .. py:method:: set_structurelist(structurelist)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.set_structurelist

      Create trajectory from the list of
      :py:class:`aiida.orm.nodes.data.structure.StructureData` instances.

      :param structurelist: a list of
          :py:class:`aiida.orm.nodes.data.structure.StructureData` instances.

      :raises ValueError: if symbol lists of supplied structures are
          different

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._validate

      Verify that the required arrays are present and that their type and
      dimension are correct.

   .. py:property:: numsteps
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsteps

      Return the number of stored steps, or zero if nothing has been stored yet.

   .. py:property:: numsites
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.numsites

      Return the number of stored sites, or zero if nothing has been stored yet.

   .. py:method:: get_stepids()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_stepids

      Return the array of steps, if it has already been set.

      .. versionadded:: 0.7
         Renamed from get_steps

      :raises KeyError: if the trajectory has not been set yet.

   .. py:method:: get_times()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_times

      Return the array of times (in ps), if it has already been set.

      :raises KeyError: if the trajectory has not been set yet.

   .. py:method:: get_cells()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cells

      Return the array of cells, if it has already been set.

      :raises KeyError: if the trajectory has not been set yet.

   .. py:property:: symbols
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.symbols

      Return the array of symbols, if it has already been set.

      :raises KeyError: if the trajectory has not been set yet.

   .. py:method:: get_positions()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_positions

      Return the array of positions, if it has already been set.

      :raises KeyError: if the trajectory has not been set yet.

   .. py:method:: get_velocities()
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_velocities

      Return the array of velocities, if it has already been set.

      .. note :: This function (differently from all other ``get_*``
        functions, will not raise an exception if the velocities are not
        set, but rather return ``None`` (both if no trajectory was not set yet,
        and if it the trajectory was set but no velocities were specified).

   .. py:method:: get_index_from_stepid(stepid)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_index_from_stepid

      Given a value for the stepid (i.e., a value among those of the ``steps``
      array), return the array index of that stepid, that can be used in other
      methods such as :py:meth:`.get_step_data` or
      :py:meth:`.get_step_structure`.

      .. versionadded:: 0.7
         Renamed from get_step_index

      .. note:: Note that this function returns the first index found
          (i.e. if multiple steps are present with the same value,
          only the index of the first one is returned).

      :raises ValueError: if no step with the given value is found.

   .. py:method:: get_step_data(index)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_data

      Return a tuple with all information concerning the stepid with given
      index (0 is the first step, 1 the second step and so on). If you know
      only the step value, use the :py:meth:`.get_index_from_stepid` method
      to get the corresponding index.

      If no velocities, cells, or times were specified, None is returned as
      the corresponding element.

      :return: A tuple in the format
        ``(stepid, time, cell, symbols, positions, velocities)``,
        where ``stepid`` is an integer, ``time`` is a float, ``cell`` is a
        :math:`3      imes 3` matrix, ``symbols`` is an array of length ``n``,
        positions is a :math:`n       imes 3` array, and velocities is either
        ``None`` or a :math:`n        imes 3` array

      :param index: The index of the step that you want to retrieve, from
         0 to ``self.numsteps - 1``.
      :raises IndexError: if you require an index beyond the limits.
      :raises KeyError: if you did not store the trajectory yet.

   .. py:method:: get_step_structure(index, custom_kinds=None)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_step_structure

      Return an AiiDA :py:class:`aiida.orm.nodes.data.structure.StructureData` node
      (not stored yet!) with the coordinates of the given step, identified by
      its index. If you know only the step value, use the
      :py:meth:`.get_index_from_stepid` method to get the corresponding index.

      .. note:: The periodic boundary conditions are always set to True.

      .. versionadded:: 0.7
         Renamed from step_to_structure

      :param index: The index of the step that you want to retrieve, from
         0 to ``self.numsteps- 1``.
      :param custom_kinds: (Optional) If passed must be a list of
        :py:class:`aiida.orm.nodes.data.structure.Kind` objects. There must be one
        kind object for each different string in the ``symbols`` array, with
        ``kind.name`` set to this string.
        If this parameter is omitted, the automatic kind generation of AiiDA
        :py:class:`aiida.orm.nodes.data.structure.StructureData` nodes is used,
        meaning that the strings in the ``symbols`` array must be valid
        chemical symbols.

      :return: :py:class:`aiida.orm.nodes.data.structure.StructureData` node.

   .. py:method:: _prepare_xsf(index=None, main_file_name='')
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_xsf

      Write the given trajectory to a string of format XSF (for XCrySDen).

   .. py:method:: _prepare_cif(trajectory_index=None, main_file_name='')
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._prepare_cif

      Write the given trajectory to a string of format CIF.

   .. py:method:: get_structure(store=False, **kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_structure

      Creates :py:class:`aiida.orm.nodes.data.structure.StructureData`.

      .. versionadded:: 1.0
          Renamed from _get_aiida_structure

      :param store: If True, intermediate calculation gets stored in the
          AiiDA database for record. Default False.
      :param index: The index of the step that you want to retrieve, from
         0 to ``self.numsteps- 1``.
      :param custom_kinds: (Optional) If passed must be a list of
        :py:class:`aiida.orm.nodes.data.structure.Kind` objects. There must be one
        kind object for each different string in the ``symbols`` array, with
        ``kind.name`` set to this string.
        If this parameter is omitted, the automatic kind generation of AiiDA
        :py:class:`aiida.orm.nodes.data.structure.StructureData` nodes is used,
        meaning that the strings in the ``symbols`` array must be valid
        chemical symbols.
      :param custom_cell: (Optional) The cell matrix of the structure.
        If omitted, the cell will be read from the trajectory, if present,
        otherwise the default cell of
        :py:class:`aiida.orm.nodes.data.structure.StructureData` will be used.

      :return: :py:class:`aiida.orm.nodes.data.structure.StructureData` node.

   .. py:method:: get_cif(index=None, **kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.get_cif

      Creates :py:class:`aiida.orm.nodes.data.cif.CifData`

      .. versionadded:: 1.0
         Renamed from _get_cif

   .. py:method:: _parse_xyz_pos(inputstring)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_pos

      Load positions from a XYZ file.

      .. note:: The steps and symbols must be set manually before calling this
          import function as a consistency measure. Even though the symbols
          and steps could be extracted from the XYZ file, the data present in
          the XYZ file may or may not be correct and the same logic would have
          to be present in the XYZ-velocities function. It was therefore
          decided not to implement it at all but require it to be set
          explicitly.

      Usage::

          from aiida.orm.nodes.data.array.trajectory import TrajectoryData

          t = TrajectoryData()
          # get sites and number of timesteps
          t.set_array('steps', arange(ntimesteps))
          t.set_array('symbols', array([site.kind for site in s.sites]))
          t.importfile('some-calc/AIIDA-PROJECT-pos-1.xyz', 'xyz_pos')

   .. py:method:: _parse_xyz_vel(inputstring)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData._parse_xyz_vel

      Load velocities from a XYZ file.

      .. note:: The steps and symbols must be set manually before calling this
          import function as a consistency measure. See also comment for
          :py:meth:`._parse_xyz_pos`

   .. py:method:: show_mpl_pos(**kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_pos

      Shows the positions as a function of time, separate for XYZ coordinates

      :param int stepsize: The stepsize for the trajectory, set higher than 1 to
          reduce number of points
      :param int mintime: Time to start from
      :param int maxtime: Maximum time
      :param list elements:
          A list of atomic symbols that should be displayed.
          If not specified, all atoms are displayed.
      :param list indices:
          A list of indices of that atoms that can be displayed.
          If not specified, all atoms of the correct species are displayed.
      :param bool dont_block: If True, interpreter is not blocked when figure is displayed.

   .. py:method:: show_mpl_heatmap(**kwargs)
      :canonical: aiida.orm.nodes.data.array.trajectory.TrajectoryData.show_mpl_heatmap

      Show a heatmap of the trajectory with matplotlib.

.. py:class:: UpfData(file, filename=None, **kwargs)
   :canonical: aiida.orm.nodes.data.upf.UpfData

   Bases: :py:obj:`aiida.orm.nodes.data.singlefile.SinglefileData`

   `Data` sub class to represent a pseudopotential single file in UPF format.

   .. rubric:: Initialization

   Construct a new instance and set the contents to that of the file.

   :param file: an absolute filepath or filelike object whose contents to copy.
       Hint: Pass io.BytesIO(b"my string") to construct the SinglefileData directly from a string.
   :param filename: specify filename to use (defaults to name of provided file).

   .. py:method:: get_or_create(filepath, use_first=False, store_upf=True)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_or_create
      :classmethod:

      Get the `UpfData` with the same md5 of the given file, or create it if it does not yet exist.

      :param filepath: an absolute filepath on disk
      :param use_first: if False (default), raise an exception if more than one potential is found.
          If it is True, instead, use the first available pseudopotential.
      :param store_upf: boolean, if false, the `UpfData` if created will not be stored.
      :return: tuple of `UpfData` and boolean indicating whether it was created.

   .. py:method:: store(*args, **kwargs)
      :canonical: aiida.orm.nodes.data.upf.UpfData.store

      Store the node, reparsing the file so that the md5 and the element are correctly reset.

   .. py:method:: from_md5(md5, backend=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.from_md5
      :classmethod:

      Return a list of all `UpfData` that match the given md5 hash.

      .. note:: assumes hash of stored `UpfData` nodes is stored in the `md5` attribute

      :param md5: the file hash
      :return: list of existing `UpfData` nodes that have the same md5 hash

   .. py:method:: set_file(file, filename=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.set_file

      Store the file in the repository and parse it to set the `element` and `md5` attributes.

      :param file: filepath or filelike object of the UPF potential file to store.
          Hint: Pass io.BytesIO(b"my string") to construct the file directly from a string.
      :param filename: specify filename to use (defaults to name of provided file).

   .. py:method:: get_upf_family_names()
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_family_names

      Get the list of all upf family names to which the pseudo belongs.

   .. py:property:: element
      :canonical: aiida.orm.nodes.data.upf.UpfData.element

      Return the element of the UPF pseudopotential.

      :return: the element

   .. py:property:: md5sum
      :canonical: aiida.orm.nodes.data.upf.UpfData.md5sum

      Return the md5 checksum of the UPF pseudopotential file.

      :return: the md5 checksum

   .. py:method:: _validate()
      :canonical: aiida.orm.nodes.data.upf.UpfData._validate

      Validate the UPF potential file stored for this node.

   .. py:method:: _prepare_upf(main_file_name='')
      :canonical: aiida.orm.nodes.data.upf.UpfData._prepare_upf

      Return UPF content.

   .. py:method:: get_upf_group(group_label)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_group
      :classmethod:

      Return the UPF family group with the given label.

      :param group_label: the family group label
      :return: the `Group` with the given label, if it exists

   .. py:method:: get_upf_groups(filter_elements=None, user=None, backend=None)
      :canonical: aiida.orm.nodes.data.upf.UpfData.get_upf_groups
      :classmethod:

      Return all names of groups of type UpfFamily, possibly with some filters.

      :param filter_elements: A string or a list of strings.
          If present, returns only the groups that contains one UPF for every element present in the list. The default
          is `None`, meaning that all families are returned.
      :param user: if None (default), return the groups for all users.
          If defined, it should be either a `User` instance or the user email.
      :return: list of `Group` entities of type UPF.

   .. py:method:: _prepare_json(main_file_name='')
      :canonical: aiida.orm.nodes.data.upf.UpfData._prepare_json

      Returns UPF PP in json format.

.. py:class:: UpfFamily(label: typing.Optional[str] = None, user: typing.Optional[aiida.orm.User] = None, description: str = '', type_string: typing.Optional[str] = None, backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.groups.UpfFamily

   Bases: :py:obj:`aiida.orm.groups.Group`

   Group that represents a pseudo potential family containing `UpfData` nodes.

   .. rubric:: Initialization

   Create a new group. Either pass a dbgroup parameter, to reload
   a group from the DB (and then, no further parameters are allowed),
   or pass the parameters for the Group creation.

   :param label: The group label, required on creation
   :param description: The group description (by default, an empty string)
   :param user: The owner of the group (by default, the automatic user)
   :param type_string: a string identifying the type of group (by default,
       an empty string, indicating an user-defined group.

.. py:class:: User(email: str, first_name: str = '', last_name: str = '', institution: str = '', backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.orm.users.User

   Bases: :py:obj:`aiida.orm.entities.Entity`\ [\ :py:obj:`aiida.orm.implementation.BackendUser`\ , :py:obj:`aiida.orm.users.UserCollection`\ ]

   AiiDA User

   .. rubric:: Initialization

   Create a new `User`.

   .. py:attribute:: _CLS_COLLECTION
      :canonical: aiida.orm.users.User._CLS_COLLECTION
      :value: None

   .. py:method:: __str__() -> str
      :canonical: aiida.orm.users.User.__str__

   .. py:method:: normalize_email(email: str) -> str
      :canonical: aiida.orm.users.User.normalize_email
      :staticmethod:

      Normalize the address by lowercasing the domain part of the email address (taken from Django).

   .. py:property:: email
      :canonical: aiida.orm.users.User.email
      :type: str

   .. py:property:: first_name
      :canonical: aiida.orm.users.User.first_name
      :type: str

   .. py:property:: last_name
      :canonical: aiida.orm.users.User.last_name
      :type: str

   .. py:property:: institution
      :canonical: aiida.orm.users.User.institution
      :type: str

   .. py:method:: get_full_name() -> str
      :canonical: aiida.orm.users.User.get_full_name

      Return the user full name

      :return: the user full name

   .. py:method:: get_short_name() -> str
      :canonical: aiida.orm.users.User.get_short_name

      Return the user short name (typically, this returns the email)

      :return: The short name

   .. py:property:: uuid
      :canonical: aiida.orm.users.User.uuid
      :type: None

      For now users do not have UUIDs so always return None

.. py:class:: WorkChainNode
   :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode

   Bases: :py:obj:`aiida.orm.nodes.process.workflow.workflow.WorkflowNode`

   ORM class for all nodes representing the execution of a WorkChain.

   .. py:attribute:: STEPPER_STATE_INFO_KEY
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.STEPPER_STATE_INFO_KEY
      :value: 'stepper_state_info'

   .. py:method:: _updatable_attributes() -> typing.Tuple[str, ...]
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode._updatable_attributes

   .. py:property:: stepper_state_info
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.stepper_state_info
      :type: typing.Optional[str]

      Return the stepper state info

      :returns: string representation of the stepper state info

   .. py:method:: set_stepper_state_info(stepper_state_info: str) -> None
      :canonical: aiida.orm.nodes.process.workflow.workchain.WorkChainNode.set_stepper_state_info

      Set the stepper state info

      :param state: string representation of the stepper state info

.. py:class:: WorkFunctionNode
   :canonical: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode

   Bases: :py:obj:`aiida.orm.utils.mixins.FunctionCalculationMixin`, :py:obj:`aiida.orm.nodes.process.workflow.workflow.WorkflowNode`

   ORM class for all nodes representing the execution of a workfunction.

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.workflow.workfunction.WorkFunctionNode._CLS_NODE_LINKS
      :value: None

.. py:class:: WorkflowNode(backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None, user: typing.Optional[aiida.orm.users.User] = None, computer: typing.Optional[aiida.orm.computers.Computer] = None, **kwargs: typing.Any)
   :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode

   Bases: :py:obj:`aiida.orm.nodes.process.process.ProcessNode`

   Base class for all nodes representing the execution of a workflow process.

   .. rubric:: Initialization

   :param backend_entity: the backend model supporting this entity

   .. py:attribute:: _CLS_NODE_LINKS
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._CLS_NODE_LINKS
      :value: None

   .. py:attribute:: _storable
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._storable
      :value: True

   .. py:attribute:: _unstorable_message
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode._unstorable_message
      :value: 'storing for this node has been disabled'

   .. py:property:: inputs
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.inputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      Return an instance of `NodeLinksManager` to manage incoming INPUT_WORK links

      The returned Manager allows you to easily explore the nodes connected to this node
      via an incoming INPUT_WORK link.
      The incoming nodes are reachable by their link labels which are attributes of the manager.

      :return: `NodeLinksManager`

   .. py:property:: outputs
      :canonical: aiida.orm.nodes.process.workflow.workflow.WorkflowNode.outputs
      :type: aiida.orm.utils.managers.NodeLinksManager

      Return an instance of `NodeLinksManager` to manage outgoing RETURN links

      The returned Manager allows you to easily explore the nodes connected to this node
      via an outgoing RETURN link.
      The outgoing nodes are reachable by their link labels which are attributes of the manager.

      :return: `NodeLinksManager`

.. py:class:: XyData
   :canonical: aiida.orm.nodes.data.array.xy.XyData

   Bases: :py:obj:`aiida.orm.nodes.data.array.array.ArrayData`

   A subclass designed to handle arrays that have an "XY" relationship to
   each other. That is there is one array, the X array, and there are several
   Y arrays, which can be considered functions of X.

   .. py:method:: _arrayandname_validator(array, name, units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData._arrayandname_validator
      :staticmethod:

      Validates that the array is an numpy.ndarray and that the name is
      of type str. Raises TypeError or ValueError if this not the case.

   .. py:method:: set_x(x_array, x_name, x_units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData.set_x

      Sets the array and the name for the x values.

      :param x_array: A numpy.ndarray, containing only floats
      :param x_name: a string for the x array name
      :param x_units: the units of x

   .. py:method:: set_y(y_arrays, y_names, y_units)
      :canonical: aiida.orm.nodes.data.array.xy.XyData.set_y

      Set array(s) for the y part of the dataset. Also checks if the
      x_array has already been set, and that, the shape of the y_arrays
      agree with the x_array.
      :param y_arrays: A list of y_arrays, numpy.ndarray
      :param y_names: A list of strings giving the names of the y_arrays
      :param y_units: A list of strings giving the units of the y_arrays

   .. py:method:: get_x()
      :canonical: aiida.orm.nodes.data.array.xy.XyData.get_x

      Tries to retrieve the x array and x name raises a NotExistent
      exception if no x array has been set yet.
      :return x_name: the name set for the x_array
      :return x_array: the x array set earlier
      :return x_units: the x units set earlier

   .. py:method:: get_y()
      :canonical: aiida.orm.nodes.data.array.xy.XyData.get_y

      Tries to retrieve the y arrays and the y names, raises a
      NotExistent exception if they have not been set yet, or cannot be
      retrieved
      :return y_names: list of strings naming the y_arrays
      :return y_arrays: list of y_arrays
      :return y_units: list of strings giving the units for the y_arrays

.. py:function:: cif_from_ase(ase, full_occupancies=False, add_fake_biso=False)
   :canonical: aiida.orm.nodes.data.cif.cif_from_ase

   Construct a CIF datablock from the ASE structure. The code is taken
   from
   https://wiki.fysik.dtu.dk/ase/ase/io/formatoptions.html#ase.io.cif.write_cif,
   as the original ASE code contains a bug in printing the
   Hermann-Mauguin symmetry space group symbol.

   :param ase: ASE "images"
   :return: array of CIF datablocks

.. py:function:: find_bandgap(bandsdata, number_electrons=None, fermi_energy=None)
   :canonical: aiida.orm.nodes.data.array.bands.find_bandgap

   Tries to guess whether the bandsdata represent an insulator.
   This method is meant to be used only for electronic bands (not phonons)
   By default, it will try to use the occupations to guess the number of
   electrons and find the Fermi Energy, otherwise, it can be provided
   explicitely.
   Also, there is an implicit assumption that the kpoints grid is
   "sufficiently" dense, so that the bandsdata are not missing the
   intersection between valence and conduction band if present.
   Use this function with care!

   :param number_electrons: (optional, float) number of electrons in the unit cell
   :param fermi_energy: (optional, float) value of the fermi energy.

   :note: By default, the algorithm uses the occupations array
     to guess the number of electrons and the occupied bands. This is to be
     used with care, because the occupations could be smeared so at a
     non-zero temperature, with the unwanted effect that the conduction bands
     might be occupied in an insulator.
     Prefer to pass the number_of_electrons explicitly

   :note: Only one between number_electrons and fermi_energy can be specified at the
     same time.

   :return: (is_insulator, gap), where is_insulator is a boolean, and gap a
            float. The gap is None in case of a metal, zero when the homo is
            equal to the lumo (e.g. in semi-metals).

.. py:function:: get_loader(orm_class)
   :canonical: aiida.orm.utils.loaders.get_loader

   Return the correct OrmEntityLoader for the given orm class.

   :param orm_class: the orm class
   :returns: a subclass of OrmEntityLoader
   :raises ValueError: if no OrmEntityLoader subclass can be found for the given orm class

.. py:function:: get_query_type_from_type_string(type_string)
   :canonical: aiida.orm.utils.node.get_query_type_from_type_string

   Take the type string of a Node and create the queryable type string

   :param type_string: the plugin_type_string attribute of a Node
   :return: the type string that can be used to query for

.. py:function:: get_type_string_from_class(class_module, class_name)
   :canonical: aiida.orm.utils.node.get_type_string_from_class

   Given the module and name of a class, determine the orm_class_type string, which codifies the
   orm class that is to be used. The returned string will always have a terminating period, which
   is required to query for the string in the database

   :param class_module: module of the class
   :param class_name: name of the class

.. py:function:: has_pycifrw()
   :canonical: aiida.orm.nodes.data.cif.has_pycifrw

   :return: True if the PyCifRW module can be imported, False otherwise.

.. py:function:: load_code(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Code
   :canonical: aiida.orm.utils.loaders.load_code

   Load a Code instance by one of its identifiers: pk, uuid or label

   If the type of the identifier is unknown simply pass it without a keyword and the loader will attempt to
   automatically infer the type.

   :param identifier: pk (integer), uuid (string) or label (string) of a Code
   :param pk: pk of a Code
   :param uuid: uuid of a Code, or the beginning of the uuid
   :param label: label of a Code
   :param sub_classes: an optional tuple of orm classes to narrow the queryset. Each class should be a strict sub class
       of the ORM class of the given entity loader.
   :param bool query_with_dashes: allow to query for a uuid with dashes
   :return: the Code instance
   :raise ValueError: if none or more than one of the identifiers are supplied
   :raise TypeError: if the provided identifier has the wrong type
   :raise aiida.common.NotExistent: if no matching Code is found
   :raise aiida.common.MultipleObjectsError: if more than one Code was found

.. py:function:: load_computer(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Computer
   :canonical: aiida.orm.utils.loaders.load_computer

   Load a Computer instance by one of its identifiers: pk, uuid or label

   If the type of the identifier is unknown simply pass it without a keyword and the loader will attempt to
   automatically infer the type.

   :param identifier: pk (integer), uuid (string) or label (string) of a Computer
   :param pk: pk of a Computer
   :param uuid: uuid of a Computer, or the beginning of the uuid
   :param label: label of a Computer
   :param sub_classes: an optional tuple of orm classes to narrow the queryset. Each class should be a strict sub class
       of the ORM class of the given entity loader.
   :param bool query_with_dashes: allow to query for a uuid with dashes
   :return: the Computer instance
   :raise ValueError: if none or more than one of the identifiers are supplied
   :raise TypeError: if the provided identifier has the wrong type
   :raise aiida.common.NotExistent: if no matching Computer is found
   :raise aiida.common.MultipleObjectsError: if more than one Computer was found

.. py:function:: load_entity(entity_loader=None, identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True)
   :canonical: aiida.orm.utils.loaders.load_entity

   Load an entity instance by one of its identifiers: pk, uuid or label

   If the type of the identifier is unknown simply pass it without a keyword and the loader will attempt to
   automatically infer the type.

   :param identifier: pk (integer), uuid (string) or label (string) of a Code
   :param pk: pk of a Code
   :param uuid: uuid of a Code, or the beginning of the uuid
   :param label: label of a Code
   :param sub_classes: an optional tuple of orm classes to narrow the queryset. Each class should be a strict sub class
       of the ORM class of the given entity loader.
   :param bool query_with_dashes: allow to query for a uuid with dashes
   :returns: the Code instance
   :raise ValueError: if none or more than one of the identifiers are supplied
   :raise TypeError: if the provided identifier has the wrong type
   :raise aiida.common.NotExistent: if no matching Code is found
   :raise aiida.common.MultipleObjectsError: if more than one Code was found

.. py:function:: load_group(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Group
   :canonical: aiida.orm.utils.loaders.load_group

   Load a Group instance by one of its identifiers: pk, uuid or label

   If the type of the identifier is unknown simply pass it without a keyword and the loader will attempt to
   automatically infer the type.

   :param identifier: pk (integer), uuid (string) or label (string) of a Group
   :param pk: pk of a Group
   :param uuid: uuid of a Group, or the beginning of the uuid
   :param label: label of a Group
   :param sub_classes: an optional tuple of orm classes to narrow the queryset. Each class should be a strict sub class
       of the ORM class of the given entity loader.
   :param bool query_with_dashes: allow to query for a uuid with dashes
   :return: the Group instance
   :raise ValueError: if none or more than one of the identifiers are supplied
   :raise TypeError: if the provided identifier has the wrong type
   :raise aiida.common.NotExistent: if no matching Group is found
   :raise aiida.common.MultipleObjectsError: if more than one Group was found

.. py:function:: load_node(identifier=None, pk=None, uuid=None, label=None, sub_classes=None, query_with_dashes=True) -> aiida.orm.Node
   :canonical: aiida.orm.utils.loaders.load_node

   Load a node by one of its identifiers: pk or uuid. If the type of the identifier is unknown
   simply pass it without a keyword and the loader will attempt to infer the type

   :param identifier: pk (integer) or uuid (string)
   :param pk: pk of a node
   :param uuid: uuid of a node, or the beginning of the uuid
   :param label: label of a Node
   :param sub_classes: an optional tuple of orm classes to narrow the queryset. Each class should be a strict sub class
       of the ORM class of the given entity loader.
   :param bool query_with_dashes: allow to query for a uuid with dashes
   :returns: the node instance
   :raise ValueError: if none or more than one of the identifiers are supplied
   :raise TypeError: if the provided identifier has the wrong type
   :raise aiida.common.NotExistent: if no matching Node is found
   :raise aiida.common.MultipleObjectsError: if more than one Node was found

.. py:function:: load_node_class(type_string)
   :canonical: aiida.orm.utils.node.load_node_class

   Return the `Node` sub class that corresponds to the given type string.

   :param type_string: the `type` string of the node
   :return: a sub class of `Node`

.. py:function:: pycifrw_from_cif(datablocks, loops=None, names=None)
   :canonical: aiida.orm.nodes.data.cif.pycifrw_from_cif

   Constructs PyCifRW's CifFile from an array of CIF datablocks.

   :param datablocks: an array of CIF datablocks
   :param loops: optional dict of lists of CIF tag loops.
   :param names: optional list of datablock names
   :return: CifFile

.. py:function:: to_aiida_type(value)
   :canonical: aiida.orm.nodes.data.base.to_aiida_type

   Turns basic Python types (str, int, float, bool) into the corresponding AiiDA types.

.. py:function:: validate_link(source: aiida.orm.Node, target: aiida.orm.Node, link_type: aiida.common.links.LinkType, link_label: str, backend: typing.Optional[aiida.orm.implementation.storage_backend.StorageBackend] = None) -> None
   :canonical: aiida.orm.utils.links.validate_link

   Validate adding a link of the given type and label from a given node to ourself.

   This function will first validate the class types of the inputs and will subsequently validate whether a link of
   the specified type is allowed at all between the nodes types of the source and target.

   Subsequently, the validity of the "indegree" and "outdegree" of the proposed link is validated, which means
   validating that the uniqueness constraints of the incoming links into the target node and the outgoing links from
   the source node are not violated. In AiiDA's provenance graph each link type has one of the following three types
   of "degree" character::

       * unique
       * unique pair
       * unique triple

   Each degree character has a different unique constraint on its links, here defined for the indegree::

       * unique: any target node, it can only have a single incoming link of this type, regardless of the link label.
       * unique pair: a node can have an infinite amount of incoming links of this type, as long as the labels within
           that sub set, are unique. In short, it is the link pair, i.e. the tuple of the link type and label, that has
           a uniquess constraint for the incoming links to a given node.
       * unique triple: a node can have an infinite amount of incoming links of this type, as long as the triple tuple
           of source node, link type and link label is unique. In other words, it is the link triple that has a
           uniqueness constraint for the incoming links.

   The same holds for outdegree, but then it concerns outgoing links from the source node to the target node.

   For illustration purposes, consider the following example provenance graphs that are considered legal, where
   `WN`, `DN` and `CN` represent a `WorkflowNode`, a `DataNode` and a `CalculationNode`, respectively::

                   1                    2                    3
           ______     ______          ______          ______     ______
          |      |   |      |        |      |        |      |   |      |
          |  WN  |   |  DN  |        |  DN  |        |  WN  |   |  WN  |
          |______|   |______|        |______|        |______|   |______|
               |     /                |   |               |     /
             a |    / a             a |   | b           a |    / a
              _|___/                  |___|_             _|___/
             |      |                |      |           |      |
             |  CN  |                |  CN  |           |  DN  |
             |______|                |______|           |______|

   In example 1, the link uniqueness constraint is not violated because despite the labels having the same label `a`,
   their link types, `CALL_CALC` and `INPUT_CALC`, respectively, are different and their `unique_pair` indegree is
   not violated.

   Similarly, in the second example, the constraint is not violated, because despite both links having the same link
   type `INPUT_CALC`, the have different labels, so the `unique_pair` indegree of the `INPUT_CALC` is not violated.

   Finally, in the third example, we see two `WorkflowNodes` both returning the same `DataNode` and with the same
   label. Despite the two incoming links here having both the same type as well as the same label, the uniqueness
   constraint is not violated, because the indegree for `RETURN` links is `unique_triple` which means that the triple
   of source node and link type and label should be unique.

   :param source: the node from which the link is coming
   :param target: the node to which the link is going
   :param link_type: the type of link
   :param link_label: link label
   :raise TypeError: if `source` or `target` is not a Node instance, or `link_type` is not a `LinkType` enum
   :raise ValueError: if the proposed link is invalid
