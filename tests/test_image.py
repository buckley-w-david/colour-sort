import itertools
import typing
import numpy as np
from PIL import Image
import pytest
import _pytest
from colour_sort.image import as_sorted


IMAGE_SIZE = 4096


def test_as_sorted_brightness(image: Image.Image) -> None:
    output = as_sorted(image, 'brightness')

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape


@pytest.fixture(params=list(''.join(tup)for tup in itertools.permutations('rgb', 3)))
def rand_image(image, request: _pytest.fixtures.SubRequest) -> Image.Image:
    return (image, request.param)


def test_as_sorted_rgb(rand_image: typing.Tuple[Image.Image, str]) -> None:
    image, mode = rand_image
    output = as_sorted(image, mode)

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape


def test_as_sorted_unknown(image: Image.Image) -> None:
    with pytest.raises(ValueError):
        as_sorted(image, 'unknown')
