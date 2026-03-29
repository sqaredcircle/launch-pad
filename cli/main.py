import typer

app = typer.Typer()


@app.command()
def hello() -> None:
    """Print a greeting to confirm the CLI is working."""
    typer.echo("launch-pad CLI ready")


if __name__ == "__main__":
    app()
