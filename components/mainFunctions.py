#!/usr/bin/python
from components import imageCompressor as iC
from pathlib import Path
import os

# 👇️ supported source formats, you can add more formats if supported by PIL here.
support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]


# 👇️ building file list structure with generator
def build_file_list(your_folder):
    for root, dirs, files in os.walk(your_folder):
        for file_bfl in files:
            if os.path.splitext(file_bfl)[1].lower() in support_formats:
                yield os.path.join(root, file_bfl)


# 👇️ creating folder if not exist
def create_folder(your_path):
    if os.path.exists(your_path) is False:
        os.makedirs(your_path)


# 👇️ return folder size value as string
def folder_size(your_folder):
    folder_size_is = sum(file.stat().st_size for file in Path(your_folder).rglob('*')) / 1024
    return f"Total folder size is: {round(folder_size_is, 2)}.KB"


# getting percent difference between two numbers
def get_percentage_difference(num_a, num_b):
    # 👇️ use abs() function to always get positive number
    if num_b > num_a:
        return -round((abs(num_b - num_a) / num_b) * 100, 2)
    else:
        return round((abs(num_a - num_b) / num_b) * 100, 2)


# 👇️ editing single image
def start_command(image: str, original_folder: str, output_folder: str, dformat: str, max_width: int, quality: int):
    filedir_with_extension = image
    before, sep, after = image.partition(original_folder)
    try:
        create_folder(output_folder + os.path.dirname(after))
    except Exception as Err:
        # 👇️ this fix a problem which skips files, when if condition fails to detect a folder. it tries to recreate it due to multicore processing.
        _ = Err
        pass

    final_file_path = output_folder + after.replace(os.path.splitext(after)[1], '') + f".{dformat}"

    iC.compress_resize_image(filedir_with_extension, final_file_path, dformat, max_width=max_width, quality=quality)

    return image
