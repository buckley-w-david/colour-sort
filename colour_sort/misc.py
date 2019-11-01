from math import sqrt, ceil
import typing
import numpy as np

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


def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    product = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([product, len(arrays)], dtype=dtype)

    index = product // arrays[0].size
    out[:, 0] = np.repeat(arrays[0], index)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:index, 1:])
        for j in range(1, arrays[0].size):
            out[j*index:(j+1)*index, 1:] = out[0:index, 1:]
    return out


# Nudge the width and height to ints that still multiply to TOTAL_PIXELS
# TODO Better algorithm? This technique is pretty naive
# def _nudge_dims(width, height):
#     perfect_aspect = width / height
#     best_match = (abs(1-perfect_aspect), (4096, 4096))
#     for x, y in FACTORS:
#         best_err, (_, _) = best_match
#         candidate_aspect_1 = x / y
#         candidate_aspect_2 = y / x
#         candidate_error_1 = abs(candidate_aspect_1 - perfect_aspect)
#         candidate_error_2 = abs(candidate_aspect_2 - perfect_aspect)
#         if candidate_error_1 < best_err:
#             best_match = (candidate_error_1, (x, y))
#         elif candidate_error_2 < best_err:
#             best_match = (candidate_error_2, (y, x))
#     return best_match[1]


def reshape_image(image):
    # src_width, src_height = image.size
    # aspect = src_width / src_height

    # Unfortunately we can't use the "perfect" conversions that maintain the aspect ratio because it's very unlikely that
    # this math will give us 2 ints, so they can't be used as the image dimensions.
    # perfect_width = IMAGE_SIZE * sqrt(aspect)
    # perfect_height = IMAGE_SIZE / sqrt(aspect)

    # new_width, new_height = _nudge_dims(perfect_width, perfect_height)

    # Would love to use the above commented algorithm, but realistically only (2048, 8192) might be better than (4096, 4096), and only on super wide images. It's not worth the computation.
    new_width, new_height = IMAGE_SIZE, IMAGE_SIZE

    thumb = image.resize((new_width, new_height))
    return np.reshape(np.array(thumb), (TOTAL_PIXELS, 3))

def generate_all_colours():
    # TODO: Rename components, they are not always r, g,b (LAB)
    red, green, blue = np.arange(256, dtype='u1'), np.arange(256, dtype='u1'), np.arange(256, dtype='u1')
    return cartesian([red, green, blue])

