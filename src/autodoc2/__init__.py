"""Analyse a python project and create documentation for it."""

__version__ = "0.4.2"


def setup(app):  # type: ignore
    """Entrypoint for sphinx."""
    from .sphinx.extension import setup as _setup

    return _setup(app)
