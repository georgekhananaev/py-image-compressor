from components import imageCompressor as iC, localColors as Color
from pathlib import Path
from tqdm import tqdm
import argparse
import os
import time


# supported source formats, you can add more formats if supported by PIL here.
support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]


# building file list structure with generator
def build_file_list(your_folder):
    for root, dirs, files in os.walk(your_folder):
        for file_bfl in files:
            if os.path.splitext(file_bfl)[1].lower() in support_formats:
                yield os.path.join(root, file_bfl)


# creating folder if not exist
def create_folder(your_path):
    if os.path.exists(your_path) is False:
        os.makedirs(your_path)


# return folder size value as string
def folder_size(your_folder):
    return f"{Color.select.OKGREEN}Total folder size is:{Color.select.ENDC} {Color.select.WARNING}{sum(file.stat().st_size for file in Path(your_folder).rglob('*')) / 1024}.KB{Color.select.ENDC}"


# starting the loop single threaded
def start_command(original_folder, output_folder: str, dformat: str, max_width: int, quality: int):
    os.system('cls')

    # process bar handler
    pbar = tqdm([file for file in build_file_list(original_folder)])

    # looping supported file list creating missing folders and converting it.
    zero = 0  # zero value for a counter for files.

    for file in pbar:
        filedir_with_extension = file
        before, sep, after = file.partition(original_folder)
        create_folder(output_folder + os.path.dirname(after))

        zero += 1

        # final image path example output > /data/pic/my_pic.webp
        final_file_path = output_folder + after.replace(os.path.splitext(after)[1], '') + f".{dformat}"
        pbar.set_description(
            f"{Color.select.OKBLUE}Image {zero} out of {len(pbar)}{Color.select.ENDC} ")

        iC.compress_resize_image(filedir_with_extension,
                                 final_file_path, dformat,
                                 max_width=max_width, quality=quality)
    print(f"{Color.select.OKCYAN}Images saved to: {output_folder}{Color.select.ENDC}")
    print(folder_size(output_folder))


if __name__ == '__main__':
    time_start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=str, required=True)
    parser.add_argument('-d', type=str, required=True)
    parser.add_argument('-f', type=str, required=True)
    parser.add_argument('-w', type=int, required=True)
    parser.add_argument('-q', type=int, required=True)
    args = parser.parse_args()

    start_command(args.l, args.d, dformat=args.f, max_width=args.w, quality=args.q)  # noqa
    # terminal: python3 main.py -l "D:/Programming/React/resume-website/", -d "./data/out/", -f webp,  -w 300, -q 90

    time_end = time.time()

    print(f"Finished in: {round(time_end - time_start, 2)} Seconds ({round(time_end - time_start)})")
    # throw memory for test purposes.
    iC.gc.collect()

    # once finished exit app.
    exit()