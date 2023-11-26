:py:mod:`aiida.repository`
==========================

.. py:module:: aiida.repository

.. autodoc2-docstring:: aiida.repository
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
          :summary:
   * - :py:obj:`DiskObjectStoreRepositoryBackend <aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend>`
     - .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend
          :summary:
   * - :py:obj:`File <aiida.repository.common.File>`
     - .. autodoc2-docstring:: aiida.repository.common.File
          :summary:
   * - :py:obj:`FileType <aiida.repository.common.FileType>`
     - .. autodoc2-docstring:: aiida.repository.common.FileType
          :summary:
   * - :py:obj:`Repository <aiida.repository.repository.Repository>`
     - .. autodoc2-docstring:: aiida.repository.repository.Repository
          :summary:
   * - :py:obj:`SandboxRepositoryBackend <aiida.repository.backend.sandbox.SandboxRepositoryBackend>`
     - .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend
          :summary:

API
~~~

.. py:class:: AbstractRepositoryBackend
   :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend

   .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend

   .. py:property:: uuid
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.uuid
      :abstractmethod:
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.uuid

   .. py:property:: key_format
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.key_format
      :abstractmethod:
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.key_format

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.initialise
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.initialise

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_initialised
      :abstractmethod:
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_initialised

   .. py:method:: erase() -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.erase
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.erase

   .. py:method:: is_readable_byte_stream(handle) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_readable_byte_stream
      :staticmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.is_readable_byte_stream

   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_filelike

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend._put_object_from_filelike
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend._put_object_from_filelike

   .. py:method:: put_object_from_file(filepath: typing.Union[str, pathlib.Path]) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_file

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.put_object_from_file

   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_objects

   .. py:method:: has_object(key: str) -> bool
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_object

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.has_object

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.list_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.list_objects

   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_info
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_info

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.maintain
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.maintain

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.open

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.open

   .. py:method:: get_object_content(key: str) -> bytes
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_content

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_content

   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.iter_object_streams
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.iter_object_streams

   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_hash

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.get_object_hash

   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_objects
      :abstractmethod:

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_objects

   .. py:method:: delete_object(key: str) -> None
      :canonical: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_object

      .. autodoc2-docstring:: aiida.repository.backend.abstract.AbstractRepositoryBackend.delete_object

.. py:class:: DiskObjectStoreRepositoryBackend(container: disk_objectstore.Container)
   :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__init__

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__str__

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.__str__

   .. py:property:: uuid
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.uuid
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.uuid

   .. py:property:: key_format
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.key_format
      :type: typing.Optional[str]

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.initialise

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.initialise

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.is_initialised

   .. py:method:: erase()
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.erase

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.erase

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend._put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend._put_object_from_filelike

   .. py:method:: has_objects(keys: typing.List[str]) -> typing.List[bool]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.has_objects

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.open

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.open

   .. py:method:: iter_object_streams(keys: typing.List[str]) -> typing.Iterator[typing.Tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.iter_object_streams

   .. py:method:: delete_objects(keys: typing.List[str]) -> None
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.delete_objects

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.list_objects

   .. py:method:: get_object_hash(key: str) -> str
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_object_hash

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_object_hash

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, pack_loose: bool = None, do_repack: bool = None, clean_storage: bool = None, do_vacuum: bool = None) -> dict
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.maintain

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.maintain

   .. py:method:: get_info(detailed=False) -> typing.Dict[str, typing.Union[int, str, typing.Dict[str, int], typing.Dict[str, float]]]
      :canonical: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_info

      .. autodoc2-docstring:: aiida.repository.backend.disk_object_store.DiskObjectStoreRepositoryBackend.get_info

.. py:class:: File(name: str = '', file_type: aiida.repository.common.FileType = FileType.DIRECTORY, key: typing.Union[str, None] = None, objects: typing.Optional[typing.Dict[str, aiida.repository.common.File]] = None)
   :canonical: aiida.repository.common.File

   .. autodoc2-docstring:: aiida.repository.common.File

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.common.File.__init__

   .. py:method:: from_serialized(serialized: dict, name='') -> aiida.repository.common.File
      :canonical: aiida.repository.common.File.from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.common.File.from_serialized

   .. py:method:: serialize() -> dict
      :canonical: aiida.repository.common.File.serialize

      .. autodoc2-docstring:: aiida.repository.common.File.serialize

   .. py:property:: name
      :canonical: aiida.repository.common.File.name
      :type: str

      .. autodoc2-docstring:: aiida.repository.common.File.name

   .. py:property:: file_type
      :canonical: aiida.repository.common.File.file_type
      :type: aiida.repository.common.FileType

      .. autodoc2-docstring:: aiida.repository.common.File.file_type

   .. py:method:: is_file() -> bool
      :canonical: aiida.repository.common.File.is_file

      .. autodoc2-docstring:: aiida.repository.common.File.is_file

   .. py:method:: is_dir() -> bool
      :canonical: aiida.repository.common.File.is_dir

      .. autodoc2-docstring:: aiida.repository.common.File.is_dir

   .. py:property:: key
      :canonical: aiida.repository.common.File.key
      :type: typing.Union[str, None]

      .. autodoc2-docstring:: aiida.repository.common.File.key

   .. py:property:: objects
      :canonical: aiida.repository.common.File.objects
      :type: typing.Dict[str, aiida.repository.common.File]

      .. autodoc2-docstring:: aiida.repository.common.File.objects

   .. py:method:: __eq__(other) -> bool
      :canonical: aiida.repository.common.File.__eq__

      .. autodoc2-docstring:: aiida.repository.common.File.__eq__

   .. py:method:: __repr__()
      :canonical: aiida.repository.common.File.__repr__

