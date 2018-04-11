from PIL import Image
import numpy as np
from colour_sort import misc


IMAGE_SIZE = 4096


def as_sorted(image: Image.Image) -> Image.Image:
    thumb = image.resize((IMAGE_SIZE, IMAGE_SIZE))

    pic = np.reshape(np.array(thumb), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats = 'u1, u1, u1')

    r, g, b = np.arange(256, dtype='u1'), np.arange(256, dtype='u1'), np.arange(256, dtype='u1')
    base = misc.cartesian([r, g, b])
    structured_base = np.core.records.fromarrays(base.transpose(),
                                                 names='r, g, b',
                                                 formats = 'u1, u1, u1')
    structured_base.sort(order=['r', 'g', 'b'])

    mapping = np.argsort(structured_pic, order=['r', 'g', 'b'])
    reverse_mapping = np.argsort(mapping)

    sorted_base = np.reshape(structured_base[reverse_mapping], (IMAGE_SIZE, IMAGE_SIZE))

    return Image.fromarray(sorted_base.view('u1').reshape(sorted_base.shape + (-1,)))

