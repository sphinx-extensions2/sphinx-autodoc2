"""CLI for the package."""
from pathlib import Path
import re
import typing as t

from rich import progress as rp
from rich.console import Console
import typer

from autodoc2 import __name__ as package_name
from autodoc2 import __version__
from autodoc2.analysis import analyse_module
from autodoc2.config import Config
from autodoc2.db import InMemoryDb, UniqueError
from autodoc2.utils import WarningSubtypes, yield_modules

console = Console()


app_main = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]},
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:
    """Print the version and exit."""
    if value:
        console.print(f"{package_name} version: {__version__}")
        raise typer.Exit()


@app_main.callback()
def main_app(
    version: t.Optional[bool] = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the application version and exit.",
    ),
) -> None:
    """[underline]CLI for sphinx-autodoc2[/underline]"""


@app_main.command("list")
def list_items(
    path: Path = typer.Argument(..., exists=True, help="Path to analyse"),
    module: t.Optional[str] = typer.Option(
        None,
        "-m",
        "--module",
        help="The name of the module, otherwise it will be guessed from the path",
    ),
    inherited: bool = typer.Option(
        False, "-i", "--inherited", help="Show inherited members"
    ),
    private: bool = typer.Option(False, "-p", "--private", help="Show private members"),
    one_line: bool = typer.Option(
        False, "-o", "--one-line", help="Show only full name and type"
    ),
    filter_types_str: t.Optional[str] = typer.Option(
        None,
        "-ft",
        "--filter-types",
        help="Only show members of types (comma separated)",
    ),
    skip_types_str: str = typer.Option(
        "import_from",
        "-st",
        "--skip-types",
        help="Do not show members of types (comma separated)",
    ),
    filter_name: t.Optional[str] = typer.Option(
        None, "-fn", "--filter-name", help="Only show members with this name regex"
    ),
) -> None:
    """Analyse a python module or package and stream the results to the console."""
    # initialise filters
    skip_types = skip_types_str.split(",")
    filter_types = filter_types_str.split(",") if filter_types_str else None
    filter_name_func: t.Callable[[str], bool] = (
        re.compile(filter_name).match if filter_name else lambda _: True  # type: ignore
    )

    # gather the modules
    modules: t.Iterable[t.Tuple[Path, str]]
    if path.is_dir():
        root_module = module or path.name
        modules = yield_modules(path, root_module=root_module)
    else:
        root_module = module or path.stem
        modules = [(path, root_module)]

    for mod_path, mod_name in modules:
        for data in analyse_module(mod_path, mod_name):
            if not filter_name_func(data["full_name"]):
                continue
            if data["type"] in skip_types or (
                filter_types and data["type"] not in filter_types
            ):
                continue
            if not inherited and data.get("inherited", None):
                continue
            if not private and data["full_name"].split(".")[-1].startswith("_"):
                continue
            if one_line:
                console.print(f'{data["full_name"]} ({data["type"]})')
            else:
                console.print(data)


@app_main.command("create-db")
def create_db(
    path: Path = typer.Argument(..., exists=True, help="Path to analyse"),
    output: Path = typer.Argument("autodoc.db.json", help="File to write to"),
    module: t.Optional[str] = typer.Option(
        None,
        "-m",
        "--module",
        help="The name of the module, otherwise it will be guessed from the path",
    ),
) -> None:
    """Create a database for a python module or package."""
    # gather the modules
    modules: t.Iterable[t.Tuple[Path, str]]
    if path.is_dir():
        root_module = module or path.name
        modules = list(yield_modules(path, root_module=root_module))
    else:
        root_module = module or path.stem
        modules = [(path, root_module)]

    # analyse the modules and write to the database
    db = InMemoryDb()
    with rp.Progress(
        rp.TextColumn("[bold]Analyse[/bold]"),
        rp.BarColumn(),
        rp.TaskProgressColumn(),
        rp.TimeElapsedColumn(),
        rp.TextColumn("[progress.description]{task.description}"),
    ) as progress:
        task = progress.add_task("", total=len(modules))
        for mod_path, mod_name in modules:
            progress.update(task, description=mod_name)
            for data in analyse_module(mod_path, mod_name):
                try:
                    db.add(data)
                except UniqueError:
                    progress.console.print(
                        f"[yellow]Warning[/yellow] Duplicate item {data['full_name']} ({data['type']})"
                    )
            progress.advance(task)

    # write the database to file
    with output.open("w") as f:
        db.write(f)
    console.print(f"[green]Database written[/green]: {output}")


