import enum
from functools import partial

import numpy as np
from PIL import Image, ImageCms
from colour_sort import misc, sort_type

IMAGE_SIZE = 4096

def _rgb_to_lab(image):
    # Convert the image to LAB colour space - https://stackoverflow.com/a/53353542
    srgb_p = ImageCms.createProfile("sRGB")
    lab_p  = ImageCms.createProfile("LAB")

    rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
    return ImageCms.applyTransform(image, rgb2lab)

# image needs to be in LAB colour space
def _sort_brightness(image, result):
    return image[:,0], result[:,0]


def _sort_avg(image, result):
    return np.sum(image, axis=1), np.sum(result, axis=1)


def _sort_rgb(mode, image, result):
    if sort_type.is_clip(mode):
        # Originally this was a bug, since this allows the results of the left shifts to overflow
        # but I'm keeping it because I like the images it results in
        res_r, res_g, res_b = result.transpose()
        src_r, src_g, src_b = image.transpose()
    else:
        res_r, res_g, res_b = result.astype(np.uint32).transpose()
        src_r, src_g, src_b = image.astype(np.uint32).transpose()

    mode = sort_type.unclip(mode)

    # TODO better logic
    if mode is sort_type.SortType.RGB:
        combined_res = (res_r << 16) | (res_g << 8) | res_b
        combined_src = (src_r << 16) | (src_g << 8) | src_b
    elif mode is sort_type.SortType.RBG:
        combined_res = (res_r << 16) | (res_b << 8) | res_g
        combined_src = (src_r << 16) | (src_b << 8) | src_g
    elif mode is sort_type.SortType.BRG:
        combined_res = (res_b << 16) | (res_r << 8) | res_g
        combined_src = (src_b << 16) | (src_r << 8) | src_g
    elif mode is sort_type.SortType.BGR:
        combined_res = (res_b << 16) | (res_g << 8) | res_r
        combined_src = (src_b << 16) | (src_g << 8) | src_r
    elif mode is sort_type.SortType.GBR:
        combined_res = (res_g << 16) | (res_b << 8) | res_r
        combined_src = (src_g << 16) | (src_b << 8) | src_r
    elif mode is sort_type.SortType.GRB:
        combined_res = (res_g << 16) | (res_r << 8) | res_b
        combined_src = (src_g << 16) | (src_r << 8) | src_b

    return combined_src, combined_res


def _sorted_image(image, map_func, mode='RGB'):
    result = misc.generate_all_colours()

    criteria_image, criteria_result = map_func(image, result)
    results_sorted = result[np.argsort(criteria_result)]

    mapped = misc.sort_map(criteria_image, results_sorted)
    return Image.fromarray(np.reshape(mapped, (IMAGE_SIZE, IMAGE_SIZE, 3)), mode=mode)


def create_sorted_image(image: Image.Image, mode: sort_type.SortType) -> Image.Image:
    image = image.convert('RGB')
    result_mode = 'RGB'

    if mode is sort_type.SortType.BRIGHTNESS:
        image = _rgb_to_lab(image)
        map_func = _sort_brightness
        result_mode = 'LAB'
    elif mode is sort_type.SortType.AVG:
        map_func = _sort_avg
    else:
        map_func = partial(_sort_rgb, mode)

    reshaped = misc.reshape_image(image)
    return _sorted_image(reshaped, map_func, result_mode)
