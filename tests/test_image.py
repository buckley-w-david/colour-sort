import numpy as np
from PIL import Image
from colour_sort.image import as_sorted

IMAGE_SIZE = 4096

def test_as_sorted(image: Image.Image) -> None:
    output = as_sorted(image)

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape
