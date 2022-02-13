import os
import shutil
# path
path = r"C:\PyTest\MoveDirs\pynative\\"

# List files and directories in C:\PyTest\MoveDirs\pynative
print("Before copying file:")
print(os.listdir(path))

# Source path
src = path + r"1\source\\"

# Destination path
dest = path + r"1\\"

# Copy the content of source to destination
destination = shutil.move(src, dest)

# List files and directories in C:\PyTest\MoveDirs\pynative
print("After copying file:")
print(os.listdir(path))

# Print path of newly created file
print("Destination path:", destination)
