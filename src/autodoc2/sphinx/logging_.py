"""Handle sphinx logging."""
from __future__ import annotations

from docutils.nodes import Element
from sphinx.util import logging

from autodoc2.utils import WarningSubtypes

LOGGER = logging.getLogger("autodoc2")


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
