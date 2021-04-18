import typer

app = typer.Typer()


@app.command()
def init(complete_dataset_path: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":  # pragma: no mutate
    app()
