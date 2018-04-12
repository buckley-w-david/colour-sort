import typing
import click
from PIL import Image
from colour_sort import image

@click.group()
def main() -> None:
    pass


@main.command()
@click.argument('file', type=click.File('rb'))
@click.argument('out', type=click.File('wb'))
@click.option('--filetype', type=click.Choice(['png', 'jpeg']))
@click.option('--sorttype', type=click.Choice(['brightness', 'rgb']), default='brightness')
def generate(file: typing.IO[bytes], out: typing.IO[bytes], filetype: str, sorttype: str) -> None:
    if not filetype:
        if out.name != '<stdout>':
            filetype = out.name.split('.')[-1]
        elif file.name != '<stdin>':
            filetype = file.name.split('.')[-1]
        else:
            exit(1)

    input_image = Image.open(file).convert('RGB')
    generated = image.as_sorted(input_image, mode=sorttype)
    generated.save(out, filetype)
