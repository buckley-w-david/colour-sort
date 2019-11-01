import argparse
import itertools
import sys
import typing

from PIL import Image
from colour_sort import image, verify

def generate_image(args):
    infile = args.infile
    outfile = args.outfile
    sort_type = args.sort

    input_image = Image.open(infile)
    mode = image.SortType.from_str(sort_type)

    generated = image.create_sorted_image(input_image, mode=mode)
    generated.save(outfile)


def verify_image(args):
    infile = args.infile
    input_image = Image.open(infile)
    valid = verify.verify_image(input_image)
    if valid:
        print('%s is a valid allrgb image!' % infile)
    else:
        print('%s is not a valid allrgb image' % infile)


def run():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    generate_parser = subparsers.add_parser('generate')
    generate_parser.add_argument('infile')
    generate_parser.add_argument('outfile')
    generate_parser.add_argument('--sort', default='brightness', choices=[mode.name.lower() for mode in image.SortType])
    generate_parser.set_defaults(func=generate_image)

    verify_parser = subparsers.add_parser('verify')
    verify_parser.add_argument('infile')
    verify_parser.set_defaults(func=verify_image)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    run()
