import typer


def main(name: str):
    typer.echo(f"Hola {name}")


if __name__ == "__main__":
    typer.run(main)
