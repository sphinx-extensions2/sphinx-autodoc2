"""Handle sphinx logging."""

from __future__ import annotations

import typing as t

from docutils.nodes import Element
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging

from autodoc2.config import CONFIG_PREFIX, Config, ValidationError
from autodoc2.db import Database, InMemoryDb
from autodoc2.resolve_all import AllResolver
from autodoc2.utils import WarningSubtypes

if t.TYPE_CHECKING:
    from docutils.parsers.rst.states import RSTStateMachine

LOGGER = logging.getLogger("autodoc2")


def load_config(
    app: Sphinx,
    *,
    overrides: None | dict[str, t.Any] = None,
    location: None | Element = None,
) -> Config:
    """Load the configuration."""
    values: dict[str, t.Any] = {}
    overrides = overrides or {}
    config_fields = {name: field for name, _, field in Config().as_triple()}
    # check if keys in overrides are valid
    difference = set(overrides.keys()) - set(config_fields.keys())
    if difference:
        warn_sphinx(
            f"Unknown configuration keys: {', '.join(difference)}",
            WarningSubtypes.CONFIG_ERROR,
            location,
        )
    for name, field in config_fields.items():
        sphinx_name = f"{CONFIG_PREFIX}{name}"
        value = overrides.get(name, app.config[sphinx_name])
        if "sphinx_validate" in field.metadata:
            try:
                value = field.metadata["sphinx_validate"](sphinx_name, value)
            except ValidationError as err:
                warn_sphinx(str(err), WarningSubtypes.CONFIG_ERROR, location)
                continue
        values[name] = value
    return Config(**values)


def warn_sphinx(
    msg: str, subtype: WarningSubtypes, location: None | Element = None
) -> None:
    """Log a warning in Sphinx."""
    LOGGER.warning(
        f"{msg} [autodoc2.{subtype.value}]",
        type="autodoc2",
        subtype=subtype.value,
        location=location,
    )


def get_database(env: BuildEnvironment) -> Database:
    """Get the database from the environment."""
    # We store it persistently in the environment so that it can be
    # accessed by directives and other extensions.
    if not hasattr(env, "autodoc2_db"):
        env.autodoc2_db = InMemoryDb()  # type: ignore
    return env.autodoc2_db  # type: ignore


def _warn(msg: str) -> None:
    warn_sphinx(msg, WarningSubtypes.ALL_RESOLUTION)


def get_all_analyser(env: BuildEnvironment) -> AllResolver:
    """Get the all analyser from the environment."""
    # We store it persistently in the environment so that it can be
    # accessed by directives and other extensions.
    if not hasattr(env, "autodoc2_all_analyser"):
        env.autodoc2_all_analyser = AllResolver(get_database(env), _warn)  # type: ignore
    return env.autodoc2_all_analyser  # type: ignore


def nested_parse_generated(
    state: RSTStateMachine,
    content: list[str],
    source: str,
    line: int,
    *,
    match_titles: bool = False,
    base: Element | None = None,
) -> Element:
    """This function, nested parses generated content in a directive.

    All reported warnings are redirected to a specific source document and line.

    This is useful for directives that want to parse generated content.
    """
    base = Element() if base is None else base
    base.source = source
    base.line = line
    string_list = StringList(
        content,
        items=[(source, line - 1) for _ in content],
    )
    line_func = getattr(state.reporter, "get_source_and_line", None)
    state.reporter.get_source_and_line = lambda li: (
        source,
        line,
    )
    try:
        state.nested_parse(string_list, 0, base, match_titles=match_titles)
    finally:
        if line_func is not None:
            state.reporter.get_source_and_line = line_func
        else:
            del state.reporter.get_source_and_line

    return base
