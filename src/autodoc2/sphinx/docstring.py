"""Directive for rendering docstrings."""
from __future__ import annotations

from contextlib import contextmanager
import typing as t

from docutils import nodes
from docutils.parsers import Parser, get_parser_class
from docutils.parsers.rst import directives, roles
from docutils.parsers.rst.states import RSTStateMachine
from docutils.statemachine import StringList
from docutils.utils import new_document
from sphinx.util.docutils import SphinxDirective

from autodoc2.sphinx.logging_ import warn_sphinx
from autodoc2.utils import ItemData, WarningSubtypes

if t.TYPE_CHECKING:
    from autodoc2.sphinx.extension import EnvCache


def parser_name(argument: str) -> Parser:
    """
    Return a docutils parser whose name matches the argument.
    (Directive option conversion function.)

    Return `None`, if the argument evaluates to `False`.
    Raise `ValueError` if importing the parser module fails.
    """
    if not argument or not argument.strip():
        return None
    if argument in ("myst", "markdown", "md"):
        # we want to use the sphinx parser, not the docutils one
        argument = "myst_parser.sphinx_"
    try:
        return get_parser_class(argument)
    except ImportError as err:
        raise ValueError(str(err))


class DocstringRenderer(SphinxDirective):
    """Directive to render a docstring of an object."""

    has_content = False
    required_arguments = 1  # the full name
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "parser": parser_name,
        "allowtitles": directives.flag,  # used for module docstrings
        "summary": directives.flag,  # return first child only
        "literal": directives.flag,  # return the literal docstring
        "literal-lexer": directives.unchanged,  # the lexer to use for literal
        "literal-linenos": directives.flag,  # add line numbers to literal
    }

    def run(self) -> list[nodes.Node]:
        """Run the directive."""

        # find the database item for this object
        name = self.arguments[0]
        dbs: dict[str, EnvCache] = self.env.autodoc2_cache  # type: ignore
        item: ItemData | None = None
        for cache in dbs.values():
            item = cache["db"].get_item(name)
            if item:
                break

        if item is None:
            if "summary" not in self.options:
                # summaries can include items imported from external modules
                # which may not be in the database, so we don't warn about those
                warn_sphinx(
                    f"Could not find {name}",
                    WarningSubtypes.NAME_NOT_FOUND,
                    location=self.get_source_info(),
                )
            return []

        # find the source path for this object, by walking up the parent tree
        source_path = None
        parts = name.split(".")
        while parts:
            parent = cache["db"].get_item(".".join(parts))
            if parent and ("file_path" in parent):
                source_path = parent["file_path"]
                break
            parts.pop()
        # also get the line number within the file
        line_offset = item["range"][0] if "range" in item else 0

        if source_path:
            # ensure rebuilds when the source file changes
            self.env.note_dependency(source_path)

        if not item["doc"]:
            return []

        if "literal" in self.options:
            # return the literal docstring
            literal = nodes.literal_block(text=item["doc"])
            if "literal-lexer" in self.options:
                literal["language"] = self.options["literal-lexer"]
            if "literal-linenos" in self.options:
                literal["linenos"] = True
                literal["highlight_args"] = {"linenostart": 1 + line_offset}
            return [literal]

        # now we run the actual parsing
        # here things get a little tricky:
        # 1. We want to parse the docstring according to the correct parser,
        #    which, may not be the same as the current parser.
        # 2. We want to set the source path and line number correctly
        #    so that warnings and errors are reported against the actual source documentation.

        if self.options.get("parser", None):
            # parse into a dummy document and return created nodes
            parser: Parser = self.options["parser"]()
            document = new_document(
                source_path or self.state.document["source"],
                self.state.document.settings,
            )
            document.reporter.get_source_and_line = lambda li: (
                source_path,
                li + line_offset,
            )
            with parsing_context():
                parser.parse(item["doc"], document)
            children = document.children or []

        else:
            base = nodes.Element()
            if source_path:
                # Here we perform a nested render, but temporarily setup the document/reporter
                # with the correct document path and lineno for the included file.
                with change_source(self.state, source_path, line_offset):
                    lines = item["doc"].splitlines()
                    content = StringList(
                        lines,
                        source=source_path,
                        items=[
                            (source_path, i + line_offset) for i in range(len(lines))
                        ],
                    )
                    self.state.nested_parse(
                        content, 0, base, match_titles="allowtitles" in self.options
                    )

            else:
                self.state.nested_parse(
                    StringList(item["doc"].splitlines()),
                    self.content_offset,
                    base,
                    match_titles="allowtitles" in self.options,
                )
            children = base.children or []

        if children and ("summary" in self.options):
            return [children[0]]

        return children


@contextmanager
def parsing_context() -> t.Generator[None, None, None]:
    """Restore the parsing context after a nested parse with a different parser."""
    should_restore = False
    if "" in roles._roles:
        blankrole = roles._roles[""]
    try:
        yield
    finally:
        if should_restore:
            roles._roles[""] = blankrole


@contextmanager
def change_source(
    state: RSTStateMachine, source_path: str, line_offset: int
) -> t.Generator[None, None, None]:
    """Temporarily change the source and line number."""
    source = state.document["source"]
    rsource = state.reporter.source
    line_func = getattr(state.reporter, "get_source_and_line", None)
    try:
        state.document["source"] = source_path
        state.reporter.source = source_path
        state.reporter.get_source_and_line = lambda li: (
            source_path,
            li + line_offset,
        )
        yield
    finally:
        state.document["source"] = source
        state.reporter.source = rsource
        if line_func is not None:
            state.reporter.get_source_and_line = line_func
        else:
            del state.reporter.get_source_and_line


def _example() -> None:
    """This is an example docstring, written in MyST.

    It has a code fence:

    ```python
    a = "hallo"
    ```

    and a table:

    | a | b | c |
    | - | - | - |
    | 1 | 2 | 3 |

    and, using the `fieldlist` extension, a field list:

    :param a: the first parameter
    :param b: the second parameter
    :return: the return value

    """
