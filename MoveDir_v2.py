# Python program to explain shutil.copytree() method

# importing os module
# import os

# importing shutil module
import shutil

# path
path = r"C:\PyTest\MoveDirs\pynative\\"

src = path + r"1\source\\"
dest = path + r"1\\"


# Copy the content of
# source to destination
# destination = shutil.copytree(src, dest)
destination = shutil.copytree(src, dest, dirs_exist_ok=True)
