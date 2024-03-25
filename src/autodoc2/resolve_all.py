"""Handling of ``__all__`` resolution."""

from __future__ import annotations

import typing as t

from autodoc2.db import Database


class AllResolutionError(Exception):
    """An error occurred while resolving the ``__all__``."""


class ObjectMissingError(AllResolutionError):
    """An object in the ``__all__`` is not available in the database."""


class CircularImportError(AllResolutionError):
    """A circular import was detected."""


class NoAllError(AllResolutionError):
    """The module does not have an ``__all__``."""


class AllResolveResult(t.TypedDict):
    resolved: dict[str, str]
    """Resolved is a dict of ``{full_name: {name}}``"""
    errors: list[tuple[str, str]]
    """Errors are tuples of ``(full_name, error_message)``"""


class AllResolver:
    def __init__(
        self, db: Database, warn_func: t.Callable[[str], None] | None = None
    ) -> None:
        """Initialise the resolver.

        :param db: the database to use
        :param warn_func: a function to call with warnings
        """
        self._db = db
        self._warn_func = (lambda x: None) if warn_func is None else warn_func
        self._resolve_cache: dict[str, AllResolveResult] = {}

    def clear_cache(self) -> None:
        """Clear the cache."""
        self._resolve_cache = {}

    def get_resolved_all(
        self, full_name: str, _breadcrumbs: tuple[str, ...] = ()
    ) -> AllResolveResult:
        """Yield all names that would be imported by star.

        :param full_name: the fully qualified name of the module
        :param _breadcrumbs: used to detect circular imports
        """
        if full_name in self._resolve_cache:
            return self._resolve_cache[full_name]
        if full_name in self._resolve_cache:
            return self._resolve_cache[full_name]
        if full_name in _breadcrumbs:
            raise CircularImportError(
                f"Circular import detected: {full_name} -> {_breadcrumbs}"
            )
        if (item := self._db.get_item(full_name)) is None:
            raise ObjectMissingError(full_name)
        if (all_list := item.get("all")) is None:
            raise NoAllError(f"{full_name!r} does not have an __all__")

        resolved: dict[str, set[str]] = {name: set() for name in all_list}
        errors: list[tuple[str, str]] = []

        # direct children
        for name in all_list:
            if f"{full_name}.{name}" in self._db:
                resolved[name].add(f"{full_name}.{name}")

        # direct imports
        star_imports: list[str] = []
        for import_name, alias in item.get("imports", []):
            final_name = alias or import_name.split(".")[-1]
            if final_name == "*":
                star_imports.append(import_name[:-2])
            elif final_name in resolved:
                resolved[final_name].add(import_name)

        # star imports
        for import_name in star_imports:
            # TODO how do we "bubble up" errors? so that we can report them
            try:
                resolved_import = self.get_resolved_all(
                    import_name, (*_breadcrumbs, full_name)
                )
            except ObjectMissingError:
                errors.append((full_name, f"from {import_name} import *; is unknown"))
            except CircularImportError:
                errors.append(
                    (full_name, f"from {import_name} import *; is a circular import")
                )
            except NoAllError:
                errors.append(
                    (
                        full_name,
                        f"from {import_name} import *; does not have an __all__",
                    )
                )
            else:
                errors.extend(resolved_import["errors"])
                for name, items in resolved_import["resolved"].items():
                    if name in resolved:
                        resolved[name].add(items)

        final_resolved: dict[str, str] = {}
        for name, rnames in resolved.items():
            if not rnames:
                errors.append((full_name, f"{name!r} is unknown"))
            elif len(rnames) > 1:
                errors.append((full_name, f"{name!r} is ambiguous: {rnames}"))
            else:
                final_resolved[name] = rnames.pop()

        for error in errors:
            self._warn_func(f"{full_name}: {error[0]}: {error[1]}")

        self._resolve_cache[full_name] = {
            "resolved": final_resolved,
            "errors": errors,
        }
        return self._resolve_cache[full_name]

    def get_name(self, name: str) -> str | None:
        """Get the item, first by trying the fully qualified name,
        then by looking at __all__ in parent modules.
        """
        if name in self._db:
            return name

        parts = name.split(".")
        if len(parts) < 2:
            return None

        parent, child = ".".join(parts[:-1]), parts[-1]
        try:
            resolved = self.get_resolved_all(parent)
        except AllResolutionError:
            return None
        return resolved["resolved"].get(child, None)
