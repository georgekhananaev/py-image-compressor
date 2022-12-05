#!/usr/bin/python
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()  # adding heic, heif support


# 👇️ compressing and resizing an image based on function parameters.
def compress_resize_image(file_location, output_location, file_type, max_width: int, optimize=True, quality=100):
    try:
        with Image.open(file_location) as im:
            im = im.convert('RGB')
            if None is max_width or im.width <= max_width:
                w, h = int(im.width), int(im.height)
            else:
                new_width = im.height / max_width
                w, h = round(im.width // new_width + 0.5), round(im.height // new_width + 0.5)

            im_resized = im.resize((w, h))
            im_resized.save(output_location, file_type, optimize=optimize, quality=quality)

    except Exception as Err:
        print(Err)
        # del Err, file_location
        # gc.collect()
