from math import sqrt, ceil
import typing
import numpy as np
from PIL import Image

try:
    import importlib.resource as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

# FIXME duplicate constant
IMAGE_SIZE = 4096
TOTAL_PIXELS = IMAGE_SIZE*IMAGE_SIZE
FACTORS = {(32, 524288), (64, 262144), (128, 131072), (256, 65536), (512, 32768), (1024, 16384), (2048, 8192), (4096, 4096), (8, 2097152), (2, 8388608), (16, 1048576), (1, 16777216), (4, 4194304)}

def sort_map(src: np.ndarray, mapped: np.ndarray, order: typing.Optional[typing.List[str]] = None) -> np.ndarray:
    if order is not None:
        mapping = np.argsort(src)
    else:
        mapping = np.argsort(src, order=order)
    reverse_mapping = np.argsort(mapping)

    return mapped[reverse_mapping]


def reshape_image(image):
    new_width, new_height = IMAGE_SIZE, IMAGE_SIZE

    thumb = image.resize((new_width, new_height))
    return np.reshape(np.array(thumb), (TOTAL_PIXELS, 3))

def generate_all_colours():
    with pkg_resources.open_binary('colour_sort', 'all.npy') as colours:
        return np.load(colours)
