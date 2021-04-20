import typer
import common_task_framework

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    ctf = common_task_framework.Referee(path_to_complete_dataset)
    ctf.init()


@app.command()
def evaluate(path_to_complete_dataset: str, path_to_submission: str, directory: bool = False):
    ctf = common_task_framework.Referee(path_to_complete_dataset)
    if directory:
        ctf.evaluate_submission_directory(path_to_submission)
    else:
        ctf.evaluate_single_submission(path_to_submission)


if __name__ == "__main__":
    app()
