import os
import shutil

path = r"C:\PyTest\MoveDirs\pynative\\"

temp_dir = r"C:\PyTest\MoveDirs\pynative\temp\\"
source_dir = path + r"1\source\\"
target_dir = path + r"1\\"


root_src_dir = source_dir
root_dst_dir = target_dir
# root_src_dir = 'Src Directory\\'
# root_dst_dir = 'Dst Directory\\'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 0)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)
# shutil.rmtree(source_dir)
