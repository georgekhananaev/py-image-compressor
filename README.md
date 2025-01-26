# Python Bulk Image Compressor

[![PyPI](https://img.shields.io/pypi/v/py-bulk-image-compressor.svg)](https://pypi.org/project/py-bulk-image-compressor/)
[![Python Versions](https://img.shields.io/pypi/pyversions/py-bulk-image-compressor.svg)](https://pypi.org/project/py-bulk-image-compressor/)

**py-bulk-image-compressor** is a user-friendly CLI tool for compressing and resizing images in bulk. It offers extensive options for managing image quality, format, and metadata while maintaining fast, efficient performance.

![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/multicore.gif?raw=true)

### Key Features

- **Supports Multiple Formats:** JPEG, PNG, WEBP, AVIF, HEIF, and more.
- **Metadata Handling:** Choose whether to preserve or remove EXIF data.
- **Multicore Processing:** Utilizes all available CPU cores.
- **Flexible Settings:** Customize output quality, max width, and destination directory.

## Installation

### From PyPI

```bash
pip install py-bulk-image-compressor
```

> **Requires Python 3.10+**

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/georgekhananaev/py-image-compressor.git
   cd py-image-compressor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install locally:
   ```bash
   pip install .
   ```
4. Run the CLI:
   ```bash
   py-bulk-image-compressor -h
   ```

## Usage

After installation, you can run:

```bash
py-bulk-image-compressor -h
```

### Example Commands

1. **Basic compression and resize**:
   ```bash
   py-bulk-image-compressor -l "path/to/original_images" -d "path/to/output"
   ```
   Uses default format (`jpeg`), quality=80, max_width=1920px.

2. **Specific format and quality**:
   ```bash
   py-bulk-image-compressor -l "path/to/original_images" \
       -d "path/to/output" -f webp -w 800 -q 70
   ```
   
3. **Remove metadata & skip larger compressed files**:
   ```bash
   py-bulk-image-compressor -l "path/to/original_images" \
       -d "path/to/output" -rm y -r y
   ```

Logs are saved to logs.txt in the current cmd/terminal working directory. Installation & Usage screenshot below:

![terminal](https://github.com/georgekhananaev/py-image-compressor/blob/main/screenshots/usage_example_pypi.png?raw=true)


### Command-Line Options

| Option | Required | Default Value       | Description                                                            |
|-------:|:--------:|:-------------------:|:-----------------------------------------------------------------------|
| `-l`   | **Yes**  | *(No Default)*      | Input directory for original images. *(Example: `-l "C:/images/"`)*    |
| `-d`   | No       | `/data/output/`     | Output directory for compressed images.                                |
| `-f`   | No       | `jpeg`              | Output format (e.g., `webp`, `png`, `avif`).                           |
| `-w`   | No       | `1920`              | Maximum width (px).                                                    |
| `-q`   | No       | `80`                | Image quality (0-100).                                                 |
| `-r`   | No       | `n` (off)           | Remove compressed if it’s larger than the original (`-r y`).           |
| `-rm`  | No       | `n` (off)           | Remove all metadata (`-rm y`).                                         |

---

## Logging

- Generates or appends to a `logs.txt` file in your current working directory.
- The `configurations.ini` file controls log settings (e.g., `max_rows`).

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add awesome feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request on GitHub.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Questions or Issues?

- [Open an issue](https://github.com/georgekhananaev/py-image-compressor/issues) on GitHub
- Contributions, suggestions, and bug reports are welcome!

---

## Support

If you find this tool helpful, consider supporting:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/georgekhananaev)

Your support helps me continue to create and maintain useful projects.


---

## Updates

#### **27/01/2025**
1. Deployed to pypi, **installation**:
    ```shell
      pip install py-bulk-image-compressor
    ```
   **usage**:
    ```shell
      py-bulk-image-compressor -h
    ```

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
   ```
   python main.py -l "C:/Your Folder/"
   ```
   Defaults: JPEG format, 80% quality, 1920px max width, `/data/output/` as the destination folder.
2. Simplified the code using `*args` and `**kwargs`.

#### **05/12/2022**
1. Added support for `.heif` and `.heic` formats (e.g., iPhone photos).
2. Updated `requirements.txt` to include `pillow-heif`.

#### **04/12/2022**
1. Improved the output to display the actual size saved for each image, with full multithreading conversion support.
2. Enhanced terminal output for better visualization of size savings.
3. Began GUI development for Windows and Ubuntu.
4. Added `-r y` to skip retaining larger compressed images.

---

