"""Utility functions and types."""
from __future__ import annotations

import enum
from fnmatch import fnmatch
import itertools
import os
from pathlib import Path
import typing as t

from typing_extensions import Required

if t.TYPE_CHECKING:
    from .db import Database


PROPERTY_TYPE = t.Literal[
    "async", "staticmethod", "classmethod", "abstractmethod", "singledispatch"
]
ARGS_TYPE = t.List[
    t.Tuple[t.Optional[str], t.Optional[str], t.Optional[str], t.Optional[str]]
]


class ItemData(t.TypedDict, total=False):
    """A data item, for the results of the analysis."""

    type: Required[str]
    full_name: Required[str]  # this is delimited by dots
    doc: Required[str]

    range: tuple[int, int]

    ## module / package
    file_path: None | str
    encoding: str
    all: None | list[str]
    imports: list[tuple[str, str | None]]  # path, alias

    # assign (data)
    value: None | str | t.Any  # TODO make value JSON serializable
    annotation: None | str

    # function/method/overload
    properties: list[PROPERTY_TYPE]
    args: ARGS_TYPE
    return_annotation: None | str

    # class
    bases: list[str]

    # child of class
    inherited: bool


class WarningSubtypes(enum.Enum):
    """The subtypes of warnings for the extension."""

    CONFIG_ERROR = "config_error"
    """Issue with configuration validation."""
    GIT_CLONE_FAILED = "git_clone"
    """Failed to clone a git repository."""
    MISSING_MODULE = "missing_module"
    """If the package file/folder does not exist."""
    DUPLICATE_ITEM = "dup_item"
    """Duplicate fully qualified name found during package analysis."""
    RENDER_ERROR = "render"
    """Generic rendering error."""
    ALL_MISSING = "all_missing"
    """__all__ attribute missing or empty in a module."""
    ALL_RESOLUTION = "all_resolve"
    """Issue with resolution of an item in a module's __all__ attribute."""


def yield_modules(
    folder: str | Path,
    *,
    root_module: str | None = None,
    extensions: t.Sequence[str] = (".py", ".pyi"),
    exclude_dirs: t.Sequence[str] = ("__pycache__",),
    exclude_files: t.Sequence[str] = (),
) -> t.Iterable[tuple[Path, str]]:
    """Walk the given folder and yield all required modules.

    :param folder: The path to walk.
    :param root_module: The name of the root module,
        otherwise the folder name is used.
    :param extensions: The extensions to include.
        If multiple files with the same stem,
        only the first extension will be used.
    :param exclude_dirs: Directory names to exclude (matched with fnmatch).
    :param exclude_files: File names to exclude (matched with fnmatch).
    """
    folder = Path(folder)
    root_mod = (root_module or folder.name).split(".")
    exc_dirs = set(exclude_dirs or [])
    exc_files = set(exclude_files or [])

    def _suffix_sort_key(s: str) -> int:
        return extensions.index(s)

    for root, dirs, filenames in os.walk(folder, topdown=True):
        dirs[:] = [d for d in dirs if not any(fnmatch(d, m) for m in exc_dirs)]
        to_yield: dict[str, list[str]] = {}
        for filename in filenames:
            if any(fnmatch(filename, m) for m in exc_files):
                continue
            name, suffix = os.path.splitext(filename)
            if suffix in extensions:
                to_yield.setdefault(name, []).append(suffix)
        root_path = Path(root)
        rel_mod = root_path.relative_to(folder).parts
        for name, suffixes in to_yield.items():
            suffix = sorted(suffixes, key=_suffix_sort_key)[0]
            yield (root_path / f"{name}{suffix}", ".".join([*root_mod, *rel_mod, name]))


class ResolvedDict(t.TypedDict):
    """The outcome of resolving a packages's __all__ attributes."""

    resolved: dict[str, set[str]]
    """These are names in __all__ that we have successfully resolved,
    to one or more items.
    """
    unresolved: set[str]
    """These are names in __all__ that we have not been able to resolve."""
    stars_unresolved: set[str]
    """These are star imports in the module, that we have not yet resolved."""
    stars_no_all: set[str]
    """These are star imports in the module, that have no recognised __all__.
    At present we do not resolve them.
    """
    stars_unknown: set[str]
    """These are star imports in the module, that we cannot resolve.
    Because they point to a module that is not in the database.
    """


