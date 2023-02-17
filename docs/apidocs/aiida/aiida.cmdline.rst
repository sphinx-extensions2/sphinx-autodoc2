:py:mod:`aiida.cmdline`
=======================

.. py:module:: aiida.cmdline


Description
-----------

The command line interface of AiiDA.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbsolutePathParamType <aiida.cmdline.params.types.path.AbsolutePathParamType>`
     - The ParamType for identifying absolute Paths (derived from click.Path).
   * - :py:obj:`CalculationParamType <aiida.cmdline.params.types.calculation.CalculationParamType>`
     - The ParamType for identifying Calculation entities or its subclasses
   * - :py:obj:`CodeParamType <aiida.cmdline.params.types.code.CodeParamType>`
     - The ParamType for identifying Code entities or its subclasses
   * - :py:obj:`ComputerParamType <aiida.cmdline.params.types.computer.ComputerParamType>`
     - The ParamType for identifying Computer entities or its subclasses
   * - :py:obj:`ConfigOptionParamType <aiida.cmdline.params.types.config.ConfigOptionParamType>`
     - ParamType for configuration options.
   * - :py:obj:`DataParamType <aiida.cmdline.params.types.data.DataParamType>`
     - The ParamType for identifying Data entities or its subclasses
   * - :py:obj:`DynamicEntryPointCommandGroup <aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup>`
     - Subclass of :class:`click.Group` that loads subcommands dynamically from entry points.
   * - :py:obj:`EmailType <aiida.cmdline.params.types.strings.EmailType>`
     - Parameter whose values have to correspond to a valid email address format.
   * - :py:obj:`EntryPointType <aiida.cmdline.params.types.strings.EntryPointType>`
     - Parameter whose values have to be valid Python entry point strings.
   * - :py:obj:`FileOrUrl <aiida.cmdline.params.types.path.FileOrUrl>`
     - Extension of click's File-type to include URLs.
   * - :py:obj:`GroupParamType <aiida.cmdline.params.types.group.GroupParamType>`
     - The ParamType for identifying Group entities or its subclasses.
   * - :py:obj:`HostnameType <aiida.cmdline.params.types.strings.HostnameType>`
     - Parameter corresponding to a valid hostname (or empty) string.
   * - :py:obj:`IdentifierParamType <aiida.cmdline.params.types.identifier.IdentifierParamType>`
     - An extension of click.ParamType for a generic identifier parameter. In AiiDA, orm entities can often be identified by either their ID, UUID or optionally some LABEL identifier. This parameter type implements the convert method, which attempts to convert a value passed to the command for a parameter with this type, to an orm entity. The actual loading of the entity is delegated to the orm class loader. Subclasses of this parameter type should implement the `orm_class_loader` method to return the appropriate orm class loader, which should be a subclass of `aiida.orm.utils.loaders.OrmEntityLoader` for the corresponding orm class.
   * - :py:obj:`LabelStringType <aiida.cmdline.params.types.strings.LabelStringType>`
     - Parameter accepting valid label strings.
   * - :py:obj:`LazyChoice <aiida.cmdline.params.types.choice.LazyChoice>`
     - This is a delegate of click's Choice ParamType that evaluates the set of choices lazily. This is useful if the choices set requires an import that is slow. Using the vanilla click.Choice will call this on import which will slow down verdi and its autocomplete. This type will generate the choices set lazily through the choices property
   * - :py:obj:`MpirunCommandParamType <aiida.cmdline.params.types.computer.MpirunCommandParamType>`
     - Custom click param type for mpirun-command
   * - :py:obj:`MultipleValueParamType <aiida.cmdline.params.types.multiple.MultipleValueParamType>`
     - An extension of click.ParamType that can parse multiple values for a given ParamType
   * - :py:obj:`NodeParamType <aiida.cmdline.params.types.node.NodeParamType>`
     - The ParamType for identifying Node entities or its subclasses
   * - :py:obj:`NonEmptyStringParamType <aiida.cmdline.params.types.strings.NonEmptyStringParamType>`
     - Parameter whose values have to be string and non-empty.
   * - :py:obj:`PathOrUrl <aiida.cmdline.params.types.path.PathOrUrl>`
     - Extension of click's Path-type to include URLs.
   * - :py:obj:`PluginParamType <aiida.cmdline.params.types.plugin.PluginParamType>`
     - AiiDA Plugin name parameter type.
   * - :py:obj:`ProcessParamType <aiida.cmdline.params.types.process.ProcessParamType>`
     - The ParamType for identifying ProcessNode entities or its subclasses
   * - :py:obj:`ProfileParamType <aiida.cmdline.params.types.profile.ProfileParamType>`
     - The profile parameter type for click.
   * - :py:obj:`ShebangParamType <aiida.cmdline.params.types.computer.ShebangParamType>`
     - Custom click param type for shebang line
   * - :py:obj:`UserParamType <aiida.cmdline.params.types.user.UserParamType>`
     - The user parameter type for click.   Can get or create a user.
   * - :py:obj:`VerdiCommandGroup <aiida.cmdline.groups.verdi.VerdiCommandGroup>`
     - Subclass of :class:`click.Group` for the ``verdi`` CLI.
   * - :py:obj:`WorkflowParamType <aiida.cmdline.params.types.workflow.WorkflowParamType>`
     - The ParamType for identifying WorkflowNode entities or its subclasses

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`dbenv <aiida.cmdline.utils.decorators.dbenv>`
     - Loads the dbenv for a specific region of code, does not unload afterwards
   * - :py:obj:`echo_critical <aiida.cmdline.utils.echo.echo_critical>`
     - Log a critical error message to the cmdline logger and exit with ``exit_status``.
   * - :py:obj:`echo_dictionary <aiida.cmdline.utils.echo.echo_dictionary>`
     - Log the given dictionary to stdout in the given format
   * - :py:obj:`echo_error <aiida.cmdline.utils.echo.echo_error>`
     - Log an error message to the cmdline logger.
   * - :py:obj:`echo_info <aiida.cmdline.utils.echo.echo_info>`
     - Log an info message to the cmdline logger.
   * - :py:obj:`echo_report <aiida.cmdline.utils.echo.echo_report>`
     - Log an report message to the cmdline logger.
   * - :py:obj:`echo_success <aiida.cmdline.utils.echo.echo_success>`
     - Log a success message to the cmdline logger.
   * - :py:obj:`echo_warning <aiida.cmdline.utils.echo.echo_warning>`
     - Log a warning message to the cmdline logger.
   * - :py:obj:`format_call_graph <aiida.cmdline.utils.ascii_vis.format_call_graph>`
     - Print a tree like the POSIX tree command for the calculation call graph
   * - :py:obj:`is_verbose <aiida.cmdline.utils.common.is_verbose>`
     - Return whether the configured logging verbosity is considered verbose, i.e., equal or lower to ``INFO`` level.
   * - :py:obj:`only_if_daemon_running <aiida.cmdline.utils.decorators.only_if_daemon_running>`
     - Function decorator for CLI command to print critical error and exit automatically when daemon is not running.
   * - :py:obj:`with_dbenv <aiida.cmdline.utils.decorators.with_dbenv>`
     - Function decorator that will load the database environment for the currently loaded profile.

API
~~~

.. py:class:: AbsolutePathParamType
   :canonical: aiida.cmdline.params.types.path.AbsolutePathParamType

   Bases: :py:obj:`click.Path`

   The ParamType for identifying absolute Paths (derived from click.Path).

   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.path.AbsolutePathParamType.name
      :value: 'AbsolutePath'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.path.AbsolutePathParamType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.path.AbsolutePathParamType.__repr__

.. py:class:: CalculationParamType
   :canonical: aiida.cmdline.params.types.calculation.CalculationParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Calculation entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.calculation.CalculationParamType.name
      :value: 'Calculation'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.calculation.CalculationParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


.. py:class:: CodeParamType(sub_classes=None, entry_point=None)
   :canonical: aiida.cmdline.params.types.code.CodeParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Code entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.code.CodeParamType.name
      :value: 'Code'

   .. py:method:: __init__(sub_classes=None, entry_point=None)
      :canonical: aiida.cmdline.params.types.code.CodeParamType.__init__

      Construct the param type

      :param sub_classes: specify a tuple of Code sub classes to narrow the query set
      :param entry_point: specify an optional calculation entry point that the Code's input plugin should match


   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.code.CodeParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.code.CodeParamType.shell_complete

      Return possible completions based on an incomplete value.

      :returns: list of tuples of valid entry points (matching incomplete) and a description


   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.code.CodeParamType.convert

.. py:class:: ComputerParamType
   :canonical: aiida.cmdline.params.types.computer.ComputerParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Computer entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.computer.ComputerParamType.name
      :value: 'Computer'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.computer.ComputerParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.computer.ComputerParamType.shell_complete

      Return possible completions based on an incomplete value.

      :returns: list of tuples of valid entry points (matching incomplete) and a description


.. py:class:: ConfigOptionParamType
   :canonical: aiida.cmdline.params.types.config.ConfigOptionParamType

   Bases: :py:obj:`click.types.StringParamType`

   ParamType for configuration options.

   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.config.ConfigOptionParamType.name
      :value: 'config option'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.config.ConfigOptionParamType.convert

   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.config.ConfigOptionParamType.shell_complete

      Return possible completions based on an incomplete value

      :returns: list of tuples of valid entry points (matching incomplete) and a description


.. py:class:: DataParamType(sub_classes=None)
   :canonical: aiida.cmdline.params.types.data.DataParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Data entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.data.DataParamType.name
      :value: 'Data'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.data.DataParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


.. py:class:: DynamicEntryPointCommandGroup(command, entry_point_group: str, entry_point_name_filter='.*', **kwargs)
   :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup

   Bases: :py:obj:`aiida.cmdline.groups.verdi.VerdiCommandGroup`

   Subclass of :class:`click.Group` that loads subcommands dynamically from entry points.

   A command group using this class will automatically generate the sub commands from the entry points registered in
   the given ``entry_point_group``. The entry points can be additionally filtered using a regex defined for the
   ``entry_point_name_filter`` keyword. The actual command for each entry point is defined by ``command``, which should
   take as a first argument the class that corresponds to the entry point. In addition, it should accept ``kwargs``
   which will be the values for the options passed when the command is invoked. The help string of the command will be
   provided by the docstring of the class registered at the respective entry point. Example usage:

   .. code:: python

       def create_instance(cls, **kwargs):
           instance = cls(**kwargs)
           instance.store()
           echo.echo_success(f'Created {cls.__name__}<{instance.pk}>')

       @click.group('create', cls=DynamicEntryPointCommandGroup, command=create_instance,)
       def cmd_create():
           pass



   .. py:method:: __init__(command, entry_point_group: str, entry_point_name_filter='.*', **kwargs)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.__init__

   .. py:method:: list_commands(ctx) -> list[str]
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.list_commands

      Return the sorted list of subcommands for this group.

      :param ctx: The :class:`click.Context`.


   .. py:method:: get_command(ctx, cmd_name)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.get_command

      Return the command with the given name.

      :param ctx: The :class:`click.Context`.
      :param cmd_name: The name of the command.
      :returns: The :class:`click.Command`.


   .. py:method:: create_command(entry_point)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.create_command

      Create a subcommand for the given ``entry_point``.

   .. py:method:: create_options(entry_point)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.create_options

      Create the option decorators for the command function for the given entry point.

      :param entry_point: The entry point.


   .. py:method:: list_options(entry_point)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.list_options

      Return the list of options that should be applied to the command for the given entry point.

      :param entry_point: The entry point.


   .. py:method:: create_option(name, spec)
      :canonical: aiida.cmdline.groups.dynamic.DynamicEntryPointCommandGroup.create_option
      :staticmethod:

      Create a click option from a name and a specification.

.. py:class:: EmailType
   :canonical: aiida.cmdline.params.types.strings.EmailType

   Bases: :py:obj:`click.types.StringParamType`

   Parameter whose values have to correspond to a valid email address format.

   .. note:: For the moment, we do not require the domain suffix, i.e. 'aiida@localhost' is still valid.


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.strings.EmailType.name
      :value: 'email'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.strings.EmailType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.strings.EmailType.__repr__

.. py:class:: EntryPointType
   :canonical: aiida.cmdline.params.types.strings.EntryPointType

   Bases: :py:obj:`aiida.cmdline.params.types.strings.NonEmptyStringParamType`

   Parameter whose values have to be valid Python entry point strings.

   See https://packaging.python.org/en/latest/specifications/entry-points/


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.strings.EntryPointType.name
      :value: 'entrypoint'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.strings.EntryPointType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.strings.EntryPointType.__repr__

.. py:class:: FileOrUrl(timeout_seconds=URL_TIMEOUT_SECONDS, **kwargs)
   :canonical: aiida.cmdline.params.types.path.FileOrUrl

   Bases: :py:obj:`click.File`

   Extension of click's File-type to include URLs.

   Returns handle either to local file or to remote file fetched from URL.

   :param int timeout_seconds: Maximum timeout accepted for URL response.
       Must be an integer in the range [0;60].


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.path.FileOrUrl.name
      :value: 'FileOrUrl'

   .. py:method:: __init__(timeout_seconds=URL_TIMEOUT_SECONDS, **kwargs)
      :canonical: aiida.cmdline.params.types.path.FileOrUrl.__init__

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.path.FileOrUrl.convert

      Return file handle.

   .. py:method:: get_url(url, param, ctx)
      :canonical: aiida.cmdline.params.types.path.FileOrUrl.get_url

      Retrieve file from URL.

.. py:class:: GroupParamType(create_if_not_exist=False, sub_classes=('aiida.groups:core', ))
   :canonical: aiida.cmdline.params.types.group.GroupParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Group entities or its subclasses.

   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.group.GroupParamType.name
      :value: 'Group'

   .. py:method:: __init__(create_if_not_exist=False, sub_classes=('aiida.groups:core', ))
      :canonical: aiida.cmdline.params.types.group.GroupParamType.__init__

      Construct the parameter type.

      The `sub_classes` argument can be used to narrow the set of subclasses of `Group` that should be matched. By
      default all subclasses of `Group` will be matched, otherwise it is restricted to the subclasses that correspond
      to the entry point names in the tuple of `sub_classes`.

      To prevent having to load the database environment at import time, the actual loading of the entry points is
      deferred until the call to `convert` is made. This is to keep the command line autocompletion light and
      responsive. The entry point strings will be validated, however, to see if they correspond to known entry points.

      :param create_if_not_exist: boolean, if True, will create the group if it does not yet exist. By default the
          group created will be of class `Group`, unless another subclass is specified through `sub_classes`. Note
          that in this case, only a single entry point name can be specified
      :param sub_classes: a tuple of entry point strings from the `aiida.groups` entry point group.


   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.group.GroupParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of `OrmEntityLoader`.

      This class is supposed to be used to load the entity for a given identifier.

      :return: the orm entity loader class for this `ParamType`


   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.group.GroupParamType.shell_complete

      Return possible completions based on an incomplete value.

      :returns: list of tuples of valid entry points (matching incomplete) and a description


   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.group.GroupParamType.convert

.. py:class:: HostnameType
   :canonical: aiida.cmdline.params.types.strings.HostnameType

   Bases: :py:obj:`click.types.StringParamType`

   Parameter corresponding to a valid hostname (or empty) string.

   Regex according to https://stackoverflow.com/a/3824105/1069467


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.strings.HostnameType.name
      :value: 'hostname'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.strings.HostnameType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.strings.HostnameType.__repr__

.. py:class:: IdentifierParamType(sub_classes=None)
   :canonical: aiida.cmdline.params.types.identifier.IdentifierParamType

   Bases: :py:obj:`click.ParamType`, :py:obj:`abc.ABC`

   An extension of click.ParamType for a generic identifier parameter. In AiiDA, orm entities can often be
   identified by either their ID, UUID or optionally some LABEL identifier. This parameter type implements
   the convert method, which attempts to convert a value passed to the command for a parameter with this type,
   to an orm entity. The actual loading of the entity is delegated to the orm class loader. Subclasses of this
   parameter type should implement the `orm_class_loader` method to return the appropriate orm class loader,
   which should be a subclass of `aiida.orm.utils.loaders.OrmEntityLoader` for the corresponding orm class.


   .. py:method:: __init__(sub_classes=None)
      :canonical: aiida.cmdline.params.types.identifier.IdentifierParamType.__init__

      Construct the parameter type, optionally specifying a tuple of entry points that reference classes
      that should be a sub class of the base orm class of the orm class loader. The classes pointed to by
      these entry points will be passed to the OrmEntityLoader when converting an identifier and they will
      restrict the query set by demanding that the class of the corresponding entity matches these sub classes.

      To prevent having to load the database environment at import time, the actual loading of the entry points
      is deferred until the call to `convert` is made. This is to keep the command line autocompletion light
      and responsive. The entry point strings will be validated, however, to see if the correspond to known
      entry points.

      :param sub_classes: a tuple of entry point strings that can narrow the set of orm classes that values
          will be mapped upon. These classes have to be strict sub classes of the base orm class defined
          by the orm class loader


   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.identifier.IdentifierParamType.orm_class_loader
      :abstractmethod:

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.identifier.IdentifierParamType.convert

      Attempt to convert the given value to an instance of the orm class using the orm class loader.

      :return: the loaded orm entity
      :raises click.BadParameter: if the value is ambiguous and leads to multiple entities
      :raises click.BadParameter: if the value cannot be mapped onto any existing instance
      :raises RuntimeError: if the defined orm class loader is not a subclass of the OrmEntityLoader class


.. py:class:: LabelStringType
   :canonical: aiida.cmdline.params.types.strings.LabelStringType

   Bases: :py:obj:`aiida.cmdline.params.types.strings.NonEmptyStringParamType`

   Parameter accepting valid label strings.

   Non-empty string, made up of word characters (includes underscores [1]), dashes, and dots.

   [1] See https://docs.python.org/3/library/re.html


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.strings.LabelStringType.name
      :value: 'labelstring'

   .. py:attribute:: ALPHABET
      :canonical: aiida.cmdline.params.types.strings.LabelStringType.ALPHABET
      :value: '\\w\\.\\-'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.strings.LabelStringType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.strings.LabelStringType.__repr__

.. py:class:: LazyChoice(get_choices)
   :canonical: aiida.cmdline.params.types.choice.LazyChoice

   Bases: :py:obj:`click.ParamType`

   This is a delegate of click's Choice ParamType that evaluates the set of choices
   lazily. This is useful if the choices set requires an import that is slow. Using
   the vanilla click.Choice will call this on import which will slow down verdi and
   its autocomplete. This type will generate the choices set lazily through the
   choices property


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.name
      :value: 'choice'

   .. py:method:: __init__(get_choices)
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.__init__

   .. py:property:: _click_choice
      :canonical: aiida.cmdline.params.types.choice.LazyChoice._click_choice

      Get the internal click Choice object that we delegate functionality to.
      Will construct it lazily if necessary.

      :return: The click Choice
      :rtype: :class:`click.Choice`


   .. py:property:: choices
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.choices

   .. py:method:: get_metavar(param)
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.get_metavar

   .. py:method:: get_missing_message(param)
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.get_missing_message

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.choice.LazyChoice.__repr__

.. py:class:: MpirunCommandParamType
   :canonical: aiida.cmdline.params.types.computer.MpirunCommandParamType

   Bases: :py:obj:`click.types.StringParamType`

   Custom click param type for mpirun-command

   .. note:: requires also a scheduler to be provided, and the scheduler
      must be called first!

   Validate that the provided 'mpirun' command only contains replacement fields
   (e.g. ``{tot_num_mpiprocs}``) that are known.

   Return a list of arguments (by using 'value.strip().split(" ") on the input string)


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.computer.MpirunCommandParamType.name
      :value: 'mpiruncommandstring'

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.computer.MpirunCommandParamType.__repr__

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.computer.MpirunCommandParamType.convert

.. py:class:: MultipleValueParamType(param_type)
   :canonical: aiida.cmdline.params.types.multiple.MultipleValueParamType

   Bases: :py:obj:`click.ParamType`

   An extension of click.ParamType that can parse multiple values for a given ParamType


   .. py:method:: __init__(param_type)
      :canonical: aiida.cmdline.params.types.multiple.MultipleValueParamType.__init__

   .. py:method:: get_metavar(param)
      :canonical: aiida.cmdline.params.types.multiple.MultipleValueParamType.get_metavar

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.multiple.MultipleValueParamType.convert

.. py:class:: NodeParamType
   :canonical: aiida.cmdline.params.types.node.NodeParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying Node entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.node.NodeParamType.name
      :value: 'Node'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.node.NodeParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


.. py:class:: NonEmptyStringParamType
   :canonical: aiida.cmdline.params.types.strings.NonEmptyStringParamType

   Bases: :py:obj:`click.types.StringParamType`

   Parameter whose values have to be string and non-empty.

   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.strings.NonEmptyStringParamType.name
      :value: 'nonemptystring'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.strings.NonEmptyStringParamType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.strings.NonEmptyStringParamType.__repr__

.. py:class:: PathOrUrl(timeout_seconds=URL_TIMEOUT_SECONDS, **kwargs)
   :canonical: aiida.cmdline.params.types.path.PathOrUrl

   Bases: :py:obj:`click.Path`

   Extension of click's Path-type to include URLs.

   A PathOrUrl can either be a `click.Path`-type or a URL.

   :param int timeout_seconds: Maximum timeout accepted for URL response.
       Must be an integer in the range [0;60].


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.path.PathOrUrl.name
      :value: 'PathOrUrl'

   .. py:method:: __init__(timeout_seconds=URL_TIMEOUT_SECONDS, **kwargs)
      :canonical: aiida.cmdline.params.types.path.PathOrUrl.__init__

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.path.PathOrUrl.convert

      Overwrite `convert` Check first if `click.Path`-type, then check if URL.

   .. py:method:: checks_url(url, param, ctx)
      :canonical: aiida.cmdline.params.types.path.PathOrUrl.checks_url

      Check whether URL is reachable within timeout.

.. py:class:: PluginParamType(group=None, load=False, *args, **kwargs)
   :canonical: aiida.cmdline.params.types.plugin.PluginParamType

   Bases: :py:obj:`aiida.cmdline.params.types.strings.EntryPointType`

   AiiDA Plugin name parameter type.

   :param group: string or tuple of strings, where each is a valid entry point group. Adding the `aiida.`
       prefix is optional. If it is not detected it will be prepended internally.
   :param load: when set to True, convert will not return the entry point, but the loaded entry point

   Usage::

       click.option(... type=PluginParamType(group='aiida.calculations')

   or::

       click.option(... type=PluginParamType(group=('calculations', 'data'))



   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.name
      :value: 'plugin'

   .. py:attribute:: _factory_mapping
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType._factory_mapping
      :value: None

   .. py:method:: __init__(group=None, load=False, *args, **kwargs)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.__init__

      Validate that group is either a string or a tuple of valid entry point groups, or if it
      is not specified use the tuple of all recognized entry point groups.


   .. py:method:: _init_entry_points()
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType._init_entry_points

      Populate entry point information that will be used later on.  This should only be called
      once in the constructor after setting self.groups because the groups should not be changed
      after instantiation


   .. py:property:: groups
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.groups

   .. py:property:: has_potential_ambiguity
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.has_potential_ambiguity

      Returns whether the set of supported entry point groups can lead to ambiguity when only an entry point name
      is specified. This will happen if one ore more groups share an entry point with a common name


   .. py:method:: get_valid_arguments()
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.get_valid_arguments

      Return a list of all available plugins for the groups configured for this PluginParamType instance.
      If the entry point names are not unique, because there are multiple groups that contain an entry
      point that has an identical name, we need to prefix the names with the full group name

      :returns: list of valid entry point strings


   .. py:method:: get_possibilities(incomplete='')
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.get_possibilities

      Return a list of plugins starting with incomplete


   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.shell_complete

      Return possible completions based on an incomplete value

      :returns: list of tuples of valid entry points (matching incomplete) and a description


   .. py:method:: get_missing_message(param)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.get_missing_message

   .. py:method:: get_entry_point_from_string(entry_point_string)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.get_entry_point_from_string

      Validate a given entry point string, which means that it should have a valid entry point string format
      and that the entry point unambiguously corresponds to an entry point in the groups configured for this
      instance of PluginParameterType.

      :returns: the entry point if valid
      :raises: ValueError if the entry point string is invalid


   .. py:method:: validate_entry_point_group(group)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.validate_entry_point_group

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.plugin.PluginParamType.convert

      Convert the string value to an entry point instance, if the value can be successfully parsed
      into an actual entry point. Will raise click.BadParameter if validation fails.


.. py:class:: ProcessParamType
   :canonical: aiida.cmdline.params.types.process.ProcessParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying ProcessNode entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.process.ProcessParamType.name
      :value: 'Process'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.process.ProcessParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


.. py:class:: ProfileParamType(*args, **kwargs)
   :canonical: aiida.cmdline.params.types.profile.ProfileParamType

   Bases: :py:obj:`aiida.cmdline.params.types.strings.LabelStringType`

   The profile parameter type for click.

   This parameter type requires the command that uses it to define the ``context_class`` class attribute to be the
   :class:`aiida.cmdline.groups.verdi.VerdiContext` class, as that is responsible for creating the user defined object
   ``obj`` on the context and loads the instance config.


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.profile.ProfileParamType.name
      :value: 'profile'

   .. py:method:: __init__(*args, **kwargs)
      :canonical: aiida.cmdline.params.types.profile.ProfileParamType.__init__

   .. py:method:: deconvert_default(value)
      :canonical: aiida.cmdline.params.types.profile.ProfileParamType.deconvert_default
      :staticmethod:

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.profile.ProfileParamType.convert

      Attempt to match the given value to a valid profile.

   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.profile.ProfileParamType.shell_complete

      Return possible completions based on an incomplete value

      :returns: list of tuples of valid entry points (matching incomplete) and a description


.. py:class:: ShebangParamType
   :canonical: aiida.cmdline.params.types.computer.ShebangParamType

   Bases: :py:obj:`click.types.StringParamType`

   Custom click param type for shebang line


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.computer.ShebangParamType.name
      :value: 'shebangline'

   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.computer.ShebangParamType.convert

   .. py:method:: __repr__()
      :canonical: aiida.cmdline.params.types.computer.ShebangParamType.__repr__

.. py:class:: UserParamType(create=False)
   :canonical: aiida.cmdline.params.types.user.UserParamType

   Bases: :py:obj:`click.ParamType`

   The user parameter type for click.   Can get or create a user.


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.user.UserParamType.name
      :value: 'user'

   .. py:method:: __init__(create=False)
      :canonical: aiida.cmdline.params.types.user.UserParamType.__init__

      :param create: If the user does not exist, create a new instance (unstored).


   .. py:method:: convert(value, param, ctx)
      :canonical: aiida.cmdline.params.types.user.UserParamType.convert

   .. py:method:: shell_complete(ctx, param, incomplete)
      :canonical: aiida.cmdline.params.types.user.UserParamType.shell_complete

      Return possible completions based on an incomplete value

      :returns: list of tuples of valid entry points (matching incomplete) and a description


.. py:class:: VerdiCommandGroup
   :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup

   Bases: :py:obj:`click.Group`

   Subclass of :class:`click.Group` for the ``verdi`` CLI.

   The class automatically adds the verbosity option to all commands in the interface. It also adds some functionality
   to provide suggestions of commands in case the user provided command name does not exist.


   .. py:attribute:: context_class
      :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup.context_class
      :value: None

   .. py:method:: add_verbosity_option(cmd)
      :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup.add_verbosity_option
      :staticmethod:

      Apply the ``verbosity`` option to the command, which is common to all ``verdi`` commands.

   .. py:method:: fail_with_suggestions(ctx, cmd_name)
      :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup.fail_with_suggestions

      Fail the command while trying to suggest commands to resemble the requested ``cmd_name``.

   .. py:method:: get_command(ctx, cmd_name)
      :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup.get_command

      Return the command that corresponds to the requested ``cmd_name``.

      This method is overridden from the base class in order to two functionalities:

          * If the command is found, automatically add the verbosity option.
          * If the command is not found, attempt to provide a list of suggestions with existing commands that resemble
            the requested command name.

      Note that if the command is not found and ``resilient_parsing`` is set to True on the context, then the latter
      feature is disabled because most likely we are operating in tab-completion mode.


   .. py:method:: group(*args, **kwargs)
      :canonical: aiida.cmdline.groups.verdi.VerdiCommandGroup.group

      Ensure that sub command groups use the same class but do not override an explicitly set value.

.. py:class:: WorkflowParamType
   :canonical: aiida.cmdline.params.types.workflow.WorkflowParamType

   Bases: :py:obj:`aiida.cmdline.params.types.identifier.IdentifierParamType`

   The ParamType for identifying WorkflowNode entities or its subclasses


   .. py:attribute:: name
      :canonical: aiida.cmdline.params.types.workflow.WorkflowParamType.name
      :value: 'WorkflowNode'

   .. py:property:: orm_class_loader
      :canonical: aiida.cmdline.params.types.workflow.WorkflowParamType.orm_class_loader

      Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
      to be used to load the entity for a given identifier

      :return: the orm entity loader class for this ParamType


.. py:function:: dbenv()
   :canonical: aiida.cmdline.utils.decorators.dbenv

   Loads the dbenv for a specific region of code, does not unload afterwards

   Only use when it makes it possible to avoid loading the dbenv for certain
   code paths

   Good Example::

       # do this
       @click.command()
       @click.option('--with-db', is_flag=True)
       def profile_info(with_db):
           # read the config file
           click.echo(profile_config)

           # load the db only if necessary
           if with_db:
               with dbenv():
                   # gather db statistics for the profile
                   click.echo(db_statistics)

   This will run very fast without the --with-db flag and slow only if database info is requested

   Do not use if you will end up loading the dbenv anyway

   Bad Example::

       # don't do this
       def my_function():
           with dbenv():
               # read from db

           # do db unrelated stuff


.. py:function:: echo_critical(message: str, bold: bool = False, nl: bool = True, err: bool = True, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_critical

   Log a critical error message to the cmdline logger and exit with ``exit_status``.

   This should be used to print messages for errors that cannot be recovered from and so the script should be directly
   terminated with a non-zero exit status to indicate that the command failed.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: echo_dictionary(dictionary, fmt='json+date', sort_keys=True)
   :canonical: aiida.cmdline.utils.echo.echo_dictionary

   Log the given dictionary to stdout in the given format

   :param dictionary: the dictionary
   :param fmt: the format to use for printing
   :param sort_keys: Whether to automatically sort keys


.. py:function:: echo_error(message: str, bold: bool = False, nl: bool = True, err: bool = True, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_error

   Log an error message to the cmdline logger.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: echo_info(message: str, bold: bool = False, nl: bool = True, err: bool = False, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_info

   Log an info message to the cmdline logger.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: echo_report(message: str, bold: bool = False, nl: bool = True, err: bool = False, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_report

   Log an report message to the cmdline logger.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: echo_success(message: str, bold: bool = False, nl: bool = True, err: bool = False, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_success

   Log a success message to the cmdline logger.

   .. note:: The message will be logged at the ``REPORT`` level and always with the ``Success:`` prefix.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: echo_warning(message: str, bold: bool = False, nl: bool = True, err: bool = False, prefix: bool = True) -> None
   :canonical: aiida.cmdline.utils.echo.echo_warning

   Log a warning message to the cmdline logger.

   :param message: the message to log.
   :param bold: whether to format the message in bold.
   :param nl: whether to add a newline at the end of the message.
   :param err: whether to log to stderr.
   :param prefix: whether the message should be prefixed with a colored version of the log level.


.. py:function:: format_call_graph(calc_node, max_depth: int = None, info_fn=calc_info)
   :canonical: aiida.cmdline.utils.ascii_vis.format_call_graph

   Print a tree like the POSIX tree command for the calculation call graph

   :param calc_node: The calculation node
   :param max_depth: Maximum depth of the call graph to print
   :param info_fn: An optional function that takes the node and returns a string
       of information to be displayed for each node.


.. py:function:: is_verbose()
   :canonical: aiida.cmdline.utils.common.is_verbose

   Return whether the configured logging verbosity is considered verbose, i.e., equal or lower to ``INFO`` level.

   .. note:: This checks the effective logging level that is set on the ``CMDLINE_LOGGER``. This means that it will
       consider the logging level set on the parent ``AIIDA_LOGGER`` if not explicitly set on itself. The level of the
       main logger can be manipulated from the command line through the ``VERBOSITY`` option that is available for all
       commands.



.. py:function:: only_if_daemon_running(echo_function=echo.echo_critical, message=None)
   :canonical: aiida.cmdline.utils.decorators.only_if_daemon_running

   Function decorator for CLI command to print critical error and exit automatically when daemon is not running.

   The error printing and exit behavior can be controlled with the decorator keyword arguments. The default message
   that is printed can be overridden as well as the echo function that is to be used. By default it uses the
   `aiida.cmdline.utils.echo.echo_critical` function which automatically aborts the command. The function can be
   substituted by for example `aiida.cmdline.utils.echo.echo_warning` to instead print just a warning and continue.

   Example::

       @only_if_daemon_running(echo_function=echo.echo_warning, message='beware that the daemon is not running')
       def create_node():
           pass

   :param echo_function: echo function to issue the message, should be from `aiida.cmdline.utils.echo`
   :param message: optional message to override the default message


.. py:function:: with_dbenv()
   :canonical: aiida.cmdline.utils.decorators.with_dbenv

   Function decorator that will load the database environment for the currently loaded profile.

   .. note:: if no profile has been loaded yet, the default profile will be loaded first.

   Example::

       @with_dbenv()
       def create_node():
           from aiida.orm import Int  # note the local import
           node = Int(1).store()

