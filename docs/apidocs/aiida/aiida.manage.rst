:py:mod:`aiida.manage`
======================

.. py:module:: aiida.manage

.. autodoc2-docstring:: aiida.manage
   :renderer: rst
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Config <aiida.manage.configuration.config.Config>`
     - .. autodoc2-docstring:: aiida.manage.configuration.config.Config
          :renderer: rst
          :summary:
   * - :py:obj:`Option <aiida.manage.configuration.options.Option>`
     - .. autodoc2-docstring:: aiida.manage.configuration.options.Option
          :renderer: rst
          :summary:
   * - :py:obj:`Postgres <aiida.manage.external.postgres.Postgres>`
     - .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres
          :renderer: rst
          :summary:
   * - :py:obj:`ProcessLauncher <aiida.manage.external.rmq.launcher.ProcessLauncher>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.launcher.ProcessLauncher
          :renderer: rst
          :summary:
   * - :py:obj:`Profile <aiida.manage.configuration.profile.Profile>`
     - .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile
          :renderer: rst
          :summary:
   * - :py:obj:`RabbitmqManagementClient <aiida.manage.external.rmq.client.RabbitmqManagementClient>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`check_and_migrate_config <aiida.manage.configuration.migrations.migrations.check_and_migrate_config>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.check_and_migrate_config
          :renderer: rst
          :summary:
   * - :py:obj:`config_needs_migrating <aiida.manage.configuration.migrations.migrations.config_needs_migrating>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.config_needs_migrating
          :renderer: rst
          :summary:
   * - :py:obj:`config_schema <aiida.manage.configuration.config.config_schema>`
     - .. autodoc2-docstring:: aiida.manage.configuration.config.config_schema
          :renderer: rst
          :summary:
   * - :py:obj:`disable_caching <aiida.manage.caching.disable_caching>`
     - .. autodoc2-docstring:: aiida.manage.caching.disable_caching
          :renderer: rst
          :summary:
   * - :py:obj:`downgrade_config <aiida.manage.configuration.migrations.migrations.downgrade_config>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.downgrade_config
          :renderer: rst
          :summary:
   * - :py:obj:`enable_caching <aiida.manage.caching.enable_caching>`
     - .. autodoc2-docstring:: aiida.manage.caching.enable_caching
          :renderer: rst
          :summary:
   * - :py:obj:`get_current_version <aiida.manage.configuration.migrations.migrations.get_current_version>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.get_current_version
          :renderer: rst
          :summary:
   * - :py:obj:`get_launch_queue_name <aiida.manage.external.rmq.utils.get_launch_queue_name>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_launch_queue_name
          :renderer: rst
          :summary:
   * - :py:obj:`get_manager <aiida.manage.manager.get_manager>`
     - .. autodoc2-docstring:: aiida.manage.manager.get_manager
          :renderer: rst
          :summary:
   * - :py:obj:`get_message_exchange_name <aiida.manage.external.rmq.utils.get_message_exchange_name>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_message_exchange_name
          :renderer: rst
          :summary:
   * - :py:obj:`get_option <aiida.manage.configuration.options.get_option>`
     - .. autodoc2-docstring:: aiida.manage.configuration.options.get_option
          :renderer: rst
          :summary:
   * - :py:obj:`get_option_names <aiida.manage.configuration.options.get_option_names>`
     - .. autodoc2-docstring:: aiida.manage.configuration.options.get_option_names
          :renderer: rst
          :summary:
   * - :py:obj:`get_rmq_url <aiida.manage.external.rmq.utils.get_rmq_url>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_rmq_url
          :renderer: rst
          :summary:
   * - :py:obj:`get_task_exchange_name <aiida.manage.external.rmq.utils.get_task_exchange_name>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_task_exchange_name
          :renderer: rst
          :summary:
   * - :py:obj:`get_use_cache <aiida.manage.caching.get_use_cache>`
     - .. autodoc2-docstring:: aiida.manage.caching.get_use_cache
          :renderer: rst
          :summary:
   * - :py:obj:`parse_option <aiida.manage.configuration.options.parse_option>`
     - .. autodoc2-docstring:: aiida.manage.configuration.options.parse_option
          :renderer: rst
          :summary:
   * - :py:obj:`upgrade_config <aiida.manage.configuration.migrations.migrations.upgrade_config>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.upgrade_config
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BROKER_DEFAULTS <aiida.manage.external.rmq.defaults.BROKER_DEFAULTS>`
     - .. autodoc2-docstring:: aiida.manage.external.rmq.defaults.BROKER_DEFAULTS
          :renderer: rst
          :summary:
   * - :py:obj:`CURRENT_CONFIG_VERSION <aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION
          :renderer: rst
          :summary:
   * - :py:obj:`MIGRATIONS <aiida.manage.configuration.migrations.migrations.MIGRATIONS>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.MIGRATIONS
          :renderer: rst
          :summary:
   * - :py:obj:`OLDEST_COMPATIBLE_CONFIG_VERSION <aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION>`
     - .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION
          :renderer: rst
          :summary:

External
~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DEFAULT_DSN <pgsu.DEFAULT_DSN>`
     - .. autodoc2-docstring:: pgsu.DEFAULT_DSN
          :renderer: rst
          :summary:
   * - :py:obj:`PostgresConnectionMode <pgsu.PostgresConnectionMode>`
     - .. autodoc2-docstring:: pgsu.PostgresConnectionMode
          :renderer: rst
          :summary:

