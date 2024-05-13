"""Directive for rendering docstrings."""

from __future__ import annotations

from contextlib import contextmanager
import typing as t

from docutils import nodes
from docutils.parsers import Parser, get_parser_class
from docutils.parsers.rst import directives, roles
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective, new_document
from sphinx.util.logging import prefixed_warnings

from autodoc2.sphinx.utils import get_database, nested_parse_generated, warn_sphinx
from autodoc2.utils import WarningSubtypes

if t.TYPE_CHECKING:
    from docutils.parsers.rst.states import RSTStateMachine


def parser_options(argument: str) -> Parser | None:
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
        raise ValueError(str(err)) from err


def summary_option(argument: str) -> int | None:
    """Must be empty or a positive integer."""
    if argument and argument.strip():
        try:
            value = int(argument)
        except ValueError as err:
            raise ValueError("non-integer value; must be an integer") from err
        if value < 0:
            raise ValueError("negative value; must be positive or zero")
        return value
    else:
        return None


class DocstringRenderer(SphinxDirective):
    """Directive to render a docstring of an object."""

    has_content = False
    required_arguments = 1  # the full name
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec: t.ClassVar[dict[str, t.Any]] = {
        "parser": parser_options,
        "allowtitles": directives.flag,  # used for module docstrings
        "summary": summary_option,  # number of children to return
        "literal": directives.flag,  # return the literal docstring
        "literal-lexer": directives.unchanged,  # the lexer to use for literal
        "literal-linenos": directives.flag,  # add line numbers to literal
    }

    def run(self) -> list[nodes.Node]:
        """Run the directive {a}`1`."""
        directive_source, directive_line = self.get_source_info()
        # warnings take the docname and line number
        warning_loc = (self.env.docname, directive_line)

        # find the database item for this object
        full_name: str = self.arguments[0]
        autodoc2_db = get_database(self.env)
        item = autodoc2_db.get_item(full_name)

        if item is None:
            if "summary" not in self.options:
                # summaries can include items imported from external modules
                # which may not be in the database, so we don't warn about those
                warn_sphinx(
                    f"Could not find {full_name}",
                    WarningSubtypes.NAME_NOT_FOUND,
                    location=warning_loc,
                )
            return []

        # find the source path for this object, by walking up the parent tree
        source_name = item["doc_inherited"] if item.get("doc_inherited") else full_name
        source_path: str | None = None
        for ancestor in autodoc2_db.get_ancestors(source_name, include_self=True):
            if ancestor is None:
                break  # should never happen
            if "file_path" in ancestor:
                source_path = ancestor["file_path"]
                break
        source_item = autodoc2_db.get_item(source_name)
        # also get the line number within the file
        source_offset = (
            source_item["range"][0] if source_item and ("range" in source_item) else 0
        )

        if source_path:
            # ensure rebuilds when the source file changes
            self.env.note_dependency(source_path)

        if not item["doc"].strip():
            return []

        if "literal" in self.options:
            # return the literal docstring
            literal = nodes.literal_block(text=item["doc"])
            self.set_source_info(literal)
            if "literal-lexer" in self.options:
                literal["language"] = self.options["literal-lexer"]
            if "literal-linenos" in self.options:
                literal["linenos"] = True
                literal["highlight_args"] = {"linenostart": 1 + source_offset}
            return [literal]

        # now we run the actual parsing
        # here things get a little tricky:
        # 1. We want to parse the docstring according to the correct parser,
        #    which, may not be the same as the current parser.
        # 2. We want to set the source path and line number correctly
        #    so that warnings and errors are reported against the actual source documentation.

        with prefixed_warnings("[Autodoc2]:"):
            if self.options.get("parser", None):
                # parse into a dummy document and return created nodes
                parser: Parser = self.options["parser"]()
                document = new_document(
                    source_path or self.state.document["source"],
                    self.state.document.settings,
                )
                document.reporter.get_source_and_line = lambda li: (
                    source_path,
                    li + source_offset,
                )
                with parsing_context():
                    parser.parse(item["doc"], document)
                children = document.children or []

            else:
                doc_lines = item["doc"].splitlines()
                if source_path:
                    # Here we perform a nested render, but temporarily setup the document/reporter
                    # with the correct document path and lineno for the included file.
                    with change_source(
                        self.state, source_path, source_offset - directive_line
                    ):
                        base = nodes.Element()
                        base.source = source_path
                        base.line = source_offset
                        content = StringList(
                            doc_lines,
                            source=source_path,
                            items=[
                                (source_path, i + source_offset + 1)
                                for i in range(len(doc_lines))
                            ],
                        )
                        self.state.nested_parse(
                            content, 0, base, match_titles="allowtitles" in self.options
                        )

                else:
                    base = nested_parse_generated(
                        self.state,
                        doc_lines,
                        directive_source,
                        directive_line,
                        match_titles="allowtitles" in self.options,
                    )

                children = base.children or []

            if children and ("summary" in self.options):
                if self.options["summary"] in (None, 1):
                    return [children[0]]
                return children[: self.options["summary"]]

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
    # TODO also override the warning message to include the original source
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


def _example(a: int, b: str) -> None:
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
