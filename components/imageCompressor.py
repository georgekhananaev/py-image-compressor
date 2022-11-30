from components import localColors as Color
from PIL import Image
import gc
import os


# compressing and resizing files based on required parameters
def compress_resize_image(file_location, output_location, file_type, max_width=800, optimize=True, quality=80):
    try:
        with Image.open(file_location) as im:
            im = im.convert('RGB')
            new_width = im.height / max_width
            w, h = int(im.width // new_width), int(im.height // new_width)
            print(f"{Color.select.OKCYAN}Processing file: {os.path.basename(file_location)}{Color.select.ENDC}, {Color.select.OKBLUE}it will be resized to: {w, h}{Color.select.ENDC}")
            im_resized = im.resize((w, h))
            im_resized.save(output_location, file_type, optimize=optimize, quality=quality)
            print(f"{Color.select.OKGREEN}Done!{Color.select.ENDC}")

    except Exception as Err:
        gc.collect()
        print(Err)

# # progress bar example
# for i in tqdm(range(10)):
#     sleep(3)
