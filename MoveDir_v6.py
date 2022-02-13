from pathlib import Path
# shutil.copy(sourcePath, destinationPath)
# from pathlib import Path
# my_file = Path("/path/to/file")
# if my_file.exists():
# if my_file.is_dir():
# if my_file.is_file():
#
# To delete directory with all its contents use: shutil.rmtree(path)
# Or delete a single file with os.remove(path) and then move them one by one

path = r"C:\PyTest\MoveDirs\pynative\\"
src = path + r"1\source\\*"
dest: str = path + r"1\\"