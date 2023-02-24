:py:mod:`autodoc2.config`
=========================

.. py:module:: autodoc2.config


Description
-----------

.. autodoc2-docstring:: autodoc2.config
   :renderer: rst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RenderConfig <autodoc2.config.RenderConfig>`
     - .. autodoc2-docstring:: autodoc2.config.RenderConfig
          :renderer: rst
          :summary:
   * - :py:obj:`PackageConfig <autodoc2.config.PackageConfig>`
     - .. autodoc2-docstring:: autodoc2.config.PackageConfig
          :renderer: rst
          :summary:
   * - :py:obj:`Config <autodoc2.config.Config>`
     - .. autodoc2-docstring:: autodoc2.config.Config
          :renderer: rst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_coerce_packages <autodoc2.config._coerce_packages>`
     - .. autodoc2-docstring:: autodoc2.config._coerce_packages
          :renderer: rst
          :summary:
   * - :py:obj:`_validate_string_list <autodoc2.config._validate_string_list>`
     - .. autodoc2-docstring:: autodoc2.config._validate_string_list
          :renderer: rst
          :summary:
   * - :py:obj:`_validate_replace_list <autodoc2.config._validate_replace_list>`
     - .. autodoc2-docstring:: autodoc2.config._validate_replace_list
          :renderer: rst
          :summary:
   * - :py:obj:`_validate_hidden_objects <autodoc2.config._validate_hidden_objects>`
     - .. autodoc2-docstring:: autodoc2.config._validate_hidden_objects
          :renderer: rst
          :summary:
   * - :py:obj:`_validate_regex_list <autodoc2.config._validate_regex_list>`
     - .. autodoc2-docstring:: autodoc2.config._validate_regex_list
          :renderer: rst
          :summary:
   * - :py:obj:`_load_renderer <autodoc2.config._load_renderer>`
     - .. autodoc2-docstring:: autodoc2.config._load_renderer
          :renderer: rst
          :summary:
   * - :py:obj:`_load_regex_renderers <autodoc2.config._load_regex_renderers>`
     - .. autodoc2-docstring:: autodoc2.config._load_regex_renderers
          :renderer: rst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CONFIG_PREFIX <autodoc2.config.CONFIG_PREFIX>`
     - .. autodoc2-docstring:: autodoc2.config.CONFIG_PREFIX
          :renderer: rst
          :summary:

API
~~~

.. py:exception:: ValidationError()
   :canonical: autodoc2.config.ValidationError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: autodoc2.config.ValidationError
      :renderer: rst

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.config.ValidationError.__init__
      :renderer: rst

.. py:data:: CONFIG_PREFIX
   :canonical: autodoc2.config.CONFIG_PREFIX
   :value: 'autodoc2_'

   .. autodoc2-docstring:: autodoc2.config.CONFIG_PREFIX
      :renderer: rst

.. py:class:: RenderConfig
   :canonical: autodoc2.config.RenderConfig

   .. autodoc2-docstring:: autodoc2.config.RenderConfig
      :renderer: rst

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.RenderConfig.module_all_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.module_all_regexes
         :renderer: rst

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.RenderConfig.skip_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.skip_module_regexes
         :renderer: rst

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.RenderConfig.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.hidden_objects
         :renderer: rst

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.RenderConfig.hidden_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.hidden_regexes
         :renderer: rst

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.RenderConfig.deprecated_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.deprecated_module_regexes
         :renderer: rst

   .. py:attribute:: no_index
      :canonical: autodoc2.config.RenderConfig.no_index
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.no_index
         :renderer: rst

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.RenderConfig.module_summary
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.module_summary
         :renderer: rst

   .. py:attribute:: class_docstring
      :canonical: autodoc2.config.RenderConfig.class_docstring
      :type: typing.Literal[merge, both]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.class_docstring
         :renderer: rst

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.RenderConfig.class_inheritance
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.class_inheritance
         :renderer: rst

   .. py:attribute:: annotations
      :canonical: autodoc2.config.RenderConfig.annotations
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.annotations
         :renderer: rst

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.RenderConfig.sort_names
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.sort_names
         :renderer: rst

   .. py:attribute:: replace_annotations
      :canonical: autodoc2.config.RenderConfig.replace_annotations
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.replace_annotations
         :renderer: rst

   .. py:attribute:: replace_bases
      :canonical: autodoc2.config.RenderConfig.replace_bases
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.RenderConfig.replace_bases
         :renderer: rst

.. py:class:: PackageConfig
   :canonical: autodoc2.config.PackageConfig

   .. autodoc2-docstring:: autodoc2.config.PackageConfig
      :renderer: rst

   .. py:attribute:: path
      :canonical: autodoc2.config.PackageConfig.path
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.path
         :renderer: rst

   .. py:attribute:: from_git_clone
      :canonical: autodoc2.config.PackageConfig.from_git_clone
      :type: tuple[str, str] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.from_git_clone
         :renderer: rst

   .. py:attribute:: module
      :canonical: autodoc2.config.PackageConfig.module
      :type: str | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.module
         :renderer: rst

   .. py:attribute:: exclude_dirs
      :canonical: autodoc2.config.PackageConfig.exclude_dirs
      :type: list[str] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.exclude_dirs
         :renderer: rst

   .. py:attribute:: exclude_files
      :canonical: autodoc2.config.PackageConfig.exclude_files
      :type: list[str] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.exclude_files
         :renderer: rst

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.PackageConfig.module_all_regexes
      :type: list[typing.Pattern[str]] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.module_all_regexes
         :renderer: rst

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.PackageConfig.skip_module_regexes
      :type: list[typing.Pattern[str]] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.skip_module_regexes
         :renderer: rst

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.PackageConfig.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.hidden_objects
         :renderer: rst

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.PackageConfig.hidden_regexes
      :type: list[typing.Pattern[str]] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.hidden_regexes
         :renderer: rst

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.PackageConfig.deprecated_module_regexes
      :type: list[typing.Pattern[str]] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.deprecated_module_regexes
         :renderer: rst

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.PackageConfig.module_summary
      :type: bool | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.module_summary
         :renderer: rst

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.PackageConfig.class_inheritance
      :type: bool | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.class_inheritance
         :renderer: rst

   .. py:attribute:: class_docstring
      :canonical: autodoc2.config.PackageConfig.class_docstring
      :type: typing.Literal[merge, both] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.class_docstring
         :renderer: rst

   .. py:attribute:: annotations
      :canonical: autodoc2.config.PackageConfig.annotations
      :type: bool | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.annotations
         :renderer: rst

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.PackageConfig.sort_names
      :type: bool | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.sort_names
         :renderer: rst

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.PackageConfig.as_triple

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.as_triple
         :renderer: rst

.. py:function:: _coerce_packages(name: str, item: typing.Any) -> list[autodoc2.config.PackageConfig]
   :canonical: autodoc2.config._coerce_packages

   .. autodoc2-docstring:: autodoc2.config._coerce_packages
      :renderer: rst

.. py:function:: _validate_string_list(name: str, item: typing.Any) -> list[str]
   :canonical: autodoc2.config._validate_string_list

   .. autodoc2-docstring:: autodoc2.config._validate_string_list
      :renderer: rst

.. py:function:: _validate_replace_list(name: str, item: typing.Any) -> list[typing.Tuple[str, str]]
   :canonical: autodoc2.config._validate_replace_list

   .. autodoc2-docstring:: autodoc2.config._validate_replace_list
      :renderer: rst

.. py:function:: _validate_hidden_objects(name: str, item: typing.Any) -> set[str]
   :canonical: autodoc2.config._validate_hidden_objects

   .. autodoc2-docstring:: autodoc2.config._validate_hidden_objects
      :renderer: rst

.. py:function:: _validate_regex_list(name: str, item: typing.Any) -> list[typing.Pattern[str]]
   :canonical: autodoc2.config._validate_regex_list

   .. autodoc2-docstring:: autodoc2.config._validate_regex_list
      :renderer: rst

.. py:function:: _load_renderer(name: str, item: typing.Any) -> type[autodoc2.render.base.RendererBase]
   :canonical: autodoc2.config._load_renderer

   .. autodoc2-docstring:: autodoc2.config._load_renderer
      :renderer: rst

.. py:function:: _load_regex_renderers(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
   :canonical: autodoc2.config._load_regex_renderers

   .. autodoc2-docstring:: autodoc2.config._load_regex_renderers
      :renderer: rst

.. py:class:: Config
   :canonical: autodoc2.config.Config

   .. autodoc2-docstring:: autodoc2.config.Config
      :renderer: rst

   .. py:attribute:: packages
      :canonical: autodoc2.config.Config.packages
      :type: list[autodoc2.config.PackageConfig]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.packages
         :renderer: rst

   .. py:attribute:: output_dir
      :canonical: autodoc2.config.Config.output_dir
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.output_dir
         :renderer: rst

   .. py:attribute:: exclude_dirs
      :canonical: autodoc2.config.Config.exclude_dirs
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.exclude_dirs
         :renderer: rst

   .. py:attribute:: exclude_files
      :canonical: autodoc2.config.Config.exclude_files
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.exclude_files
         :renderer: rst

   .. py:attribute:: render_plugin
      :canonical: autodoc2.config.Config.render_plugin
      :type: type[autodoc2.render.base.RendererBase]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.render_plugin
         :renderer: rst

   .. py:attribute:: render_plugin_regexes
      :canonical: autodoc2.config.Config.render_plugin_regexes
      :type: list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.render_plugin_regexes
         :renderer: rst

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.Config.module_all_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.module_all_regexes
         :renderer: rst

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.Config.skip_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.skip_module_regexes
         :renderer: rst

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.Config.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.hidden_objects
         :renderer: rst

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.Config.hidden_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.hidden_regexes
         :renderer: rst

   .. py:attribute:: no_index
      :canonical: autodoc2.config.Config.no_index
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.no_index
         :renderer: rst

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.Config.deprecated_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.deprecated_module_regexes
         :renderer: rst

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.Config.module_summary
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.module_summary
         :renderer: rst

   .. py:attribute:: class_docstring
      :canonical: autodoc2.config.Config.class_docstring
      :type: typing.Literal[merge, both]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.class_docstring
         :renderer: rst

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.Config.class_inheritance
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.class_inheritance
         :renderer: rst

   .. py:attribute:: annotations
      :canonical: autodoc2.config.Config.annotations
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.annotations
         :renderer: rst

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.Config.sort_names
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.sort_names
         :renderer: rst

   .. py:attribute:: replace_annotations
      :canonical: autodoc2.config.Config.replace_annotations
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.replace_annotations
         :renderer: rst

   .. py:attribute:: replace_bases
      :canonical: autodoc2.config.Config.replace_bases
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.replace_bases
         :renderer: rst

   .. py:attribute:: index_template
      :canonical: autodoc2.config.Config.index_template
      :type: str | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.index_template
         :renderer: rst

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.Config.as_triple

      .. autodoc2-docstring:: autodoc2.config.Config.as_triple
         :renderer: rst

   .. py:method:: to_render_config(pkg_index: int | None) -> autodoc2.config.RenderConfig
      :canonical: autodoc2.config.Config.to_render_config

      .. autodoc2-docstring:: autodoc2.config.Config.to_render_config
         :renderer: rst