API
~~~

.. py:data:: BROKER_DEFAULTS
   :canonical: aiida.manage.external.rmq.defaults.BROKER_DEFAULTS
   :value: None

   .. autodoc2-docstring:: aiida.manage.external.rmq.defaults.BROKER_DEFAULTS
      :renderer: rst

.. py:data:: CURRENT_CONFIG_VERSION
   :canonical: aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION
   :value: 9

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.CURRENT_CONFIG_VERSION
      :renderer: rst

.. py:class:: Config(filepath: str, config: dict, validate: bool = True)
   :canonical: aiida.manage.configuration.config.Config

   .. autodoc2-docstring:: aiida.manage.configuration.config.Config
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.configuration.config.Config.__init__
      :renderer: rst

   .. py:attribute:: KEY_VERSION
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION
      :value: 'CONFIG_VERSION'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_VERSION
         :renderer: rst

   .. py:attribute:: KEY_VERSION_CURRENT
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION_CURRENT
      :value: 'CURRENT'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_VERSION_CURRENT
         :renderer: rst

   .. py:attribute:: KEY_VERSION_OLDEST_COMPATIBLE
      :canonical: aiida.manage.configuration.config.Config.KEY_VERSION_OLDEST_COMPATIBLE
      :value: 'OLDEST_COMPATIBLE'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_VERSION_OLDEST_COMPATIBLE
         :renderer: rst

   .. py:attribute:: KEY_DEFAULT_PROFILE
      :canonical: aiida.manage.configuration.config.Config.KEY_DEFAULT_PROFILE
      :value: 'default_profile'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_DEFAULT_PROFILE
         :renderer: rst

   .. py:attribute:: KEY_PROFILES
      :canonical: aiida.manage.configuration.config.Config.KEY_PROFILES
      :value: 'profiles'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_PROFILES
         :renderer: rst

   .. py:attribute:: KEY_OPTIONS
      :canonical: aiida.manage.configuration.config.Config.KEY_OPTIONS
      :value: 'options'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_OPTIONS
         :renderer: rst

   .. py:attribute:: KEY_SCHEMA
      :canonical: aiida.manage.configuration.config.Config.KEY_SCHEMA
      :value: '$schema'

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.KEY_SCHEMA
         :renderer: rst

   .. py:method:: from_file(filepath)
      :canonical: aiida.manage.configuration.config.Config.from_file
      :classmethod:

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.from_file
         :renderer: rst

   .. py:method:: _backup(filepath)
      :canonical: aiida.manage.configuration.config.Config._backup
      :classmethod:

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config._backup
         :renderer: rst

   .. py:method:: validate(config: dict, filepath: typing.Optional[str] = None)
      :canonical: aiida.manage.configuration.config.Config.validate
      :staticmethod:

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.validate
         :renderer: rst

   .. py:method:: __eq__(other)
      :canonical: aiida.manage.configuration.config.Config.__eq__

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.__eq__
         :renderer: rst

   .. py:method:: __ne__(other)
      :canonical: aiida.manage.configuration.config.Config.__ne__

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.__ne__
         :renderer: rst

   .. py:method:: handle_invalid(message)
      :canonical: aiida.manage.configuration.config.Config.handle_invalid

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.handle_invalid
         :renderer: rst

   .. py:property:: dictionary
      :canonical: aiida.manage.configuration.config.Config.dictionary
      :type: dict

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.dictionary
         :renderer: rst

   .. py:property:: version
      :canonical: aiida.manage.configuration.config.Config.version

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.version
         :renderer: rst

   .. py:property:: version_oldest_compatible
      :canonical: aiida.manage.configuration.config.Config.version_oldest_compatible

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.version_oldest_compatible
         :renderer: rst

   .. py:property:: version_settings
      :canonical: aiida.manage.configuration.config.Config.version_settings

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.version_settings
         :renderer: rst

   .. py:property:: filepath
      :canonical: aiida.manage.configuration.config.Config.filepath

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.filepath
         :renderer: rst

   .. py:property:: dirpath
      :canonical: aiida.manage.configuration.config.Config.dirpath

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.dirpath
         :renderer: rst

   .. py:property:: default_profile_name
      :canonical: aiida.manage.configuration.config.Config.default_profile_name

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.default_profile_name
         :renderer: rst

   .. py:property:: profile_names
      :canonical: aiida.manage.configuration.config.Config.profile_names

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.profile_names
         :renderer: rst

   .. py:property:: profiles
      :canonical: aiida.manage.configuration.config.Config.profiles

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.profiles
         :renderer: rst

   .. py:method:: validate_profile(name)
      :canonical: aiida.manage.configuration.config.Config.validate_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.validate_profile
         :renderer: rst

   .. py:method:: get_profile(name: typing.Optional[str] = None) -> aiida.manage.configuration.profile.Profile
      :canonical: aiida.manage.configuration.config.Config.get_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.get_profile
         :renderer: rst

   .. py:method:: add_profile(profile)
      :canonical: aiida.manage.configuration.config.Config.add_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.add_profile
         :renderer: rst

   .. py:method:: update_profile(profile)
      :canonical: aiida.manage.configuration.config.Config.update_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.update_profile
         :renderer: rst

   .. py:method:: remove_profile(name)
      :canonical: aiida.manage.configuration.config.Config.remove_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.remove_profile
         :renderer: rst

   .. py:method:: delete_profile(name: str, include_database: bool = True, include_database_user: bool = False, include_repository: bool = True)
      :canonical: aiida.manage.configuration.config.Config.delete_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.delete_profile
         :renderer: rst

   .. py:method:: set_default_profile(name, overwrite=False)
      :canonical: aiida.manage.configuration.config.Config.set_default_profile

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.set_default_profile
         :renderer: rst

   .. py:property:: options
      :canonical: aiida.manage.configuration.config.Config.options

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.options
         :renderer: rst

   .. py:method:: set_option(option_name, option_value, scope=None, override=True)
      :canonical: aiida.manage.configuration.config.Config.set_option

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.set_option
         :renderer: rst

   .. py:method:: unset_option(option_name: str, scope=None)
      :canonical: aiida.manage.configuration.config.Config.unset_option

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.unset_option
         :renderer: rst

   .. py:method:: get_option(option_name, scope=None, default=True)
      :canonical: aiida.manage.configuration.config.Config.get_option

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.get_option
         :renderer: rst

   .. py:method:: get_options(scope: typing.Optional[str] = None) -> typing.Dict[str, typing.Tuple[aiida.manage.configuration.options.Option, str, typing.Any]]
      :canonical: aiida.manage.configuration.config.Config.get_options

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.get_options
         :renderer: rst

   .. py:method:: store()
      :canonical: aiida.manage.configuration.config.Config.store

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config.store
         :renderer: rst

   .. py:method:: _atomic_write(filepath=None)
      :canonical: aiida.manage.configuration.config.Config._atomic_write

      .. autodoc2-docstring:: aiida.manage.configuration.config.Config._atomic_write
         :renderer: rst

