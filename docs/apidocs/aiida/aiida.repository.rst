:py:mod:`aiida.repository`
==========================

.. py:module:: aiida.repository


Description
-----------

Module with resources dealing with the file repository.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbstractRepositoryBackend <aiida.repository.backend.abstract.AbstractRepositoryBackend>`
     - Class that defines the abstract interface for an object repository.
   * - :py:obj:`DiskObjectStoreRepositoryBackend <aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend>`
     - Implementation of the ``AbstractRepositoryBackend`` using the ``disk-object-store`` as the backend.
   * - :py:obj:`File <aiida.repository.common.File>`
     - Data class representing a file object.
   * - :py:obj:`FileType <aiida.repository.common.FileType>`
     - Enumeration to represent the type of a file object.
   * - :py:obj:`Repository <aiida.repository.repository.Repository>`
     - File repository.
   * - :py:obj:`SandboxRepositoryBackend <aiida.repository.backend.sandbox.SandboxRepositoryBackend>`
     - Implementation of the ``AbstractRepositoryBackend`` using a sandbox folder on disk as the backend.

API
~~~

.. py:class:: AbstractRepositoryBackend
   :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend

   Class that defines the abstract interface for an object repository.

   The repository backend only deals with raw bytes, both when creating new objects as well as when returning a stream
   or the content of an existing object. The encoding and decoding of the byte content should be done by the client
   upstream. The file repository backend is also not expected to keep any kind of file hierarchy but must be assumed
   to be a simple flat data store. When files are created in the file object repository, the implementation will return
   a string-based key with which the content of the stored object can be addressed. This key is guaranteed to be unique
   and persistent. Persisting the key or mapping it onto a virtual file hierarchy is again up to the client upstream.


   .. py:property:: uuid
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.uuid
      :abstractmethod:
      :type: typing.Optional[str]

      Return the unique identifier of the repository.

   .. py:property:: key_format
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.key_format
      :abstractmethod:
      :type: typing.Optional[str]

      Return the format for the keys of the repository.

      Important for when migrating between backends (e.g. archive -> main), as if they are not equal then it is
      necessary to re-compute all the `Node.base.repository.metadata` before importing (otherwise they will not match
      with the repository).


   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.initialise
      :abstractmethod:

      Initialise the repository if it hasn't already been initialised.

      :param kwargs: parameters for the initialisation.


   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_initialised
      :abstractmethod:
      :type: bool

      Return whether the repository has been initialised.

   .. py:method:: erase() -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.erase
      :abstractmethod:

      Delete the repository itself and all its contents.

      .. note:: This should not merely delete the contents of the repository but any resources it created. For
          example, if the repository is essentially a folder on disk, the folder itself should also be deleted, not
          just its contents.


   .. py:method:: is_readable_byte_stream(handle) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_readable_byte_stream
      :staticmethod:

   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_filelike

      Store the byte contents of a file in the repository.

      :param handle: filelike object with the byte content to be stored.
      :return: the generated fully qualified identifier for the object within the repository.
      :raises TypeError: if the handle is not a byte stream.


   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend._put_object_from_filelike
      :abstractmethod:

   .. py:method:: put_object_from_file(filepath: typing.Union[str, pathlib.Path]) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_file

      Store a new object with contents of the file located at `filepath` on this file system.

      :param filepath: absolute path of file whose contents to copy to the repository.
      :return: the generated fully qualified identifier for the object within the repository.
      :raises TypeError: if the handle is not a byte stream.


   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_objects
      :abstractmethod:

      Return whether the repository has an object with the given key.

      :param keys:
          list of fully qualified identifiers for objects within the repository.
      :return:
          list of logicals, in the same order as the keys provided, with value True if the respective
          object exists and False otherwise.


   .. py:method:: has_object(key: str) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_object

      Return whether the repository has an object with the given key.

      :param key: fully qualified identifier for the object within the repository.
      :return: True if the object exists, False otherwise.


   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.list_objects
      :abstractmethod:

      Return iterable that yields all available objects by key.

      :return: An iterable for all the available object keys.


   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_info
      :abstractmethod:

      Returns relevant information about the content of the repository.

      :param detailed:
          flag to enable extra information (detailed=False by default, only returns basic information).

      :return: a dictionary with the information.


   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.maintain
      :abstractmethod:

      Performs maintenance operations.

      :param dry_run:
          flag to only print the actions that would be taken without actually executing them.

      :param live:
          flag to indicate to the backend whether AiiDA is live or not (i.e. if the profile of the
          backend is currently being used/accessed). The backend is expected then to only allow (and
          thus set by default) the operations that are safe to perform in this state.


   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.open

      Open a file handle to an object stored under the given key.

      .. note:: this should only be used to open a handle to read an existing file. To write a new file use the method
          ``put_object_from_filelike`` instead.

      :param key: fully qualified identifier for the object within the repository.
      :return: yield a byte stream object.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be opened.


   .. py:method:: get_object_content(key: str) -> bytes
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_content

      Return the content of a object identified by key.

      :param key: fully qualified identifier for the object within the repository.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be opened.


   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.iter_object_streams
      :abstractmethod:

      Return an iterator over the (read-only) byte streams of objects identified by key.

      .. note:: handles should only be read within the context of this iterator.

      :param keys: fully qualified identifiers for the objects within the repository.
      :return: an iterator over the object byte streams.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if a file could not be opened.


   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_hash

      Return the SHA-256 hash of an object stored under the given key.

      .. important::
          A SHA-256 hash should always be returned,
          to ensure consistency across different repository implementations.

      :param key: fully qualified identifier for the object within the repository.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be opened.


   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_objects
      :abstractmethod:

      Delete the objects from the repository.

      :param keys: list of fully qualified identifiers for the objects within the repository.
      :raise FileNotFoundError: if any of the files does not exist.
      :raise OSError: if any of the files could not be deleted.


   .. py:method:: delete_object(key: str) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_object

      Delete the object from the repository.

      :param key: fully qualified identifier for the object within the repository.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be deleted.


.. py:class:: DiskObjectStoreRepositoryBackend(container: disk_objectstore.Container)
   :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   Implementation of the ``AbstractRepositoryBackend`` using the ``disk-object-store`` as the backend.

   .. note:: For certain methods, the container may create a sessions which should be closed after the operation is
       done to make sure the connection to the underlying sqlite database is closed. The best way is to accomplish this
       is by using the container as a context manager, which will automatically call the ``close`` method when it exits
       which ensures the session being closed. Note that not all methods may open the session and so need closing it,
       but to be on the safe side, we put every use of the container in a context manager. If no session is created,
       the ``close`` method is essentially a no-op.



   .. py:method:: __init__(container: disk_objectstore.Container)
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__init__

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__str__

      Return the string representation of this repository.

   .. py:property:: uuid
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.uuid
      :type: typing.Optional[str]

      Return the unique identifier of the repository.

   .. py:property:: key_format
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.key_format
      :type: typing.Optional[str]

      Return the format for the keys of the repository.

      Important for when migrating between backends (e.g. archive -> main), as if they are not equal then it is
      necessary to re-compute all the `Node.base.repository.metadata` before importing (otherwise they will not match
      with the repository).


   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.initialise

      Initialise the repository if it hasn't already been initialised.

      :param kwargs: parameters for the initialisation.


   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.is_initialised
      :type: bool

      Return whether the repository has been initialised.

   .. py:method:: erase()
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.erase

      Delete the repository itself and all its contents.

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend._put_object_from_filelike

      Store the byte contents of a file in the repository.

      :param handle: filelike object with the byte content to be stored.
      :return: the generated fully qualified identifier for the object within the repository.
      :raises TypeError: if the handle is not a byte stream.


   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.has_objects

      Return whether the repository has an object with the given key.

      :param keys:
          list of fully qualified identifiers for objects within the repository.
      :return:
          list of logicals, in the same order as the keys provided, with value True if the respective
          object exists and False otherwise.


   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.open

      Open a file handle to an object stored under the given key.

      .. note:: this should only be used to open a handle to read an existing file. To write a new file use the method
          ``put_object_from_filelike`` instead.

      :param key: fully qualified identifier for the object within the repository.
      :return: yield a byte stream object.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be opened.


   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.iter_object_streams

      Return an iterator over the (read-only) byte streams of objects identified by key.

      .. note:: handles should only be read within the context of this iterator.

      :param keys: fully qualified identifiers for the objects within the repository.
      :return: an iterator over the object byte streams.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if a file could not be opened.


   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.delete_objects

      Delete the objects from the repository.

      :param keys: list of fully qualified identifiers for the objects within the repository.
      :raise FileNotFoundError: if any of the files does not exist.
      :raise OSError: if any of the files could not be deleted.


   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.list_objects

      Return iterable that yields all available objects by key.

      :return: An iterable for all the available object keys.


   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_object_hash

      Return the SHA-256 hash of an object stored under the given key.

      .. important::
          A SHA-256 hash should always be returned,
          to ensure consistency across different repository implementations.

      :param key: fully qualified identifier for the object within the repository.
      :raise FileNotFoundError: if the file does not exist.



   .. py:method:: maintain(dry_run: bool = False, live: bool = True, pack_loose: bool = None, do_repack: bool = None, clean_storage: bool = None, do_vacuum: bool = None) -> dict
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.maintain

      Performs maintenance operations.

      :param live:if True, will only perform operations that are safe to do while the repository is in use.
      :param pack_loose:flag for forcing the packing of loose files.
      :param do_repack:flag for forcing the re-packing of already packed files.
      :param clean_storage:flag for forcing the cleaning of soft-deleted files from the repository.
      :param do_vacuum:flag for forcing the vacuuming of the internal database when cleaning the repository.
      :return:a dictionary with information on the operations performed.


   .. py:method:: get_info(detailed=False) -> typing.Dict[str, typing.Union[int, str, typing.Dict[str, int], typing.Dict[str, float]]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_info

      Return information on configuration and content of the repository.

.. py:class:: File(name: str = '', file_type: aiida.repository.common.FileType = FileType.DIRECTORY, key: typing.Union[str, None] = None, objects: typing.Optional[typing.Dict[str, aiida.repository.common.File]] = None)
   :canonical: aiida.repository.common.File

   Data class representing a file object.

   .. py:method:: __init__(name: str = '', file_type: aiida.repository.common.FileType = FileType.DIRECTORY, key: typing.Union[str, None] = None, objects: typing.Optional[typing.Dict[str, aiida.repository.common.File]] = None) -> None
      :canonical: aiida.repository.common.File.__init__

      Construct a new instance.

      :param name: The final element of the file path
      :param file_type: Identifies whether the File is a file or a directory
      :param key: A key to map the file to its contents in the backend repository (file only)
      :param objects: Mapping of child names to child Files (directory only)

      :raises ValueError: If a key is defined for a directory,
          or objects are defined for a file


   .. py:method:: from_serialized(serialized: dict, name='') -> aiida.repository.common.File
      :canonical: aiida.repository.common.File.from_serialized
      :classmethod:

      Construct a new instance from a serialized instance.

      :param serialized: the serialized instance.
      :return: the reconstructed file object.


   .. py:method:: serialize() -> dict
      :canonical: aiida.repository.common.File.serialize

      Serialize the metadata into a JSON-serializable format.

      .. note:: the serialization format is optimized to reduce the size in bytes.

      :return: dictionary with the content metadata.


   .. py:property:: name
      :canonical: aiida.repository.common.File.name
      :type: str

      Return the name of the file object.

   .. py:property:: file_type
      :canonical: aiida.repository.common.File.file_type
      :type: aiida.repository.common.FileType

      Return the file type of the file object.

   .. py:method:: is_file() -> bool
      :canonical: aiida.repository.common.File.is_file

      Return whether this instance is a file object.

   .. py:method:: is_dir() -> bool
      :canonical: aiida.repository.common.File.is_dir

      Return whether this instance is a directory object.

   .. py:property:: key
      :canonical: aiida.repository.common.File.key
      :type: typing.Union[str, None]

      Return the key of the file object.

   .. py:property:: objects
      :canonical: aiida.repository.common.File.objects
      :type: typing.Dict[str, aiida.repository.common.File]

      Return the objects of the file object.

   .. py:method:: __eq__(other) -> bool
      :canonical: aiida.repository.common.File.__eq__

      Return whether this instance is equal to another file object instance.

   .. py:method:: __repr__()
      :canonical: aiida.repository.common.File.__repr__

      Return repr(self).

.. py:class:: FileType
   :canonical: aiida.repository.common.FileType

   Bases: :py:obj:`enum.Enum`

   Enumeration to represent the type of a file object.

   .. py:attribute:: DIRECTORY
      :canonical: aiida.repository.common.FileType.DIRECTORY
      :value: 0

   .. py:attribute:: FILE
      :canonical: aiida.repository.common.FileType.FILE
      :value: 1

.. py:class:: Repository(backend: typing.Optional[aiida.repository.backend.AbstractRepositoryBackend] = None)
   :canonical: aiida.repository.repository.Repository

   File repository.

   This class provides an interface to a backend file repository instance, but unlike the backend repository, this
   class keeps a reference of the virtual file hierarchy. This means that through this interface, a client can create
   files and directories with a file hierarchy, just as they would on a local file system, except it is completely
   virtual as the files are stored by the backend which can store them in a completely flat structure. This also means
   that the internal virtual hierarchy of a ``Repository`` instance does not necessarily represent all the files that
   are stored by repository backend. The repository exposes a mere subset of all the file objects stored in the
   backend. This is why object deletion is also implemented as a soft delete, by default, where the files are just
   removed from the internal virtual hierarchy, but not in the actual backend. This is because those objects can be
   referenced by other instances.


   .. py:attribute:: _file_cls
      :canonical: aiida.repository.repository.Repository._file_cls
      :value: None

   .. py:method:: __init__(backend: typing.Optional[aiida.repository.backend.AbstractRepositoryBackend] = None)
      :canonical: aiida.repository.repository.Repository.__init__

      Construct a new instance with empty metadata.

      :param backend: instance of repository backend to use to actually store the file objects. By default, an
          instance of the ``SandboxRepositoryBackend`` will be created.


   .. py:method:: __str__() -> str
      :canonical: aiida.repository.repository.Repository.__str__

      Return the string representation of this repository.

   .. py:property:: uuid
      :canonical: aiida.repository.repository.Repository.uuid
      :type: typing.Optional[str]

      Return the unique identifier of the repository backend or ``None`` if it doesn't have one.

   .. py:property:: is_initialised
      :canonical: aiida.repository.repository.Repository.is_initialised
      :type: bool

      Return whether the repository backend has been initialised.

   .. py:method:: from_serialized(backend: aiida.repository.backend.AbstractRepositoryBackend, serialized: typing.Dict[str, typing.Any]) -> aiida.repository.repository.Repository
      :canonical: aiida.repository.repository.Repository.from_serialized
      :classmethod:

      Construct an instance where the metadata is initialized from the serialized content.

      :param backend: instance of repository backend to use to actually store the file objects.


   .. py:method:: reset() -> None
      :canonical: aiida.repository.repository.Repository.reset

   .. py:method:: serialize() -> typing.Dict[str, typing.Any]
      :canonical: aiida.repository.repository.Repository.serialize

      Serialize the metadata into a JSON-serializable format.

      :return: dictionary with the content metadata.


   .. py:method:: flatten(serialized=Optional[Dict[str, Any]], delimiter: str = '/') -> typing.Dict[str, typing.Optional[str]]
      :canonical: aiida.repository.repository.Repository.flatten
      :classmethod:

      Flatten the serialized content of a repository into a mapping of path -> key or None (if folder).

      Note, all folders are represented in the flattened output, and their path is suffixed with the delimiter.

      :param serialized: the serialized content of the repository.
      :param delimiter: the delimiter to use to separate the path elements.
      :return: dictionary with the flattened content.


   .. py:method:: hash() -> str
      :canonical: aiida.repository.repository.Repository.hash

      Generate a hash of the repository's contents.

      .. warning:: this will read the content of all file objects contained within the virtual hierarchy into memory.

      :return: the hash representing the contents of the repository.


   .. py:method:: _pre_process_path(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> pathlib.PurePosixPath
      :canonical: aiida.repository.repository.Repository._pre_process_path
      :staticmethod:

      Validate and convert the path to instance of ``pathlib.PurePosixPath``.

      This should be called by every method of this class before doing anything, such that it can safely assume that
      the path is a ``pathlib.PurePosixPath`` object, which makes path manipulation a lot easier.

      :param path: the path as a ``pathlib.PurePosixPath`` object or `None`.
      :raises TypeError: if the type of path was not a str nor a ``pathlib.PurePosixPath`` instance.


   .. py:property:: backend
      :canonical: aiida.repository.repository.Repository.backend
      :type: aiida.repository.backend.AbstractRepositoryBackend

      Return the current repository backend.

      :return: the repository backend.


   .. py:method:: set_backend(backend: aiida.repository.backend.AbstractRepositoryBackend) -> None
      :canonical: aiida.repository.repository.Repository.set_backend

      Set the backend for this repository.

      :param backend: the repository backend.
      :raises TypeError: if the type of the backend is invalid.


   .. py:method:: _insert_file(path: pathlib.PurePosixPath, key: str) -> None
      :canonical: aiida.repository.repository.Repository._insert_file

      Insert a new file object in the object mapping.

      .. note:: this assumes the path is a valid relative path, so should be checked by the caller.

      :param path: the relative path where to store the object in the repository.
      :param key: fully qualified identifier for the object within the repository.


   .. py:method:: create_directory(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.create_directory

      Create a new directory with the given path.

      :param path: the relative path of the directory.
      :return: the created directory.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.


   .. py:method:: get_file_keys() -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.get_file_keys

      Return the keys of all file objects contained within this repository.

      :return: list of keys, which map a file to its content in the backend repository.


   .. py:method:: get_object(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_object

      Return the object at the given path.

      :param path: the relative path where to store the object in the repository.
      :return: the `File` representing the object located at the given relative path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.


   .. py:method:: get_directory(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_directory

      Return the directory object at the given path.

      :param path: the relative path of the directory.
      :return: the `File` representing the object located at the given relative path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises NotADirectoryError: if the object at the given path is not a directory.


   .. py:method:: get_file(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_file

      Return the file object at the given path.

      :param path: the relative path of the file object.
      :return: the `File` representing the object located at the given relative path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises IsADirectoryError: if the object at the given path is not a directory.


   .. py:method:: list_objects(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[aiida.repository.common.File]
      :canonical: aiida.repository.repository.Repository.list_objects

      Return a list of the objects contained in this repository sorted by name, optionally in given sub directory.

      :param path: the relative path of the directory.
      :return: a list of `File` named tuples representing the objects present in directory with the given path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises NotADirectoryError: if the object at the given path is not a directory.


   .. py:method:: list_object_names(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.list_object_names

      Return a sorted list of the object names contained in this repository, optionally in the given sub directory.

      :param path: the relative path of the directory.
      :return: a list of `File` named tuples representing the objects present in directory with the given path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if no object exists for the given path.
      :raises NotADirectoryError: if the object at the given path is not a directory.


   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_filelike

      Store the byte contents of a file in the repository.

      :param handle: filelike object with the byte content to be stored.
      :param path: the relative path where to store the object in the repository.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.


   .. py:method:: put_object_from_file(filepath: aiida.repository.repository.FilePath, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_file

      Store a new object under `path` with contents of the file located at `filepath` on the local file system.

      :param filepath: absolute path of file whose contents to copy to the repository
      :param path: the relative path where to store the object in the repository.
      :raises TypeError: if the path is not a string and relative path, or the handle is not a byte stream.


   .. py:method:: put_object_from_tree(filepath: aiida.repository.repository.FilePath, path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_tree

      Store the entire contents of `filepath` on the local file system in the repository with under given `path`.

      :param filepath: absolute path of the directory whose contents to copy to the repository.
      :param path: the relative path where to store the objects in the repository.
      :raises TypeError: if the filepath is not a string or ``Path``, or is a relative path.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.


   .. py:method:: is_empty() -> bool
      :canonical: aiida.repository.repository.Repository.is_empty

      Return whether the repository is empty.

      :return: True if the repository contains no file objects.


   .. py:method:: has_object(path: aiida.repository.repository.FilePath) -> bool
      :canonical: aiida.repository.repository.Repository.has_object

      Return whether the repository has an object with the given path.

      :param path: the relative path of the object within the repository.
      :return: True if the object exists, False otherwise.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.


   .. py:method:: open(path: aiida.repository.repository.FilePath) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.repository.Repository.open

      Open a file handle to an object stored under the given path.

      .. note:: this should only be used to open a handle to read an existing file. To write a new file use the method
          ``put_object_from_filelike`` instead.

      :param path: the relative path of the object within the repository.
      :return: yield a byte stream object.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be opened.


   .. py:method:: get_object_content(path: aiida.repository.repository.FilePath) -> bytes
      :canonical: aiida.repository.repository.Repository.get_object_content

      Return the content of a object identified by path.

      :param path: the relative path of the object within the repository.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be opened.


   .. py:method:: delete_object(path: aiida.repository.repository.FilePath, hard_delete: bool = False) -> None
      :canonical: aiida.repository.repository.Repository.delete_object

      Soft delete the object from the repository.

      .. note:: can only delete file objects, but not directories.

      :param path: the relative path of the object within the repository.
      :param hard_delete: when true, not only remove the file from the internal mapping but also call through to the
          ``delete_object`` method of the actual repository backend.
      :raises TypeError: if the path is not a string or ``Path``, or is an absolute path.
      :raises FileNotFoundError: if the file does not exist.
      :raises IsADirectoryError: if the object is a directory and not a file.
      :raises OSError: if the file could not be deleted.


   .. py:method:: erase() -> None
      :canonical: aiida.repository.repository.Repository.erase

      Delete all objects from the repository.

      .. important: this intentionally does not call through to any ``erase`` method of the backend, because unlike
          this class, the backend does not just store the objects of a single node, but potentially of a lot of other
          nodes. Therefore, we manually delete all file objects and then simply reset the internal file hierarchy.



   .. py:method:: clone(source: aiida.repository.repository.Repository) -> None
      :canonical: aiida.repository.repository.Repository.clone

      Clone the contents of another repository instance.

   .. py:method:: walk(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.Iterable[typing.Tuple[pathlib.PurePosixPath, typing.List[str], typing.List[str]]]
      :canonical: aiida.repository.repository.Repository.walk

      Walk over the directories and files contained within this repository.

      .. note:: the order of the dirname and filename lists that are returned is not necessarily sorted. This is in
          line with the ``os.walk`` implementation where the order depends on the underlying file system used.

      :param path: the relative path of the directory within the repository whose contents to walk.
      :return: tuples of root, dirnames and filenames just like ``os.walk``, with the exception that the root path is
          always relative with respect to the repository root, instead of an absolute path and it is an instance of
          ``pathlib.PurePosixPath`` instead of a normal string


   .. py:method:: copy_tree(target: typing.Union[str, pathlib.Path], path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.copy_tree

      Copy the contents of the entire node repository to another location on the local file system.

      .. note:: If ``path`` is specified, only its contents are copied, and the relative path with respect to the
          root is discarded. For example, if ``path`` is ``relative/sub``, the contents of ``sub`` will be copied
          directly to the target, without the ``relative/sub`` directory.

      :param target: absolute path of the directory where to copy the contents to.
      :param path: optional relative path whose contents to copy.
      :raises TypeError: if ``target`` is of incorrect type or not absolute.
      :raises NotADirectoryError: if ``path`` does not reference a directory.


   .. py:method:: initialise(**kwargs: typing.Any) -> None
      :canonical: aiida.repository.repository.Repository.initialise

      Initialise the repository if it hasn't already been initialised.

      :param kwargs: keyword argument that will be passed to the ``initialise`` call of the backend.


   .. py:method:: delete() -> None
      :canonical: aiida.repository.repository.Repository.delete

      Delete the repository.

      .. important:: This will not just delete the contents of the repository but also the repository itself and all
          of its assets. For example, if the repository is stored inside a folder on disk, the folder may be deleted.


.. py:class:: SandboxRepositoryBackend(filepath: str | None = None)
   :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   Implementation of the ``AbstractRepositoryBackend`` using a sandbox folder on disk as the backend.

   .. py:method:: __init__(filepath: str | None = None)
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__init__

      Construct a new instance.

      :param filepath: The path to the directory in which the sandbox folder should be created.


   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__str__

      Return the string representation of this repository.

   .. py:method:: __del__()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__del__

      Delete the entire sandbox folder if it was instantiated and still exists.

   .. py:property:: uuid
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.uuid
      :type: str | None

      Return the unique identifier of the repository.

      .. note:: A sandbox folder does not have the concept of a unique identifier and so always returns ``None``.


   .. py:property:: key_format
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.key_format
      :type: str | None

      Return the format for the keys of the repository.

      Important for when migrating between backends (e.g. archive -> main), as if they are not equal then it is
      necessary to re-compute all the `Node.base.repository.metadata` before importing (otherwise they will not match
      with the repository).


   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.initialise

      Initialise the repository if it hasn't already been initialised.

      :param kwargs: parameters for the initialisation.


   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.is_initialised
      :type: bool

      Return whether the repository has been initialised.

   .. py:property:: sandbox
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.sandbox

      Return the sandbox instance of this repository.

   .. py:method:: erase()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.erase

      Delete the repository itself and all its contents.

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend._put_object_from_filelike

      Store the byte contents of a file in the repository.

      :param handle: filelike object with the byte content to be stored.
      :return: the generated fully qualified identifier for the object within the repository.
      :raises TypeError: if the handle is not a byte stream.


   .. py:method:: has_objects(keys: list[str]) -> list[bool]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.has_objects

      Return whether the repository has an object with the given key.

      :param keys:
          list of fully qualified identifiers for objects within the repository.
      :return:
          list of logicals, in the same order as the keys provided, with value True if the respective
          object exists and False otherwise.


   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.open

      Open a file handle to an object stored under the given key.

      .. note:: this should only be used to open a handle to read an existing file. To write a new file use the method
          ``put_object_from_filelike`` instead.

      :param key: fully qualified identifier for the object within the repository.
      :return: yield a byte stream object.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if the file could not be opened.


   .. py:method:: iter_object_streams(keys: list[str]) -> typing.Iterator[tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.iter_object_streams

      Return an iterator over the (read-only) byte streams of objects identified by key.

      .. note:: handles should only be read within the context of this iterator.

      :param keys: fully qualified identifiers for the objects within the repository.
      :return: an iterator over the object byte streams.
      :raise FileNotFoundError: if the file does not exist.
      :raise OSError: if a file could not be opened.


   .. py:method:: delete_objects(keys: list[str]) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.delete_objects

      Delete the objects from the repository.

      :param keys: list of fully qualified identifiers for the objects within the repository.
      :raise FileNotFoundError: if any of the files does not exist.
      :raise OSError: if any of the files could not be deleted.


   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.list_objects

      Return iterable that yields all available objects by key.

      :return: An iterable for all the available object keys.


   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.maintain
      :abstractmethod:

      Performs maintenance operations.

      :param dry_run:
          flag to only print the actions that would be taken without actually executing them.

      :param live:
          flag to indicate to the backend whether AiiDA is live or not (i.e. if the profile of the
          backend is currently being used/accessed). The backend is expected then to only allow (and
          thus set by default) the operations that are safe to perform in this state.


   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.get_info
      :abstractmethod:

      Returns relevant information about the content of the repository.

      :param detailed:
          flag to enable extra information (detailed=False by default, only returns basic information).

      :return: a dictionary with the information.

