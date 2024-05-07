:py:mod:`autodoc2.config`
=========================

.. py:module:: autodoc2.config

.. autodoc2-docstring:: autodoc2.config
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PackageConfig <autodoc2.config.PackageConfig>`
     - .. autodoc2-docstring:: autodoc2.config.PackageConfig
          :summary:
   * - :py:obj:`Config <autodoc2.config.Config>`
     - .. autodoc2-docstring:: autodoc2.config.Config
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_coerce_packages <autodoc2.config._coerce_packages>`
     - .. autodoc2-docstring:: autodoc2.config._coerce_packages
          :summary:
   * - :py:obj:`_validate_replace_list <autodoc2.config._validate_replace_list>`
     - .. autodoc2-docstring:: autodoc2.config._validate_replace_list
          :summary:
   * - :py:obj:`_validate_hidden_objects <autodoc2.config._validate_hidden_objects>`
     - .. autodoc2-docstring:: autodoc2.config._validate_hidden_objects
          :summary:
   * - :py:obj:`_validate_regex_list <autodoc2.config._validate_regex_list>`
     - .. autodoc2-docstring:: autodoc2.config._validate_regex_list
          :summary:
   * - :py:obj:`_validate_list_tuple_regex_str <autodoc2.config._validate_list_tuple_regex_str>`
     - .. autodoc2-docstring:: autodoc2.config._validate_list_tuple_regex_str
          :summary:
   * - :py:obj:`_load_renderer <autodoc2.config._load_renderer>`
     - .. autodoc2-docstring:: autodoc2.config._load_renderer
          :summary:
   * - :py:obj:`_load_regex_renderers <autodoc2.config._load_regex_renderers>`
     - .. autodoc2-docstring:: autodoc2.config._load_regex_renderers
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CONFIG_PREFIX <autodoc2.config.CONFIG_PREFIX>`
     - .. autodoc2-docstring:: autodoc2.config.CONFIG_PREFIX
          :summary:

API
~~~

.. py:exception:: ValidationError()
   :canonical: autodoc2.config.ValidationError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: autodoc2.config.ValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.config.ValidationError.__init__

.. py:data:: CONFIG_PREFIX
   :canonical: autodoc2.config.CONFIG_PREFIX
   :value: 'autodoc2_'

   .. autodoc2-docstring:: autodoc2.config.CONFIG_PREFIX

.. py:class:: PackageConfig
   :canonical: autodoc2.config.PackageConfig

   .. autodoc2-docstring:: autodoc2.config.PackageConfig

   .. py:attribute:: path
      :canonical: autodoc2.config.PackageConfig.path
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.path

   .. py:attribute:: from_git_clone
      :canonical: autodoc2.config.PackageConfig.from_git_clone
      :type: tuple[str, str] | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.from_git_clone

   .. py:attribute:: module
      :canonical: autodoc2.config.PackageConfig.module
      :type: str | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.module

   .. py:attribute:: exclude_dirs
      :canonical: autodoc2.config.PackageConfig.exclude_dirs
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.exclude_dirs

   .. py:attribute:: exclude_files
      :canonical: autodoc2.config.PackageConfig.exclude_files
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.exclude_files

   .. py:attribute:: auto_mode
      :canonical: autodoc2.config.PackageConfig.auto_mode
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.auto_mode

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.PackageConfig.as_triple

      .. autodoc2-docstring:: autodoc2.config.PackageConfig.as_triple

.. py:function:: _coerce_packages(name: str, item: typing.Any) -> list[autodoc2.config.PackageConfig]
   :canonical: autodoc2.config._coerce_packages

   .. autodoc2-docstring:: autodoc2.config._coerce_packages

.. py:function:: _validate_replace_list(name: str, item: typing.Any) -> list[tuple[str, str]]
   :canonical: autodoc2.config._validate_replace_list

   .. autodoc2-docstring:: autodoc2.config._validate_replace_list

.. py:function:: _validate_hidden_objects(name: str, item: typing.Any) -> set[str]
   :canonical: autodoc2.config._validate_hidden_objects

   .. autodoc2-docstring:: autodoc2.config._validate_hidden_objects

.. py:function:: _validate_regex_list(name: str, item: typing.Any) -> list[typing.Pattern[str]]
   :canonical: autodoc2.config._validate_regex_list

   .. autodoc2-docstring:: autodoc2.config._validate_regex_list

.. py:function:: _validate_list_tuple_regex_str(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], str]]
   :canonical: autodoc2.config._validate_list_tuple_regex_str

   .. autodoc2-docstring:: autodoc2.config._validate_list_tuple_regex_str

.. py:function:: _load_renderer(name: str, item: typing.Any) -> type[autodoc2.render.base.RendererBase]
   :canonical: autodoc2.config._load_renderer

   .. autodoc2-docstring:: autodoc2.config._load_renderer

.. py:function:: _load_regex_renderers(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
   :canonical: autodoc2.config._load_regex_renderers

   .. autodoc2-docstring:: autodoc2.config._load_regex_renderers

.. py:class:: Config
   :canonical: autodoc2.config.Config

   .. autodoc2-docstring:: autodoc2.config.Config

   .. py:attribute:: packages
      :canonical: autodoc2.config.Config.packages
      :type: list[autodoc2.config.PackageConfig]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.packages

   .. py:attribute:: output_dir
      :canonical: autodoc2.config.Config.output_dir
      :type: str
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.output_dir

   .. py:attribute:: render_plugin
      :canonical: autodoc2.config.Config.render_plugin
      :type: type[autodoc2.render.base.RendererBase]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.render_plugin

   .. py:attribute:: render_plugin_regexes
      :canonical: autodoc2.config.Config.render_plugin_regexes
      :type: list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.render_plugin_regexes

   .. py:attribute:: module_all_regexes
      :canonical: autodoc2.config.Config.module_all_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.module_all_regexes

   .. py:attribute:: skip_module_regexes
      :canonical: autodoc2.config.Config.skip_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.skip_module_regexes

   .. py:attribute:: hidden_objects
      :canonical: autodoc2.config.Config.hidden_objects
      :type: set[typing.Literal[undoc, dunder, private, inherited]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.hidden_objects

   .. py:attribute:: hidden_regexes
      :canonical: autodoc2.config.Config.hidden_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.hidden_regexes

   .. py:attribute:: no_index
      :canonical: autodoc2.config.Config.no_index
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.no_index

   .. py:attribute:: deprecated_module_regexes
      :canonical: autodoc2.config.Config.deprecated_module_regexes
      :type: list[typing.Pattern[str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.deprecated_module_regexes

   .. py:attribute:: module_summary
      :canonical: autodoc2.config.Config.module_summary
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.module_summary

   .. py:attribute:: docstring_parser_regexes
      :canonical: autodoc2.config.Config.docstring_parser_regexes
      :type: list[tuple[typing.Pattern[str], str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.docstring_parser_regexes

   .. py:attribute:: class_docstring
      :canonical: autodoc2.config.Config.class_docstring
      :type: typing.Literal[merge, both]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.class_docstring

   .. py:attribute:: class_inheritance
      :canonical: autodoc2.config.Config.class_inheritance
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.class_inheritance

   .. py:attribute:: annotations
      :canonical: autodoc2.config.Config.annotations
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.annotations

   .. py:attribute:: docstrings
      :canonical: autodoc2.config.Config.docstrings
      :type: typing.Literal[all, direct, none]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.docstrings

   .. py:attribute:: sort_names
      :canonical: autodoc2.config.Config.sort_names
      :type: bool
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.sort_names

   .. py:attribute:: replace_annotations
      :canonical: autodoc2.config.Config.replace_annotations
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.replace_annotations

   .. py:attribute:: replace_bases
      :canonical: autodoc2.config.Config.replace_bases
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.replace_bases

   .. py:attribute:: index_template
      :canonical: autodoc2.config.Config.index_template
      :type: str | None
      :value: None

      .. autodoc2-docstring:: autodoc2.config.Config.index_template

   .. py:method:: as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
      :canonical: autodoc2.config.Config.as_triple

      .. autodoc2-docstring:: autodoc2.config.Config.as_triple
