![Version](https://img.shields.io/badge/Python%203+-Supported-brightgreen)

# Python Bulk Image Compressor + Resizer
![alt text](https://github.com/georgekhananaev/py-image-compressor/blob/main/animation.gif?raw=true)


### Basics
1. Install [Python 3+](https://www.python.org/downloads/)
2. Install [requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/)


### Command line usage:

```
python main.py -l <Your Location> -d <Your Destination> -f <File Format> -w <Max Width> -q <Max Quality>
```

Options: 
* -l = location
* -d = destination
* -w = max width
* -q = quality 
* -f = format (supported formats: webp, jpeg, png, gif, tiff) for more check[ PIL Documentation](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

**Example:**

COMMAND:

```
python main.py -l D:/Programming/React/resume-website/ -d ./data/out/ -f webp -w 500 -q 100
```

OUTPUT:
![alt text](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshot.jpg?raw=true)


## ---- UNDER DEVELOPMENT ----

Discussion is opened. Leave your suggestions. Will be considered seriously!


#### GUI interface, will be added soon...

