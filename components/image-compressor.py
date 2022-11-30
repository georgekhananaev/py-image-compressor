import glob
from PIL import Image
import os
import gc

support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]
original_folder = "../data/*"
desired_format = "webp"

all_supported_files = [os.path.splitext(file) for file in glob.glob(original_folder) if os.path.splitext(file)[1].lower() in support_formats]


# compressing and resizing files based on required parameters
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


if __name__ == '__main__':
    for i in all_supported_files:
        # filedir_with_extension = i[0] + i[1]  # this is file location and file extension
        # out_filedir_with_extension = i[0] + f".{desired_format}"
        print(i)
        # compress_resize_image(filedir_with_extension, out_filedir_with_extension, desired_format, quality=80)
    # releasing all memory
    gc.collect()

# # progress bar example
# for i in tqdm(range(10)):
#     sleep(3)
