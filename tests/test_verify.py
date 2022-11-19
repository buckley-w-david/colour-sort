import numpy as np
from PIL import Image
import pytest

from colour_sort.verify import verify_image
from colour_sort.misc import generate_all_colours


def test_verify_valid():
    data = generate_all_colours()
    reshaped = np.reshape(data, (4096, 4096, 3))
    image = Image.fromarray(reshaped, mode='RGB')
    assert verify_image(image)


def test_verify_invalid():
    data = np.zeros((4096, 4096, 3))
    image =  Image.fromarray(data, mode='RGB')
    assert not verify_image(image)


def test_verify_invalid_size():
    data = np.zeros((100, 100, 3))
    image = Image.fromarray(data, mode='RGB')
    with pytest.raises(Exception) as e_info:
        verify_image(image)

