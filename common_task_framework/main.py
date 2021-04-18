import typer

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    ctf.init(path_to_complete_dataset)


if __name__ == "__main__":
    app()
