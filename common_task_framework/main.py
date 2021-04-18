import typer
import common_task_framework

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    ctf = common_task_framework.Initializator(path_to_complete_dataset)
    ctf.init()


@app.command()
def evaluate(path_to_complete_dataset: str, path_to_submission: str):
    ctf = common_task_framework.Evaluator(path_to_complete_dataset, path_to_submission)
    ctf.evaluate()


if __name__ == "__main__":
    app()
