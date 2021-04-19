import typer
import common_task_framework

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    ctf = common_task_framework.Referee(path_to_complete_dataset)
    ctf.init()


@app.command()
def evaluate(path_to_complete_dataset: str, path_to_submission: str):
    ctf = common_task_framework.Referee(path_to_complete_dataset)
    ctf.evaluate(path_to_submission)


if __name__ == "__main__":
    app()
