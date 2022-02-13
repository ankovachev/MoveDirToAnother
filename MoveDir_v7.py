import shutil
import os

# In the first two cases the directory in which the new file
# # is being created must already exist.
# os.rename  ("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# os.replace ("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")


path = r"C:\PyTest\MoveDirs\pynative\\"

temp_dir = r"C:\PyTest\MoveDirs\pynative\temp\\"
source_dir = path + r"1\source\\"
target_dir = path + r"1\\"

element_names = os.listdir(source_dir)

for element_name in element_names:
    s_el_name = os.path.join(source_dir, element_name)
    t_el_name = os.path.join(target_dir, element_name)

    s_el_is_folder = os.path.isdir(s_el_name)
    s_el_is_file = os.path.isfile(s_el_name)

    t_el_is_folder = os.path.isdir(t_el_name)
    t_el_is_exist = os.path.exists(t_el_name)

    if s_el_is_folder:
        if not t_el_is_exist:
            shutil.move(s_el_name, target_dir, )
    else:
        print(f"{s_el_name} is file ###{s_el_is_file}###")
        ren_file_name = element_name
        while True:
            if os.path.exists(os.path.join(target_dir, ren_file_name)):
                ren_file_name = ren_file_name + ".ori.txt"
            else:
                shutil.move(s_el_name, temp_dir)
                os.rename(os.path.join(temp_dir, element_name), os.path.join(temp_dir, ren_file_name))
                shutil.move(os.path.join(temp_dir, ren_file_name), target_dir)
                break
