import os
import pytest
from PIL import Image
from py_bulk_image_compressor.components import imageCompressor as ic


@pytest.mark.parametrize("img_format", ["jpeg", "png", "webp"])
def test_compress_resize_image(tmp_path, img_format):
    """
    Using a small sample image in tests/sample_images,
    compress/resize it and ensure output file is created.
    """
    # Prepare sample image path
    sample_dir = os.path.join(os.path.dirname(__file__), "sample_images")
    sample_image = os.path.join(sample_dir, "sample.jpeg")

    # Output path
    output_image = tmp_path / f"compressed.{img_format}"

    # Call compressor
    ic.compress_resize_image(
        image_location=sample_image,
        image_destination=str(output_image),
        set_format=img_format,
        max_width=500,
        quality=80,
        remove_meta=False
    )

    # Check if file is created
    assert output_image.exists()

    # Check if it can be opened by Pillow
    with Image.open(output_image) as img:
        assert img.width <= 500  # we used max_width=500
