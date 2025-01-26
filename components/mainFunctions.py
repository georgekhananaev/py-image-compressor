#!/usr/bin/python
import os
import shutil
from pathlib import Path
from datetime import datetime

from components import imageCompressor as iC, setConfigurations

config = setConfigurations.get_resources()

LOG_FILE = "logs.txt"


def build_file_list(your_folder) -> dir:
    """
    Builds a generator of files from 'your_folder' that match any of the
    supported formats in 'configurations.ini'.
    """
    for root, dirs, files in os.walk(your_folder):
        for file_bfl in files:
            if os.path.splitext(file_bfl)[1].lower() in config['supported_formats'].values():
                yield os.path.join(root, file_bfl)


def create_folder(your_path) -> None:
    """Creates a folder if it does not exist."""
    if not os.path.exists(your_path):
        os.makedirs(your_path)


def folder_size(your_folder) -> str:
    """Returns a string representing total folder size in KB."""
    if not os.path.exists(your_folder):
        return "Total folder size: 0 KB"

    total_size_kb = sum(
        file.stat().st_size for file in Path(your_folder).rglob('*') if file.is_file()
    ) / 1024
    return f"Total folder size: {round(total_size_kb, 2)} KB"


def get_percentage_difference(num_a, num_b) -> float:
    """
    Positive if compressed is smaller, negative if compressed is larger.
    """
    if num_b == 0:
        return 0.0
    if num_b >= num_a:
        return -round((abs(num_b - num_a) / num_b) * 100, 2)
    else:
        return round((abs(num_a - num_b) / num_b) * 100, 2)


def start_command(**kwargs) -> None:
    """
    1) Creates destination folder.
    2) Compresses/resizes.
    3) Copies timestamps (unless remove_meta == True).
    """
    src_image = kwargs['source_image']
    before, sep, after = src_image.partition(kwargs['img_path'])

    try:
        create_folder(kwargs['img_destination'] + os.path.dirname(after))
    except Exception: # noqa
        pass

    new_file_path = (
        kwargs['img_destination']
        + after.replace(os.path.splitext(after)[1], '')
        + f".{kwargs['set_format']}"
    )

    # Compress
    iC.compress_resize_image(
        image_location=kwargs['source_image'],
        image_destination=new_file_path,
        set_format=kwargs['set_format'],
        max_width=kwargs['max_width'],
        quality=kwargs['quality'],
        remove_meta=kwargs.get('remove_meta', False)
    )

    # If removing metadata, skip copying timestamps
    if not kwargs.get('remove_meta', False):
        if os.path.exists(new_file_path):
            try:
                shutil.copystat(src_image, new_file_path)
            except Exception as e:
                log_message(
                    config,
                    "error",
                    f"[{datetime.now()}] ERROR copying timestamps {new_file_path}: {e}\n"
                )


def log_message(config, log_type: str, message: str): # noqa
    """
    Logs a message if the corresponding log_<type> is True in config.
    The log types are "success", "warning", "error".
    """
    # read booleans from config
    max_rows = int(config['logs']['max_rows'])

    # For safety, using getboolean
    log_success = config['logs'].getboolean('log_success')
    log_errors = config['logs'].getboolean('log_errors')
    log_warnings = config['logs'].getboolean('log_warnings')

    if log_type == "success" and not log_success:
        return
    if log_type == "warning" and not log_warnings:
        return
    if log_type == "error" and not log_errors:
        return

    log_path = os.path.join(os.getcwd(), LOG_FILE)

    # Append log
    try:
        with open(log_path, 'a', encoding='utf-8') as file:
            file.write(message)
    except Exception as e:
        print(f"Cannot write to log file: {e}")
        return

    # Now enforce max_rows limit
    try:
        with open(log_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) > max_rows:
            new_lines = lines[-max_rows:]
            with open(log_path, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
    except Exception as e:
        print(f"Error trimming log file: {e}")