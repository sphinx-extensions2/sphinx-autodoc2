"""Utility functions and types."""

from __future__ import annotations

import enum
from fnmatch import fnmatch
import os
from pathlib import Path
import typing as t

from typing_extensions import Required

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

    # class or method
    doc_inherited: str

    # child of class
    inherited: str


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
    NAME_NOT_FOUND = "missing"


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
            name, suffix = os.path.splitext(filename)  # noqa: PTH122
            if suffix in extensions:
                to_yield.setdefault(name, []).append(suffix)
        root_path = Path(root)
        rel_mod = root_path.relative_to(folder).parts
        for name, suffixes in to_yield.items():
            suffix = sorted(suffixes, key=_suffix_sort_key)[0]
            yield (root_path / f"{name}{suffix}", ".".join([*root_mod, *rel_mod, name]))
