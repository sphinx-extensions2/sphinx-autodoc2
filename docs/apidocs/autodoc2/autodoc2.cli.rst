:py:mod:`autodoc2.cli`
======================

.. py:module:: autodoc2.cli

.. autodoc2-docstring:: autodoc2.cli
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`version_callback <autodoc2.cli.version_callback>`
     - .. autodoc2-docstring:: autodoc2.cli.version_callback
          :summary:
   * - :py:obj:`main_app <autodoc2.cli.main_app>`
     - .. autodoc2-docstring:: autodoc2.cli.main_app
          :summary:
   * - :py:obj:`list_items <autodoc2.cli.list_items>`
     - .. autodoc2-docstring:: autodoc2.cli.list_items
          :summary:
   * - :py:obj:`create_db <autodoc2.cli.create_db>`
     - .. autodoc2-docstring:: autodoc2.cli.create_db
          :summary:
   * - :py:obj:`analyse_all <autodoc2.cli.analyse_all>`
     - .. autodoc2-docstring:: autodoc2.cli.analyse_all
          :summary:
   * - :py:obj:`write <autodoc2.cli.write>`
     - .. autodoc2-docstring:: autodoc2.cli.write
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`console <autodoc2.cli.console>`
     - .. autodoc2-docstring:: autodoc2.cli.console
          :summary:
   * - :py:obj:`app_main <autodoc2.cli.app_main>`
     - .. autodoc2-docstring:: autodoc2.cli.app_main
          :summary:

API
~~~

.. py:data:: console
   :canonical: autodoc2.cli.console
   :value: None

   .. autodoc2-docstring:: autodoc2.cli.console

.. py:data:: app_main
   :canonical: autodoc2.cli.app_main
   :value: None

   .. autodoc2-docstring:: autodoc2.cli.app_main

.. py:function:: version_callback(value: bool) -> None
   :canonical: autodoc2.cli.version_callback

   .. autodoc2-docstring:: autodoc2.cli.version_callback

.. py:function:: main_app(version: typing.Optional[bool] = typer.Option(None, '-v', '--version', callback=version_callback, is_eager=True, help='Show the application version and exit.')) -> None
   :canonical: autodoc2.cli.main_app

   .. autodoc2-docstring:: autodoc2.cli.main_app

.. py:function:: list_items(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path'), inherited: bool = typer.Option(False, '-i', '--inherited', help='Show inherited members'), private: bool = typer.Option(False, '-p', '--private', help='Show private members'), one_line: bool = typer.Option(False, '-o', '--one-line', help='Show only full name and type'), filter_types_str: typing.Optional[str] = typer.Option(None, '-ft', '--filter-types', help='Only show members of types (comma separated)'), skip_types_str: str = typer.Option('import_from', '-st', '--skip-types', help='Do not show members of types (comma separated)'), filter_name: typing.Optional[str] = typer.Option(None, '-fn', '--filter-name', help='Only show members with this name regex')) -> None
   :canonical: autodoc2.cli.list_items

   .. autodoc2-docstring:: autodoc2.cli.list_items

.. py:function:: create_db(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), output: pathlib.Path = typer.Argument('autodoc.db.json', help='File to write to'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path')) -> None
   :canonical: autodoc2.cli.create_db

   .. autodoc2-docstring:: autodoc2.cli.create_db

.. py:function:: analyse_all(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to a database file'), package: str = typer.Argument(..., help='The name of the package to resolve.')) -> None
   :canonical: autodoc2.cli.analyse_all

   .. autodoc2-docstring:: autodoc2.cli.analyse_all

.. py:function:: write(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path'), output: pathlib.Path = typer.Option('_autodoc', help='Folder to write to'), clean: bool = typer.Option(False, '-c', '--clean', help='Remove old files')) -> None
   :canonical: autodoc2.cli.write

   .. autodoc2-docstring:: autodoc2.cli.write
