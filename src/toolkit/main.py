import typer

from toolkit.calculator import calculate
from toolkit.converter import convert as convert_value
from toolkit.errors import ToolkitError
from toolkit.tokenizer import tokenize

app = typer.Typer()

@app.command(
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    }
)
def calc(ctx: typer.Context):
    """Вычислить выражение."""
    expression = " ".join(ctx.args)

    try:
        tokens = tokenize(expression)
        result = calculate(tokens)
    except ToolkitError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)

    print(result)


@app.command(
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    }
)
def convert(
        ctx: typer.Context,
        value: float | None = None,
        from_unit: str = typer.Option(..., "--from"),
        to_unit: str = typer.Option(..., "--to"),
):
    """Преобразовать значение между единицами измерения."""
    if value is None:
        if not ctx.args:
            typer.echo("Missing value", err=True)
            raise typer.Exit(code=2)

        try:
            value = float(ctx.args[0])
        except ValueError:
            typer.echo(f"Invalid numeric value: {ctx.args[0]}", err=True)
            raise typer.Exit(code=2)

    try:
        result = convert_value(value, from_unit, to_unit)
    except ToolkitError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)

    typer.echo(result)
