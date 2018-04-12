from PIL import Image
import numpy as np
from colour_sort import misc


IMAGE_SIZE = 4096


def as_sorted(image: Image.Image) -> Image.Image:
    thumb = image.resize((IMAGE_SIZE, IMAGE_SIZE))

    pic = np.reshape(np.array(thumb), (IMAGE_SIZE*IMAGE_SIZE, 3))
    pic_brightness = np.sum(pic, axis=1)

    red, green, blue = np.arange(256, dtype='u1'), np.arange(256, dtype='u1'), np.arange(256, dtype='u1')
    base = misc.cartesian([red, green, blue])
    base_brightness = np.sum(base, axis=1)

    base_by_brightness = base[np.argsort(base_brightness)]

    mapping = np.argsort(pic_brightness)
    reverse_mapping = np.argsort(mapping)

    sorted_base = np.reshape(base_by_brightness[reverse_mapping], (IMAGE_SIZE, IMAGE_SIZE, 3))

    return Image.fromarray(sorted_base)
