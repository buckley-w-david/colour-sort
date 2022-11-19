from pathlib import Path

from PIL import Image
from rich import print
import typer

from colour_sort.methods import MethodType 
from colour_sort.colour_space import ColourSpace
from colour_sort.convert import ConverterType

from colour_sort.verify import missing_colours
from colour_sort.errors import IncorrectSizeError

from colour_sort.sort import create_sorted_image

app = typer.Typer()

@app.command()
def generate(
    source: Path,
    dest: Path,
    method: MethodType = "brightness", # type: ignore
    colour_space: ColourSpace = "rgb", # type: ignore
    converter: ConverterType = "PIL", # type: ignore
):
    """Generate an allRGB image"""

    input_image = Image.open(source)

    converter_ = ConverterType.to_converter(converter)

    generated = create_sorted_image(input_image, method=method, colour_space=colour_space, converter=converter_)
    try:
        generated.save(dest, lossless=True)
    except:
        generated.save(dest)


@app.command()
def verify(source: Path):
    """Verify that an image contains all RGB values"""

    input_image = Image.open(source)
    try:
        check = missing_colours(input_image)
        valid = not len(check)
        if valid:
            print('%s is a valid allrgb image!' % source)
        else:
            print('%s is not a valid allrgb image' % source)
        # TODO: Somehow convey what the image is missing
    except IncorrectSizeError as e:
        print("%s is not a valid allrgb image: %s" % (source, e))
