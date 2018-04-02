
import os
import time
import datetime
# os stands for operating system


# get current working directory
print('1-->   ' + os.getcwd())

# change directory
os.chdir('/home/utshaw/PycharmProjects/practice/sample') # moving down one level below


# making directory
try:
    os.mkdir('utshaws sample folder')
except FileExistsError:
    print('Error: ' + 'File already exists!!!')

try:
    os.makedirs('utshaws sample folder/this is a new folder/root folder')
except FileExistsError:
    print('Error: File Already exists!!!')


print('2--> ' + os.getcwd())

print('3--> ' + str(os.listdir()))

time.sleep(2) # waiting for some time for seeing the effect of creating and removing directories


os.rmdir('utshaws sample folder/this is a new folder/root folder') # removes only the 'root folder'

os.removedirs('utshaws sample folder/this is a new folder') # remove all directories along the way

print('4--> ' + str(os.listdir()))

os.chdir('/home/utshaw/PycharmProjects/practice/') # back to original

os.rename('sample', 'old_sample') # renaming from sample to old_sample





# list all files in current directory
# os.listdir(fileName) # paremeter fileName (optional) for going into fileName folder and list all of files inside that

file_list = os.listdir('old_sample')
for file in file_list:
    print(file)



os.rename('old_sample', 'sample')

os.chdir('sample/')

print('5 -- >' + str(os.stat('sample_text.txt'))) # stats about file

mod_time = os.stat('sample_text.txt').st_mtime


print('6 -- >' + str(datetime.datetime.fromtimestamp(mod_time)))


print('------------------------------------------------------------------------------')


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('7 --> Current Directory Path: '  + dirpath)
    print('8 --> Directories under this path: ' + dirpath)
    print('9 --> All files under this path: ' + str(filenames))



print('------------------------------------------------------------------------------')

print('10-->' + str(os.environ)) # all environment variables

print('11-->' + str(os.environ.get('HOME'))) # /home/utshaw


file_path = os.path.join(os.environ.get('HOME'), 'sample.txt') # creating complex file path (/home/utshaw/sample.txt)
print('12-->' + file_path)

print('13--> ' + os.path.basename(file_path)) # sample.txt
print('14--> ' + os.path.dirname(file_path)) # /home/utshaw
print('15--> ' + str(os.path.split(file_path)))
print('16-->' + str(os.path.exists(file_path))) # path actually exists or not (False)
print('17-->' + str(os.path.isdir(file_path))) # is the path a directory
print('18-->' + str(os.path.isfile(file_path))) # is the path a file
print('19-->' + str(os.path.splitext(file_path))) # split the path into (from root to file_name ) and extension






# os.rename(src, dest) # https://docs.python.org/3/library/os.html#os.rename



