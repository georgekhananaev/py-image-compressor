import glob
from PIL import Image
import os
import gc

support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]

all_files = glob.glob("../data/*")


def get_all_supported_files(path):
    glob.glob(path)
    temporary_memory = []
    for file in all_files:
        file_location, file_extension = os.path.splitext(file)
        if file_extension.lower() in support_formats:
            temporary_memory.append(file)
    return temporary_memory


def compress_resize_image(file_location, output_location, file_type, max_width=800, optimize=True, quality=80):
    try:
        with Image.open(file_location) as im:
            im = im.convert('RGB')
            new_width = im.height / max_width
            w, h = int(im.width // new_width), int(im.height // new_width)
            print(f"will be resized to: {w, h}")
            im_resized = im.resize((w, h))
            im_resized.save(output_location, file_type, optimize=quality, quality=quality)
            print("done")

    except Exception as Err:
        gc.collect()
        print(Err)


all_supported_files = get_all_supported_files("../data/*")

# cleaning memory after passing the function into a list
del all_files

compress_resize_image(all_supported_files[0], "output.WEBP", "WEBP", quality=80)

# releasing all memory
gc.collect()


# # progress bar example
# for i in tqdm(range(10)):
#     sleep(3)
