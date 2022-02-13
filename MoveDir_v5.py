import os.path
import shutil
import glob

temp_true = True
path = r"C:\PyTest\MoveDirs\pynative\\"
src = path + r"1\source\\*"
dest: str = path + r"1\\"

files = glob.glob(src)
for fil in files:
    try:
        shutil.move(fil, dest)
    except FileNotFoundError:
        print('File Not Found')
    except FileExistsError:
        print(f'{fil} File already exists')
    except IsADirectoryError:
        print(f'{fil} Is A Directory error')
    except NotADirectoryError:
        print(f'{fil} Not A Directory error')
    except
        # Add whatever logic you want to execute
#    except:
#       print('Some Other error')
# shutil.move(fil, dest)
