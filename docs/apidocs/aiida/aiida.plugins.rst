:py:mod:`aiida.plugins`
=======================

.. py:module:: aiida.plugins


Description
-----------

Classes and functions to load and interact with plugin classes accessible through defined entry points.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PluginVersionProvider <aiida.plugins.utils.PluginVersionProvider>`
     - Utility class that determines version information about a given plugin resource.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BaseFactory <aiida.plugins.factories.BaseFactory>`
     - Return the plugin class registered under a given entry point group and name.
   * - :py:obj:`CalcJobImporterFactory <aiida.plugins.factories.CalcJobImporterFactory>`
     - Return the plugin registered under the given entry point.
   * - :py:obj:`CalculationFactory <aiida.plugins.factories.CalculationFactory>`
     - Return the `CalcJob` sub class registered under the given entry point.
   * - :py:obj:`DataFactory <aiida.plugins.factories.DataFactory>`
     - Return the `Data` sub class registered under the given entry point.
   * - :py:obj:`DbImporterFactory <aiida.plugins.factories.DbImporterFactory>`
     - Return the `DbImporter` sub class registered under the given entry point.
   * - :py:obj:`GroupFactory <aiida.plugins.factories.GroupFactory>`
     - Return the `Group` sub class registered under the given entry point.
   * - :py:obj:`OrbitalFactory <aiida.plugins.factories.OrbitalFactory>`
     - Return the `Orbital` sub class registered under the given entry point.
   * - :py:obj:`ParserFactory <aiida.plugins.factories.ParserFactory>`
     - Return the `Parser` sub class registered under the given entry point.
   * - :py:obj:`SchedulerFactory <aiida.plugins.factories.SchedulerFactory>`
     - Return the `Scheduler` sub class registered under the given entry point.
   * - :py:obj:`StorageFactory <aiida.plugins.factories.StorageFactory>`
     - Return the ``StorageBackend`` sub class registered under the given entry point.
   * - :py:obj:`TransportFactory <aiida.plugins.factories.TransportFactory>`
     - Return the `Transport` sub class registered under the given entry point.
   * - :py:obj:`WorkflowFactory <aiida.plugins.factories.WorkflowFactory>`
     - Return the `WorkChain` sub class registered under the given entry point.
   * - :py:obj:`get_entry_points <aiida.plugins.entry_point.get_entry_points>`
     - Return a list of all the entry points within a specific group
   * - :py:obj:`load_entry_point <aiida.plugins.entry_point.load_entry_point>`
     - Load the class registered under the entry point for a given name and group
   * - :py:obj:`load_entry_point_from_string <aiida.plugins.entry_point.load_entry_point_from_string>`
     - Load the class registered for a given entry point string that determines group and name
   * - :py:obj:`parse_entry_point <aiida.plugins.entry_point.parse_entry_point>`
     - Return an entry point, given its group and spec (as formatted in the setup)

API
~~~

.. py:function:: BaseFactory(group: str, name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Any]
   :canonical: aiida.plugins.factories.BaseFactory

   Return the plugin class registered under a given entry point group and name.

   :param group: entry point group
   :param name: entry point name
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: the plugin class
   :raises aiida.common.MissingEntryPointError: entry point was not registered
   :raises aiida.common.MultipleEntryPointError: entry point could not be uniquely resolved
   :raises aiida.common.LoadingEntryPointError: entry point could not be loaded


.. py:function:: CalcJobImporterFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.CalcJobImporter]]
   :canonical: aiida.plugins.factories.CalcJobImporterFactory

   Return the plugin registered under the given entry point.

   :param entry_point_name: the entry point name.
   :return: the loaded :class:`~aiida.engine.processes.calcjobs.importer.CalcJobImporter` plugin.
   :raises ``aiida.common.InvalidEntryPointTypeError``: if the type of the loaded entry point is invalid.


