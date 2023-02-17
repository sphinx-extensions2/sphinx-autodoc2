:py:mod:`autodoc2.config`
=========================

.. py:module:: autodoc2.config


Description
-----------

The configuration for the extension.

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RenderConfig <autodoc2.config.RenderConfig>`
     - The configuration for rendering.
   * - :py:obj:`PackageConfig <autodoc2.config.PackageConfig>`
     - A package-level config item.
   * - :py:obj:`Config <autodoc2.config.Config>`
     - The configuration for autoapi.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_coerce_packages <autodoc2.config._coerce_packages>`
     - Coerce the packages config option to a set.
   * - :py:obj:`_validate_string_list <autodoc2.config._validate_string_list>`
     - Validate that an item is a string.
   * - :py:obj:`_validate_hidden_objects <autodoc2.config._validate_hidden_objects>`
     - Validate that the hidden objects config option is a set.
   * - :py:obj:`_validate_regex_list <autodoc2.config._validate_regex_list>`
     - Validate that an item is a list of regexes.
   * - :py:obj:`_load_renderer <autodoc2.config._load_renderer>`
     - Load a renderer class.
   * - :py:obj:`_load_regex_renderers <autodoc2.config._load_regex_renderers>`
     - Load a list of (regex, renderer).

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CONFIG_PREFIX <autodoc2.config.CONFIG_PREFIX>`
     - 

API
~~~

.. py:exception:: ValidationError()
   :canonical: autodoc2.config.ValidationError

   Bases: :py:obj:`Exception`

   An error validating a config value.

.. py:data:: CONFIG_PREFIX
   :canonical: autodoc2.config.CONFIG_PREFIX
   :value: 'autodoc2_'

.. py:class:: RenderConfig
   :canonical: autodoc2.config.RenderConfig

   The configuration for rendering.

   This uses the global, with package level overrides.


   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.RenderConfig.module_all_regexes
      :type: list[re.Pattern[str]]
      :value: None

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.RenderConfig.skip_module_regexes
      :type: list[re.Pattern[str]]
      :value: None

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.RenderConfig.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]]
      :value: None

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.RenderConfig.hidden_regexes
      :type: list[re.Pattern[str]]
      :value: None

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.RenderConfig.deprecated_module_regexes
      :type: list[re.Pattern[str]]
      :value: None

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.RenderConfig.module_summary
      :type: bool
      :value: None

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.RenderConfig.class_inheritance
      :type: bool
      :value: None

   .. py:attribute:: annotations
      :canonical: autodoc2.config.RenderConfig.annotations
      :type: bool
      :value: None

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.RenderConfig.sort_names
      :type: bool
      :value: None

.. py:class:: PackageConfig
   :canonical: autodoc2.config.PackageConfig

   A package-level config item.

   .. py:attribute:: path
      :canonical: autodoc2.config.PackageConfig.path
      :type: str
      :value: None

   .. py:attribute:: from_git_clone
      :canonical: autodoc2.config.PackageConfig.from_git_clone
      :type: tuple[str, str] | None
      :value: None

   .. py:attribute:: module
      :canonical: autodoc2.config.PackageConfig.module
      :type: str | None
      :value: None

   .. py:attribute:: exclude_dirs
      :canonical: autodoc2.config.PackageConfig.exclude_dirs
      :type: list[str] | None
      :value: None

   .. py:attribute:: exclude_files
      :canonical: autodoc2.config.PackageConfig.exclude_files
      :type: list[str] | None
      :value: None

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.PackageConfig.module_all_regexes
      :type: list[re.Pattern[str]] | None
      :value: None

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.PackageConfig.skip_module_regexes
      :type: list[re.Pattern[str]] | None
      :value: None

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.PackageConfig.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]] | None
      :value: None

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.PackageConfig.hidden_regexes
      :type: list[re.Pattern[str]] | None
      :value: None

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.PackageConfig.deprecated_module_regexes
      :type: list[re.Pattern[str]] | None
      :value: None

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.PackageConfig.module_summary
      :type: bool | None
      :value: None

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.PackageConfig.class_inheritance
      :type: bool | None
      :value: None

   .. py:attribute:: annotations
      :canonical: autodoc2.config.PackageConfig.annotations
      :type: bool | None
      :value: None

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.PackageConfig.sort_names
      :type: bool | None
      :value: None

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.PackageConfig.as_triple

      Yield triples of (name, value, field).

.. py:function:: _coerce_packages(name: str, item: typing.Any) -> list[autodoc2.config.PackageConfig]
   :canonical: autodoc2.config._coerce_packages

   Coerce the packages config option to a set.

.. py:function:: _validate_string_list(name: str, item: typing.Any) -> list[str]
   :canonical: autodoc2.config._validate_string_list

   Validate that an item is a string.

.. py:function:: _validate_hidden_objects(name: str, item: typing.Any) -> set[str]
   :canonical: autodoc2.config._validate_hidden_objects

   Validate that the hidden objects config option is a set.

.. py:function:: _validate_regex_list(name: str, item: typing.Any) -> list[typing.Pattern[str]]
   :canonical: autodoc2.config._validate_regex_list

   Validate that an item is a list of regexes.

.. py:function:: _load_renderer(name: str, item: typing.Any) -> type[autodoc2.render.base.RendererBase]
   :canonical: autodoc2.config._load_renderer

   Load a renderer class.

.. py:function:: _load_regex_renderers(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
   :canonical: autodoc2.config._load_regex_renderers

   Load a list of (regex, renderer).

.. py:class:: Config
   :canonical: autodoc2.config.Config

   The configuration for autoapi.

   .. py:attribute:: packages
      :canonical: autodoc2.config.Config.packages
      :type: list[autodoc2.config.PackageConfig]
      :value: None

   .. py:attribute:: output_dir
      :canonical: autodoc2.config.Config.output_dir
      :type: str
      :value: None

   .. py:attribute:: exclude_dirs
      :canonical: autodoc2.config.Config.exclude_dirs
      :type: list[str]
      :value: None

   .. py:attribute:: exclude_files
      :canonical: autodoc2.config.Config.exclude_files
      :type: list[str]
      :value: None

   .. py:attribute:: render_plugin
      :canonical: autodoc2.config.Config.render_plugin
      :type: type[autodoc2.render.base.RendererBase]
      :value: None

   .. py:attribute:: render_plugin_regexes
      :canonical: autodoc2.config.Config.render_plugin_regexes
      :type: list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
      :value: None

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.Config.module_all_regexes
      :type: list[typing.Pattern[str]]
      :value: None

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.Config.skip_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.Config.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]]
      :value: None

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.Config.hidden_regexes
      :type: list[typing.Pattern[str]]
      :value: None

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.Config.deprecated_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.Config.module_summary
      :type: bool
      :value: None

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.Config.class_inheritance
      :type: bool
      :value: None

   .. py:attribute:: annotations
      :canonical: autodoc2.config.Config.annotations
      :type: bool
      :value: None

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.Config.sort_names
      :type: bool
      :value: None

   .. py:attribute:: index_template
      :canonical: autodoc2.config.Config.index_template
      :type: str | None
      :value: None

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.Config.as_triple

      Yield triples of (name, value, field).

   .. py:method:: to_render_config(pkg_index: int | None) -> autodoc2.config.RenderConfig
      :canonical: autodoc2.config.Config.to_render_config

      Convert a module level render config.
