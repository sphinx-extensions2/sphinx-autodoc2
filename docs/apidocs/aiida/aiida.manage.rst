:py:mod:`aiida.manage`
======================

.. py:module:: aiida.manage


Description
-----------

Managing an AiiDA instance:

    * configuration file
    * profiles
    * databases
    * repositories
    * external components (such as Postgres, RabbitMQ)

.. note:: Modules in this sub package may require the database environment to be loaded


Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Config <aiida.manage.configuration.config.Config>`
     - Object that represents the configuration file of an AiiDA instance.
   * - :py:obj:`Option <aiida.manage.configuration.options.Option>`
     - Represent a configuration option schema.
   * - :py:obj:`Postgres <aiida.manage.external.postgres.Postgres>`
     - Adds convenience functions to :py:class:`pgsu.PGSU`.
   * - :py:obj:`ProcessLauncher <aiida.manage.external.rmq.launcher.ProcessLauncher>`
     - A sub class of :class:`plumpy.ProcessLauncher` to launch a ``Process``.
   * - :py:obj:`Profile <aiida.manage.configuration.profile.Profile>`
     - Class that models a profile as it is stored in the configuration file of an AiiDA instance.
   * - :py:obj:`RabbitmqManagementClient <aiida.manage.external.rmq.client.RabbitmqManagementClient>`
     - Client for RabbitMQ Management HTTP API.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`check_and_migrate_config <aiida.manage.configuration.migrations.migrations.check_and_migrate_config>`
     - Checks if the config needs to be migrated, and performs the migration if needed.
   * - :py:obj:`config_needs_migrating <aiida.manage.configuration.migrations.migrations.config_needs_migrating>`
     - Checks if the config needs to be migrated.
   * - :py:obj:`config_schema <aiida.manage.configuration.config.config_schema>`
     - Return the configuration schema.
   * - :py:obj:`disable_caching <aiida.manage.caching.disable_caching>`
     - Context manager to disable caching, either for a specific node class, or globally.
   * - :py:obj:`downgrade_config <aiida.manage.configuration.migrations.migrations.downgrade_config>`
     - Run the registered configuration migrations down to the target version.
   * - :py:obj:`enable_caching <aiida.manage.caching.enable_caching>`
     - Context manager to enable caching, either for a specific node class, or globally.
   * - :py:obj:`get_current_version <aiida.manage.configuration.migrations.migrations.get_current_version>`
     - Return the current version of the config.
   * - :py:obj:`get_launch_queue_name <aiida.manage.external.rmq.utils.get_launch_queue_name>`
     - Return the launch queue name with an optional prefix.
   * - :py:obj:`get_manager <aiida.manage.manager.get_manager>`
     - Return the AiiDA global manager instance.
   * - :py:obj:`get_message_exchange_name <aiida.manage.external.rmq.utils.get_message_exchange_name>`
     - Return the message exchange name for a given prefix.
   * - :py:obj:`get_option <aiida.manage.configuration.options.get_option>`
     - Return option.
   * - :py:obj:`get_option_names <aiida.manage.configuration.options.get_option_names>`
     - Return a list of available option names.
   * - :py:obj:`get_rmq_url <aiida.manage.external.rmq.utils.get_rmq_url>`
     - Return the URL to connect to RabbitMQ.
   * - :py:obj:`get_task_exchange_name <aiida.manage.external.rmq.utils.get_task_exchange_name>`
     - Return the task exchange name for a given prefix.
   * - :py:obj:`get_use_cache <aiida.manage.caching.get_use_cache>`
     - Return whether the caching mechanism should be used for the given process type according to the configuration.
   * - :py:obj:`parse_option <aiida.manage.configuration.options.parse_option>`
     - Parse and validate a value for a configuration option.
   * - :py:obj:`upgrade_config <aiida.manage.configuration.migrations.migrations.upgrade_config>`
     - Run the registered configuration migrations up to the target version.

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BROKER_DEFAULTS <aiida.manage.external.rmq.defaults.BROKER_DEFAULTS>`
     - 
   * - :py:obj:`CURRENT_CONFIG_VERSION <aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION>`
     - 
   * - :py:obj:`MIGRATIONS <aiida.manage.configuration.migrations.migrations.MIGRATIONS>`
     - 
   * - :py:obj:`OLDEST_COMPATIBLE_CONFIG_VERSION <aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION>`
     - 

