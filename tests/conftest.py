import os
import numpy as np
import py
import pytest
from PIL import Image


@pytest.fixture(scope='session')
def image() -> Image.Image:
    data = np.random.randint(0, 255, size=(4096, 4096, 3), dtype='u1')
    return Image.fromarray(data, mode='RGB')

@pytest.fixture
def image_path(tmpdir: py._path.local.LocalPath, image: Image.Image) -> str:
    path = os.path.join(tmpdir, 'tmp.png')
    image.save(path)
    return path
