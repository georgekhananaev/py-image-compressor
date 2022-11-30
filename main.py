from components import imageCompressor as iC

support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]
original_folder = "D:\\Programming\\React\\resume-website\\public\\"
output_folder = "./data2/out/"
desired_format = "webp"
all_supported_files = []


def build_file_list(your_folder, your_list):
    for root, dirs, files in iC.os.walk(your_folder):
        [your_list.append(iC.os.path.join(root, file)) for file in files if
         iC.os.path.splitext(file)[1].lower() in support_formats]


# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if iC.os.path.isfile(iC.os.path.join(dir, f))]


# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter
# shutil.copytree(original_folder, output_folder, ignore=ignore_files)

def create_folder(your_path):
    if iC.os.path.exists(your_path) is False:
        iC.os.makedirs(your_path)


if __name__ == '__main__':
    # building a file list to memory.
    build_file_list(original_folder, all_supported_files)

    # looping supported file list creating missing folders and converting it.
    for file in all_supported_files:
        filedir_with_extension = file
        before, sep, after = file.partition(original_folder)
        create_folder(output_folder + iC.os.path.dirname(after))
        iC.compress_resize_image(filedir_with_extension,
                                 output_folder + after, desired_format,
                                 max_width=200, quality=80)
    # once finished throw memory.
    iC.gc.collect()