.. py:exception:: ConfigValidationError(message: str, keypath: typing.Sequence[typing.Any] = (), schema: typing.Optional[dict] = None, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.config.ConfigValidationError

   Bases: :py:obj:`aiida.common.exceptions.ConfigurationError`

   .. autodoc2-docstring:: aiida.manage.configuration.config.ConfigValidationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.configuration.config.ConfigValidationError.__init__
      :renderer: rst

   .. py:method:: __str__() -> str
      :canonical: aiida.manage.configuration.config.ConfigValidationError.__str__

      .. autodoc2-docstring:: aiida.manage.configuration.config.ConfigValidationError.__str__
         :renderer: rst

.. py:data:: MIGRATIONS
   :canonical: aiida.manage.configuration.migrations.migrations.MIGRATIONS
   :value: ()

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.MIGRATIONS
      :renderer: rst

.. py:exception:: ManagementApiConnectionError()
   :canonical: aiida.manage.external.rmq.client.ManagementApiConnectionError

   Bases: :py:obj:`aiida.common.exceptions.AiidaException`

   .. autodoc2-docstring:: aiida.manage.external.rmq.client.ManagementApiConnectionError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.external.rmq.client.ManagementApiConnectionError.__init__
      :renderer: rst

.. py:data:: OLDEST_COMPATIBLE_CONFIG_VERSION
   :canonical: aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION
   :value: 9

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.OLDEST_COMPATIBLE_CONFIG_VERSION
      :renderer: rst

.. py:class:: Option(name: str, schema: typing.Dict[str, typing.Any])
   :canonical: aiida.manage.configuration.options.Option

   .. autodoc2-docstring:: aiida.manage.configuration.options.Option
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.configuration.options.Option.__init__
      :renderer: rst

   .. py:method:: __str__() -> str
      :canonical: aiida.manage.configuration.options.Option.__str__

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.__str__
         :renderer: rst

   .. py:property:: name
      :canonical: aiida.manage.configuration.options.Option.name
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.name
         :renderer: rst

   .. py:property:: schema
      :canonical: aiida.manage.configuration.options.Option.schema
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.schema
         :renderer: rst

   .. py:property:: valid_type
      :canonical: aiida.manage.configuration.options.Option.valid_type
      :type: typing.Any

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.valid_type
         :renderer: rst

   .. py:property:: default
      :canonical: aiida.manage.configuration.options.Option.default
      :type: typing.Any

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.default
         :renderer: rst

   .. py:property:: description
      :canonical: aiida.manage.configuration.options.Option.description
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.description
         :renderer: rst

   .. py:property:: global_only
      :canonical: aiida.manage.configuration.options.Option.global_only
      :type: bool

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.global_only
         :renderer: rst

   .. py:method:: validate(value: typing.Any, cast: bool = True) -> typing.Any
      :canonical: aiida.manage.configuration.options.Option.validate

      .. autodoc2-docstring:: aiida.manage.configuration.options.Option.validate
         :renderer: rst

.. py:class:: Postgres(dbinfo=None, **kwargs)
   :canonical: aiida.manage.external.postgres.Postgres

   Bases: :py:obj:`pgsu.PGSU`

   .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.__init__
      :renderer: rst

   .. py:method:: from_profile(profile: aiida.manage.configuration.Profile, **kwargs)
      :canonical: aiida.manage.external.postgres.Postgres.from_profile
      :classmethod:

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.from_profile
         :renderer: rst

   .. py:method:: dbuser_exists(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.dbuser_exists

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.dbuser_exists
         :renderer: rst

   .. py:method:: create_dbuser(dbuser, dbpass, privileges='')
      :canonical: aiida.manage.external.postgres.Postgres.create_dbuser

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.create_dbuser
         :renderer: rst

   .. py:method:: drop_dbuser(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.drop_dbuser

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.drop_dbuser
         :renderer: rst

   .. py:method:: check_dbuser(dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.check_dbuser

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.check_dbuser
         :renderer: rst

   .. py:method:: db_exists(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.db_exists

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.db_exists
         :renderer: rst

   .. py:method:: create_db(dbuser, dbname)
      :canonical: aiida.manage.external.postgres.Postgres.create_db

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.create_db
         :renderer: rst

   .. py:method:: drop_db(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.drop_db

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.drop_db
         :renderer: rst

   .. py:method:: copy_db(src_db, dest_db, dbuser)
      :canonical: aiida.manage.external.postgres.Postgres.copy_db

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.copy_db
         :renderer: rst

   .. py:method:: check_db(dbname)
      :canonical: aiida.manage.external.postgres.Postgres.check_db

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.check_db
         :renderer: rst

   .. py:method:: create_dbuser_db_safe(dbname, dbuser, dbpass)
      :canonical: aiida.manage.external.postgres.Postgres.create_dbuser_db_safe

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.create_dbuser_db_safe
         :renderer: rst

   .. py:property:: host_for_psycopg2
      :canonical: aiida.manage.external.postgres.Postgres.host_for_psycopg2

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.host_for_psycopg2
         :renderer: rst

   .. py:property:: port_for_psycopg2
      :canonical: aiida.manage.external.postgres.Postgres.port_for_psycopg2

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.port_for_psycopg2
         :renderer: rst

   .. py:property:: dbinfo
      :canonical: aiida.manage.external.postgres.Postgres.dbinfo

      .. autodoc2-docstring:: aiida.manage.external.postgres.Postgres.dbinfo
         :renderer: rst

.. py:class:: ProcessLauncher
   :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher

   Bases: :py:obj:`plumpy.ProcessLauncher`

   .. autodoc2-docstring:: aiida.manage.external.rmq.launcher.ProcessLauncher
      :renderer: rst

   .. py:method:: handle_continue_exception(node, exception, message)
      :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher.handle_continue_exception
      :staticmethod:

      .. autodoc2-docstring:: aiida.manage.external.rmq.launcher.ProcessLauncher.handle_continue_exception
         :renderer: rst

   .. py:method:: _continue(communicator, pid, nowait, tag=None)
      :canonical: aiida.manage.external.rmq.launcher.ProcessLauncher._continue
      :async:

      .. autodoc2-docstring:: aiida.manage.external.rmq.launcher.ProcessLauncher._continue
         :renderer: rst

.. py:class:: Profile(name: str, config: typing.Mapping[str, typing.Any], validate=True)
   :canonical: aiida.manage.configuration.profile.Profile

   .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.__init__
      :renderer: rst

   .. py:attribute:: KEY_UUID
      :canonical: aiida.manage.configuration.profile.Profile.KEY_UUID
      :value: 'PROFILE_UUID'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_UUID
         :renderer: rst

   .. py:attribute:: KEY_DEFAULT_USER_EMAIL
      :canonical: aiida.manage.configuration.profile.Profile.KEY_DEFAULT_USER_EMAIL
      :value: 'default_user_email'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_DEFAULT_USER_EMAIL
         :renderer: rst

   .. py:attribute:: KEY_STORAGE
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE
      :value: 'storage'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_STORAGE
         :renderer: rst

   .. py:attribute:: KEY_PROCESS
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS
      :value: 'process_control'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_PROCESS
         :renderer: rst

   .. py:attribute:: KEY_STORAGE_BACKEND
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE_BACKEND
      :value: 'backend'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_STORAGE_BACKEND
         :renderer: rst

   .. py:attribute:: KEY_STORAGE_CONFIG
      :canonical: aiida.manage.configuration.profile.Profile.KEY_STORAGE_CONFIG
      :value: 'config'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_STORAGE_CONFIG
         :renderer: rst

   .. py:attribute:: KEY_PROCESS_BACKEND
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS_BACKEND
      :value: 'backend'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_PROCESS_BACKEND
         :renderer: rst

   .. py:attribute:: KEY_PROCESS_CONFIG
      :canonical: aiida.manage.configuration.profile.Profile.KEY_PROCESS_CONFIG
      :value: 'config'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_PROCESS_CONFIG
         :renderer: rst

   .. py:attribute:: KEY_OPTIONS
      :canonical: aiida.manage.configuration.profile.Profile.KEY_OPTIONS
      :value: 'options'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_OPTIONS
         :renderer: rst

   .. py:attribute:: KEY_TEST_PROFILE
      :canonical: aiida.manage.configuration.profile.Profile.KEY_TEST_PROFILE
      :value: 'test_profile'

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.KEY_TEST_PROFILE
         :renderer: rst

   .. py:attribute:: REQUIRED_KEYS
      :canonical: aiida.manage.configuration.profile.Profile.REQUIRED_KEYS
      :value: ()

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.REQUIRED_KEYS
         :renderer: rst

   .. py:method:: __repr__() -> str
      :canonical: aiida.manage.configuration.profile.Profile.__repr__

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.__repr__
         :renderer: rst

   .. py:method:: copy()
      :canonical: aiida.manage.configuration.profile.Profile.copy

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.copy
         :renderer: rst

   .. py:property:: uuid
      :canonical: aiida.manage.configuration.profile.Profile.uuid
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.uuid
         :renderer: rst

   .. py:property:: default_user_email
      :canonical: aiida.manage.configuration.profile.Profile.default_user_email
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.default_user_email
         :renderer: rst

   .. py:property:: storage_backend
      :canonical: aiida.manage.configuration.profile.Profile.storage_backend
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.storage_backend
         :renderer: rst

   .. py:property:: storage_config
      :canonical: aiida.manage.configuration.profile.Profile.storage_config
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.storage_config
         :renderer: rst

   .. py:method:: set_storage(name: str, config: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.manage.configuration.profile.Profile.set_storage

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.set_storage
         :renderer: rst

   .. py:property:: storage_cls
      :canonical: aiida.manage.configuration.profile.Profile.storage_cls
      :type: typing.Type[aiida.orm.implementation.StorageBackend]

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.storage_cls
         :renderer: rst

   .. py:property:: process_control_backend
      :canonical: aiida.manage.configuration.profile.Profile.process_control_backend
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.process_control_backend
         :renderer: rst

   .. py:property:: process_control_config
      :canonical: aiida.manage.configuration.profile.Profile.process_control_config
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.process_control_config
         :renderer: rst

   .. py:method:: set_process_controller(name: str, config: typing.Dict[str, typing.Any]) -> None
      :canonical: aiida.manage.configuration.profile.Profile.set_process_controller

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.set_process_controller
         :renderer: rst

   .. py:property:: options
      :canonical: aiida.manage.configuration.profile.Profile.options

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.options
         :renderer: rst

   .. py:method:: get_option(option_key, default=None)
      :canonical: aiida.manage.configuration.profile.Profile.get_option

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.get_option
         :renderer: rst

   .. py:method:: set_option(option_key, value, override=True)
      :canonical: aiida.manage.configuration.profile.Profile.set_option

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.set_option
         :renderer: rst

   .. py:method:: unset_option(option_key)
      :canonical: aiida.manage.configuration.profile.Profile.unset_option

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.unset_option
         :renderer: rst

   .. py:property:: name
      :canonical: aiida.manage.configuration.profile.Profile.name

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.name
         :renderer: rst

   .. py:property:: dictionary
      :canonical: aiida.manage.configuration.profile.Profile.dictionary
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.dictionary
         :renderer: rst

   .. py:property:: is_test_profile
      :canonical: aiida.manage.configuration.profile.Profile.is_test_profile
      :type: bool

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.is_test_profile
         :renderer: rst

   .. py:property:: repository_path
      :canonical: aiida.manage.configuration.profile.Profile.repository_path
      :type: pathlib.Path

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.repository_path
         :renderer: rst

   .. py:property:: rmq_prefix
      :canonical: aiida.manage.configuration.profile.Profile.rmq_prefix
      :type: str

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.rmq_prefix
         :renderer: rst

   .. py:method:: get_rmq_url() -> str
      :canonical: aiida.manage.configuration.profile.Profile.get_rmq_url

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.get_rmq_url
         :renderer: rst

   .. py:property:: filepaths
      :canonical: aiida.manage.configuration.profile.Profile.filepaths

      .. autodoc2-docstring:: aiida.manage.configuration.profile.Profile.filepaths
         :renderer: rst

.. py:class:: RabbitmqManagementClient(username: str, password: str, hostname: str, virtual_host: str)
   :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient

   .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient.__init__
      :renderer: rst

   .. py:method:: format_url(url: str, url_params: dict[str, str] | None = None) -> str
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.format_url

      .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient.format_url
         :renderer: rst

   .. py:method:: request(url: str, url_params: dict[str, str] | None = None, method: str = 'GET', params: dict[str, typing.Any] | None = None) -> requests.Response
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.request

      .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient.request
         :renderer: rst

   .. py:property:: is_connected
      :canonical: aiida.manage.external.rmq.client.RabbitmqManagementClient.is_connected
      :type: bool

      .. autodoc2-docstring:: aiida.manage.external.rmq.client.RabbitmqManagementClient.is_connected
         :renderer: rst

.. py:function:: check_and_migrate_config(config, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.migrations.migrations.check_and_migrate_config

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.check_and_migrate_config
      :renderer: rst

.. py:function:: config_needs_migrating(config, filepath: typing.Optional[str] = None)
   :canonical: aiida.manage.configuration.migrations.migrations.config_needs_migrating

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.config_needs_migrating
      :renderer: rst

.. py:function:: config_schema() -> typing.Dict[str, typing.Any]
   :canonical: aiida.manage.configuration.config.config_schema

   .. autodoc2-docstring:: aiida.manage.configuration.config.config_schema
      :renderer: rst

.. py:function:: disable_caching(*, identifier=None)
   :canonical: aiida.manage.caching.disable_caching

   .. autodoc2-docstring:: aiida.manage.caching.disable_caching
      :renderer: rst

.. py:function:: downgrade_config(config: aiida.manage.configuration.migrations.migrations.ConfigType, target: int, migrations: typing.Iterable[typing.Type[aiida.manage.configuration.migrations.migrations.SingleMigration]] = MIGRATIONS) -> aiida.manage.configuration.migrations.migrations.ConfigType
   :canonical: aiida.manage.configuration.migrations.migrations.downgrade_config

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.downgrade_config
      :renderer: rst

.. py:function:: enable_caching(*, identifier=None)
   :canonical: aiida.manage.caching.enable_caching

   .. autodoc2-docstring:: aiida.manage.caching.enable_caching
      :renderer: rst

.. py:function:: get_current_version(config)
   :canonical: aiida.manage.configuration.migrations.migrations.get_current_version

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.get_current_version
      :renderer: rst

.. py:function:: get_launch_queue_name(prefix=None)
   :canonical: aiida.manage.external.rmq.utils.get_launch_queue_name

   .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_launch_queue_name
      :renderer: rst

.. py:function:: get_manager() -> Manager
   :canonical: aiida.manage.manager.get_manager

   .. autodoc2-docstring:: aiida.manage.manager.get_manager
      :renderer: rst

.. py:function:: get_message_exchange_name(prefix)
   :canonical: aiida.manage.external.rmq.utils.get_message_exchange_name

   .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_message_exchange_name
      :renderer: rst

.. py:function:: get_option(name: str) -> aiida.manage.configuration.options.Option
   :canonical: aiida.manage.configuration.options.get_option

   .. autodoc2-docstring:: aiida.manage.configuration.options.get_option
      :renderer: rst

.. py:function:: get_option_names() -> typing.List[str]
   :canonical: aiida.manage.configuration.options.get_option_names

   .. autodoc2-docstring:: aiida.manage.configuration.options.get_option_names
      :renderer: rst

.. py:function:: get_rmq_url(protocol=None, username=None, password=None, host=None, port=None, virtual_host=None, **kwargs)
   :canonical: aiida.manage.external.rmq.utils.get_rmq_url

   .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_rmq_url
      :renderer: rst

.. py:function:: get_task_exchange_name(prefix)
   :canonical: aiida.manage.external.rmq.utils.get_task_exchange_name

   .. autodoc2-docstring:: aiida.manage.external.rmq.utils.get_task_exchange_name
      :renderer: rst

.. py:function:: get_use_cache(*, identifier=None)
   :canonical: aiida.manage.caching.get_use_cache

   .. autodoc2-docstring:: aiida.manage.caching.get_use_cache
      :renderer: rst

.. py:function:: parse_option(option_name: str, option_value: typing.Any) -> typing.Tuple[aiida.manage.configuration.options.Option, typing.Any]
   :canonical: aiida.manage.configuration.options.parse_option

   .. autodoc2-docstring:: aiida.manage.configuration.options.parse_option
      :renderer: rst

.. py:function:: upgrade_config(config: aiida.manage.configuration.migrations.migrations.ConfigType, target: int = CURRENT_CONFIG_VERSION, migrations: typing.Iterable[typing.Type[aiida.manage.configuration.migrations.migrations.SingleMigration]] = MIGRATIONS) -> aiida.manage.configuration.migrations.migrations.ConfigType
   :canonical: aiida.manage.configuration.migrations.migrations.upgrade_config

   .. autodoc2-docstring:: aiida.manage.configuration.migrations.migrations.upgrade_config
      :renderer: rst
