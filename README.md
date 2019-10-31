## Colour Sort 

Generating Images using all 256<sup>3</sup> RGB colours, inspired by [https://allrgb.com/]

### Technique

To generate a re-coloured image, the source image's pixel data is sorted (using one of several different sorting modes) using numpy's `argsort` function, giving us a mapping from the original to the sorted version. This mapping is then used to "unsort" an array of all 256<sup>3</sup> colours that in sorted order. The result of this operation is then written out as our result.

#### Installing

Inside an activated virtualenv, and from the python folder of the project, run:
```
pip install -r requirements.txt
pip install .
```

### Running

Once the tool has been installed, it can be ran with the following command
```
Usage: colour generate [OPTIONS] FILE OUT

Options:
  --filetype [png|jpeg]
  --sorttype [brightness|rgb|rbg|grb|gbr|brg|bgr]
  --help                          Show this message and exit.
```

### Verifying

The repository also contains `verify.py`, which contains logic to check that an image is valid (uses all 256<sup>3</sup> colours with no dups). 
