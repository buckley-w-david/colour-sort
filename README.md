## Colour Sort 

Generating Images using all 256<sup>3</sup> RGB colours, inspired by https://allrgb.com/

### Technique

To generate a re-coloured image, the source image's pixel data is sorted (using one of several different sorting modes) using numpy's `argsort` function, giving us a mapping from the original to the sorted version. This mapping is then used to "unsort" an array of all 256<sup>3</sup> colours that in sorted order. The result of this operation is then written out as our result.

### Installing

```
$ pip install colour_sort
```

### Running

Once the tool has been installed, it can be ran with the following command
```
$ colour generate --help
                                                                                
 Usage: colour generate [OPTIONS] SOURCE DEST                                   
                                                                                
 Generate an allRGB image                                                       
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    source      PATH  [default: None] [required]                            │
│ *    dest        PATH  [default: None] [required]                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --method              [brightness|average|abc|ac  [default: brightness]      │
│                       b|bac|bca|cab|cba|abcc|acb                             │
│                       c|bacc|bcac|cabc|cbac|z-or                             │
│                       der|pca]                                               │
│ --colour-space        [rgb|lab|hsv]               [default: rgb]             │
│ --converter           [PIL|cv2|scikit-image]      [default: PIL]             │
│ --help                                            Show this message and      │
│                                                   exit.                      │
╰──────────────────────────────────────────────────────────────────────────────╯


$ colour verify --help
                                                                                
 Usage: colour verify [OPTIONS] SOURCE                                          
                                                                                
 Verify that an image contains all RGB values                                   
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    source      PATH  [default: None] [required]                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
```
