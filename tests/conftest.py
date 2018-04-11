import os
import numpy as np
import py
import pytest
from PIL import Image


@pytest.fixture(scope='session')
def image() -> Image.Image:
    rand_colour = lambda: np.random.randint(0, 255, size=(4096, 4096), dtype='u1')
    data_red, data_blue, data_green = rand_colour(), rand_colour(), rand_colour()
    data = np.vstack(([data_red.T], [data_green.T], [data_blue.T])).T
    return Image.fromarray(data, mode='RGB')

@pytest.fixture
def image_path(tmpdir: py._path.local.LocalPath, image: Image.Image) -> str:
    path = os.path.join(tmpdir, 'tmp.png')
    image.save(path)
    return path
