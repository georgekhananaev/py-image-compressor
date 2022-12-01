from tqdm import tqdm

from components import imageCompressor as iC, localColors as Color

support_formats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp", ".webp"]
original_folder = "D:\Programming\React\\resume-website\\src"  # noqa
output_folder = "./data/out/"  # noqa
desired_format = "webp"
all_supported_files = []


def build_file_list(your_folder, your_list):
    for root, dirs, files in iC.os.walk(your_folder):
        [your_list.append(iC.os.path.join(root, file_bfl)) for file_bfl in files if
         iC.os.path.splitext(file_bfl)[1].lower() in support_formats]


def create_folder(your_path):
    if iC.os.path.exists(your_path) is False:
        iC.os.makedirs(your_path)


if __name__ == '__main__':
    # building a file list to memory.
    build_file_list(original_folder, all_supported_files)

    pbar = tqdm(all_supported_files)
    # looping supported file list creating missing folders and converting it.
    zero = 0
    for file in pbar:
        iC.os.system('cls')

        filedir_with_extension = file
        before, sep, after = file.partition(original_folder)
        create_folder(output_folder + iC.os.path.dirname(after))

        zero += 1
        print(f"{Color.select.OKCYAN}Processing file: {iC.os.path.basename(after)}{Color.select.ENDC}")

        # final image path example output > /data/pic/my_pic.webp
        final_file_path = output_folder + after.replace(iC.os.path.splitext(after)[1], '') + f".{desired_format}"
        pbar.set_description(f"{Color.select.OKBLUE}Image {zero} out of {len(all_supported_files)}{Color.select.ENDC} ")

        iC.compress_resize_image(filedir_with_extension,
                                 final_file_path, desired_format,
                                 max_width=400, quality=100)
    # once finished throw memory.
    iC.gc.collect()
    exit()

    # for i in tqdm(range(len(all_supported_files))):
