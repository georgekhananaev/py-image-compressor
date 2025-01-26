# Python Bulk Image Compressor + Resizer

## Overview
The Python Bulk Image Compressor + Resizer is a command-line tool that simplifies the process of compressing and resizing images in bulk. This tool is designed to handle large batches of images efficiently, while allowing you to control various aspects of the compression process, such as quality, output format, and metadata preservation.

### Features
- **Ease of Use:** Intuitive CLI commands for fast and simple operations.
- **Customizable:** Configure options like image quality, format, maximum width, and metadata handling.
- **Metadata Management:** Preserve or strip EXIF data such as GPS location, camera settings, and timestamps.
- **Supported Formats:** Wide compatibility with popular image formats, including advanced formats like AVIF and HEIF.
- **Performance:** Built-in multithreading for faster processing of large image batches.
- **Logs:** Comprehensive logging for operation tracking, configurable via `configurations.ini`.
- **Extensibility:** Future-ready for GUI development and cloud integration.

![Animation](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/animation.gif?raw=true)

---

## Installation

### **Option 1: Install via PyPI**

For a simplified installation process, the package is available on PyPI:

```bash
pip install py-bulk-image-compressor
```

> **Note:** Python version **3.10 or higher** is required. (Older versions may work but are not officially supported.)

---

### **Option 2: Manual Installation**

1. Install [Python 3+](https://www.python.org/downloads/).
2. Install [Git](https://git-scm.com/).
3. Clone the repository:
   ```bash
   git clone https://github.com/georgekhananaev/py-image-compressor.git
   ```
4. Navigate to the project directory and install dependencies:
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

#### **26/01/2025**
1. EXIF metadata is preserved if supported by the output format (e.g., JPEG).
2. Added support for `.avif` format (requires `pillow-avif-plugin`).
3. Minor speed optimizations for faster compression.
4. Updated `requirements.txt` with the latest package versions.
5. Added logs, which is exported to logs.txt
6. Added tests, use 
    ```shell
      pytest --maxfail=1 --disable-warnings -v
    ```

#### **02/12/2023**
1. Automatic detection and handling of RGB/RGBA channels.
2. Thanks to "ZenithVal" for the suggestion.

#### **06/04/2023**
1. Updated `README.md`.
2. Updated `requirements.txt` with the latest package versions.

#### **12/12/2022**
1. Introduced a `resources` folder containing `configurations.ini` for storing program settings.
2. Set up future GUI plans using `customtkinter`.
3. Removed PySimpleGUI from dependencies.

#### **06/12/2022**
1. Default values added for `-d`, `-f`, and `-q` options. You can run:
   ```bash
   python main.py -l "C:/Your Folder/"
   ```
   Defaults: JPEG format, 80% quality, 1920px max width, `/data/output/` as the destination folder.
2. Simplified the code using `*args` and `**kwargs`.

#### **05/12/2022**
1. Added support for `.heif` and `.heic` formats (e.g., iPhone photos).
2. Updated `requirements.txt` to include `pillow-heif`.

#### **04/12/2022**
1. Improved the output to display the actual size saved for each image, with full multithreading conversion support.
    > ![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/multicore.gif?raw=true)
2. Enhanced terminal output for better visualization of size savings.
3. Began GUI development for Windows and Ubuntu.
4. Added `-r y` to skip retaining larger compressed images.

---

### Future Plans
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