.. py:function:: CalculationFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.CalcJob], typing.Callable]
   :canonical: aiida.plugins.factories.CalculationFactory

   Return the `CalcJob` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.engine.processes.calcjobs.calcjob.CalcJob`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: DataFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.Data]]
   :canonical: aiida.plugins.factories.DataFactory

   Return the `Data` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.orm.nodes.data.data.Data`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: DbImporterFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.tools.dbimporters.DbImporter]]
   :canonical: aiida.plugins.factories.DbImporterFactory

   Return the `DbImporter` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.tools.dbimporters.baseclasses.DbImporter`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: GroupFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.Group]]
   :canonical: aiida.plugins.factories.GroupFactory

   Return the `Group` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.orm.groups.Group`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: OrbitalFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.tools.data.orbital.Orbital]]
   :canonical: aiida.plugins.factories.OrbitalFactory

   Return the `Orbital` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.tools.data.orbital.orbital.Orbital`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: ParserFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.parsers.Parser]]
   :canonical: aiida.plugins.factories.ParserFactory

   Return the `Parser` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.parsers.parser.Parser`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:class:: PluginVersionProvider()
   :canonical: aiida.plugins.utils.PluginVersionProvider

   Utility class that determines version information about a given plugin resource.

   .. py:method:: __init__()
      :canonical: aiida.plugins.utils.PluginVersionProvider.__init__

   .. py:property:: logger
      :canonical: aiida.plugins.utils.PluginVersionProvider.logger
      :type: logging.Logger

   .. py:method:: get_version_info(plugin: str | type) -> dict[typing.Any, dict[typing.Any, typing.Any]]
      :canonical: aiida.plugins.utils.PluginVersionProvider.get_version_info

      Get the version information for a given plugin.

      .. note::

          This container will keep a cache, so if this method was already called for the given ``plugin`` before for
          this instance, the result computed at the last invocation will be returned.

      :param plugin: A class, function, or an entry point string. If the type is string, it will be assumed to be an
          entry point string and the class will attempt to load it first. It should be a full entry point string,
          including the entry point group.
      :return: Dictionary with the `version.core` and optionally `version.plugin` if it could be determined.
      :raises EntryPointError: If ``plugin`` is a string but could not be loaded as a valid entry point.
      :raises TypeError: If ``plugin`` (or the resource pointed to it in the case of an entry point) is not a class
          or a function.


.. py:function:: SchedulerFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.schedulers.Scheduler]]
   :canonical: aiida.plugins.factories.SchedulerFactory

   Return the `Scheduler` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.schedulers.scheduler.Scheduler`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: StorageFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.implementation.StorageBackend]]
   :canonical: aiida.plugins.factories.StorageFactory

   Return the ``StorageBackend`` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.orm.implementation.storage_backend.StorageBackend`.
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: TransportFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.transports.Transport]]
   :canonical: aiida.plugins.factories.TransportFactory

   Return the `Transport` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: WorkflowFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.WorkChain], typing.Callable]
   :canonical: aiida.plugins.factories.WorkflowFactory

   Return the `WorkChain` sub class registered under the given entry point.

   :param entry_point_name: the entry point name.
   :param load: if True, load the matched entry point and return the loaded resource instead of the entry point itself.
   :return: sub class of :py:class:`~aiida.engine.processes.workchains.workchain.WorkChain` or a `workfunction`
   :raises aiida.common.InvalidEntryPointTypeError: if the type of the loaded entry point is invalid.


.. py:function:: get_entry_points(group: str) -> importlib_metadata.EntryPoints
   :canonical: aiida.plugins.entry_point.get_entry_points

   Return a list of all the entry points within a specific group

   :param group: the entry point group
   :return: a list of entry points


.. py:function:: load_entry_point(group: str, name: str) -> typing.Any
   :canonical: aiida.plugins.entry_point.load_entry_point

   Load the class registered under the entry point for a given name and group

   :param group: the entry point group
   :param name: the name of the entry point
   :return: class registered at the given entry point
   :raises TypeError: if the entry_point_string is not a string type
   :raises ValueError: if the entry_point_string cannot be split into two parts on the entry point string separator
   :raises aiida.common.MissingEntryPointError: entry point was not registered
   :raises aiida.common.MultipleEntryPointError: entry point could not be uniquely resolved
   :raises aiida.common.LoadingEntryPointError: entry point could not be loaded


.. py:function:: load_entry_point_from_string(entry_point_string: str) -> typing.Any
   :canonical: aiida.plugins.entry_point.load_entry_point_from_string

   Load the class registered for a given entry point string that determines group and name

   :param entry_point_string: the entry point string
   :return: class registered at the given entry point
   :raises TypeError: if the entry_point_string is not a string type
   :raises ValueError: if the entry_point_string cannot be split into two parts on the entry point string separator
   :raises aiida.common.MissingEntryPointError: entry point was not registered
   :raises aiida.common.MultipleEntryPointError: entry point could not be uniquely resolved
   :raises aiida.common.LoadingEntryPointError: entry point could not be loaded


.. py:function:: parse_entry_point(group: str, spec: str) -> importlib_metadata.EntryPoint
   :canonical: aiida.plugins.entry_point.parse_entry_point

   Return an entry point, given its group and spec (as formatted in the setup)
