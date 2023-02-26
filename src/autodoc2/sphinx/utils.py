"""Handle sphinx logging."""
from __future__ import annotations

import typing as t

from docutils.nodes import Element
from sphinx.application import Sphinx
from sphinx.util import logging

from autodoc2.config import CONFIG_PREFIX, Config, ValidationError
from autodoc2.utils import WarningSubtypes

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
