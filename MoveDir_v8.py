import shutil
import os

path = r"C:\PyTest\MoveDirs\pynative\\"

temp_dir = r"C:\PyTest\MoveDirs\pynative\temp\\"
source_dir = path + r"1\source\\"
target_dir = path + r"1\\"

file_names = os.listdir(source_dir)

for file_name in file_names:
    s_file_name = os.path.join(source_dir, file_name)
    element_is_folder = os.path.isdir(s_file_name)
    element_is_file = os.path.isfile(s_file_name)
    if element_is_folder:
            print(f"{s_file_name} is Folder!")
            continue
    if element_is_file:
            print(f"{s_file_name} ---------> is a file!")
            continue
    print(f"{s_file_name} ---------> is a NOTHING!")
        # ren_file_name = file_name
        # while True:
        #     if os.path.isfile(os.path.join(target_dir, ren_file_name)):
        #         ren_file_name = ren_file_name + ".ori"
        #     else:
        #         shutil.move(os.path.join(source_dir, file_name), temp_dir)
        #         os.rename(os.path.join(source_dir, file_name), os.path.join(temp_dir, ren_file_name))
        #         shutil.move(os.path.join(temp_dir, ren_file_name), target_dir)
        #         break
    #shutil.move(os.path.join(source_dir, file_name), target_dir)
