import numpy as np
from PIL import Image
from colour_sort import misc


IMAGE_SIZE = 4096


class ColourSorter():

    def __init__(self, image: Image.Image) -> None:
        red, green, blue = np.arange(256, dtype='u1'), np.arange(256, dtype='u1'), np.arange(256, dtype='u1')
        thumb = image.resize((IMAGE_SIZE, IMAGE_SIZE))

        self._result_arr = misc.cartesian([red, green, blue])
        self._src_arr = np.reshape(np.array(thumb), (IMAGE_SIZE*IMAGE_SIZE, 3))\

    def _sort_brightness(self) -> np.ndarray:
        src_brightness = np.sum(self._src_arr, axis=1)
        result_brightness = np.sum(self._result_arr, axis=1)

        result_by_brightness = self._result_arr[np.argsort(result_brightness)]

        mapped = misc.sort_map(src_brightness, result_by_brightness)

        return np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE, 3))

    def _sort_rgb(self, mode) -> np.ndarray:
        src_structures = np.core.records.fromarrays(self._src_arr.transpose(),
                                                    names='r, g, b',
                                                    formats='u1, u1, u1')
        structured_base = np.core.records.fromarrays(self._result_arr.transpose(),
                                                     names='r, g, b',
                                                     formats='u1, u1, u1')
        structured_base.sort(order=[c for c in mode])

        mapped = misc.sort_map(src_structures, structured_base, order=[c for c in mode])
        shaped = np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE))

        return shaped.view('u1').reshape(shaped.shape + (-1,))

    def transform(self, mode: str = 'brightness') -> Image.Image:
        if mode == 'brightness':
            return Image.fromarray(self._sort_brightness())
        elif ''.join(sorted(mode)) == 'bgr':
            return Image.fromarray(self._sort_rgb(mode))

        raise ValueError('"mode" must be one of: ["brightness", "rgb"]')


def as_sorted(image: Image.Image, mode: str = 'brightness') -> Image.Image:
    sorter = ColourSorter(image)
    return sorter.transform(mode)
