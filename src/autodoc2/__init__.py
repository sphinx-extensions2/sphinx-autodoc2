"""Analyse a python project and create documentation for it."""

__version__ = "0.2.2"


def setup(app):  # type: ignore
    """Entrypoint for sphinx."""
    from .extension import setup as _setup

    return _setup(app)
