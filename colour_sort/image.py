import enum
import itertools

import numpy as np
from PIL import Image, ImageCms
from colour_sort import misc

IMAGE_SIZE = 4096

class SortType(enum.Enum):
    BRIGHTNESS = enum.auto()
    AVG        = enum.auto()
    RGB        = enum.auto()
    RBG        = enum.auto()
    BRG        = enum.auto()
    BGR        = enum.auto()
    GRB        = enum.auto()
    GBR        = enum.auto()

    @staticmethod
    def from_str(sort_type: str) -> 'SortType':
        return getattr(SortType, sort_type.upper())


def _rgb_to_lab(image):
    # Convert the image to LAB colour space - https://stackoverflow.com/a/53353542
    srgb_p = ImageCms.createProfile("sRGB")
    lab_p  = ImageCms.createProfile("LAB")

    rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
    return ImageCms.applyTransform(image, rgb2lab)

# image needs to be in LAB colour space
def _sort_brightness(image):
    results = misc.generate_all_colours()

    src_brightness = image[:,0]
    result_brightness = results[:,0]

    result_by_brightness = results[np.argsort(result_brightness)]

    mapped = misc.sort_map(src_brightness, result_by_brightness)

    return Image.fromarray(np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE, 3)), mode='LAB')


def _sort_avg(image):
    results = misc.generate_all_colours()

    src_avg = np.sum(image, axis=1)
    result_avg = np.sum(results, axis=1)

    result_by_avg = results[np.argsort(result_avg)]

    mapped = misc.sort_map(src_avg, result_by_avg)

    return Image.fromarray(np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE, 3)))


def _sort_rgb(image, mode):
    result = misc.generate_all_colours()

    src_structures = np.core.records.fromarrays(image.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')
    structured_base = np.core.records.fromarrays(result.transpose(),
                                                 names='r, g, b',
                                                 formats='u1, u1, u1')
    structured_base.sort(order=[c for c in mode])

    mapped = misc.sort_map(src_structures, structured_base, order=[c for c in mode])
    shaped = np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE))

    return Image.fromarray(shaped.view('u1').reshape(shaped.shape + (-1,)))


def create_sorted_image(image: Image.Image, mode: SortType) -> Image.Image:
    image = image.convert('RGB')
    if mode is SortType.BRIGHTNESS:
        image = _rgb_to_lab(image)

    reshaped = misc.reshape_image(image)
    if mode is SortType.BRIGHTNESS:
        return _sort_brightness(reshaped)
    elif mode is SortType.AVG:
        return _sort_avg(reshaped)
    else:
        return _sort_rgb(reshaped, str(mode).lower())
