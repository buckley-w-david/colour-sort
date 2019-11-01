import argparse
import itertools
import sys
import typing

from PIL import Image
from colour_sort import image

def main(infile, outfile, sort_type):
    input_image = Image.open(infile)
    mode = image.SortType.from_str(sort_type)

    generated = image.create_sorted_image(input_image, mode=mode)
    generated.save(outfile)

parser = argparse.ArgumentParser()
parser.add_argument('infile')
parser.add_argument('outfile')
parser.add_argument('--sort', default='brightness', choices=[mode.name.lower() for mode in image.SortType])
args = parser.parse_args()
main(args.infile, args.outfile, args.sort)
