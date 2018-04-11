import typing
import click


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument('image', type=click.File('rb'))
def generate(image: typing.IO[bytes]) -> None:
    print(image)
