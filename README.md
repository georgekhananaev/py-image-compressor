# Python Bulk Image Compressor + Resizer

## Overview

This Python script allows you to compress and resize images in bulk. It can optionally preserve EXIF metadata and file timestamps or remove them entirely if the `-rm y` flag is used.

### Features
- **Supports Multiple Formats:**
  - **Full Metadata Preservation:** JPEG, JPG, TIFF.
  - **Partial/No Metadata:** PNG, WEBP, BMP, etc., do not reliably store EXIF data.
- **Metadata Removal:** If `-rm y` is specified, all metadata (e.g., GPS, date/time, camera info) is stripped, and timestamps are reset instead of being copied from the source.
- **Logging:** Logs each compression operation in a `logs.txt` file. You can configure the maximum row limit for the log file in the `[logs]` section of `configurations.ini`. When the log file exceeds this limit, older rows are removed.

![Animation](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/animation.gif?raw=true)

---

### Installation
![Python Version](https://img.shields.io/badge/Python_3.11-Supported-green.svg)

1. Install [Python 3+](https://www.python.org/downloads/).
2. Install [Git](https://git-scm.com/).
3. Clone this repository:
   ```bash
   git clone https://github.com/georgekhananaev/py-image-compressor.git
   ```
4. Install dependencies:
   ```bash
   cd py-image-compressor
   pip install -r requirements.txt
   ```

---

### Usage

| Command | Required | Default Value   | Description           | Details                                                                                                                                   | Example                      |
|---------|----------|-----------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| **-l**  | Yes      | N/A             | Input location        | Path to the folder containing original images.                                                                                            | `-l "C:/Original Images/"` |
| **-d**  | No       | `/data/output/` | Output location       | Path where compressed images will be saved.                                                                                              | `-d "C:/Compressed Images/"` |
| **-w**  | No       | `1920`          | Max width             | Resize images to this maximum width while maintaining aspect ratio.                                                                       | `-w 1920`                   |
| **-q**  | No       | `80`            | Quality               | Image quality (percentage). Lower values save more space.                                                                                 | `-q 80`                     |
| **-f**  | No       | `jpeg`          | Output format         | Supported formats: PNG, JPEG, JPG, PPM, GIF, TIFF, BMP, WEBP, HEIC, HEIF, AVIF. Refer to [Pillow Documentation](https://pillow.readthedocs.io/). | `-f jpeg`                   |
| **-r**  | No       | `no`            | Remove larger files   | If set to `y`, deletes compressed images if they are larger than the original.                                                            | `-r y`                      |
| **-rm** | No       | `no`            | Remove metadata       | If set to `y`, removes all metadata (EXIF, GPS, etc.) and resets timestamps.                                                              | `-rm y`                     |
| **-h**  | No       | -               | Help                  | Displays help information about commands.                                                                                                | `-h` or `--help`            |

> **Note:** Use quotation marks for paths with spaces (e.g., `"C:/My Folder/"`).

---

### Logging

- A `logs.txt` file is created/appended in the script's directory.
- Maximum rows are configured in `[logs] max_rows`. Older entries are pruned when the limit is exceeded.
- Log levels:
  - `log_success`
  - `log_errors`
  - `log_warnings`
- Enable or disable logging levels in `configurations.ini`.

---

### Examples

```bash
python main.py -l "D:/Images/Originals/" -d "D:/Images/Compressed/" -f webp -w 500 -q 80 -rm y
```

Example output:

![Terminal Screenshot](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/screenshot.jpg?raw=true)

---

## Updates

### **26/01/2025**
1. EXIF metadata is preserved if supported by the output format (e.g., JPEG).
2. Added support for `.avif` format (requires `pillow-avif-plugin`).
3. Minor speed optimizations for faster compression.
4. Updated `requirements.txt` with the latest package versions.

### **02/12/2023**
1. Automatic detection and handling of RGB/RGBA channels.
2. Thanks to "ZenithVal" for the suggestion.

### **06/04/2023**
1. Updated `README.md`.
2. Updated `requirements.txt` with the latest package versions.

### **12/12/2022**
1. Introduced a `resources` folder containing `configurations.ini` for storing program settings.
2. Set up future GUI plans using `customtkinter`.
3. Removed PySimpleGUI from dependencies.

### **06/12/2022**
1. Default values added for `-d`, `-f`, and `-q` options. You can run:
   ```bash
   python main.py -l "C:/Your Folder/"
   ```
   Defaults: JPEG format, 80% quality, 1920px max width, `/data/output/` as the destination folder.
2. Simplified the code using `*args` and `**kwargs`.

### **05/12/2022**
1. Added support for `.heif` and `.heic` formats (e.g., iPhone photos).
2. Updated `requirements.txt` to include `pillow-heif`.

### **04/12/2022**
1. Improved output to display the actual size saved for each image.
2. Enhanced terminal output for better visualization of size savings.
3. Began GUI development for Windows and Ubuntu.
4. Added `-r y` to skip retaining larger compressed images.

---

#### Future Plans
- A GUI interface will be added if this project receives 50+ stars on GitHub.
- Integration with cloud storage services like AWS S3 and Google Drive for automatic uploads.
- Support for more advanced image editing options, such as cropping and watermarking.

> **Personal Note:** I use this script for compressing images for React-based websites and converting entire folders to WebP format with a single command.

---

## Contributing 🤝

We’d love your help to make py-image-compressor even better! To contribute:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add awesome feature"`.
4. Push your branch: `git push origin feature-name`.
5. Open a pull request and tell us about your changes.

---

## License

py-image-compressor is licensed under the MIT License. See the `LICENSE` file for details.

---

## Need Help?

If you run into any issues or have questions, feel free to [open an issue](https://github.com/georgekhananaev/py-image-compressor/issues).


## Support Me

If you find my work helpful, consider supporting me by buying me a coffee at [Buy Me A Coffee](https://www.buymeacoffee.com/georgekhananaev).
Your support helps me continue to create and maintain useful projects.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/georgekhananaev)

Thank you!
