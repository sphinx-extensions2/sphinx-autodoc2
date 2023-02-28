:py:mod:`autodoc2.resolve_all`
==============================

.. py:module:: autodoc2.resolve_all

.. autodoc2-docstring:: autodoc2.resolve_all
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AllResolveResult <autodoc2.resolve_all.AllResolveResult>`
     -
   * - :py:obj:`AllResolver <autodoc2.resolve_all.AllResolver>`
     - .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver
          :summary:

API
~~~

.. py:exception:: AllResolutionError()
   :canonical: autodoc2.resolve_all.AllResolutionError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: autodoc2.resolve_all.AllResolutionError

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.resolve_all.AllResolutionError.__init__

.. py:exception:: ObjectMissingError()
   :canonical: autodoc2.resolve_all.ObjectMissingError

   Bases: :py:obj:`autodoc2.resolve_all.AllResolutionError`

   .. autodoc2-docstring:: autodoc2.resolve_all.ObjectMissingError

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.resolve_all.ObjectMissingError.__init__

.. py:exception:: CircularImportError()
   :canonical: autodoc2.resolve_all.CircularImportError

   Bases: :py:obj:`autodoc2.resolve_all.AllResolutionError`

   .. autodoc2-docstring:: autodoc2.resolve_all.CircularImportError

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.resolve_all.CircularImportError.__init__

.. py:exception:: NoAllError()
   :canonical: autodoc2.resolve_all.NoAllError

   Bases: :py:obj:`autodoc2.resolve_all.AllResolutionError`

   .. autodoc2-docstring:: autodoc2.resolve_all.NoAllError

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.resolve_all.NoAllError.__init__

.. py:class:: AllResolveResult()
   :canonical: autodoc2.resolve_all.AllResolveResult

   Bases: :py:obj:`typing.TypedDict`

   .. py:attribute:: resolved
      :canonical: autodoc2.resolve_all.AllResolveResult.resolved
      :type: dict[str, str]
      :value: None

      .. autodoc2-docstring:: autodoc2.resolve_all.AllResolveResult.resolved

   .. py:attribute:: errors
      :canonical: autodoc2.resolve_all.AllResolveResult.errors
      :type: list[tuple[str, str]]
      :value: None

      .. autodoc2-docstring:: autodoc2.resolve_all.AllResolveResult.errors

.. py:class:: AllResolver(db: autodoc2.db.Database, warn_func: typing.Callable[[str], None] | None = None)
   :canonical: autodoc2.resolve_all.AllResolver

   .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver

   .. rubric:: Initialization

   .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver.__init__

   .. py:method:: clear_cache() -> None
      :canonical: autodoc2.resolve_all.AllResolver.clear_cache

      .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver.clear_cache

   .. py:method:: get_resolved_all(full_name: str, _breadcrumbs: tuple[str, ...] = ()) -> autodoc2.resolve_all.AllResolveResult
      :canonical: autodoc2.resolve_all.AllResolver.get_resolved_all

      .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver.get_resolved_all

   .. py:method:: get_name(name: str) -> str | None
      :canonical: autodoc2.resolve_all.AllResolver.get_name

      .. autodoc2-docstring:: autodoc2.resolve_all.AllResolver.get_name