def resolve_all(db: Database, package_name: str) -> dict[str, ResolvedDict]:
    """Give a module name, yield all names that would be imported by star."""
    # see: https://docs.python.org/3/reference/simple_stmts.html#import

    # gather all the packages and modules in the database,
    # that are, or begin with package_name
    modules = {
        i["full_name"]: i
        for i in itertools.chain(db.get_by_type("module"), db.get_by_type("package"))
        if (
            i["full_name"].startswith(package_name + ".")
            or i["full_name"] == package_name
        )
    }

    res_data: dict[str, ResolvedDict] = {}

    # first do the "local" resolution,
    # i.e. everything that is not a star import
    for name in modules:
        module = modules[name]
        all_ = module.get("all") or []

        res_data[name] = {
            "resolved": {},
            "unresolved": set(),
            "stars_unresolved": set(),
            "stars_no_all": set(),
            "stars_unknown": set(),
        }

        if not all_:
            continue

        # first look at local children
        children = {
            n["full_name"].split(".")[-1]: n["full_name"]
            for n in db.get_children(name)
            if n["type"] not in {"module", "package"}
        }
        for all_name in all_:
            if all_name in children:
                res_data[name]["resolved"].setdefault(all_name, set()).add(
                    children[all_name]
                )

        # now look at imports
        for import_name, alias in module.get("imports", []):
            final_name = alias or import_name.split(".")[-1]
            if final_name == "*":
                if import_name[:-2] not in modules:
                    # these are unresolvable so we just record, so we can warn later
                    res_data[name]["stars_unknown"].add(import_name[:-2])
                elif modules[import_name[:-2]].get("all") is None:
                    # There is no recognised __all__ in this module
                    # TODO here we should check against all the modules children and imports
                    # to directly mirror the behaviour of the interpreter
                    # but for now we just record, so we can warn later
                    res_data[name]["stars_no_all"].add(import_name[:-2])
                else:
                    # we cannot resolve these stars yet, so we just record for now
                    res_data[name]["stars_unresolved"].add(import_name[:-2])
            elif final_name in all_:
                res_data[name]["resolved"].setdefault(final_name, set()).add(
                    import_name
                )

    # now resolve the stars, by continually iterating
    # to find/resolve modules with no pointers to other unresolved modules
    something_changed = True
    while something_changed:
        something_changed = False
        for module_name, module_data in res_data.items():
            module_all = modules[module_name].get("all") or []
            for star_name in list(module_data["stars_unresolved"]):
                if res_data[star_name]["stars_unresolved"]:
                    # we have not fully resolved this module yet
                    # so have to wait until the next iteration
                    continue
                module_data["stars_unresolved"].discard(star_name)
                something_changed = True
                for known, known_full_names in res_data[star_name]["resolved"].items():
                    if known in module_all:
                        module_data["resolved"].setdefault(known, set()).update(
                            known_full_names
                        )

    # add the final unresolved names
    for module_name, module_data in res_data.items():
        module_data["unresolved"] = set(modules[module_name]["all"] or []) - set(
            module_data["resolved"]
        )

    return res_data


# Deprecated as a bit of a hack, but leave here for now, to record
# def resolve_all_item(
#     db: Database, module_item: ItemData, all_name: str
# ) -> t.Iterable[str]:
#     """Resolve an item in an `__all__` list, to its full name(s)."""

#     module_name = module_item["full_name"]
#     base = module_name.split(".")[0]

#     item = db.get_item(f"{module_name}.{all_name}")
#     if item and item["type"] not in {"package", "module"}:
#         # directly declared in the module
#         yield f"{module_name}.{all_name}"

#     for import_name, alias in module_item.get("imports") or []:
#         if not import_name.startswith(f"{base}."):
#             continue

#         import_short_name = alias or import_name.split(".")[-1]

#         if import_short_name == all_name:
#             # directly declared in an import within the module
#             yield import_name

#         elif import_short_name == "*":
#             # imported as an ancestor of an import within the module
#             import_parent_name = import_name[:-2]
#             _child_item = db.get_item(f"{import_parent_name}.{all_name}")
#             for ancestor in itertools.chain(
#                 [] if _child_item is None else [_child_item],
#                 db.get_items_like(f"{import_parent_name}.*.{all_name}"),
#             ):
#                 ancestor_parts = ancestor["full_name"].split(".")
#                 ancestor_parent = db.get_item(".".join(ancestor_parts[:-1]))
#                 # TODO we should check that they are in all `__all__` s, up to the module
#                 if ancestor_parent and ancestor_parts[-1] in (
#                     ancestor_parent.get("all") or []
#                 ):
#                     yield ancestor["full_name"]
