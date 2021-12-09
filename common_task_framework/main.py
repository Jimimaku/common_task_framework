import typer
import ctf

app = typer.Typer()


@app.command()
def init(path_to_complete_dataset: str):
    referee = ctf.Referee(path_to_complete_dataset)
    referee.init()


@app.command()
def evaluate(path_to_complete_dataset: str, path_to_submission: str, directory: bool = False):
    referee = ctf.Referee(path_to_complete_dataset)
    if directory:
        referee.evaluate_submission_directory(path_to_submission)
    else:
        referee.evaluate_single_submission(path_to_submission)


if __name__ == "__main__":
    app()
