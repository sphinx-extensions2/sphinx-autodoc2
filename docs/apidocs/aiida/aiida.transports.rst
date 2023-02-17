:py:mod:`aiida.transports`
==========================

.. py:module:: aiida.transports


Description
-----------

Module for classes and utilities to define transports to other machines.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SshTransport <aiida.transports.plugins.ssh.SshTransport>`
     - Support connection, command execution and data transfer to remote computers via SSH+SFTP.
   * - :py:obj:`Transport <aiida.transports.transport.Transport>`
     - Abstract class for a generic transport (ssh, local, ...) contains the set of minimal methods.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`convert_to_bool <aiida.transports.plugins.ssh.convert_to_bool>`
     - Convert a string passed in the CLI to a valid bool.
   * - :py:obj:`parse_sshconfig <aiida.transports.plugins.ssh.parse_sshconfig>`
     - Return the ssh configuration for a given computer name.

API
~~~

.. py:class:: SshTransport(*args, **kwargs)
   :canonical: aiida.transports.plugins.ssh.SshTransport

   Bases: :py:obj:`aiida.transports.transport.Transport`

   Support connection, command execution and data transfer to remote computers via SSH+SFTP.


   .. py:attribute:: _valid_connect_options
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_connect_options
      :value: [('username',), ('port',), ('look_for_keys',), ('key_filename',), ('timeout',), ('allow_agent',), ('...

   .. py:attribute:: _valid_connect_params
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_connect_params
      :value: None

   .. py:attribute:: _valid_auth_options
      :canonical: aiida.transports.plugins.ssh.SshTransport._valid_auth_options
      :value: None

   .. py:attribute:: _MAX_EXEC_COMMAND_LOG_SIZE
      :canonical: aiida.transports.plugins.ssh.SshTransport._MAX_EXEC_COMMAND_LOG_SIZE
      :value: None

   .. py:method:: _get_username_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_username_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_port_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_port_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_key_filename_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_key_filename_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_timeout_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_timeout_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.

      Provide 60s as a default timeout for connections.


   .. py:method:: _get_allow_agent_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_allow_agent_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_look_for_keys_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_look_for_keys_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_proxy_command_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_proxy_command_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_proxy_jump_suggestion_string(_)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_proxy_jump_suggestion_string
      :classmethod:

      Return an empty suggestion since Paramiko does not parse ProxyJump from the SSH config.


   .. py:method:: _get_compress_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_compress_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_load_system_host_keys_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_load_system_host_keys_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_key_policy_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_key_policy_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_gss_auth_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_auth_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_gss_kex_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_kex_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_gss_deleg_creds_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_deleg_creds_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: _get_gss_host_suggestion_string(computer)
      :canonical: aiida.transports.plugins.ssh.SshTransport._get_gss_host_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:method:: __init__(*args, **kwargs)
      :canonical: aiida.transports.plugins.ssh.SshTransport.__init__

      Initialize the SshTransport class.

      :param machine: the machine to connect to
      :param load_system_host_keys: (optional, default False)
         if False, do not load the system host keys
      :param key_policy: (optional, default = paramiko.RejectPolicy())
         the policy to use for unknown keys

      Other parameters valid for the ssh connect function (see the
      self._valid_connect_params list) are passed to the connect
      function (as port, username, password, ...); taken from the
      accepted paramiko.SSHClient.connect() params.


   .. py:method:: open()
      :canonical: aiida.transports.plugins.ssh.SshTransport.open

      Open a SSHClient to the machine possibly using the parameters given
      in the __init__.

      Also opens a sftp channel, ready to be used.
      The current working directory is set explicitly, so it is not None.

      :raise aiida.common.InvalidOperation: if the channel is already open


   .. py:method:: _close_proxies()
      :canonical: aiida.transports.plugins.ssh.SshTransport._close_proxies

      Close all proxy connections (proxy_jump and proxy_command)

   .. py:method:: close()
      :canonical: aiida.transports.plugins.ssh.SshTransport.close

      Close the SFTP channel, and the SSHClient.

      :todo: correctly manage exceptions

      :raise aiida.common.InvalidOperation: if the channel is already open


   .. py:property:: sshclient
      :canonical: aiida.transports.plugins.ssh.SshTransport.sshclient

   .. py:property:: sftp
      :canonical: aiida.transports.plugins.ssh.SshTransport.sftp

   .. py:method:: __str__()
      :canonical: aiida.transports.plugins.ssh.SshTransport.__str__

      Return a useful string.


   .. py:method:: chdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chdir

      Change directory of the SFTP session. Emulated internally by paramiko.

      Differently from paramiko, if you pass None to chdir, nothing
      happens and the cwd is unchanged.


   .. py:method:: normalize(path='.')
      :canonical: aiida.transports.plugins.ssh.SshTransport.normalize

      Returns the normalized path (removing double slashes, etc...)


   .. py:method:: stat(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.stat

      Retrieve information about a file on the remote system.  The return
      value is an object whose attributes correspond to the attributes of
      Python's ``stat`` structure as returned by ``os.stat``, except that it
      contains fewer fields.
      The fields supported are: ``st_mode``, ``st_size``, ``st_uid``,
      ``st_gid``, ``st_atime``, and ``st_mtime``.

      :param str path: the filename to stat

      :return: a `paramiko.sftp_attr.SFTPAttributes` object containing
          attributes about the given file.


   .. py:method:: lstat(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.lstat

      Retrieve information about a file on the remote system, without
      following symbolic links (shortcuts). This otherwise behaves exactly
      the same as `stat`.

      :param str path: the filename to stat

      :return: a `paramiko.sftp_attr.SFTPAttributes` object containing
          attributes about the given file.


   .. py:method:: getcwd()
      :canonical: aiida.transports.plugins.ssh.SshTransport.getcwd

      Return the current working directory for this SFTP session, as
      emulated by paramiko. If no directory has been set with chdir,
      this method will return None. But in __enter__ this is set explicitly,
      so this should never happen within this class.


   .. py:method:: makedirs(path, ignore_existing=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.makedirs

      Super-mkdir; create a leaf directory and all intermediate ones.
      Works like mkdir, except that any intermediate path segment (not
      just the rightmost) will be created if it does not exist.

      NOTE: since os.path.split uses the separators as the host system
      (that could be windows), I assume the remote computer is Linux-based
      and use '/' as separators!

      :param path: directory to create (string)
      :param ignore_existing: if set to true, it doesn't give any error
          if the leaf directory does already exist (bool)

      :raise OSError: If the directory already exists.


   .. py:method:: mkdir(path, ignore_existing=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.mkdir

      Create a folder (directory) named path.

      :param path: name of the folder to create
      :param ignore_existing: if True, does not give any error if the directory
                already exists

      :raise OSError: If the directory already exists.


   .. py:method:: rmtree(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rmtree

      Remove a file or a directory at path, recursively
      Flags used: -r: recursive copy; -f: force, makes the command non interactive;

      :param path: remote path to delete

      :raise IOError: if the rm execution failed.


   .. py:method:: rmdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rmdir

      Remove the folder named 'path' if empty.


   .. py:method:: chown(path, uid, gid)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chown
      :abstractmethod:

      Change owner permissions of a file.

      For now, this is not implemented for the SSH transport.


   .. py:method:: isdir(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.isdir

      Return True if the given path is a directory, False otherwise.
      Return False also if the path does not exist.


   .. py:method:: chmod(path, mode)
      :canonical: aiida.transports.plugins.ssh.SshTransport.chmod

      Change permissions to path

      :param path: path to file
      :param mode: new permission bits (integer)


   .. py:method:: _os_path_split_asunder(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport._os_path_split_asunder
      :staticmethod:

      Used by makedirs. Takes path (a str)
      and returns a list deconcatenating the path


   .. py:method:: put(localpath, remotepath, callback=None, dereference=True, overwrite=True, ignore_nonexisting=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.put

      Put a file or a folder from local to remote.
      Redirects to putfile or puttree.

      :param localpath: an (absolute) local path
      :param remotepath: a remote path
      :param dereference: follow symbolic links (boolean).
          Default = True (default behaviour in paramiko). False is not implemented.
      :param  overwrite: if True overwrites files and folders (boolean).
          Default = False.

      :raise ValueError: if local path is invalid
      :raise OSError: if the localpath does not exist


   .. py:method:: putfile(localpath, remotepath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.putfile

      Put a file from local to remote.

      :param localpath: an (absolute) local path
      :param remotepath: a remote path
      :param overwrite: if True overwrites files and folders (boolean).
          Default = True.

      :raise ValueError: if local path is invalid
      :raise OSError: if the localpath does not exist,
                  or unintentionally overwriting


   .. py:method:: puttree(localpath, remotepath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.puttree

      Put a folder recursively from local to remote.

      By default, overwrite.

      :param localpath: an (absolute) local path
      :param remotepath: a remote path
      :param dereference: follow symbolic links (boolean)
          Default = True (default behaviour in paramiko). False is not implemented.
      :param overwrite: if True overwrites files and folders (boolean).
          Default = True

      :raise ValueError: if local path is invalid
      :raise OSError: if the localpath does not exist, or trying to overwrite
      :raise IOError: if remotepath is invalid

      .. note:: setting dereference equal to True could cause infinite loops.
            see os.walk() documentation


   .. py:method:: get(remotepath, localpath, callback=None, dereference=True, overwrite=True, ignore_nonexisting=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.get

      Get a file or folder from remote to local.
      Redirects to getfile or gettree.

      :param remotepath: a remote path
      :param localpath: an (absolute) local path
      :param dereference: follow symbolic links.
          Default = True (default behaviour in paramiko).
          False is not implemented.
      :param overwrite: if True overwrites files and folders.
          Default = False

      :raise ValueError: if local path is invalid
      :raise IOError: if the remotepath is not found


   .. py:method:: getfile(remotepath, localpath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.getfile

      Get a file from remote to local.

      :param remotepath: a remote path
      :param  localpath: an (absolute) local path
      :param  overwrite: if True overwrites files and folders.
              Default = False

      :raise ValueError: if local path is invalid
      :raise OSError: if unintentionally overwriting


   .. py:method:: gettree(remotepath, localpath, callback=None, dereference=True, overwrite=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.gettree

      Get a folder recursively from remote to local.

      :param remotepath: a remote path
      :param localpath: an (absolute) local path
      :param dereference: follow symbolic links.
          Default = True (default behaviour in paramiko).
          False is not implemented.
      :param  overwrite: if True overwrites files and folders.
          Default = False

      :raise ValueError: if local path is invalid
      :raise IOError: if the remotepath is not found
      :raise OSError: if unintentionally overwriting


   .. py:method:: get_attribute(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.get_attribute

      Returns the object Fileattribute, specified in aiida.transports
      Receives in input the path of a given file.


   .. py:method:: copyfile(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copyfile

      Copy a file from remote source to remote destination
      (On the same remote machine)

      :param str remotesource: path of the remote source directory / file
      :param str remotedestination: path of the remote destination directory / file
      :param dereference: if True copy the contents of any symlinks found, otherwise copy the symlinks themselves
      :type dereference: bool

      :raises IOError: if one of src or dst does not exist


   .. py:method:: copytree(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copytree

      Copy a folder from remote source to remote destination
      (On the same remote machine)

      :param str remotesource: path of the remote source directory / file
      :param str remotedestination: path of the remote destination directory / file
      :param dereference: if True copy the contents of any symlinks found, otherwise copy the symlinks themselves
      :type dereference: bool

      :raise IOError: if one of src or dst does not exist


   .. py:method:: copy(remotesource, remotedestination, dereference=False, recursive=True)
      :canonical: aiida.transports.plugins.ssh.SshTransport.copy

      Copy a file or a directory from remote source to remote destination.
      Flags used: ``-r``: recursive copy; ``-f``: force, makes the command non interactive;
      ``-L`` follows symbolic links

      :param  remotesource: file to copy from
      :param remotedestination: file to copy to
      :param dereference: if True, copy content instead of copying the symlinks only
          Default = False.
      :param recursive: if True copy directories recursively, otherwise only copy the specified file(s)
      :type recursive: bool
      :raise IOError: if the cp execution failed.

      .. note:: setting dereference equal to True could cause infinite loops.


   .. py:method:: _exec_cp(cp_exe, cp_flags, src, dst)
      :canonical: aiida.transports.plugins.ssh.SshTransport._exec_cp

      Execute the ``cp`` command on the remote machine.

   .. py:method:: _local_listdir(path, pattern=None)
      :canonical: aiida.transports.plugins.ssh.SshTransport._local_listdir
      :staticmethod:

      Acts on the local folder, for the rest, same as listdir


   .. py:method:: listdir(path='.', pattern=None)
      :canonical: aiida.transports.plugins.ssh.SshTransport.listdir

      Get the list of files at path.

      :param path: default = '.'
      :param pattern: returns the list of files matching pattern.
                           Unix only. (Use to emulate ``ls *`` for example)


   .. py:method:: remove(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.remove

      Remove a single file at 'path'


   .. py:method:: rename(oldpath, newpath)
      :canonical: aiida.transports.plugins.ssh.SshTransport.rename

      Rename a file or folder from oldpath to newpath.

      :param str oldpath: existing name of the file or folder
      :param str newpath: new name for the file or folder

      :raises IOError: if oldpath/newpath is not found
      :raises ValueError: if sroldpathc/newpath is not a valid string


   .. py:method:: isfile(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.isfile

      Return True if the given path is a file, False otherwise.
      Return False also if the path does not exist.


   .. py:method:: _exec_command_internal(command, combine_stderr=False, bufsize=-1)
      :canonical: aiida.transports.plugins.ssh.SshTransport._exec_command_internal

      Executes the specified command in bash login shell.

      Before the command is executed, changes directory to the current
      working directory as returned by self.getcwd().

      For executing commands and waiting for them to finish, use
      exec_command_wait.

      :param  command: the command to execute. The command is assumed to be
          already escaped using :py:func:`aiida.common.escaping.escape_for_bash`.
      :param combine_stderr: (default False) if True, combine stdout and
              stderr on the same buffer (i.e., stdout).
              Note: If combine_stderr is True, stderr will always be empty.
      :param bufsize: same meaning of the one used by paramiko.

      :return: a tuple with (stdin, stdout, stderr, channel),
          where stdin, stdout and stderr behave as file-like objects,
          plus the methods provided by paramiko, and channel is a
          paramiko.Channel object.


   .. py:method:: exec_command_wait_bytes(command, stdin=None, combine_stderr=False, bufsize=-1)
      :canonical: aiida.transports.plugins.ssh.SshTransport.exec_command_wait_bytes

      Executes the specified command and waits for it to finish.

      :param command: the command to execute
      :param stdin: (optional,default=None) can be a string or a
                 file-like object.
      :param combine_stderr: (optional, default=False) see docstring of
                 self._exec_command_internal()
      :param bufsize: same meaning of paramiko.

      :return: a tuple with (return_value, stdout, stderr) where stdout and stderr
          are both bytes and the return_value is an int.


   .. py:method:: gotocomputer_command(remotedir)
      :canonical: aiida.transports.plugins.ssh.SshTransport.gotocomputer_command

      Specific gotocomputer string to connect to a given remote computer via
      ssh and directly go to the calculation folder.


   .. py:method:: _symlink(source, dest)
      :canonical: aiida.transports.plugins.ssh.SshTransport._symlink

      Wrap SFTP symlink call without breaking API

      :param source: source of link
      :param dest: link to create


   .. py:method:: symlink(remotesource, remotedestination)
      :canonical: aiida.transports.plugins.ssh.SshTransport.symlink

      Create a symbolic link between the remote source and the remote
      destination.

      :param remotesource: remote source. Can contain a pattern.
      :param remotedestination: remote destination


   .. py:method:: path_exists(path)
      :canonical: aiida.transports.plugins.ssh.SshTransport.path_exists

      Check if path exists


.. py:class:: Transport(*args, **kwargs)
   :canonical: aiida.transports.transport.Transport

   Bases: :py:obj:`abc.ABC`

   Abstract class for a generic transport (ssh, local, ...) contains the set of minimal methods.

   .. py:attribute:: DEFAULT_MINIMUM_JOB_POLL_INTERVAL
      :canonical: aiida.transports.transport.Transport.DEFAULT_MINIMUM_JOB_POLL_INTERVAL
      :value: 10

   .. py:attribute:: _DEFAULT_SAFE_OPEN_INTERVAL
      :canonical: aiida.transports.transport.Transport._DEFAULT_SAFE_OPEN_INTERVAL
      :value: 30.0

   .. py:attribute:: _valid_auth_params
      :canonical: aiida.transports.transport.Transport._valid_auth_params
      :value: None

   .. py:attribute:: _MAGIC_CHECK
      :canonical: aiida.transports.transport.Transport._MAGIC_CHECK
      :value: None

   .. py:attribute:: _valid_auth_options
      :canonical: aiida.transports.transport.Transport._valid_auth_options
      :type: list
      :value: []

   .. py:attribute:: _common_auth_options
      :canonical: aiida.transports.transport.Transport._common_auth_options
      :value: [('use_login_shell',), ('safe_interval',)]

   .. py:method:: __init__(*args, **kwargs)
      :canonical: aiida.transports.transport.Transport.__init__

      __init__ method of the Transport base class.

      :param safe_interval: (optional, default self._DEFAULT_SAFE_OPEN_INTERVAL)
         Minimum time interval in seconds between opening new connections.
      :param use_login_shell: (optional, default True)
         if False, do not use a login shell when executing command


   .. py:method:: __enter__()
      :canonical: aiida.transports.transport.Transport.__enter__

      For transports that require opening a connection, opens
      all required channels (used in 'with' statements).

      This object can be used in nested `with` statements and the connection
      will only be opened once and closed when the final `with` scope
      finishes e.g.::

          t = Transport()
          with t:
              # Connection is now open..
              with t:
                  # ..still open..
                  pass
              # ..still open..
          # ...closed



   .. py:method:: __exit__(type_, value, traceback)
      :canonical: aiida.transports.transport.Transport.__exit__

      Closes connections, if needed (used in 'with' statements).


   .. py:property:: is_open
      :canonical: aiida.transports.transport.Transport.is_open

   .. py:method:: open()
      :canonical: aiida.transports.transport.Transport.open
      :abstractmethod:

      Opens a local transport channel


   .. py:method:: close()
      :canonical: aiida.transports.transport.Transport.close
      :abstractmethod:

      Closes the local transport channel


   .. py:method:: __repr__()
      :canonical: aiida.transports.transport.Transport.__repr__

      Return repr(self).

   .. py:method:: __str__()
      :canonical: aiida.transports.transport.Transport.__str__

      Return str(self).

   .. py:method:: set_logger_extra(logger_extra)
      :canonical: aiida.transports.transport.Transport.set_logger_extra

      Pass the data that should be passed automatically to self.logger
      as 'extra' keyword. This is typically useful if you pass data
      obtained using get_dblogger_extra in aiida.orm.utils.log, to automatically
      log also to the DbLog table.

      :param logger_extra: data that you want to pass as extra to the
        self.logger. To write to DbLog, it should be created by the
        aiida.orm.utils.log.get_dblogger_extra function. Pass None if you
        do not want to have extras passed.


   .. py:method:: get_short_doc()
      :canonical: aiida.transports.transport.Transport.get_short_doc
      :classmethod:

      Return the first non-empty line of the class docstring, if available


   .. py:method:: get_valid_auth_params()
      :canonical: aiida.transports.transport.Transport.get_valid_auth_params
      :classmethod:

      Return the internal list of valid auth_params


   .. py:method:: auth_options() -> collections.OrderedDict
      :canonical: aiida.transports.transport.Transport.auth_options

      Return the authentication options to be used for building the CLI.

      :return: `OrderedDict` of tuples, with first element option name and second dictionary of kwargs


   .. py:method:: _get_safe_interval_suggestion_string(computer)
      :canonical: aiida.transports.transport.Transport._get_safe_interval_suggestion_string
      :classmethod:

      Return as a suggestion the default safe interval of this Transport class.

      This is used to provide a default in ``verdi computer configure``.


   .. py:method:: _get_use_login_shell_suggestion_string(computer)
      :canonical: aiida.transports.transport.Transport._get_use_login_shell_suggestion_string
      :classmethod:

      Return a suggestion for the specific field.


   .. py:property:: logger
      :canonical: aiida.transports.transport.Transport.logger

      Return the internal logger.
      If you have set extra parameters using set_logger_extra(), a
      suitable LoggerAdapter instance is created, bringing with itself
      also the extras.


   .. py:method:: get_safe_open_interval()
      :canonical: aiida.transports.transport.Transport.get_safe_open_interval

      Get an interval (in seconds) that suggests how long the user should wait
      between consecutive calls to open the transport.  This can be used as
      a way to get the user to not swamp a limited number of connections, etc.
      However it is just advisory.

      If returns 0, it is taken that there are no reasons to limit the
      frequency of open calls.

      In the main class, it returns a default value (>0 for safety), set in
      the _DEFAULT_SAFE_OPEN_INTERVAL attribute of the class. Plugins should override it.

      :return: The safe interval between calling open, in seconds
      :rtype: float


   .. py:method:: chdir(path)
      :canonical: aiida.transports.transport.Transport.chdir
      :abstractmethod:

      Change directory to 'path'

      :param str path: path to change working directory into.
      :raises: IOError, if the requested path does not exist
      :rtype: str


   .. py:method:: chmod(path, mode)
      :canonical: aiida.transports.transport.Transport.chmod
      :abstractmethod:

      Change permissions of a path.

      :param str path: path to file
      :param int mode: new permissions


   .. py:method:: chown(path, uid, gid)
      :canonical: aiida.transports.transport.Transport.chown
      :abstractmethod:

      Change the owner (uid) and group (gid) of a file.
      As with python's os.chown function, you must pass both arguments,
      so if you only want to change one, use stat first to retrieve the
      current owner and group.

      :param str path: path to the file to change the owner and group of
      :param int uid: new owner's uid
      :param int gid: new group id


   .. py:method:: copy(remotesource, remotedestination, dereference=False, recursive=True)
      :canonical: aiida.transports.transport.Transport.copy
      :abstractmethod:

      Copy a file or a directory from remote source to remote destination
      (On the same remote machine)

      :param str remotesource: path of the remote source directory / file
      :param str remotedestination: path of the remote destination directory / file
      :param dereference: if True copy the contents of any symlinks found, otherwise copy the symlinks themselves
      :type dereference: bool
      :param recursive: if True copy directories recursively, otherwise only copy the specified file(s)
      :type recursive: bool

      :raises: IOError, if one of src or dst does not exist


   .. py:method:: copyfile(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.transport.Transport.copyfile
      :abstractmethod:

      Copy a file from remote source to remote destination
      (On the same remote machine)

      :param str remotesource: path of the remote source directory / file
      :param str remotedestination: path of the remote destination directory / file
      :param dereference: if True copy the contents of any symlinks found, otherwise copy the symlinks themselves
      :type dereference: bool

      :raises IOError: if one of src or dst does not exist


   .. py:method:: copytree(remotesource, remotedestination, dereference=False)
      :canonical: aiida.transports.transport.Transport.copytree
      :abstractmethod:

      Copy a folder from remote source to remote destination
      (On the same remote machine)

      :param str remotesource: path of the remote source directory / file
      :param str remotedestination: path of the remote destination directory / file
      :param dereference: if True copy the contents of any symlinks found, otherwise copy the symlinks themselves
      :type dereference: bool

      :raise IOError: if one of src or dst does not exist


   .. py:method:: copy_from_remote_to_remote(transportdestination, remotesource, remotedestination, **kwargs)
      :canonical: aiida.transports.transport.Transport.copy_from_remote_to_remote

      Copy files or folders from a remote computer to another remote computer.

      :param transportdestination: transport to be used for the destination computer
      :param str remotesource: path to the remote source directory / file
      :param str remotedestination: path to the remote destination directory / file
      :param kwargs: keyword parameters passed to the call to transportdestination.put,
          except for 'dereference' that is passed to self.get

      .. note:: the keyword 'dereference' SHOULD be set to False for the
       final put (onto the destination), while it can be set to the
       value given in kwargs for the get from the source. In that
       way, a symbolic link would never be followed in the final
       copy to the remote destination. That way we could avoid getting
       unknown (potentially malicious) files into the destination computer.
       HOWEVER, since dereference=False is currently NOT
       supported by all plugins, we still force it to True for the final put.

      .. note:: the supported keys in kwargs are callback, dereference,
         overwrite and ignore_nonexisting.


   .. py:method:: _exec_command_internal(command, **kwargs)
      :canonical: aiida.transports.transport.Transport._exec_command_internal
      :abstractmethod:

      Execute the command on the shell, similarly to os.system.

      Enforce the execution to be run from the cwd (as given by
      self.getcwd), if this is not None.

      If possible, use the higher-level
      exec_command_wait function.

      :param str command: execute the command given as a string
      :return: stdin, stdout, stderr and the session, when this exists                  (can be None).


   .. py:method:: exec_command_wait_bytes(command, stdin=None, **kwargs)
      :canonical: aiida.transports.transport.Transport.exec_command_wait_bytes
      :abstractmethod:

      Execute the command on the shell, waits for it to finish,
      and return the retcode, the stdout and the stderr as bytes.

      Enforce the execution to be run from the pwd (as given by self.getcwd), if this is not None.

      The command implementation can have some additional plugin-specific kwargs.

      :param str command: execute the command given as a string
      :param stdin: (optional,default=None) can be a string or a file-like object.
      :return: a tuple: the retcode (int), stdout (bytes) and stderr (bytes).


   .. py:method:: exec_command_wait(command, stdin=None, encoding='utf-8', **kwargs)
      :canonical: aiida.transports.transport.Transport.exec_command_wait

      Executes the specified command and waits for it to finish.

      :note: this function also decodes the bytes received into a string with the specified encoding,
          which is set to be ``utf-8`` by default (for backward-compatibility with earlier versions) of
          AiiDA.
          Use this method only if you are sure that you are getting a properly encoded string; otherwise,
          use the ``exec_command_wait_bytes`` method that returns the undecoded byte stream.

      :note: additional kwargs are passed to the ``exec_command_wait_bytes`` function, that might use them
          depending on the plugin.

      :param command: the command to execute
      :param stdin: (optional,default=None) can be a string or a file-like object.
      :param encoding: the encoding to use to decode the byte stream received from the remote command execution.

      :return: a tuple with (return_value, stdout, stderr) where stdout and stderr are both strings, decoded
          with the specified encoding.


   .. py:method:: get(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.get
      :abstractmethod:

      Retrieve a file or folder from remote source to local destination
      dst must be an absolute path (src not necessarily)

      :param remotepath: (str) remote_folder_path
      :param localpath: (str) local_folder_path


   .. py:method:: getfile(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.getfile
      :abstractmethod:

      Retrieve a file from remote source to local destination
      dst must be an absolute path (src not necessarily)

      :param str remotepath: remote_folder_path
      :param str localpath: local_folder_path


   .. py:method:: gettree(remotepath, localpath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.gettree
      :abstractmethod:

      Retrieve a folder recursively from remote source to local destination
      dst must be an absolute path (src not necessarily)

      :param str remotepath: remote_folder_path
      :param str localpath: local_folder_path


   .. py:method:: getcwd()
      :canonical: aiida.transports.transport.Transport.getcwd
      :abstractmethod:

      Get working directory

      :return: a string identifying the current working directory


   .. py:method:: get_attribute(path)
      :canonical: aiida.transports.transport.Transport.get_attribute
      :abstractmethod:

      Return an object FixedFieldsAttributeDict for file in a given path,
      as defined in aiida.common.extendeddicts
      Each attribute object consists in a dictionary with the following keys:

      * st_size: size of files, in bytes

      * st_uid: user id of owner

      * st_gid: group id of owner

      * st_mode: protection bits

      * st_atime: time of most recent access

      * st_mtime: time of most recent modification

      :param str path: path to file
      :return: object FixedFieldsAttributeDict


   .. py:method:: get_mode(path)
      :canonical: aiida.transports.transport.Transport.get_mode

      Return the portion of the file's mode that can be set by chmod().

      :param str path: path to file
      :return: the portion of the file's mode that can be set by chmod()


   .. py:method:: isdir(path)
      :canonical: aiida.transports.transport.Transport.isdir
      :abstractmethod:

      True if path is an existing directory.

      :param str path: path to directory
      :return: boolean


   .. py:method:: isfile(path)
      :canonical: aiida.transports.transport.Transport.isfile
      :abstractmethod:

      Return True if path is an existing file.

      :param str path: path to file
      :return: boolean


   .. py:method:: listdir(path='.', pattern=None)
      :canonical: aiida.transports.transport.Transport.listdir
      :abstractmethod:

      Return a list of the names of the entries in the given path.
      The list is in arbitrary order. It does not include the special
      entries '.' and '..' even if they are present in the directory.

      :param str path: path to list (default to '.')
      :param str pattern: if used, listdir returns a list of files matching
                          filters in Unix style. Unix only.
      :return: a list of strings


   .. py:method:: listdir_withattributes(path='.', pattern=None)
      :canonical: aiida.transports.transport.Transport.listdir_withattributes

      Return a list of the names of the entries in the given path.
      The list is in arbitrary order. It does not include the special
      entries '.' and '..' even if they are present in the directory.

      :param str path: path to list (default to '.')
      :param str pattern: if used, listdir returns a list of files matching
                          filters in Unix style. Unix only.
      :return: a list of dictionaries, one per entry.
          The schema of the dictionary is
          the following::

              {
                 'name': String,
                 'attributes': FileAttributeObject,
                 'isdir': Bool
              }

          where 'name' is the file or folder directory, and any other information is metadata
          (if the file is a folder, a directory, ...). 'attributes' behaves as the output of
          transport.get_attribute(); isdir is a boolean indicating if the object is a directory or not.


   .. py:method:: makedirs(path, ignore_existing=False)
      :canonical: aiida.transports.transport.Transport.makedirs
      :abstractmethod:

      Super-mkdir; create a leaf directory and all intermediate ones.
      Works like mkdir, except that any intermediate path segment (not
      just the rightmost) will be created if it does not exist.

      :param str path: directory to create
      :param bool ignore_existing: if set to true, it doesn't give any error
                                   if the leaf directory does already exist

      :raises: OSError, if directory at path already exists


   .. py:method:: mkdir(path, ignore_existing=False)
      :canonical: aiida.transports.transport.Transport.mkdir
      :abstractmethod:

      Create a folder (directory) named path.

      :param str path: name of the folder to create
      :param bool ignore_existing: if True, does not give any error if the
                                   directory already exists

      :raises: OSError, if directory at path already exists


   .. py:method:: normalize(path='.')
      :canonical: aiida.transports.transport.Transport.normalize
      :abstractmethod:

      Return the normalized path (on the server) of a given path.
      This can be used to quickly resolve symbolic links or determine
      what the server is considering to be the "current folder".

      :param str path: path to be normalized

      :raise IOError: if the path can't be resolved on the server


   .. py:method:: put(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.put
      :abstractmethod:

      Put a file or a directory from local src to remote dst.
      src must be an absolute path (dst not necessarily))
      Redirects to putfile and puttree.

      :param str localpath: absolute path to local source
      :param str remotepath: path to remote destination


   .. py:method:: putfile(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.putfile
      :abstractmethod:

      Put a file from local src to remote dst.
      src must be an absolute path (dst not necessarily))

      :param str localpath: absolute path to local file
      :param str remotepath: path to remote file


   .. py:method:: puttree(localpath, remotepath, *args, **kwargs)
      :canonical: aiida.transports.transport.Transport.puttree
      :abstractmethod:

      Put a folder recursively from local src to remote dst.
      src must be an absolute path (dst not necessarily))

      :param str localpath: absolute path to local folder
      :param str remotepath: path to remote folder


   .. py:method:: remove(path)
      :canonical: aiida.transports.transport.Transport.remove
      :abstractmethod:

      Remove the file at the given path. This only works on files;
      for removing folders (directories), use rmdir.

      :param str path: path to file to remove

      :raise IOError: if the path is a directory


   .. py:method:: rename(oldpath, newpath)
      :canonical: aiida.transports.transport.Transport.rename
      :abstractmethod:

      Rename a file or folder from oldpath to newpath.

      :param str oldpath: existing name of the file or folder
      :param str newpath: new name for the file or folder

      :raises IOError: if oldpath/newpath is not found
      :raises ValueError: if oldpath/newpath is not a valid string


   .. py:method:: rmdir(path)
      :canonical: aiida.transports.transport.Transport.rmdir
      :abstractmethod:

      Remove the folder named path.
      This works only for empty folders. For recursive remove, use rmtree.

      :param str path: absolute path to the folder to remove


   .. py:method:: rmtree(path)
      :canonical: aiida.transports.transport.Transport.rmtree
      :abstractmethod:

      Remove recursively the content at path

      :param str path: absolute path to remove


   .. py:method:: gotocomputer_command(remotedir)
      :canonical: aiida.transports.transport.Transport.gotocomputer_command
      :abstractmethod:

      Return a string to be run using os.system in order to connect
      via the transport to the remote directory.

      Expected behaviors:

      * A new bash session is opened

      * A reasonable error message is produced if the folder does not exist

      :param str remotedir: the full path of the remote directory


   .. py:method:: symlink(remotesource, remotedestination)
      :canonical: aiida.transports.transport.Transport.symlink
      :abstractmethod:

      Create a symbolic link between the remote source and the remote
      destination.

      :param remotesource: remote source
      :param remotedestination: remote destination


   .. py:method:: whoami()
      :canonical: aiida.transports.transport.Transport.whoami

      Get the remote username

      :return: list of username (str),
               retval (int),
               stderr (str)


   .. py:method:: path_exists(path)
      :canonical: aiida.transports.transport.Transport.path_exists
      :abstractmethod:

      Returns True if path exists, False otherwise.


   .. py:method:: glob(pathname)
      :canonical: aiida.transports.transport.Transport.glob

      Return a list of paths matching a pathname pattern.

      The pattern may contain simple shell-style wildcards a la fnmatch.


   .. py:method:: iglob(pathname)
      :canonical: aiida.transports.transport.Transport.iglob

      Return an iterator which yields the paths matching a pathname pattern.

      The pattern may contain simple shell-style wildcards a la fnmatch.



   .. py:method:: glob1(dirname, pattern)
      :canonical: aiida.transports.transport.Transport.glob1

      Match subpaths of dirname against pattern.

   .. py:method:: glob0(dirname, basename)
      :canonical: aiida.transports.transport.Transport.glob0

      Wrap basename i a list if it is empty or if dirname/basename is an existing path, else return empty list.

   .. py:method:: has_magic(string)
      :canonical: aiida.transports.transport.Transport.has_magic

   .. py:method:: _gotocomputer_string(remotedir)
      :canonical: aiida.transports.transport.Transport._gotocomputer_string

      command executed when goto computer.

.. py:function:: convert_to_bool(string)
   :canonical: aiida.transports.plugins.ssh.convert_to_bool

   Convert a string passed in the CLI to a valid bool.

   :return: the parsed bool value.
   :raise ValueError: If the value is not parsable as a bool


.. py:function:: parse_sshconfig(computername)
   :canonical: aiida.transports.plugins.ssh.parse_sshconfig

   Return the ssh configuration for a given computer name.

   This parses the ``.ssh/config`` file in the home directory and
   returns the part of configuration of the given computer name.

   :param computername: the computer name for which we want the configuration.

