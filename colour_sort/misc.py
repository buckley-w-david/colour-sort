import typing
import numpy as np

# FIXME duplicate constant
IMAGE_SIZE = 4096

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

def reshape_image(image):
    # TODO: Replace hardcoded 4096x4096 to a pair of dimentions closest to the source onces that still is a correct size
    thumb = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    return np.reshape(np.array(thumb), (IMAGE_SIZE*IMAGE_SIZE, 3))

def generate_all_colours():
    # TODO: Rename components, they are not always r, g,b (LAB)
    red, green, blue = np.arange(256, dtype='u1'), np.arange(256, dtype='u1'), np.arange(256, dtype='u1')
    return cartesian([red, green, blue])

