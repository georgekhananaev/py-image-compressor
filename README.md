# Python Bulk Image Compressor + Resizer

![animation](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/animation.gif?raw=true)

### Basics

![Generic badge](https://img.shields.io/badge/Python_3.11-Supported-green.svg)

1. Install [Python 3+](https://www.python.org/downloads/)
2. Install [git](https://github.com/georgekhananaev/py-image-compressor)
3. Clone this repository: ```git clone https://github.com/georgekhananaev/py-image-compressor.git```
4. Install [requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/), cd into main folder and
   type: ```pip install -r requirements.txt```

### Usage:

| Command |  Weight  | Default Values |   Meaning   | Details                                                                                                                                                                                                                 |        Usage example         |
|:-------:|:--------:|:--------------:|:-----------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------:|
| **-l**  | required |      N/A       |  location   | your images path, where your original images located.                                                                                                                                                                   |  `-l "C:/Original Images/"`  |
| **-d**  | optional | /data/output/  | destination | your destination path, compressed images will be saved here                                                                                                                                                             | `-d "C:/Compressed Images/"` |
| **-w**  | optional |      1920      |  max width  | if larger resolution will be set to max width without breaking the image ratio                                                                                                                                          |          `-w 1920`           |
| **-q**  | optional |       80       |   quality   | images quality by percentage.<br/>lower quality to save more space                                                                                                                                                      |           `-q 80`            |
| **-f**  | optional |      jpeg      |   format    | supported format ".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp", ".heic", ".heif" <br/>for more check [PIL Documentation](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html). |          `-f jpeg`           |
| **-r**  | optional |       no       |   remove    | remove images from destination path, <br/>if compression is worst than original file.                                                                                                                                   |            `-r y`            |
| **-h**  |    -     |       -        |    help     | if you forgot what command you want to use can write python main.py --help                                                                                                                                              |        `-h or --help`        |

_Import: for -l and -d, use quotation marks if have spaces._

**Examples:**

```
python main.py -l <Your Location> -d <Your Destination> -f <File Format> -w <Max Width> -q <Max Quality> -r <Remove Larger Files>
```

COMMAND:

```
python main.py -l "D:/Programming/React/resume-website/" -d "./data/out/" -f webp -w 500 -q 100
```

OUTPUT:
![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/screenshot.jpg?raw=true)

## Updates:

**02/12/2023 👇**
> 1. Add a condition in the imageCompressor for automatic RGB and RGBA detection and selection. Thanks to "ZenithVal" for the suggestion.

**06/04/2023 👇**
> 1. Updated readme.md.
> 2. Updated requirements.txt with latest versions packages.

**12/12/2022 👇️**
> 1. Added a 'resources' folder containing a configurations.ini file to store all program settings. This change sets the stage for an upcoming GUI interface with memory.
> 2. Removed PySimpleGUI from dependencies; instead, we will use customtkinter for a modern-looking GUI.

**06/12/2022 👇️**
> 1. Default values have been added for the -d, -f, and -q options, making them no longer required fields. You can execute the code simply by typing: python main.py -l "C:/Your Folder/". The default values are as follows: JPEG format, 80% quality, maximum width of 1080p, and the destination folder is set to /data/output/_
> 2. Simplified the code using *args and **kwargs.

**05/12/2022 👇️**
> 1. Added support for .heif and .heic formats, so now you can convert photos from your iPhone as well.
> 2. Updated requirements.txt to include PySimpleGUI (for future implementations) and pillow-heif.

**04/12/2022 👇️**
> 1. Improved the image processing output to display the actual amount of size saved for each image.
     > ![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/multicore.gif?raw=true)
> 2. Better output for each image, you can see how much size you actually saved.
> 3. I have started developing the GUI interface, which will be executable on both Windows and Ubuntu.
> 4. I've added a new command -r y to prevent retaining larger compressed images.


#### GUI interface will be added if this project receives at least 50 stars...
- Due to my busy schedule, I will continue development only if there is substantial demand.
- If you encounter any bugs, please feel free to open an issue.
- Personally, I use this script to compress images for React-based websites and convert entire folders to WebP format with a single command.

