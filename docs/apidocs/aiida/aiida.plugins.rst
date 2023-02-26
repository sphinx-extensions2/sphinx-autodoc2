:py:mod:`aiida.plugins`
=======================

.. py:module:: aiida.plugins

.. autodoc2-docstring:: aiida.plugins
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PluginVersionProvider <aiida.plugins.utils.PluginVersionProvider>`
     - .. autodoc2-docstring:: aiida.plugins.utils.PluginVersionProvider
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BaseFactory <aiida.plugins.factories.BaseFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.BaseFactory
          :summary:
   * - :py:obj:`CalcJobImporterFactory <aiida.plugins.factories.CalcJobImporterFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.CalcJobImporterFactory
          :summary:
   * - :py:obj:`CalculationFactory <aiida.plugins.factories.CalculationFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.CalculationFactory
          :summary:
   * - :py:obj:`DataFactory <aiida.plugins.factories.DataFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.DataFactory
          :summary:
   * - :py:obj:`DbImporterFactory <aiida.plugins.factories.DbImporterFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.DbImporterFactory
          :summary:
   * - :py:obj:`GroupFactory <aiida.plugins.factories.GroupFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.GroupFactory
          :summary:
   * - :py:obj:`OrbitalFactory <aiida.plugins.factories.OrbitalFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.OrbitalFactory
          :summary:
   * - :py:obj:`ParserFactory <aiida.plugins.factories.ParserFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.ParserFactory
          :summary:
   * - :py:obj:`SchedulerFactory <aiida.plugins.factories.SchedulerFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.SchedulerFactory
          :summary:
   * - :py:obj:`StorageFactory <aiida.plugins.factories.StorageFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.StorageFactory
          :summary:
   * - :py:obj:`TransportFactory <aiida.plugins.factories.TransportFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.TransportFactory
          :summary:
   * - :py:obj:`WorkflowFactory <aiida.plugins.factories.WorkflowFactory>`
     - .. autodoc2-docstring:: aiida.plugins.factories.WorkflowFactory
          :summary:
   * - :py:obj:`get_entry_points <aiida.plugins.entry_point.get_entry_points>`
     - .. autodoc2-docstring:: aiida.plugins.entry_point.get_entry_points
          :summary:
   * - :py:obj:`load_entry_point <aiida.plugins.entry_point.load_entry_point>`
     - .. autodoc2-docstring:: aiida.plugins.entry_point.load_entry_point
          :summary:
   * - :py:obj:`load_entry_point_from_string <aiida.plugins.entry_point.load_entry_point_from_string>`
     - .. autodoc2-docstring:: aiida.plugins.entry_point.load_entry_point_from_string
          :summary:
   * - :py:obj:`parse_entry_point <aiida.plugins.entry_point.parse_entry_point>`
     - .. autodoc2-docstring:: aiida.plugins.entry_point.parse_entry_point
          :summary:

API
~~~

.. py:function:: BaseFactory(group: str, name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Any]
   :canonical: aiida.plugins.factories.BaseFactory

   .. autodoc2-docstring:: aiida.plugins.factories.BaseFactory

.. py:function:: CalcJobImporterFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.CalcJobImporter]]
   :canonical: aiida.plugins.factories.CalcJobImporterFactory

   .. autodoc2-docstring:: aiida.plugins.factories.CalcJobImporterFactory

.. py:function:: CalculationFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.CalcJob], typing.Callable]
   :canonical: aiida.plugins.factories.CalculationFactory

   .. autodoc2-docstring:: aiida.plugins.factories.CalculationFactory

.. py:function:: DataFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.Data]]
   :canonical: aiida.plugins.factories.DataFactory

   .. autodoc2-docstring:: aiida.plugins.factories.DataFactory

.. py:function:: DbImporterFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.tools.dbimporters.DbImporter]]
   :canonical: aiida.plugins.factories.DbImporterFactory

   .. autodoc2-docstring:: aiida.plugins.factories.DbImporterFactory

.. py:function:: GroupFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.Group]]
   :canonical: aiida.plugins.factories.GroupFactory

   .. autodoc2-docstring:: aiida.plugins.factories.GroupFactory

.. py:function:: OrbitalFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.tools.data.orbital.Orbital]]
   :canonical: aiida.plugins.factories.OrbitalFactory

   .. autodoc2-docstring:: aiida.plugins.factories.OrbitalFactory

.. py:function:: ParserFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.parsers.Parser]]
   :canonical: aiida.plugins.factories.ParserFactory

   .. autodoc2-docstring:: aiida.plugins.factories.ParserFactory

.. py:class:: PluginVersionProvider()
   :canonical: aiida.plugins.utils.PluginVersionProvider

   .. autodoc2-docstring:: aiida.plugins.utils.PluginVersionProvider

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.plugins.utils.PluginVersionProvider.__init__

   .. py:property:: logger
      :canonical: aiida.plugins.utils.PluginVersionProvider.logger
      :type: logging.Logger

      .. autodoc2-docstring:: aiida.plugins.utils.PluginVersionProvider.logger

   .. py:method:: get_version_info(plugin: str | type) -> dict[typing.Any, dict[typing.Any, typing.Any]]
      :canonical: aiida.plugins.utils.PluginVersionProvider.get_version_info

      .. autodoc2-docstring:: aiida.plugins.utils.PluginVersionProvider.get_version_info

.. py:function:: SchedulerFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.schedulers.Scheduler]]
   :canonical: aiida.plugins.factories.SchedulerFactory

   .. autodoc2-docstring:: aiida.plugins.factories.SchedulerFactory

.. py:function:: StorageFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.orm.implementation.StorageBackend]]
   :canonical: aiida.plugins.factories.StorageFactory

   .. autodoc2-docstring:: aiida.plugins.factories.StorageFactory

.. py:function:: TransportFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.transports.Transport]]
   :canonical: aiida.plugins.factories.TransportFactory

   .. autodoc2-docstring:: aiida.plugins.factories.TransportFactory

.. py:function:: WorkflowFactory(entry_point_name: str, load: bool = True) -> typing.Union[importlib_metadata.EntryPoint, typing.Type[aiida.engine.WorkChain], typing.Callable]
   :canonical: aiida.plugins.factories.WorkflowFactory

   .. autodoc2-docstring:: aiida.plugins.factories.WorkflowFactory

.. py:function:: get_entry_points(group: str) -> importlib_metadata.EntryPoints
   :canonical: aiida.plugins.entry_point.get_entry_points

   .. autodoc2-docstring:: aiida.plugins.entry_point.get_entry_points

.. py:function:: load_entry_point(group: str, name: str) -> typing.Any
   :canonical: aiida.plugins.entry_point.load_entry_point

   .. autodoc2-docstring:: aiida.plugins.entry_point.load_entry_point

.. py:function:: load_entry_point_from_string(entry_point_string: str) -> typing.Any
   :canonical: aiida.plugins.entry_point.load_entry_point_from_string

   .. autodoc2-docstring:: aiida.plugins.entry_point.load_entry_point_from_string

.. py:function:: parse_entry_point(group: str, spec: str) -> importlib_metadata.EntryPoint
   :canonical: aiida.plugins.entry_point.parse_entry_point

   .. autodoc2-docstring:: aiida.plugins.entry_point.parse_entry_point
