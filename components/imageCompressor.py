#!/usr/bin/python
import sys
from PIL import Image, ImageFile
from pillow_heif import register_heif_opener

# Mitigate issues with truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Add HEIC/HEIF
register_heif_opener()

avif_supported = True
try:
    import avif  # noqa
except ImportError:
    avif_supported = False


def compress_resize_image(**kwargs) -> None:
    """
    Compress/resize. Remove metadata if remove_meta=True.
    If format == avif but 'pillow-avif-plugin' is not installed, skip & raise.
    """
    remove_meta = kwargs.get('remove_meta', False)
    set_format = kwargs['set_format'].lower()

    # If user wants AVIF but plugin is not installed, raise an exception
    if set_format == 'avif' and not avif_supported:
        raise ValueError("AVIF plugin (pillow-avif-plugin) not installed. Cannot save as AVIF.")

    try:
        with Image.open(kwargs['image_location']) as im:
            # If removing meta, skip exif
            if not remove_meta:
                exif_data = im.info.get('exif')
            else:
                exif_data = None

            # Convert mode
            if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
                im = im.convert("RGBA")
            else:
                im = im.convert("RGB")

            # Calculate new dimensions
            if kwargs['max_width'] is None or im.width <= kwargs['max_width']:
                w, h = im.width, im.height
            else:
                ratio = im.width / im.height
                w = kwargs['max_width']
                h = round(w / ratio)

            im_resized = im.resize((w, h), resample=Image.LANCZOS)

            # If not removing meta and set_format supports EXIF
            if exif_data and set_format in ['jpeg', 'jpg', 'tiff']:
                im_resized.save(
                    kwargs['image_destination'],
                    set_format,
                    optimize=True,
                    quality=kwargs['quality'],
                    exif=exif_data
                )
            else:
                im_resized.save(
                    kwargs['image_destination'],
                    set_format,
                    optimize=True,
                    quality=kwargs['quality']
                )

    except Exception as err:
        raise err