from setuptools import setup, find_packages

setup(
    name="py-bulk-image-compressor",
    version="1.0.6",
    description="A Python bulk image compressor and resizer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="George Khananaev",
    author_email="george.khananaev@gmail.com",
    url="https://github.com/georgekhananaev/py-image-compressor",
    packages=find_packages(),  # Finds "py_bulk_image_compressor" + subpackages
    install_requires=[
        "Pillow>=11.1.0",
        "tqdm>=4.67.1",
        "pillow-heif>=0.21.0",
        "pillow-avif-plugin>=1.4.6",
    ],
    include_package_data=True,  # Important to include configurations.ini
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "py-bulk-image-compressor=py_bulk_image_compressor.main:main",
        ],
    },
)
