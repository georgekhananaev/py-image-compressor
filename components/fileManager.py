# importing the shutil module
# importing the os module
import os
import shutil


# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter
shutil.copytree('D:/projects/base/Structure',
                'D:/projects/base/copied_structure',
                ignore=ignore_files)
