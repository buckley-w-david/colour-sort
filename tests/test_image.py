import os
import numpy as np
from PIL import Image
from colour_sort import image

IMAGE_SIZE = 4096

def test_as_sorted() -> None:
    directory, _ = os.path.split(__file__)
    test_file_path = os.path.join(directory, 'test.png')
    with open(test_file_path, 'rb') as file:
        input_image = Image.open(file).convert('RGB')
        output = image.as_sorted(input_image)

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape