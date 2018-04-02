
import os
import re

os.chdir('rename/')

print(os.getcwd())




for file in os.listdir():
    fileName, fileExt = os.path.splitext(file)
    fileTitle , fileNo = fileName.split('#')
    fileTitle = fileTitle.strip()
    fileNo = fileNo.zfill(2)
    new_name = "{} {}".format(fileNo, fileTitle)
    print(new_name)
    os.rename(file, new_name)














