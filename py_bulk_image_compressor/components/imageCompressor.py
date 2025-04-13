#!/usr/bin/env python3
import logging
import tempfile
from pathlib import Path
import importlib.util

from PIL import Image, ImageFile, UnidentifiedImageError
from pillow_heif import register_heif_opener

# Allow loading truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True
# HEIC/HEIF support
register_heif_opener()

# Dynamically detect AVIF plugin
if importlib.util.find_spec("pillow_avif"):
    import pillow_avif  # type: ignore
    _AVIF_SUPPORTED = True
else:
    _AVIF_SUPPORTED = False

# Dynamically detect libvips
if importlib.util.find_spec("pyvips"):
    import pyvips  # type: ignore
    VipsImage = pyvips.Image  # alias so static analyzers know it's not None
    _PYVIPS_AVAILABLE = True
else:
    VipsImage = None
    _PYVIPS_AVAILABLE = False

# Module‐level logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def compress_resize_image(
    image_location: str,
    image_destination: str,
    set_format: str,
    quality: int = 85,
    max_width: int = None,
    remove_meta: bool = False,
    use_vips: bool = False,
) -> None:
    """
    Compress and resize an image, optionally stripping metadata.
    Supports JPEG, PNG, TIFF, HEIF, AVIF (if pillow-avif-plugin installed).
    If use_vips=True and pyvips is available, uses libvips for faster, low‑memory processing.
    """
    src = Path(image_location)
    dest = Path(image_destination)
    fmt = set_format.lower().replace('jpg', 'jpeg')

    if fmt == 'avif' and not _AVIF_SUPPORTED:
        raise ValueError("AVIF support requires pillow-avif-plugin.")

    # Fast path: libvips
    if use_vips and VipsImage is not None:
        try:
            img = VipsImage.new_from_file(str(src), access='sequential')
            if max_width and img.width > max_width:
                img = img.resize(max_width / img.width)
            img.write_to_file(str(dest))
            return
        except Exception as e:
            logger.warning("pyvips failed, falling back to Pillow: %s", e)

    # Fallback: Pillow
    try:
        with Image.open(src) as im:
            exif = im.info.get('exif') if not remove_meta else None

            # Normalize mode
            if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
                im = im.convert("RGBA")
            else:
                im = im.convert("RGB")

            # Resize with aspect ratio
            w, h = im.size
            if max_width and w > max_width:
                ratio = w / h
                w = max_width
                h = round(max_width / ratio)

            # Modern enum for Lanczos :contentReference[oaicite:1]{index=1}
            im = im.resize((w, h), resample=Image.Resampling.LANCZOS)

            # Ensure output dir
            dest.parent.mkdir(parents=True, exist_ok=True)

            # Atomic write
            with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False, suffix=dest.suffix) as tmp:
                tmp_path = Path(tmp.name)

            save_kwargs = {'format': fmt, 'optimize': True, 'quality': quality}
            if exif and fmt in ('jpeg', 'tiff'):
                save_kwargs['exif'] = exif
            if fmt == 'jpeg':
                save_kwargs.update(progressive=True, subsampling='4:2:0')

            im.save(tmp_path, **save_kwargs)
            tmp_path.replace(dest)

    except UnidentifiedImageError as e:
        logger.error("Cannot identify image %s: %s", src, e)
        raise
    except Exception:
        logger.exception("compress_resize_image failed")
        raise

# #!/usr/bin/python
# import sys
# from PIL import Image, ImageFile
# from pillow_heif import register_heif_opener
#
# # Mitigate issues with truncated images
# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# # Add HEIC/HEIF
# register_heif_opener()
#
# avif_supported = True
# try:
#     import avif  # noqa
# except ImportError:
#     avif_supported = False
#
#
# def compress_resize_image(**kwargs) -> None:
#     """
#     Compress/resize. Remove metadata if remove_meta=True.
#     If format == avif but 'pillow-avif-plugin' is not installed, skip & raise.
#     """
#     remove_meta = kwargs.get('remove_meta', False)
#     set_format = kwargs['set_format'].lower()
#
#     # If user wants AVIF but plugin is not installed, raise an exception
#     if set_format == 'avif' and not avif_supported:
#         raise ValueError("AVIF plugin (pillow-avif-plugin) not installed. Cannot save as AVIF.")
#
#     try:
#         with Image.open(kwargs['image_location']) as im:
#             # If removing meta, skip exif
#             if not remove_meta:
#                 exif_data = im.info.get('exif')
#             else:
#                 exif_data = None
#
#             # Convert mode
#             if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
#                 im = im.convert("RGBA")
#             else:
#                 im = im.convert("RGB")
#
#             # Calculate new dimensions
#             if kwargs['max_width'] is None or im.width <= kwargs['max_width']:
#                 w, h = im.width, im.height
#             else:
#                 ratio = im.width / im.height
#                 w = kwargs['max_width']
#                 h = round(w / ratio)
#
#             im_resized = im.resize((w, h), resample=Image.LANCZOS)
#
#             # If not removing meta and set_format supports EXIF
#             if exif_data and set_format in ['jpeg', 'jpg', 'tiff']:
#                 im_resized.save(
#                     kwargs['image_destination'],
#                     set_format,
#                     optimize=True,
#                     quality=kwargs['quality'],
#                     exif=exif_data
#                 )
#             else:
#                 im_resized.save(
#                     kwargs['image_destination'],
#                     set_format,
#                     optimize=True,
#                     quality=kwargs['quality']
#                 )
#
#     except Exception as err:
#         raise err