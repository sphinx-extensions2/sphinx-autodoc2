:py:mod:`aiida.transports`
==========================

.. py:module:: aiida.transports

.. autodoc2-docstring:: aiida.transports
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SshTransport <aiida.transports.plugins.ssh.SshTransport>`
     - .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport
          :summary:
   * - :py:obj:`Transport <aiida.transports.transport.Transport>`
     - .. autodoc2-docstring:: aiida.transports.transport.Transport
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`convert_to_bool <aiida.transports.plugins.ssh.convert_to_bool>`
     - .. autodoc2-docstring:: aiida.transports.plugins.ssh.convert_to_bool
          :summary:
   * - :py:obj:`parse_sshconfig <aiida.transports.plugins.ssh.parse_sshconfig>`
     - .. autodoc2-docstring:: aiida.transports.plugins.ssh.parse_sshconfig
          :summary:

API
~~~

.. py:class:: SshTransport(*args, **kwargs)
   :canonical: aiida.transports.plugins.ssh.SshTransport

   Bases: :py:obj:`aiida.transports.transport.Transport`

   .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.__init__

   .. py:attribute:: _valid_connect_options
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_connect_options
      :value: [('username',), ('port',), ('look_for_keys',), ('key_filename',), ('timeout',), ('allow_agent',), ('...

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._valid_connect_options

   .. py:attribute:: _valid_connect_params
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_connect_params
      :value: None

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._valid_connect_params

   .. py:attribute:: _valid_auth_options
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_auth_options
      :value: None

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._valid_auth_options

   .. py:attribute:: _MAX_EXEC_COMMAND_LOG_SIZE
      :canonical: aiida.transports.plugins.ssh.SshTransport._MAX_EXEC_COMMAND_LOG_SIZE
      :value: None

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._MAX_EXEC_COMMAND_LOG_SIZE

   .. py:method:: _get_username_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_username_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_username_suggestion_string

   .. py:method:: _get_port_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_port_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_port_suggestion_string

   .. py:method:: _get_key_filename_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_key_filename_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_key_filename_suggestion_string

   .. py:method:: _get_timeout_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_timeout_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_timeout_suggestion_string

   .. py:method:: _get_allow_agent_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_allow_agent_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_allow_agent_suggestion_string

   .. py:method:: _get_look_for_keys_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_look_for_keys_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_look_for_keys_suggestion_string

   .. py:method:: _get_proxy_command_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_proxy_command_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_proxy_command_suggestion_string

   .. py:method:: _get_proxy_jump_suggestion_string(_)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_proxy_jump_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_proxy_jump_suggestion_string

   .. py:method:: _get_compress_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_compress_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_compress_suggestion_string

   .. py:method:: _get_load_system_host_keys_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_load_system_host_keys_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_load_system_host_keys_suggestion_string

   .. py:method:: _get_key_policy_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_key_policy_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_key_policy_suggestion_string

   .. py:method:: _get_gss_auth_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_auth_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_gss_auth_suggestion_string

   .. py:method:: _get_gss_kex_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_kex_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_gss_kex_suggestion_string

   .. py:method:: _get_gss_deleg_creds_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_deleg_creds_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_gss_deleg_creds_suggestion_string

   .. py:method:: _get_gss_host_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_host_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._get_gss_host_suggestion_string

   .. py:method:: open()
      :canonical: aiida.transports.plugins.ssh.SshTransport.open

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.open

   .. py:method:: _close_proxies()
      :canonical: aiida.transports.plugins.ssh.SshTransport._close_proxies

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._close_proxies

   .. py:method:: close()
      :canonical: aiida.transports.plugins.ssh.SshTransport.close

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.close

   .. py:property:: sshclient
      :canonical: aiida.transports.plugins.ssh.SshTransport.sshclient

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.sshclient

   .. py:property:: sftp
      :canonical: aiida.transports.plugins.ssh.SshTransport.sftp

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.sftp

   .. py:method:: __str__()
      :canonical: aiida.transports.plugins.ssh.SshTransport.__str__

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.__str__

   .. py:method:: chdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chdir

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.chdir

   .. py:method:: normalize(path='.')
      :canonical: aiida.transports.plugins.ssh.SshTransport.normalize

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.normalize

   .. py:method:: stat(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.stat

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.stat

   .. py:method:: lstat(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.lstat

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.lstat

   .. py:method:: getcwd()
      :canonical: aiida.transports.plugins.ssh.SshTransport.getcwd

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.getcwd

   .. py:method:: makedirs(path, ignore_existing=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.makedirs

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.makedirs

   .. py:method:: mkdir(path, ignore_existing=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.mkdir

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.mkdir

   .. py:method:: rmtree(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rmtree

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.rmtree

   .. py:method:: rmdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rmdir

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.rmdir

   .. py:method:: chown(path, uid, gid)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chown
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.chown

   .. py:method:: isdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.isdir

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.isdir

   .. py:method:: chmod(path, mode)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chmod

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.chmod

   .. py:method:: _os_path_split_asunder(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport._os_path_split_asunder
      :staticmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._os_path_split_asunder

   .. py:method:: put(localpath, remotepath, callback=None, dereference=True, overwrite=True, ignore_nonexisting=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.put

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.put

   .. py:method:: putfile(localpath, remotepath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.putfile

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.putfile

   .. py:method:: puttree(localpath, remotepath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.puttree

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.puttree

   .. py:method:: get(remotepath, localpath, callback=None, dereference=True, overwrite=True, ignore_nonexisting=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.get

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.get

   .. py:method:: getfile(remotepath, localpath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.getfile

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.getfile

   .. py:method:: gettree(remotepath, localpath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.gettree

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.gettree

   .. py:method:: get_attribute(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.get_attribute

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.get_attribute

   .. py:method:: copyfile(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copyfile

   .. py:method:: copytree(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copytree

   .. py:method:: copy(remotesource, remotedestination, dereference=False, recursive=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copy

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.copy

   .. py:method:: _exec_cp(cp_exe, cp_flags, src, dst)
      :canonical: aiida.transports.plugins.ssh.SshTransport._exec_cp

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._exec_cp

   .. py:method:: _local_listdir(path, pattern=None)
      :canonical: aiida.transports.plugins.ssh.SshTransport._local_listdir
      :staticmethod:

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._local_listdir

   .. py:method:: listdir(path='.', pattern=None)
      :canonical: aiida.transports.plugins.ssh.SshTransport.listdir

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.listdir

   .. py:method:: remove(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.remove

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.remove

   .. py:method:: rename(oldpath, newpath)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rename

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.rename

   .. py:method:: isfile(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.isfile

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.isfile

   .. py:method:: _exec_command_internal(command, combine_stderr=False, bufsize=-1)
      :canonical: aiida.transports.plugins.ssh.SshTransport._exec_command_internal

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._exec_command_internal

   .. py:method:: exec_command_wait_bytes(command, stdin=None, combine_stderr=False, bufsize=-1)
      :canonical: aiida.transports.plugins.ssh.SshTransport.exec_command_wait_bytes

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.exec_command_wait_bytes

   .. py:method:: gotocomputer_command(remotedir)
      :canonical: aiida.transports.plugins.ssh.SshTransport.gotocomputer_command

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.gotocomputer_command

   .. py:method:: _symlink(source, dest)
      :canonical: aiida.transports.plugins.ssh.SshTransport._symlink

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport._symlink

   .. py:method:: symlink(remotesource, remotedestination)
      :canonical: aiida.transports.plugins.ssh.SshTransport.symlink

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.symlink

   .. py:method:: path_exists(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.path_exists

      .. autodoc2-docstring:: aiida.transports.plugins.ssh.SshTransport.path_exists

.. py:class:: Transport(*args, **kwargs)
   :canonical: aiida.transports.transport.Transport

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: aiida.transports.transport.Transport

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.transports.transport.Transport.__init__

   .. py:attribute:: DEFAULT_MINIMUM_JOB_POLL_INTERVAL
      :canonical: aiida.transports.transport.Transport.DEFAULT_MINIMUM_JOB_POLL_INTERVAL
      :value: 10

      .. autodoc2-docstring:: aiida.transports.transport.Transport.DEFAULT_MINIMUM_JOB_POLL_INTERVAL

   .. py:attribute:: _DEFAULT_SAFE_OPEN_INTERVAL
      :canonical: aiida.transports.transport.Transport._DEFAULT_SAFE_OPEN_INTERVAL
      :value: 30.0

      .. autodoc2-docstring:: aiida.transports.transport.Transport._DEFAULT_SAFE_OPEN_INTERVAL

   .. py:attribute:: _valid_auth_params
      :canonical: aiida.transports.transport.Transport._valid_auth_params
      :value: None

      .. autodoc2-docstring:: aiida.transports.transport.Transport._valid_auth_params

   .. py:attribute:: _MAGIC_CHECK
      :canonical: aiida.transports.transport.Transport._MAGIC_CHECK
      :value: None

      .. autodoc2-docstring:: aiida.transports.transport.Transport._MAGIC_CHECK

   .. py:attribute:: _valid_auth_options
      :canonical: aiida.transports.transport.Transport._valid_auth_options
      :type: list
      :value: []

      .. autodoc2-docstring:: aiida.transports.transport.Transport._valid_auth_options

   .. py:attribute:: _common_auth_options
      :canonical: aiida.transports.transport.Transport._common_auth_options
      :value: [('use_login_shell',), ('safe_interval',)]

      .. autodoc2-docstring:: aiida.transports.transport.Transport._common_auth_options

   .. py:method:: __enter__()
      :canonical: aiida.transports.transport.Transport.__enter__

      .. autodoc2-docstring:: aiida.transports.transport.Transport.__enter__

   .. py:method:: __exit__(type_, value, traceback)
      :canonical: aiida.transports.transport.Transport.__exit__

      .. autodoc2-docstring:: aiida.transports.transport.Transport.__exit__

   .. py:property:: is_open
      :canonical: aiida.transports.transport.Transport.is_open

      .. autodoc2-docstring:: aiida.transports.transport.Transport.is_open

   .. py:method:: open()
      :canonical: aiida.transports.transport.Transport.open
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.open

   .. py:method:: close()
      :canonical: aiida.transports.transport.Transport.close
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.close

   .. py:method:: __repr__()
      :canonical: aiida.transports.transport.Transport.__repr__

   .. py:method:: __str__()
      :canonical: aiida.transports.transport.Transport.__str__

   .. py:method:: set_logger_extra(logger_extra)
      :canonical: aiida.transports.transport.Transport.set_logger_extra

      .. autodoc2-docstring:: aiida.transports.transport.Transport.set_logger_extra

   .. py:method:: get_short_doc()
      :canonical: aiida.transports.transport.Transport.get_short_doc
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get_short_doc

   .. py:method:: get_valid_auth_params()
      :canonical: aiida.transports.transport.Transport.get_valid_auth_params
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get_valid_auth_params

   .. py:method:: auth_options() -> collections.OrderedDict
      :canonical: aiida.transports.transport.Transport.auth_options

      .. autodoc2-docstring:: aiida.transports.transport.Transport.auth_options

   .. py:method:: _get_safe_interval_suggestion_string(computer)
      :canonical: aiida.transports.transport.Transport._get_safe_interval_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport._get_safe_interval_suggestion_string

   .. py:method:: _get_use_login_shell_suggestion_string(computer)
      :canonical: aiida.transports.transport.Transport._get_use_login_shell_suggestion_string
      :classmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport._get_use_login_shell_suggestion_string

   .. py:property:: logger
      :canonical: aiida.transports.transport.Transport.logger

      .. autodoc2-docstring:: aiida.transports.transport.Transport.logger

   .. py:method:: get_safe_open_interval()
      :canonical: aiida.transports.transport.Transport.get_safe_open_interval

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get_safe_open_interval

   .. py:method:: chdir(path)
      :canonical: aiida.transports.transport.Transport.chdir
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.chdir

   .. py:method:: chmod(path, mode)
      :canonical: aiida.transports.transport.Transport.chmod
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.chmod

   .. py:method:: chown(path, uid, gid)
      :canonical: aiida.transports.transport.Transport.chown
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.chown

   .. py:method:: copy(remotesource, remotedestination, dereference=False, recursive=True)
      :canonical: aiida.transports.transport.Transport.copy
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.copy

   .. py:method:: copyfile(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.transport.Transport.copyfile
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.copyfile

   .. py:method:: copytree(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.transport.Transport.copytree
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.copytree

   .. py:method:: copy_from_remote_to_remote(transportdestination, remotesource, remotedestination, **kwargs)
      :canonical: aiida.transports.transport.Transport.copy_from_remote_to_remote

      .. autodoc2-docstring:: aiida.transports.transport.Transport.copy_from_remote_to_remote

   .. py:method:: _exec_command_internal(command, **kwargs)
      :canonical: aiida.transports.transport.Transport._exec_command_internal
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport._exec_command_internal

   .. py:method:: exec_command_wait_bytes(command, stdin=None, **kwargs)
      :canonical: aiida.transports.transport.Transport.exec_command_wait_bytes
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.exec_command_wait_bytes

   .. py:method:: exec_command_wait(command, stdin=None, encoding='utf-8', **kwargs)
      :canonical: aiida.transports.transport.Transport.exec_command_wait

      .. autodoc2-docstring:: aiida.transports.transport.Transport.exec_command_wait

   .. py:method:: get(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.get
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get

   .. py:method:: getfile(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.getfile
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.getfile

   .. py:method:: gettree(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.gettree
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.gettree

   .. py:method:: getcwd()
      :canonical: aiida.transports.transport.Transport.getcwd
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.getcwd

   .. py:method:: get_attribute(path)
      :canonical: aiida.transports.transport.Transport.get_attribute
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get_attribute

   .. py:method:: get_mode(path)
      :canonical: aiida.transports.transport.Transport.get_mode

      .. autodoc2-docstring:: aiida.transports.transport.Transport.get_mode

   .. py:method:: isdir(path)
      :canonical: aiida.transports.transport.Transport.isdir
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.isdir

   .. py:method:: isfile(path)
      :canonical: aiida.transports.transport.Transport.isfile
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.isfile

   .. py:method:: listdir(path='.', pattern=None)
      :canonical: aiida.transports.transport.Transport.listdir
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.listdir

   .. py:method:: listdir_withattributes(path='.', pattern=None)
      :canonical: aiida.transports.transport.Transport.listdir_withattributes

      .. autodoc2-docstring:: aiida.transports.transport.Transport.listdir_withattributes

   .. py:method:: makedirs(path, ignore_existing=False)
      :canonical: aiida.transports.transport.Transport.makedirs
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.makedirs

   .. py:method:: mkdir(path, ignore_existing=False)
      :canonical: aiida.transports.transport.Transport.mkdir
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.mkdir

   .. py:method:: normalize(path='.')
      :canonical: aiida.transports.transport.Transport.normalize
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.normalize

   .. py:method:: put(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.put
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.put

   .. py:method:: putfile(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.putfile
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.putfile

   .. py:method:: puttree(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.puttree
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.puttree

   .. py:method:: remove(path)
      :canonical: aiida.transports.transport.Transport.remove
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.remove

   .. py:method:: rename(oldpath, newpath)
      :canonical: aiida.transports.transport.Transport.rename
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.rename

   .. py:method:: rmdir(path)
      :canonical: aiida.transports.transport.Transport.rmdir
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.rmdir

   .. py:method:: rmtree(path)
      :canonical: aiida.transports.transport.Transport.rmtree
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.rmtree

   .. py:method:: gotocomputer_command(remotedir)
      :canonical: aiida.transports.transport.Transport.gotocomputer_command
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.gotocomputer_command

   .. py:method:: symlink(remotesource, remotedestination)
      :canonical: aiida.transports.transport.Transport.symlink
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.symlink

   .. py:method:: whoami()
      :canonical: aiida.transports.transport.Transport.whoami

      .. autodoc2-docstring:: aiida.transports.transport.Transport.whoami

   .. py:method:: path_exists(path)
      :canonical: aiida.transports.transport.Transport.path_exists
      :abstractmethod:

      .. autodoc2-docstring:: aiida.transports.transport.Transport.path_exists

   .. py:method:: glob(pathname)
      :canonical: aiida.transports.transport.Transport.glob

      .. autodoc2-docstring:: aiida.transports.transport.Transport.glob

   .. py:method:: iglob(pathname)
      :canonical: aiida.transports.transport.Transport.iglob

      .. autodoc2-docstring:: aiida.transports.transport.Transport.iglob

   .. py:method:: glob1(dirname, pattern)
      :canonical: aiida.transports.transport.Transport.glob1

      .. autodoc2-docstring:: aiida.transports.transport.Transport.glob1

   .. py:method:: glob0(dirname, basename)
      :canonical: aiida.transports.transport.Transport.glob0

      .. autodoc2-docstring:: aiida.transports.transport.Transport.glob0

   .. py:method:: has_magic(string)
      :canonical: aiida.transports.transport.Transport.has_magic

      .. autodoc2-docstring:: aiida.transports.transport.Transport.has_magic

   .. py:method:: _gotocomputer_string(remotedir)
      :canonical: aiida.transports.transport.Transport._gotocomputer_string

      .. autodoc2-docstring:: aiida.transports.transport.Transport._gotocomputer_string

.. py:function:: convert_to_bool(string)
   :canonical: aiida.transports.plugins.ssh.convert_to_bool

   .. autodoc2-docstring:: aiida.transports.plugins.ssh.convert_to_bool

.. py:function:: parse_sshconfig(computername)
   :canonical: aiida.transports.plugins.ssh.parse_sshconfig

   .. autodoc2-docstring:: aiida.transports.plugins.ssh.parse_sshconfig
