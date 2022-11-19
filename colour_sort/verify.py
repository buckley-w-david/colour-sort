import numpy as np
from PIL import Image

from colour_sort.errors import IncorrectSizeError

def _colour_check(img: Image.Image) -> np.ndarray:
    check = np.zeros(256 * 256 * 256, dtype=bool)
    img_a = np.array(img).astype(
        np.uint32
    )  # They all have to be uint32 because 255 << 16 = 16711680
    if np.product(img_a.shape[:2]) != 256 * 256 * 256:
        raise IncorrectSizeError(img_a.shape[:2])

    flattened = np.reshape(img_a, (256 * 256 * 256, 3))

    np.left_shift(flattened[:, 0], 16, out=flattened[:, 0])
    np.left_shift(flattened[:, 1], 8, out=flattened[:, 1])

    indexed = flattened[:, 0] | flattened[:, 1] | flattened[:, 2]
    check[indexed] = True
    return check


def verify_image(img: Image.Image) -> bool:
    check = _colour_check(img)
    return bool(np.all(check))


def missing_colours(img: Image.Image) -> np.ndarray:
    check = _colour_check(img)
    indicies = np.where(check == False)[0]
    r = (indicies & 0x00FF0000) >> 16
    g = (indicies & 0x0000FF00) >> 8
    b = indicies & 0x000000FF
    return np.stack([r, g, b], axis=1)
