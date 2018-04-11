from PIL import Image
from colour_sort import image as imagelib



def test_as_sorted(image: Image.Image) -> None:
    sorted_image = imagelib.as_sorted(image)
    assert sorted_image
