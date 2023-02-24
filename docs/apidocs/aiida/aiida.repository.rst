:py:mod:`aiida.repository`
==========================

.. py:module:: aiida.repository

.. autodoc2-docstring:: aiida.repository
   :renderer: rst
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbstractRepositoryBackend <aiida.repository.backend.abstract.AbstractRepositoryBackend>`
     - .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend
          :renderer: rst
          :summary:
   * - :py:obj:`DiskObjectStoreRepositoryBackend <aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend>`
     - .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend
          :renderer: rst
          :summary:
   * - :py:obj:`File <aiida.repository.common.File>`
     - .. autodoc2-docstring:: aiida.repository.common.File
          :renderer: rst
          :summary:
   * - :py:obj:`FileType <aiida.repository.common.FileType>`
     - .. autodoc2-docstring:: aiida.repository.common.FileType
          :renderer: rst
          :summary:
   * - :py:obj:`Repository <aiida.repository.repository.Repository>`
     - .. autodoc2-docstring:: aiida.repository.repository.Repository
          :renderer: rst
          :summary:
   * - :py:obj:`SandboxRepositoryBackend <aiida.repository.backend.sandbox.SandboxRepositoryBackend>`
     - .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend
          :renderer: rst
          :summary:

API
~~~

.. py:class:: AbstractRepositoryBackend
   :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend

   .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend
      :renderer: rst

   .. py:property:: uuid
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.uuid
      :abstractmethod:
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.uuid
         :renderer: rst

   .. py:property:: key_format
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.key_format
      :abstractmethod:
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.key_format
         :renderer: rst

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.initialise
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.initialise
         :renderer: rst

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_initialised
      :abstractmethod:
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_initialised
         :renderer: rst

   .. py:method:: erase() -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.erase
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.erase
         :renderer: rst

   .. py:method:: is_readable_byte_stream(handle) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_readable_byte_stream
      :staticmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_readable_byte_stream
         :renderer: rst

   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_filelike
         :renderer: rst

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend._put_object_from_filelike
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend._put_object_from_filelike
         :renderer: rst

   .. py:method:: put_object_from_file(filepath: typing.Union[str, pathlib.Path]) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_file

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_file
         :renderer: rst

   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_objects
         :renderer: rst

   .. py:method:: has_object(key: str) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_object

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_object
         :renderer: rst

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.list_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.list_objects
         :renderer: rst

   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_info
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_info
         :renderer: rst

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.maintain
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.maintain
         :renderer: rst

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.open

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.open
         :renderer: rst

   .. py:method:: get_object_content(key: str) -> bytes
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_content

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_content
         :renderer: rst

   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.iter_object_streams
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.iter_object_streams
         :renderer: rst

   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_hash

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_hash
         :renderer: rst

   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_objects
         :renderer: rst

   .. py:method:: delete_object(key: str) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_object

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_object
         :renderer: rst

.. py:class:: DiskObjectStoreRepositoryBackend(container: disk_objectstore.Container)
   :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__init__
      :renderer: rst

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__str__

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__str__
         :renderer: rst

   .. py:property:: uuid
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.uuid
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.uuid
         :renderer: rst

   .. py:property:: key_format
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.key_format
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.key_format
         :renderer: rst

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.initialise

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.initialise
         :renderer: rst

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.is_initialised
         :renderer: rst

   .. py:method:: erase()
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.erase

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.erase
         :renderer: rst

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend._put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend._put_object_from_filelike
         :renderer: rst

   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.has_objects

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.has_objects
         :renderer: rst

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.open

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.open
         :renderer: rst

   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.iter_object_streams

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.iter_object_streams
         :renderer: rst

   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.delete_objects

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.delete_objects
         :renderer: rst

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.list_objects

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.list_objects
         :renderer: rst

   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_object_hash

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_object_hash
         :renderer: rst

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, pack_loose: bool = None, do_repack: bool = None, clean_storage: bool = None, do_vacuum: bool = None) -> dict
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.maintain

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.maintain
         :renderer: rst

   .. py:method:: get_info(detailed=False) -> typing.Dict[str, typing.Union[int, str, typing.Dict[str, int], typing.Dict[str, float]]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_info

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_info
         :renderer: rst

.. py:class:: File(name: str = '', file_type: aiida.repository.common.FileType = FileType.DIRECTORY, key: typing.Union[str, None] = None, objects: typing.Optional[typing.Dict[str, aiida.repository.common.File]] = None)
   :canonical: aiida.repository.common.File

   .. autodoc2-docstring:: aiida.repository.common.File
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.common.File.__init__
      :renderer: rst

   .. py:method:: from_serialized(serialized: dict, name='') -> aiida.repository.common.File
      :canonical: aiida.repository.common.File.from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.common.File.from_serialized
         :renderer: rst

   .. py:method:: serialize() -> dict
      :canonical: aiida.repository.common.File.serialize

      .. autodoc2-docstring:: aiida.repository.common.File.serialize
         :renderer: rst

   .. py:property:: name
      :canonical: aiida.repository.common.File.name
      :type: str

      .. autodoc2-docstring:: aiida.repository.common.File.name
         :renderer: rst

   .. py:property:: file_type
      :canonical: aiida.repository.common.File.file_type
      :type: aiida.repository.common.FileType

      .. autodoc2-docstring:: aiida.repository.common.File.file_type
         :renderer: rst

   .. py:method:: is_file() -> bool
      :canonical: aiida.repository.common.File.is_file

      .. autodoc2-docstring:: aiida.repository.common.File.is_file
         :renderer: rst

   .. py:method:: is_dir() -> bool
      :canonical: aiida.repository.common.File.is_dir

      .. autodoc2-docstring:: aiida.repository.common.File.is_dir
         :renderer: rst

   .. py:property:: key
      :canonical: aiida.repository.common.File.key
      :type: typing.Union[str, None]

      .. autodoc2-docstring:: aiida.repository.common.File.key
         :renderer: rst

   .. py:property:: objects
      :canonical: aiida.repository.common.File.objects
      :type: typing.Dict[str, aiida.repository.common.File]

      .. autodoc2-docstring:: aiida.repository.common.File.objects
         :renderer: rst

   .. py:method:: __eq__(other) -> bool
      :canonical: aiida.repository.common.File.__eq__

      .. autodoc2-docstring:: aiida.repository.common.File.__eq__
         :renderer: rst

   .. py:method:: __repr__()
      :canonical: aiida.repository.common.File.__repr__

      .. autodoc2-docstring:: aiida.repository.common.File.__repr__
         :renderer: rst

.. py:class:: FileType
   :canonical: aiida.repository.common.FileType

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.repository.common.FileType
      :renderer: rst

   .. py:attribute:: DIRECTORY
      :canonical: aiida.repository.common.FileType.DIRECTORY
      :value: 0

      .. autodoc2-docstring:: aiida.repository.common.FileType.DIRECTORY
         :renderer: rst

   .. py:attribute:: FILE
      :canonical: aiida.repository.common.FileType.FILE
      :value: 1

      .. autodoc2-docstring:: aiida.repository.common.FileType.FILE
         :renderer: rst

.. py:class:: Repository(backend: typing.Optional[aiida.repository.backend.AbstractRepositoryBackend] = None)
   :canonical: aiida.repository.repository.Repository

   .. autodoc2-docstring:: aiida.repository.repository.Repository
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.repository.Repository.__init__
      :renderer: rst

   .. py:attribute:: _file_cls
      :canonical: aiida.repository.repository.Repository._file_cls
      :value: None

      .. autodoc2-docstring:: aiida.repository.repository.Repository._file_cls
         :renderer: rst

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.repository.Repository.__str__

      .. autodoc2-docstring:: aiida.repository.repository.Repository.__str__
         :renderer: rst

   .. py:property:: uuid
      :canonical: aiida.repository.repository.Repository.uuid
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.repository.Repository.uuid
         :renderer: rst

   .. py:property:: is_initialised
      :canonical: aiida.repository.repository.Repository.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.repository.Repository.is_initialised
         :renderer: rst

   .. py:method:: from_serialized(backend: aiida.repository.backend.AbstractRepositoryBackend, serialized: typing.Dict[str, typing.Any]) -> aiida.repository.repository.Repository
      :canonical: aiida.repository.repository.Repository.from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository.from_serialized
         :renderer: rst

   .. py:method:: reset() -> None
      :canonical: aiida.repository.repository.Repository.reset

      .. autodoc2-docstring:: aiida.repository.repository.Repository.reset
         :renderer: rst

   .. py:method:: serialize() -> typing.Dict[str, typing.Any]
      :canonical: aiida.repository.repository.Repository.serialize

      .. autodoc2-docstring:: aiida.repository.repository.Repository.serialize
         :renderer: rst

   .. py:method:: flatten(serialized=Optional[Dict[str, Any]], delimiter: str = '/') -> typing.Dict[str, typing.Optional[str]]
      :canonical: aiida.repository.repository.Repository.flatten
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository.flatten
         :renderer: rst

   .. py:method:: hash() -> str
      :canonical: aiida.repository.repository.Repository.hash

      .. autodoc2-docstring:: aiida.repository.repository.Repository.hash
         :renderer: rst

   .. py:method:: _pre_process_path(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> pathlib.PurePosixPath
      :canonical: aiida.repository.repository.Repository._pre_process_path
      :staticmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository._pre_process_path
         :renderer: rst

   .. py:property:: backend
      :canonical: aiida.repository.repository.Repository.backend
      :type: aiida.repository.backend.AbstractRepositoryBackend

      .. autodoc2-docstring:: aiida.repository.repository.Repository.backend
         :renderer: rst

   .. py:method:: set_backend(backend: aiida.repository.backend.AbstractRepositoryBackend) -> None
      :canonical: aiida.repository.repository.Repository.set_backend

      .. autodoc2-docstring:: aiida.repository.repository.Repository.set_backend
         :renderer: rst

   .. py:method:: _insert_file(path: pathlib.PurePosixPath, key: str) -> None
      :canonical: aiida.repository.repository.Repository._insert_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository._insert_file
         :renderer: rst

   .. py:method:: create_directory(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.create_directory

      .. autodoc2-docstring:: aiida.repository.repository.Repository.create_directory
         :renderer: rst

   .. py:method:: get_file_keys() -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.get_file_keys

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_file_keys
         :renderer: rst

   .. py:method:: get_object(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_object
         :renderer: rst

   .. py:method:: get_directory(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_directory

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_directory
         :renderer: rst

   .. py:method:: get_file(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_file
         :renderer: rst

   .. py:method:: list_objects(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[aiida.repository.common.File]
      :canonical: aiida.repository.repository.Repository.list_objects

      .. autodoc2-docstring:: aiida.repository.repository.Repository.list_objects
         :renderer: rst

   .. py:method:: list_object_names(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.list_object_names

      .. autodoc2-docstring:: aiida.repository.repository.Repository.list_object_names
         :renderer: rst

   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_filelike
         :renderer: rst

   .. py:method:: put_object_from_file(filepath: aiida.repository.repository.FilePath, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_file
         :renderer: rst

   .. py:method:: put_object_from_tree(filepath: aiida.repository.repository.FilePath, path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_tree

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_tree
         :renderer: rst

   .. py:method:: is_empty() -> bool
      :canonical: aiida.repository.repository.Repository.is_empty

      .. autodoc2-docstring:: aiida.repository.repository.Repository.is_empty
         :renderer: rst

   .. py:method:: has_object(path: aiida.repository.repository.FilePath) -> bool
      :canonical: aiida.repository.repository.Repository.has_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.has_object
         :renderer: rst

   .. py:method:: open(path: aiida.repository.repository.FilePath) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.repository.Repository.open

      .. autodoc2-docstring:: aiida.repository.repository.Repository.open
         :renderer: rst

   .. py:method:: get_object_content(path: aiida.repository.repository.FilePath) -> bytes
      :canonical: aiida.repository.repository.Repository.get_object_content

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_object_content
         :renderer: rst

   .. py:method:: delete_object(path: aiida.repository.repository.FilePath, hard_delete: bool = False) -> None
      :canonical: aiida.repository.repository.Repository.delete_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.delete_object
         :renderer: rst

   .. py:method:: erase() -> None
      :canonical: aiida.repository.repository.Repository.erase

      .. autodoc2-docstring:: aiida.repository.repository.Repository.erase
         :renderer: rst

   .. py:method:: clone(source: aiida.repository.repository.Repository) -> None
      :canonical: aiida.repository.repository.Repository.clone

      .. autodoc2-docstring:: aiida.repository.repository.Repository.clone
         :renderer: rst

   .. py:method:: walk(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.Iterable[typing.Tuple[pathlib.PurePosixPath, typing.List[str], typing.List[str]]]
      :canonical: aiida.repository.repository.Repository.walk

      .. autodoc2-docstring:: aiida.repository.repository.Repository.walk
         :renderer: rst

   .. py:method:: copy_tree(target: typing.Union[str, pathlib.Path], path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.copy_tree

      .. autodoc2-docstring:: aiida.repository.repository.Repository.copy_tree
         :renderer: rst

   .. py:method:: initialise(**kwargs: typing.Any) -> None
      :canonical: aiida.repository.repository.Repository.initialise

      .. autodoc2-docstring:: aiida.repository.repository.Repository.initialise
         :renderer: rst

   .. py:method:: delete() -> None
      :canonical: aiida.repository.repository.Repository.delete

      .. autodoc2-docstring:: aiida.repository.repository.Repository.delete
         :renderer: rst

.. py:class:: SandboxRepositoryBackend(filepath: str | None = None)
   :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__init__
      :renderer: rst

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__str__

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__str__
         :renderer: rst

   .. py:method:: __del__()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__del__

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__del__
         :renderer: rst

   .. py:property:: uuid
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.uuid
      :type: str | None

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.uuid
         :renderer: rst

   .. py:property:: key_format
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.key_format
      :type: str | None

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.key_format
         :renderer: rst

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.initialise

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.initialise
         :renderer: rst

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.is_initialised
         :renderer: rst

   .. py:property:: sandbox
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.sandbox

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.sandbox
         :renderer: rst

   .. py:method:: erase()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.erase

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.erase
         :renderer: rst

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend._put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend._put_object_from_filelike
         :renderer: rst

   .. py:method:: has_objects(keys: list[str]) -> list[bool]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.has_objects

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.has_objects
         :renderer: rst

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.open

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.open
         :renderer: rst

   .. py:method:: iter_object_streams(keys: list[str]) -> typing.Iterator[tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.iter_object_streams

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.iter_object_streams
         :renderer: rst

   .. py:method:: delete_objects(keys: list[str]) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.delete_objects

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.delete_objects
         :renderer: rst

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.list_objects

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.list_objects
         :renderer: rst

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.maintain
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.maintain
         :renderer: rst

   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.get_info
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.get_info
         :renderer: rst