External
~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DEFAULT_DSN <pgsu.DEFAULT_DSN>`
     - 
   * - :py:obj:`PostgresConnectionMode <pgsu.PostgresConnectionMode>`
     - 

API
~~~

.. py:data:: BROKER_DEFAULTS
   :canonical: aiida.manage.external.rmq.defaults.BROKER_DEFAULTS
   :value: None

.. py:data:: CURRENT_CONFIG_VERSION
   :canonical: aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION
   :value: 9

.. py:class:: Config(filepath: str, config: dict, validate: bool = True)
   :canonical: aiida.manage.configuration.config.Config

   Object that represents the configuration file of an AiiDA instance.

   .. py:attribute:: KEY_VERSION
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION
      :value: 'CONFIG_VERSION'

   .. py:attribute:: KEY_VERSION_CURRENT
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION_CURRENT
      :value: 'CURRENT'

   .. py:attribute:: KEY_VERSION_OLDEST_COMPATIBLE
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION_OLDEST_COMPATIBLE
      :value: 'OLDEST_COMPATIBLE'

   .. py:attribute:: KEY_DEFAULT_PROFILE
      :canonical: aiida.manage.configuration.config.Config.KEY_DEFAULT_PROFILE
      :value: 'default_profile'

   .. py:attribute:: KEY_PROFILES
      :canonical: aiida.manage.configuration.config.Config.KEY_PROFILES
      :value: 'profiles'

   .. py:attribute:: KEY_OPTIONS
      :canonical: aiida.manage.configuration.config.Config.KEY_OPTIONS
      :value: 'options'

   .. py:attribute:: KEY_SCHEMA
      :canonical: aiida.manage.configuration.config.Config.KEY_SCHEMA
      :value: '$schema'

   .. py:method:: from_file(filepath)
      :canonical: aiida.manage.configuration.config.Config.from_file
      :classmethod:

      Instantiate a configuration object from the contents of a given file.

      .. note:: if the filepath does not exist an empty file will be created with the current default configuration
          and will be written to disk. If the filepath does already exist but contains a configuration with an
          outdated schema, the content will be migrated and then written to disk.

      :param filepath: the absolute path to the configuration file
      :return: `Config` instance


   .. py:method:: _backup(filepath)
      :canonical: aiida.manage.configuration.config.Config._backup
      :classmethod:

      Create a backup of the configuration file with the given filepath.

      :param filepath: absolute path to the configuration file to backup
      :return: the absolute path of the created backup


   .. py:method:: validate(config: dict, filepath: typing.Optional[str] = None)
      :canonical: aiida.manage.configuration.config.Config.validate
      :staticmethod:

      Validate a configuration dictionary.

   .. py:method:: __init__(filepath: str, config: dict, validate: bool = True)
      :canonical: aiida.manage.configuration.config.Config.__init__

      Instantiate a configuration object from a configuration dictionary and its filepath.

      If an empty dictionary is passed, the constructor will create the skeleton configuration dictionary.

      :param filepath: the absolute filepath of the configuration file
      :param config: the content of the configuration file in dictionary form
      :param validate: validate the dictionary against the schema


   .. py:method:: __eq__(other)
      :canonical: aiida.manage.configuration.config.Config.__eq__

      Two configurations are considered equal, when their dictionaries are equal.

   .. py:method:: __ne__(other)
      :canonical: aiida.manage.configuration.config.Config.__ne__

      Two configurations are considered unequal, when their dictionaries are unequal.

   .. py:method:: handle_invalid(message)
      :canonical: aiida.manage.configuration.config.Config.handle_invalid

      Handle an incoming invalid configuration dictionary.

      The current content of the configuration file will be written to a backup file.

      :param message: a string message to echo with describing the infraction


   .. py:property:: dictionary
      :canonical: aiida.manage.configuration.config.Config.dictionary
      :type: dict

      Return the dictionary representation of the config as it would be written to file.

      :return: dictionary representation of config as it should be written to file


   .. py:property:: version
      :canonical: aiida.manage.configuration.config.Config.version

   .. py:property:: version_oldest_compatible
      :canonical: aiida.manage.configuration.config.Config.version_oldest_compatible

   .. py:property:: version_settings
      :canonical: aiida.manage.configuration.config.Config.version_settings

   .. py:property:: filepath
      :canonical: aiida.manage.configuration.config.Config.filepath

   .. py:property:: dirpath
      :canonical: aiida.manage.configuration.config.Config.dirpath

   .. py:property:: default_profile_name
      :canonical: aiida.manage.configuration.config.Config.default_profile_name

      Return the default profile name.

      :return: the default profile name or None if not defined


   .. py:property:: profile_names
      :canonical: aiida.manage.configuration.config.Config.profile_names

      Return the list of profile names.

      :return: list of profile names


   .. py:property:: profiles
      :canonical: aiida.manage.configuration.config.Config.profiles

      Return the list of profiles.

      :return: the profiles
      :rtype: list of `Profile` instances


   .. py:method:: validate_profile(name)
      :canonical: aiida.manage.configuration.config.Config.validate_profile

      Validate that a profile exists.

      :param name: name of the profile:
      :raises aiida.common.ProfileConfigurationError: if the name is not found in the configuration file


   .. py:method:: get_profile(name: typing.Optional[str] = None) -> aiida.manage.configuration.profile.Profile
      :canonical: aiida.manage.configuration.config.Config.get_profile

      Return the profile for the given name or the default one if not specified.

      :return: the profile instance or None if it does not exist
      :raises aiida.common.ProfileConfigurationError: if the name is not found in the configuration file


   .. py:method:: add_profile(profile)
      :canonical: aiida.manage.configuration.config.Config.add_profile

      Add a profile to the configuration.

      :param profile: the profile configuration dictionary
      :return: self


   .. py:method:: update_profile(profile)
      :canonical: aiida.manage.configuration.config.Config.update_profile

      Update a profile in the configuration.

      :param profile: the profile instance to update
      :return: self


   .. py:method:: remove_profile(name)
      :canonical: aiida.manage.configuration.config.Config.remove_profile

      Remove a profile from the configuration.

      :param name: the name of the profile to remove
      :raises aiida.common.ProfileConfigurationError: if the given profile does not exist
      :return: self


   .. py:method:: delete_profile(name: str, include_database: bool = True, include_database_user: bool = False, include_repository: bool = True)
      :canonical: aiida.manage.configuration.config.Config.delete_profile

      Delete a profile including its storage.

      :param include_database: also delete the database configured for the profile.
      :param include_database_user: also delete the database user configured for the profile.
      :param include_repository: also delete the repository configured for the profile.


   .. py:method:: set_default_profile(name, overwrite=False)
      :canonical: aiida.manage.configuration.config.Config.set_default_profile

      Set the given profile as the new default.

      :param name: name of the profile to set as new default
      :param overwrite: when True, set the profile as the new default even if a default profile is already defined
      :raises aiida.common.ProfileConfigurationError: if the given profile does not exist
      :return: self


   .. py:property:: options
      :canonical: aiida.manage.configuration.config.Config.options

   .. py:method:: set_option(option_name, option_value, scope=None, override=True)
      :canonical: aiida.manage.configuration.config.Config.set_option

      Set a configuration option for a certain scope.

      :param option_name: the name of the configuration option
      :param option_value: the option value
      :param scope: set the option for this profile or globally if not specified
      :param override: boolean, if False, will not override the option if it already exists

      :returns: the parsed value (potentially cast to a valid type)


   .. py:method:: unset_option(option_name: str, scope=None)
      :canonical: aiida.manage.configuration.config.Config.unset_option

      Unset a configuration option for a certain scope.

      :param option_name: the name of the configuration option
      :param scope: unset the option for this profile or globally if not specified


   .. py:method:: get_option(option_name, scope=None, default=True)
      :canonical: aiida.manage.configuration.config.Config.get_option

      Get a configuration option for a certain scope.

      :param option_name: the name of the configuration option
      :param scope: get the option for this profile or globally if not specified
      :param default: boolean, If True will return the option default, even if not defined within the given scope
      :return: the option value or None if not set for the given scope


   .. py:method:: get_options(scope: typing.Optional[str] = None) -> typing.Dict[str, typing.Tuple[aiida.manage.configuration.options.Option, str, typing.Any]]
      :canonical: aiida.manage.configuration.config.Config.get_options

      Return a dictionary of all option values and their source ('profile', 'global', or 'default').

      :param scope: the profile name or globally if not specified
      :returns: (option, source, value)


   .. py:method:: store()
      :canonical: aiida.manage.configuration.config.Config.store

      Write the current config to file.

      .. note:: if the configuration file already exists on disk and its contents differ from those in memory, a
          backup of the original file on disk will be created before overwriting it.

      :return: self


   .. py:method:: _atomic_write(filepath=None)
      :canonical: aiida.manage.configuration.config.Config._atomic_write

      Write the config as it is in memory, i.e. the contents of ``self.dictionary``, to disk.

      .. note:: this command will write the config from memory to a temporary file in the same directory as the
          target file ``filepath``. It will then use ``os.rename`` to move the temporary file to ``filepath`` which
          will be overwritten if it already exists. The ``os.rename`` is the operation that gives the best guarantee
          of being atomic within the limitations of the application.

      :param filepath: optional filepath to write the contents to, if not specified, the default filename is used.


.. py:exception:: ConfigValidationError(message: str, keypath: typing.Sequence[typing.Any] = (), schema: typing.Optional[dict] = None, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.config.ConfigValidationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   Configuration error raised when the file contents fails validation.

   .. py:method:: __init__(message: str, keypath: typing.Sequence[typing.Any] = (), schema: typing.Optional[dict] = None, filepath: typing.Optional[str] = None)
      :canonical: aiida.manage.configuration.config.ConfigValidationError.__init__

      Initialize self.  See help(type(self)) for accurate signature.

   .. py:method:: __str__() -> str
      :canonical: aiida.manage.configuration.config.ConfigValidationError.__str__

      Return str(self).

.. py:data:: MIGRATIONS
   :canonical: aiida.manage.configuration.migrations.migrations.MIGRATIONS
   :value: ()

.. py:exception:: ManagementApiConnectionError()
   :canonical: aiida.manage.external.rmq.client.ManagementApiConnectionError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   Raised when no connection can be made to the management HTTP API.

.. py:data:: OLDEST_COMPATIBLE_CONFIG_VERSION
   :canonical: aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION
   :value: 9

.. py:class:: Option(name: str, schema: typing.Dict[str, typing.Any])
   :canonical: aiida.manage.configuration.options.Option

   Represent a configuration option schema.

   .. py:method:: __init__(name: str, schema: typing.Dict[str, typing.Any])
      :canonical: aiida.manage.configuration.options.Option.__init__

   .. py:method:: __str__() -> str
      :canonical: aiida.manage.configuration.options.Option.__str__

      Return str(self).

   .. py:property:: name
      :canonical: aiida.manage.configuration.options.Option.name
      :type: str

   .. py:property:: schema
      :canonical: aiida.manage.configuration.options.Option.schema
      :type: typing.Dict[str, typing.Any]

   .. py:property:: valid_type
      :canonical: aiida.manage.configuration.options.Option.valid_type
      :type: typing.Any

   .. py:property:: default
      :canonical: aiida.manage.configuration.options.Option.default
      :type: typing.Any

   .. py:property:: description
      :canonical: aiida.manage.configuration.options.Option.description
      :type: str

   .. py:property:: global_only
      :canonical: aiida.manage.configuration.options.Option.global_only
      :type: bool

   .. py:method:: validate(value: typing.Any, cast: bool = True) -> typing.Any
      :canonical: aiida.manage.configuration.options.Option.validate

      Validate a value

      :param value: The input value
      :param cast: Attempt to cast the value to the required type

      :return: The output value
      :raise: ConfigValidationError



.. py:class:: Postgres(dbinfo=None, **kwargs)
   :canonical: aiida.manage.external.postgres.Postgres

   Bases: :py:obj:`pgsu.PGSU`

   Adds convenience functions to :py:class:`pgsu.PGSU`.

   Provides convenience functions for
     * creating/dropping users
     * creating/dropping databases

   etc.

   Example::

       postgres = Postgres()
       postgres.create_dbuser('username', 'password')
       if not postgres.db_exists('dbname'):
           postgres.create_db('username', 'dbname')


   .. py:method:: __init__(dbinfo=None, **kwargs)
      :canonical: aiida.manage.external.postgres.Postgres.__init__

      See documentation of :py:meth:`pgsu.PGSU.__init__`.

   .. py:method:: from_profile(profile: aiida.manage.configuration.Profile, **kwargs)
      :canonical: aiida.manage.external.postgres.Postgres.from_profile
      :classmethod:

      Create Postgres instance with dbinfo from AiiDA profile data.

      Note: This only uses host and port from the profile, since the others are not going to be relevant for the
        database superuser.

      :param profile: AiiDA profile instance
      :param kwargs: keyword arguments forwarded to PGSU constructor

      :returns: Postgres instance pre-populated with data from AiiDA profile


   .. py:method:: dbuser_exists(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.dbuser_exists

      Find out if postgres user with name dbuser exists

      :param str dbuser: database user to check for
      :return: (bool) True if user exists, False otherwise


   .. py:method:: create_dbuser(dbuser, dbpass, privileges='')
      :canonical: aiida.manage.external.postgres.Postgres.create_dbuser

      Create a database user in postgres

      :param str dbuser: Name of the user to be created.
      :param str dbpass: Password the user should be given.
      :raises: psycopg2.errors.DuplicateObject if user already exists and
          self.connection_mode == PostgresConnectionMode.PSYCOPG


   .. py:method:: drop_dbuser(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.drop_dbuser

      Drop a database user in postgres

      :param str dbuser: Name of the user to be dropped.


   .. py:method:: check_dbuser(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.check_dbuser

      Looks up if a given user already exists, prompts for using or creating a differently named one.

      :param str dbuser: Name of the user to be created or reused.
      :returns: tuple (dbuser, created)


   .. py:method:: db_exists(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.db_exists

      Check wether a postgres database with dbname exists

      :param str dbname: Name of the database to check for
      :return: (bool), True if database exists, False otherwise


   .. py:method:: create_db(dbuser, dbname)
      :canonical: aiida.manage.external.postgres.Postgres.create_db

      Create a database in postgres

      :param str dbuser: Name of the user which should own the db.
      :param str dbname: Name of the database.


   .. py:method:: drop_db(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.drop_db

      Drop a database in postgres

      :param str dbname: Name of the database.


   .. py:method:: copy_db(src_db, dest_db, dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.copy_db

   .. py:method:: check_db(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.check_db

      Looks up if a database with the name exists, prompts for using or creating a differently named one.

      :param str dbname: Name of the database to be created or reused.
      :returns: tuple (dbname, created)


   .. py:method:: create_dbuser_db_safe(dbname, dbuser, dbpass)
      :canonical: aiida.manage.external.postgres.Postgres.create_dbuser_db_safe

      Create DB and user + grant privileges.

      Prompts when reusing existing users / databases.


   .. py:property:: host_for_psycopg2
      :canonical: aiida.manage.external.postgres.Postgres.host_for_psycopg2

      Return correct host for psycopg2 connection (as required by regular AiiDA operation).

   .. py:property:: port_for_psycopg2
      :canonical: aiida.manage.external.postgres.Postgres.port_for_psycopg2

      Return port for psycopg2 connection (as required by regular AiiDA operation).

   .. py:property:: dbinfo
      :canonical: aiida.manage.external.postgres.Postgres.dbinfo

      Alias for Postgres.dsn.

.. py:class:: ProcessLauncher
   :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher

   Bases: :py:obj:`plumpy.ProcessLauncher`

   A sub class of :class:`plumpy.ProcessLauncher` to launch a ``Process``.

   It overrides the _continue method to make sure the node corresponding to the task can be loaded and
   that if it is already marked as terminated, it is not continued but the future is reconstructed and returned


   .. py:method:: handle_continue_exception(node, exception, message)
      :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher.handle_continue_exception
      :staticmethod:

      Handle exception raised in `_continue` call.

      If the process state of the node has not yet been put to excepted, the exception was raised before the process
      instance could be reconstructed, for example when the process class could not be loaded, thereby circumventing
      the exception handling of the state machine. Raising this exception will then acknowledge the process task with
      RabbitMQ leaving an uncleaned node in the `CREATED` state for ever. Therefore we have to perform the node
      cleaning manually.

      :param exception: the exception object
      :param message: string message to use for the log message


   .. py:method:: _continue(communicator, pid, nowait, tag=None)
      :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher._continue
      :async:

      Continue the task.

      Note that the task may already have been completed, as indicated from the corresponding the node, in which
      case it is not continued, but the corresponding future is reconstructed and returned. This scenario may
      occur when the Process was already completed by another worker that however failed to send the acknowledgment.

      :param communicator: the communicator that called this method
      :param pid: the pid of the process to continue
      :param nowait: if True don't wait for the process to finish, just return the pid, otherwise wait and
          return the results
      :param tag: the tag of the checkpoint to continue from


.. py:class:: Profile(name: str, config: typing.Mapping[str, typing.Any], validate=True)
   :canonical: aiida.manage.configuration.profile.Profile

   Class that models a profile as it is stored in the configuration file of an AiiDA instance.

   .. py:attribute:: KEY_UUID
      :canonical: aiida.manage.configuration.profile.Profile.KEY_UUID
      :value: 'PROFILE_UUID'

   .. py:attribute:: KEY_DEFAULT_USER_EMAIL
      :canonical: aiida.manage.configuration.profile.Profile.KEY_DEFAULT_USER_EMAIL
      :value: 'default_user_email'

   .. py:attribute:: KEY_STORAGE
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE
      :value: 'storage'

   .. py:attribute:: KEY_PROCESS
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS
      :value: 'process_control'

   .. py:attribute:: KEY_STORAGE_BACKEND
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE_BACKEND
      :value: 'backend'

   .. py:attribute:: KEY_STORAGE_CONFIG
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE_CONFIG
      :value: 'config'

   .. py:attribute:: KEY_PROCESS_BACKEND
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS_BACKEND
      :value: 'backend'

   .. py:attribute:: KEY_PROCESS_CONFIG
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS_CONFIG
      :value: 'config'

   .. py:attribute:: KEY_OPTIONS
      :canonical: aiida.manage.configuration.profile.Profile.KEY_OPTIONS
      :value: 'options'

   .. py:attribute:: KEY_TEST_PROFILE
      :canonical: aiida.manage.configuration.profile.Profile.KEY_TEST_PROFILE
      :value: 'test_profile'

   .. py:attribute:: REQUIRED_KEYS
      :canonical: aiida.manage.configuration.profile.Profile.REQUIRED_KEYS
      :value: ()

   .. py:method:: __init__(name: str, config: typing.Mapping[str, typing.Any], validate=True)
      :canonical: aiida.manage.configuration.profile.Profile.__init__

      Load a profile with the profile configuration.

   .. py:method:: __repr__() -> str
      :canonical: aiida.manage.configuration.profile.Profile.__repr__

      Return repr(self).

   .. py:method:: copy()
      :canonical: aiida.manage.configuration.profile.Profile.copy

      Return a copy of the profile.

   .. py:property:: uuid
      :canonical: aiida.manage.configuration.profile.Profile.uuid
      :type: str

      Return the profile uuid.

      :return: string UUID


   .. py:property:: default_user_email
      :canonical: aiida.manage.configuration.profile.Profile.default_user_email
      :type: typing.Optional[str]

      Return the default user email.

   .. py:property:: storage_backend
      :canonical: aiida.manage.configuration.profile.Profile.storage_backend
      :type: str

      Return the type of the storage backend.

   .. py:property:: storage_config
      :canonical: aiida.manage.configuration.profile.Profile.storage_config
      :type: typing.Dict[str, typing.Any]

      Return the configuration required by the storage backend.

   .. py:method:: set_storage(name: str, config: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.manage.configuration.profile.Profile.set_storage

      Set the storage backend and its configuration.

      :param name: the name of the storage backend
      :param config: the configuration of the storage backend


   .. py:property:: storage_cls
      :canonical: aiida.manage.configuration.profile.Profile.storage_cls
      :type: typing.Type[aiida.orm.implementation.StorageBackend]

      Return the storage backend class for this profile.

   .. py:property:: process_control_backend
      :canonical: aiida.manage.configuration.profile.Profile.process_control_backend
      :type: str

      Return the type of the process control backend.

   .. py:property:: process_control_config
      :canonical: aiida.manage.configuration.profile.Profile.process_control_config
      :type: typing.Dict[str, typing.Any]

      Return the configuration required by the process control backend.

   .. py:method:: set_process_controller(name: str, config: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.manage.configuration.profile.Profile.set_process_controller

      Set the process control backend and its configuration.

      :param name: the name of the process backend
      :param config: the configuration of the process backend


   .. py:property:: options
      :canonical: aiida.manage.configuration.profile.Profile.options

   .. py:method:: get_option(option_key, default=None)
      :canonical: aiida.manage.configuration.profile.Profile.get_option

   .. py:method:: set_option(option_key, value, override=True)
      :canonical: aiida.manage.configuration.profile.Profile.set_option

      Set a configuration option for a certain scope.

      :param option_key: the key of the configuration option
      :param option_value: the option value
      :param override: boolean, if False, will not override the option if it already exists


   .. py:method:: unset_option(option_key)
      :canonical: aiida.manage.configuration.profile.Profile.unset_option

   .. py:property:: name
      :canonical: aiida.manage.configuration.profile.Profile.name

      Return the profile name.

      :return: the profile name


   .. py:property:: dictionary
      :canonical: aiida.manage.configuration.profile.Profile.dictionary
      :type: typing.Dict[str, typing.Any]

      Return the profile attributes as a dictionary with keys as it is stored in the config

      :return: the profile configuration dictionary


   .. py:property:: is_test_profile
      :canonical: aiida.manage.configuration.profile.Profile.is_test_profile
      :type: bool

      Return whether the profile is a test profile

      :return: boolean, True if test profile, False otherwise


   .. py:property:: repository_path
      :canonical: aiida.manage.configuration.profile.Profile.repository_path
      :type: pathlib.Path

      Return the absolute path of the repository configured for this profile.

      The URI should be in the format `protocol://address`

      :note: At the moment, only the file protocol is supported.

      :return: absolute filepath of the profile's file repository


   .. py:property:: rmq_prefix
      :canonical: aiida.manage.configuration.profile.Profile.rmq_prefix
      :type: str

      Return the prefix that should be used for RMQ resources

      :return: the rmq prefix string


   .. py:method:: get_rmq_url() -> str
      :canonical: aiida.manage.configuration.profile.Profile.get_rmq_url

      Return the RMQ url for this profile.

   .. py:property:: filepaths
      :canonical: aiida.manage.configuration.profile.Profile.filepaths

      Return the filepaths used by this profile.

      :return: a dictionary of filepaths


