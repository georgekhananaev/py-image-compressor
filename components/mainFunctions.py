#!/usr/bin/python
from components import imageCompressor as iC, setConfigurations
from pathlib import Path
import os

# 👇️ supported source formats, you can add more formats if supported by PIL here.
# support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp", ".heic", ".heif"]
config = setConfigurations.get_resources()

# 👇️ building file list structure with generator
def build_file_list(your_folder) -> dir:
    for root, dirs, files in os.walk(your_folder):
        for file_bfl in files:
            if os.path.splitext(file_bfl)[1].lower() in config['supported_formats'].values():
                yield os.path.join(root, file_bfl)


# 👇️ creating folder if not exist
def create_folder(your_path) -> None:
    if os.path.exists(your_path) is False:
        os.makedirs(your_path)


# 👇️ return folder size value as string
def folder_size(your_folder) -> str:
    folder_size_is = sum(file.stat().st_size for file in Path(your_folder).rglob('*')) / 1024
    return f"Total folder size is: {round(folder_size_is, 2)}.KB"


# getting percent difference between two numbers
def get_percentage_difference(num_a, num_b) -> round:
    # 👇️ use abs() function to always get positive number
    if num_b > num_a:
        return -round((abs(num_b - num_a) / num_b) * 100, 2)
    else:
        return round((abs(num_a - num_b) / num_b) * 100, 2)


# 👇️ editing single image
def start_command(**kwargs) -> None:
    before, sep, after = kwargs['source_image'].partition(kwargs['img_path'])
    try:
        create_folder(kwargs['img_destination'] + os.path.dirname(after))
    except Exception as Err:
        # 👇️ this fix a problem which skips files, when if condition fails to detect a folder. it tries to recreate it due to multicore processing.
        _ = Err
        pass
    new_file_path = kwargs['img_destination'] + after.replace(os.path.splitext(after)[1], '') + f".{kwargs['set_format']}"
    iC.compress_resize_image(image_location=kwargs['source_image'], image_destination=new_file_path, set_format=kwargs['set_format'], max_width=kwargs['max_width'], quality=kwargs['quality'])
