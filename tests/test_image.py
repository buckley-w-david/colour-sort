import numpy as np
from PIL import Image
import pytest
from colour_sort.image import create_sorted_image
from colour_sort.sort_type import SortType
from colour_sort.verify import verify_image


@pytest.fixture(scope='session')
def image():
    data = np.random.randint(0, 255, size=(4096, 4096, 3), dtype='u1')

    return Image.fromarray(data, mode='RGB')


@pytest.fixture(params=[sort_type for sort_type in SortType])
def rand_image(image, request):
    return (image, request.param)


def test_as_sorted(rand_image):
    image, mode = rand_image
    output = create_sorted_image(image, mode)
    assert verify_image(output)
