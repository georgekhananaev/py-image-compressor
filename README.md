# Python Bulk Image Compressor + Resizer
![animation](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/animation.gif?raw=true)


### Basics
![Generic badge](https://img.shields.io/badge/Python_3.11-Supported-green.svg)

1. Install [Python 3+](https://www.python.org/downloads/)
2. Install [requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/)


### Command line usage:

```
python main.py -l <Your Location> -d <Your Destination> -f <File Format> -w <Max Width> -q <Max Quality> -r <Remove Larger Files>
```

Options: 
* -l = location
* -d = destination
* -w = max width
* -q = quality 
* -f = format (supported formats: webp, jpeg, png, gif, tiff) for more check[ PIL Documentation](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
* -r = (optional), won't keep new images if become larger size. Usage: `-r y` (y for yes, no is default)

**Example:**

COMMAND:

```
python main.py -l D:/Programming/React/resume-website/ -d ./data/out/ -f webp -w 500 -q 100
```

OUTPUT:
![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/screenshot.jpg?raw=true)

## Updates:

**04/12/2022 👇️**
> 1. Added multicore image processing, now this is nearly 10 times faster.
> ![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/multicore.gif?raw=true)
> 2. Better output for each image, you can see how much size you actually saved.
> 3. Started working on the GUI interface, will be executable at least on Windows/Ubuntu.
> 4. new command -r y, to avoid keeping larger compression images


## ---- UNDER DEVELOPMENT ----

Discussion is opened. Leave your suggestions. Will be considered seriously!
#### GUI interface, will be added soon...