.. py:class:: RabbitmqManagementClient(username: str, password: str, hostname: str, virtual_host: str)
   :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient

   Client for RabbitMQ Management HTTP API.

   This requires the ``rabbitmq_management`` plugin (https://www.rabbitmq.com/management.html) to be enabled. Typically
   this is enabled by running ``rabbitmq-plugins enable rabbitmq_management``.


   .. py:method:: __init__(username: str, password: str, hostname: str, virtual_host: str)
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.__init__

      Construct a new instance.

      :param username: The username to authenticate with.
      :param password: The password to authenticate with.
      :param hostname: The hostname of the RabbitMQ server.
      :param virtual_host: The virtual host.


   .. py:method:: format_url(url: str, url_params: dict[str, str] | None = None) -> str
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.format_url

      Format the complete URL from a partial resource path with placeholders.

      The base URL will be automatically prepended.

      :param url: The resource path with placeholders, e.g., ``queues/{virtual_host}/{queue}``.
      :param url_params: Dictionary with values for the placeholders in the ``url``. The ``virtual_host`` value is
          automatically inserted and should not be specified.
      :returns: The complete URL.


   .. py:method:: request(url: str, url_params: dict[str, str] | None = None, method: str = 'GET', params: dict[str, typing.Any] | None = None) -> requests.Response
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.request

      Make a request.

      :param url: The resource path with placeholders, e.g., ``queues/{virtual_host}/{queue}``.
      :param url_params: Dictionary with values for the placeholders in the ``url``. The ``virtual_host`` value is
          automatically inserted and should not be specified.
      :param method: The HTTP method.
      :param params: Query parameters to add to the URL.
      :returns: The response of the request.
      :raises `ManagementApiConnectionError`: If connection to the API cannot be made.


   .. py:property:: is_connected
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.is_connected
      :type: bool

      Return whether the API server can be connected to.

      .. note:: Tries to reach the server at the ``/api/cluster-name`` end-point.

      :returns: ``True`` if the server can be reached, ``False`` otherwise.


.. py:function:: check_and_migrate_config(config, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.migrations.migrations.check_and_migrate_config

   Checks if the config needs to be migrated, and performs the migration if needed.

   :param config: the configuration dictionary
   :param filepath: the path to the configuration file (optional, for error reporting)
   :return: the migrated configuration dictionary


.. py:function:: config_needs_migrating(config, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.migrations.migrations.config_needs_migrating

   Checks if the config needs to be migrated.

   If the oldest compatible version of the configuration is higher than the current configuration version defined
   in the code, the config cannot be used and so the function will raise.

   :param filepath: the path to the configuration file (optional, for error reporting)
   :return: True if the configuration has an older version and needs to be migrated, False otherwise
   :raises aiida.common.ConfigurationVersionError: if the config's oldest compatible version is higher than the current


.. py:function:: config_schema() -> typing.Dict[str, typing.Any]
   :canonical: aiida.manage.configuration.config.config_schema

   Return the configuration schema.

.. py:function:: disable_caching(*, identifier=None)
   :canonical: aiida.manage.caching.disable_caching

   Context manager to disable caching, either for a specific node class, or globally.

   .. warning:: this does not affect the behavior of the daemon, only the local Python interpreter.

   :param identifier: Process type string of the node, or a pattern with '*' wildcard that matches it.
       If not provided, caching is disabled for all classes.
   :type identifier: str


.. py:function:: downgrade_config(config: aiida.manage.configuration.migrations.migrations.ConfigType, target: int, migrations: typing.Iterable[typing.Type[aiida.manage.configuration.migrations.migrations.SingleMigration]] = MIGRATIONS) -> aiida.manage.configuration.migrations.migrations.ConfigType
   :canonical: aiida.manage.configuration.migrations.migrations.downgrade_config

   Run the registered configuration migrations down to the target version.

   :param config: the configuration dictionary
   :return: the migrated configuration dictionary


.. py:function:: enable_caching(*, identifier=None)
   :canonical: aiida.manage.caching.enable_caching

   Context manager to enable caching, either for a specific node class, or globally.

   .. warning:: this does not affect the behavior of the daemon, only the local Python interpreter.

   :param identifier: Process type string of the node, or a pattern with '*' wildcard that matches it.
       If not provided, caching is enabled for all classes.
   :type identifier: str


.. py:function:: get_current_version(config)
   :canonical: aiida.manage.configuration.migrations.migrations.get_current_version

   Return the current version of the config.

   :return: current config version or 0 if not defined


.. py:function:: get_launch_queue_name(prefix=None)
   :canonical: aiida.manage.external.rmq.utils.get_launch_queue_name

   Return the launch queue name with an optional prefix.

   :returns: launch queue name


.. py:function:: get_manager() -> Manager
   :canonical: aiida.manage.manager.get_manager

   Return the AiiDA global manager instance.

.. py:function:: get_message_exchange_name(prefix)
   :canonical: aiida.manage.external.rmq.utils.get_message_exchange_name

   Return the message exchange name for a given prefix.

   :returns: message exchange name


.. py:function:: get_option(name: str) -> aiida.manage.configuration.options.Option
   :canonical: aiida.manage.configuration.options.get_option

   Return option.

.. py:function:: get_option_names() -> typing.List[str]
   :canonical: aiida.manage.configuration.options.get_option_names

   Return a list of available option names.

.. py:function:: get_rmq_url(protocol=None, username=None, password=None, host=None, port=None, virtual_host=None, **kwargs)
   :canonical: aiida.manage.external.rmq.utils.get_rmq_url

   Return the URL to connect to RabbitMQ.

   .. note::

       The default of the ``host`` is set to ``127.0.0.1`` instead of ``localhost`` because on some computers localhost
       resolves first to IPv6 with address ::1 and if RMQ is not running on IPv6 one gets an annoying warning. For more
       info see: https://github.com/aiidateam/aiida-core/issues/1142

   :param protocol: the protocol to use, `amqp` or `amqps`.
   :param username: the username for authentication.
   :param password: the password for authentication.
   :param host: the hostname of the RabbitMQ server.
   :param port: the port of the RabbitMQ server.
   :param virtual_host: the virtual host to connect to.
   :param kwargs: remaining keyword arguments that will be encoded as query parameters.
   :returns: the connection URL string.


.. py:function:: get_task_exchange_name(prefix)
   :canonical: aiida.manage.external.rmq.utils.get_task_exchange_name

   Return the task exchange name for a given prefix.

   :returns: task exchange name


.. py:function:: get_use_cache(*, identifier=None)
   :canonical: aiida.manage.caching.get_use_cache

   Return whether the caching mechanism should be used for the given process type according to the configuration.

   :param identifier: Process type string of the node
   :type identifier: str
   :return: boolean, True if caching is enabled, False otherwise
   :raises: `~aiida.common.exceptions.ConfigurationError` if the configuration is invalid, either due to a general
       configuration error, or by defining the class both enabled and disabled


.. py:function:: parse_option(option_name: str, option_value: typing.Any) -> typing.Tuple[aiida.manage.configuration.options.Option, typing.Any]
   :canonical: aiida.manage.configuration.options.parse_option

   Parse and validate a value for a configuration option.

   :param option_name: the name of the configuration option
   :param option_value: the option value
   :return: a tuple of the option and the parsed value



.. py:function:: upgrade_config(config: aiida.manage.configuration.migrations.migrations.ConfigType, target: int = CURRENT_CONFIG_VERSION, migrations: typing.Iterable[typing.Type[aiida.manage.configuration.migrations.migrations.SingleMigration]] = MIGRATIONS) -> aiida.manage.configuration.migrations.migrations.ConfigType
   :canonical: aiida.manage.configuration.migrations.migrations.upgrade_config

   Run the registered configuration migrations up to the target version.

   :param config: the configuration dictionary
   :return: the migrated configuration dictionary