@app_main.command("resolve-all")
def analyse_all(
    path: Path = typer.Argument(..., exists=True, help="Path to a database file"),
    package: str = typer.Argument(
        ...,
        help="The name of the package to resolve.",
    ),
) -> None:
    """Analyse the __all__ of a module and find potential matches"""
    with path.open("r") as f:
        db = InMemoryDb.read(f)

    from autodoc2.utils import resolve_all

    data = resolve_all(db, package)

    console.print(data)

    console.print("")
    console.print("[green]Done![/green]")


@app_main.command("write")
def write(
    path: Path = typer.Argument(..., exists=True, help="Path to analyse"),
    module: t.Optional[str] = typer.Option(
        None,
        "-m",
        "--module",
        help="The name of the module, otherwise it will be guessed from the path",
    ),
    # TODO read from config file, to populate config object
    output: Path = typer.Option("_autodoc", help="Folder to write to"),
    clean: bool = typer.Option(False, "-c", "--clean", help="Remove old files"),
) -> None:
    """Create sphinx files for a python module or package."""
    # gather the module
    modules: t.Iterable[t.Tuple[Path, str]]
    if path.is_dir():
        root_module = module or path.name
        modules = list(yield_modules(path, root_module=root_module))
    else:
        root_module = module or path.stem
        modules = [(path, root_module)]

    # analyse the modules and write to the database
    db = InMemoryDb()
    with rp.Progress(
        rp.TextColumn("[bold]Analyse[/bold]"),
        rp.BarColumn(),
        rp.TaskProgressColumn(),
        rp.TimeElapsedColumn(),
        rp.TextColumn("[progress.description]{task.description}"),
    ) as progress:
        task = progress.add_task("", total=len(modules))
        for mod_path, mod_name in modules:
            progress.update(task, advance=1, description=mod_name)
            for data in analyse_module(mod_path, mod_name):
                try:
                    db.add(data)
                except UniqueError:
                    progress.console.print(
                        f"[yellow]Warning[/yellow] Duplicate item {data['full_name']} ({data['type']})"
                    )

    # find all the package/module, so we know what files to write
    # To following __all__ strategy
    console.print("Determining files to write...")
    to_write: t.List[str] = []
    stack = [root_module]
    while stack:
        item = stack.pop()
        to_write.append(item)
        stack.extend(list(db.get_children_names(item, {"package", "module"})))

    # write the files
    output.mkdir(parents=True, exist_ok=True)
    paths = []
    with rp.Progress(
        rp.TextColumn("[bold]Write[/bold]"),
        rp.BarColumn(),
        rp.TaskProgressColumn(),
        rp.TimeElapsedColumn(),
        rp.TextColumn("[progress.description]{task.description}"),
    ) as progress:
        task = progress.add_task("", total=len(to_write))

        def _warn(msg: str, type_: WarningSubtypes) -> None:
            progress.console.print(f"[yellow]Warning[/yellow] {msg} [{type_.value}]")

        config = Config()
        for mod_name in to_write:
            progress.update(task, advance=1, description=mod_name)
            content = "\n".join(
                config.render_plugin(
                    db, config.to_render_config(None), _warn
                ).render_item(mod_name)
            )
            out_path = output / (mod_name + config.render_plugin.EXTENSION)
            paths.append(out_path)
            if out_path.exists() and out_path.read_text("utf8") == content:
                # Don't write the file if it hasn't changed
                # this means that sphinx doesn't mark it for rebuild (mtime based)
                continue
            out_path.write_text(content, "utf8")

    # remove any files that are no longer needed
    if clean:
        console.print("[bold]Cleaning old files[/bold]")
        for path in output.iterdir():
            if path.is_dir():
                continue
            if path not in paths:
                path.unlink()

    console.print("[bold green]Success![/bold green]")
    console.print(f"Files written to: {output}")
