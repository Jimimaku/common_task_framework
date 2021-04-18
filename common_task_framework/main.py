import typer
import common_task_framework as ctf

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    ctf.init(path_to_complete_dataset)


@app.command()
def evaluate(path_to_complete_dataset: str, path_to_submission: str):
    ctf.evaluate(path_to_complete_dataset, path_to_submission)


if __name__ == "__main__":
    app()
