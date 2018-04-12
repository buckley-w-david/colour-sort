import numpy as np
from colour_sort import misc


def test_cartesian() -> None:
    assert np.array_equal(misc.cartesian(([1, 2, 3], [4, 5], [6, 7])), np.array([
        [1, 4, 6],
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
        [3, 5, 7],
    ]))


def test_sort_map() -> None:
    arr1 = np.array([1, 5, 4, 2, 3])
    arr2 = np.array([1, 3, 5, 4, 2])
    assert np.array_equal(misc.sort_map(arr1, arr2), np.array([1, 2, 4, 3, 5]))
