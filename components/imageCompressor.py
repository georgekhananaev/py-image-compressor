#!/usr/bin/python
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()  # adding heic, heif support


# image, args.l, args.d, args.f, args.w, quality=args.q
# 👇️ compressing and resizing an image based on function parameters.
def compress_resize_image(**kwargs) -> None:
    try:
        with Image.open(kwargs['image_location']) as im:
            if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
                im = im.convert("RGBA")
            else:
                im = im.convert("RGB")
            if None is kwargs['max_width'] or im.width <= kwargs['max_width']:
                w, h = int(im.width), int(im.height)
            else:
                new_width = im.height / kwargs['max_width']
                w, h = round(im.width // new_width + 0.5), round(im.height // new_width + 0.5)

            im_resized = im.resize((w, h))
            im_resized.save(kwargs['image_destination'], kwargs['set_format'], optimize=True, quality=kwargs['quality'])

    except Exception as Err:
        print(Err)
