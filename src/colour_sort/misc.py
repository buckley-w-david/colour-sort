import numpy as np

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
        # import pdb; pdb.set_trace()
        cartesian(arrays[1:], out=out[0:index, 1:])
        for j in range(1, arrays[0].size):
            out[j*index:(j+1)*index, 1:] = out[0:index, 1:]
    return out