.. py:class:: FileType(*args, **kwds)
   :canonical: aiida.repository.common.FileType

   Bases: :py:obj:`enum.Enum`

   .. autodoc2-docstring:: aiida.repository.common.FileType

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.common.FileType.__init__

   .. py:attribute:: DIRECTORY
      :canonical: aiida.repository.common.FileType.DIRECTORY
      :value: 0

      .. autodoc2-docstring:: aiida.repository.common.FileType.DIRECTORY

   .. py:attribute:: FILE
      :canonical: aiida.repository.common.FileType.FILE
      :value: 1

      .. autodoc2-docstring:: aiida.repository.common.FileType.FILE

.. py:class:: Repository(backend: typing.Optional[aiida.repository.backend.AbstractRepositoryBackend] = None)
   :canonical: aiida.repository.repository.Repository

   .. autodoc2-docstring:: aiida.repository.repository.Repository

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.repository.Repository.__init__

   .. py:attribute:: _file_cls
      :canonical: aiida.repository.repository.Repository._file_cls
      :value: None

      .. autodoc2-docstring:: aiida.repository.repository.Repository._file_cls

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.repository.Repository.__str__

      .. autodoc2-docstring:: aiida.repository.repository.Repository.__str__

   .. py:property:: uuid
      :canonical: aiida.repository.repository.Repository.uuid
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.repository.repository.Repository.uuid

   .. py:property:: is_initialised
      :canonical: aiida.repository.repository.Repository.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.repository.Repository.is_initialised

   .. py:method:: from_serialized(backend: aiida.repository.backend.AbstractRepositoryBackend, serialized: typing.Dict[str, typing.Any]) -> aiida.repository.repository.Repository
      :canonical: aiida.repository.repository.Repository.from_serialized
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository.from_serialized

   .. py:method:: reset() -> None
      :canonical: aiida.repository.repository.Repository.reset

      .. autodoc2-docstring:: aiida.repository.repository.Repository.reset

   .. py:method:: serialize() -> typing.Dict[str, typing.Any]
      :canonical: aiida.repository.repository.Repository.serialize

      .. autodoc2-docstring:: aiida.repository.repository.Repository.serialize

   .. py:method:: flatten(serialized=Optional[Dict[str, Any]], delimiter: str = '/') -> typing.Dict[str, typing.Optional[str]]
      :canonical: aiida.repository.repository.Repository.flatten
      :classmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository.flatten

   .. py:method:: hash() -> str
      :canonical: aiida.repository.repository.Repository.hash

      .. autodoc2-docstring:: aiida.repository.repository.Repository.hash

   .. py:method:: _pre_process_path(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> pathlib.PurePosixPath
      :canonical: aiida.repository.repository.Repository._pre_process_path
      :staticmethod:

      .. autodoc2-docstring:: aiida.repository.repository.Repository._pre_process_path

   .. py:property:: backend
      :canonical: aiida.repository.repository.Repository.backend
      :type: aiida.repository.backend.AbstractRepositoryBackend

      .. autodoc2-docstring:: aiida.repository.repository.Repository.backend

   .. py:method:: set_backend(backend: aiida.repository.backend.AbstractRepositoryBackend) -> None
      :canonical: aiida.repository.repository.Repository.set_backend

      .. autodoc2-docstring:: aiida.repository.repository.Repository.set_backend

   .. py:method:: _insert_file(path: pathlib.PurePosixPath, key: str) -> None
      :canonical: aiida.repository.repository.Repository._insert_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository._insert_file

   .. py:method:: create_directory(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.create_directory

      .. autodoc2-docstring:: aiida.repository.repository.Repository.create_directory

   .. py:method:: get_file_keys() -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.get_file_keys

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_file_keys

   .. py:method:: get_object(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_object

   .. py:method:: get_directory(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_directory

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_directory

   .. py:method:: get_file(path: aiida.repository.repository.FilePath) -> aiida.repository.common.File
      :canonical: aiida.repository.repository.Repository.get_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_file

   .. py:method:: list_objects(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[aiida.repository.common.File]
      :canonical: aiida.repository.repository.Repository.list_objects

      .. autodoc2-docstring:: aiida.repository.repository.Repository.list_objects

   .. py:method:: list_object_names(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.List[str]
      :canonical: aiida.repository.repository.Repository.list_object_names

      .. autodoc2-docstring:: aiida.repository.repository.Repository.list_object_names

   .. py:method:: put_object_from_filelike(handle: typing.BinaryIO, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_filelike

   .. py:method:: put_object_from_file(filepath: aiida.repository.repository.FilePath, path: aiida.repository.repository.FilePath) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_file

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_file

   .. py:method:: put_object_from_tree(filepath: aiida.repository.repository.FilePath, path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.put_object_from_tree

      .. autodoc2-docstring:: aiida.repository.repository.Repository.put_object_from_tree

   .. py:method:: is_empty() -> bool
      :canonical: aiida.repository.repository.Repository.is_empty

      .. autodoc2-docstring:: aiida.repository.repository.Repository.is_empty

   .. py:method:: has_object(path: aiida.repository.repository.FilePath) -> bool
      :canonical: aiida.repository.repository.Repository.has_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.has_object

   .. py:method:: open(path: aiida.repository.repository.FilePath) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.repository.Repository.open

      .. autodoc2-docstring:: aiida.repository.repository.Repository.open

   .. py:method:: get_object_content(path: aiida.repository.repository.FilePath) -> bytes
      :canonical: aiida.repository.repository.Repository.get_object_content

      .. autodoc2-docstring:: aiida.repository.repository.Repository.get_object_content

   .. py:method:: delete_object(path: aiida.repository.repository.FilePath, hard_delete: bool = False) -> None
      :canonical: aiida.repository.repository.Repository.delete_object

      .. autodoc2-docstring:: aiida.repository.repository.Repository.delete_object

   .. py:method:: erase() -> None
      :canonical: aiida.repository.repository.Repository.erase

      .. autodoc2-docstring:: aiida.repository.repository.Repository.erase

   .. py:method:: clone(source: aiida.repository.repository.Repository) -> None
      :canonical: aiida.repository.repository.Repository.clone

      .. autodoc2-docstring:: aiida.repository.repository.Repository.clone

   .. py:method:: walk(path: typing.Optional[aiida.repository.repository.FilePath] = None) -> typing.Iterable[typing.Tuple[pathlib.PurePosixPath, typing.List[str], typing.List[str]]]
      :canonical: aiida.repository.repository.Repository.walk

      .. autodoc2-docstring:: aiida.repository.repository.Repository.walk

   .. py:method:: copy_tree(target: typing.Union[str, pathlib.Path], path: typing.Optional[aiida.repository.repository.FilePath] = None) -> None
      :canonical: aiida.repository.repository.Repository.copy_tree

      .. autodoc2-docstring:: aiida.repository.repository.Repository.copy_tree

   .. py:method:: initialise(**kwargs: typing.Any) -> None
      :canonical: aiida.repository.repository.Repository.initialise

      .. autodoc2-docstring:: aiida.repository.repository.Repository.initialise

   .. py:method:: delete() -> None
      :canonical: aiida.repository.repository.Repository.delete

      .. autodoc2-docstring:: aiida.repository.repository.Repository.delete

.. py:class:: SandboxRepositoryBackend(filepath: str | None = None)
   :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend

   Bases: :py:obj:`aiida.repository.backend.abstract.AbstractRepositoryBackend`

   .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__init__

   .. py:method:: __str__() -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__str__

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__str__

   .. py:method:: __del__()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__del__

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.__del__

   .. py:property:: uuid
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.uuid
      :type: str | None

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.uuid

   .. py:property:: key_format
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.key_format
      :type: str | None

   .. py:method:: initialise(**kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.initialise

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.initialise

   .. py:property:: is_initialised
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.is_initialised
      :type: bool

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.is_initialised

   .. py:property:: sandbox
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.sandbox

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.sandbox

   .. py:method:: erase()
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.erase

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend.erase

   .. py:method:: _put_object_from_filelike(handle: typing.BinaryIO) -> str
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend._put_object_from_filelike

      .. autodoc2-docstring:: aiida.repository.backend.sandbox.SandboxRepositoryBackend._put_object_from_filelike

   .. py:method:: has_objects(keys: list[str]) -> list[bool]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.has_objects

   .. py:method:: open(key: str) -> typing.Iterator[typing.BinaryIO]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.open

   .. py:method:: iter_object_streams(keys: list[str]) -> typing.Iterator[tuple[str, typing.BinaryIO]]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.iter_object_streams

   .. py:method:: delete_objects(keys: list[str]) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.delete_objects

   .. py:method:: list_objects() -> typing.Iterable[str]
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.list_objects

   .. py:method:: maintain(dry_run: bool = False, live: bool = True, **kwargs) -> None
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.maintain
      :abstractmethod:

   .. py:method:: get_info(detailed: bool = False, **kwargs) -> dict
      :canonical: aiida.repository.backend.sandbox.SandboxRepositoryBackend.get_info
      :abstractmethod:
