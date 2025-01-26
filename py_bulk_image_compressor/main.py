#!/usr/bin/python
#
# 8888888b.                  888b     d888               888 d8b                  .d8888b.
# 888   Y88b                 8888b   d8888               888 Y8P                 d88P  Y88b
# 888    888                 88888b.d88888               888                     888    888
# 888   d88P 888  888        888Y88888P888  .d88b.   .d88888 888  8888b.         888         .d88b.  88888b.d88b.  88888b.  888d888 .d88b.  .d8888b  .d8888b   .d88b.  888d888
# 8888888P"  888  888        888 Y888P 888 d8P  Y8b d88" 888 888     "88b        888        d88""88b 888 "888 "88b 888 "88b 888P"  d8P  Y8b 88K      88K      d88""88b 888P"
# 888        888  888        888  Y8P  888 88888888 888  888 888 .d888888        888    888 888  888 888  888  888 888  888 888    88888888 "Y8888b. "Y8888b. 888  888 888
# 888        Y88b 888        888   "   888 Y8b.     Y88b 888 888 888  888        Y88b  d88P Y88..88P 888  888  888 888 d88P 888    Y8b.          X88      X88 Y88..88P 888
# 888         "Y88888        888       888  "Y8888   "Y88888 888 "Y888888         "Y8888P"   "Y88P"  888  888  888 88888P"  888     "Y8888   88888P'  88888P'  "Y88P"  888
#                 888                                                                                              888
#            Y8b d88P                                                                                              888
#             "Y88P"                                                                                               888
#
# github: https://github.com/georgekhananaev/py-image-compressor

import argparse
import concurrent.futures
import os
import time
from datetime import datetime

from py_bulk_image_compressor.components import mainClasses as mC, mainFunctions as mF, localColors as Color

# Measure number of CPU cores
n_cores = os.cpu_count()

if __name__ == '__main__':

    # Load config
    config = py_bulk_image_compressor.components.setConfigurations.get_resources()

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=str, required=True,
                        help='Set your location path, e.g.: -l "C:/original_images/"')
    parser.add_argument('-d', type=str, required=False,
                        help='Set your destination path, e.g.: -d "C:/new_images/"')
    parser.add_argument('-f', type=str, required=False, help="Set image format, e.g.: -f webp")
    parser.add_argument('-w', type=int, required=False, help="Max width, e.g.: -w 1920")
    parser.add_argument('-q', type=int, required=False, help="Quality, e.g.: -q 90")
    parser.add_argument('-r', type=str, required=False,
                        help="Remove if compressed is worse, e.g.: -r y")
    parser.add_argument('-rm', type=str, required=False,
                        help="Remove ALL metadata, e.g.: -rm y")
    args = parser.parse_args()

    # Default values
    default_max_width = mC.set_default_values(int(config['default_parameters']['max_width']), args.w)
    default_quality = mC.set_default_values(int(config['default_parameters']['quality']), args.q)
    default_format = mC.set_default_values(config['default_parameters']['format'], args.f)
    default_destination = mC.set_default_values(config['default_parameters']['destination'], args.d)

    remove_metadata = (args.rm and args.rm.lower() == 'y')

    start_time = time.time()

    # Build list
    image_list = [f for f in mF.build_file_list(args.l)]

    # Multi-core
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_cores) as executor:
        future_to_image = {
            executor.submit(
                mF.start_command,
                source_image=image,
                img_path=args.l,
                img_destination=default_destination.set,
                set_format=default_format.set,
                max_width=default_max_width.set,
                quality=default_quality.set,
                remove_meta=remove_metadata
            ): image for image in image_list
        }

        for future in concurrent.futures.as_completed(future_to_image):
            image = future_to_image[future]
            try:
                future.result()
            except Exception as exc:
                error_msg = f"[{datetime.now()}] ERROR processing {image}: {exc}\n"
                mF.log_message(config, "error", error_msg)
                print(error_msg)
            else:
                try:
                    file_name = os.path.basename(image)
                    _, _, after = image.partition(args.l)
                    new_img = os.path.splitext(
                        default_destination.set + after
                    )[0] + f".{default_format.set}"

                    # Possibly removed if bigger
                    if not os.path.exists(new_img):
                        continue

                    original_size = os.path.getsize(image)
                    new_size = os.path.getsize(new_img)
                    orig_kb = round(original_size / 1024, 2)
                    new_kb = round(new_size / 1024, 2)
                    size_diff = mF.get_percentage_difference(original_size, new_size)

                    image_size_is = f"Image {file_name} size: {orig_kb}KB, new size: {new_kb}KB"
                    if size_diff < 0:
                        # Worse compression
                        saved_size = f"{Color.select.FAIL}, worse by {size_diff}%{Color.select.ENDC}"
                        if args.r and args.r.lower() == "y":
                            # Remove if requested
                            os.remove(new_img)
                            warn_msg = f"[{datetime.now()}] WARNING removed bigger file: {new_img} (Diff: {size_diff}%)\n"
                            print(Color.select.WARNING + warn_msg + Color.select.ENDC)
                            mF.log_message(config, "warning", warn_msg)
                            continue
                    else:
                        saved_size = f"{Color.select.OKBLUE} saved {size_diff}%{Color.select.ENDC}"

                    output_msg = f"{image_size_is} {saved_size}"
                    print(output_msg)

                    # Log success
                    success_msg = f"[{datetime.now()}] SUCCESS: {image} -> {new_img}, " \
                                  f"Orig: {orig_kb}KB, New: {new_kb}KB, Diff: {size_diff}%\n"
                    mF.log_message(config, "success", success_msg)

                except Exception as err:
                    error_msg = f"[{datetime.now()}] ERROR finalizing {image}: {err}\n"
                    print(error_msg)
                    mF.log_message(config, "error", error_msg)

    end_time = time.time()

    print(f"{Color.select.BOLD}{Color.select.HEADER}Images saved to: {default_destination.set}")
    print(f"{mF.folder_size(default_destination.set)}")
    print(
        f"Processed {len(image_list)} images in {round(end_time - start_time, 2)} seconds{Color.select.ENDC}"
    )