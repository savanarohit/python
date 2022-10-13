# OS Module
from dataclasses import dataclass
from fileinput import close
import os
from datetime import datetime
print("current working dir is", os.getcwd())


# Changing dir , For python use forward slash in the path
os.chdir('C:/')
print(os.getcwd())

# Creating a directory
# os.mkdir('Test')

# Creating Sub directories
# os.makedirs('Test/subdir')
# os.makedirs('Test/subdir2')

# Remove a directory
# First chdir
os.chdir('C:/Test/')
print("Changed to Test dir", os.getcwd())

# Listing content of a directory
print("Content of the dir are", os.listdir())

# os.remove('Test')
# os.removedirs('subdir')             # we are in Test dir now
# os.removedirs('subdir2')

# Renaming a File
#print("File test.txt renamed to hello.txt", os.rename('test.txt', 'hello.txt'))

# Renaming a Dir
# print("Dir subdir renamed to subdir3", os.rename('subdir2', 'subdir3'))

# Information about a file
print(os.stat('hello.txt'))

# Printing the size of a file
print(os.stat('hello.txt').st_size)         # size in bytes
print(os.stat('hello.txt').st_mtime)        # modification time

# Using datetime module to get human readable form of modification time
mod_time = os.stat('hello.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# Traversing a dir  ( three value tuple)
for dirpath, dirnames, filename in os.walk('C:/Users/rohit/Documents'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files', filename)
    print()

# Accessing information using Environment variables
print(os.environ.get('JAVA_HOME'))

# Joining two paths
file_path = os.path.join('JAVA_HOME', 'test.txt')
print(file_path)

# Creating temp path
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))

# Checking if path exist in the filesystem
print(os.path.exists('/tmp/test.txt'))

# Checking if it is dir or file
print(os.path.isdir('C:/Test/subdir1'))
print(os.path.isfile('C:/Test/hello.txt'))

# Getting file name without extension (like all the files with hello name regardless of the extensions)
print(os.path.splitext('C:/Test/hello.txt'))

# Listing all the details of os.path module
print(dir(os.path))
