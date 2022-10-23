# Renaming multiple image files (creating a proper naming structure for files)
import os

# going into a dir
os.chdir('E:/onedrive/Tech/python/1_basics/test')
print(os.getcwd())

# print all files in a dir
for f in os.listdir():
    print(f)

# getting file name and file extension
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)  # print(file_name, file_ext)

    # file name split using - (which is in file names)
    # print(file_name.split('-'))
    file_title, file_course, file_num = file_name.split('-')

    # striping any white spaces
    file_title = file_title.strip()
    file_course = file_course.strip()
    file_num = file_num.strip()[1:].zfill(2)
    file_ext = file_ext.strip()

    # using {} as place holder to store objects in format -
    print('{}-{}-{}-{}'.format(file_title, file_course, file_num, file_ext))

    # creating new object
    new_name = '{}-{}{}'.format(file_name, file_title, file_ext)
    os.rename(f, new_name)
