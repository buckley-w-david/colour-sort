import numpy as np

try:
    import importlib.resource as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

# FIXME duplicate constant
IMAGE_SIZE = 4096
TOTAL_PIXELS = IMAGE_SIZE*IMAGE_SIZE

def sort_map(src: np.ndarray, mapped: np.ndarray, order = None) -> np.ndarray:
    if order is not None:
        mapping = np.argsort(src)
    else:
        mapping = np.argsort(src, order=order)
    reverse_mapping = np.argsort(mapping)

    return mapped[reverse_mapping]


def reshape_image(image):
    new_width, new_height = IMAGE_SIZE, IMAGE_SIZE

    thumb = image.resize((new_width, new_height))
    return np.reshape(np.array(thumb), (TOTAL_PIXELS, 3))

def generate_all_colours():
    with pkg_resources.open_binary('colour_sort', 'all.npy') as colours:
        return np.load(colours)
