"""
Issues with python command

# Unable to find python
Run python from source python dir
C:\Python27\Python

Add this to PATH environment in the OS

# pip not found
same drill

# In python idle
import sys
sys.executable

# Know PATH
echo %path%

# Installing a pip
pip install django

# To get the details of a pip package
pip show boto3

Name: boto3
Version: 1.24.65
Summary: The AWS SDK for Python
Home-page: https://github.com/boto/boto3
Author: Amazon Web Services
Author-email:
License: Apache License 2.0
Location: c:\users\testuser\appdata\roaming\python\python310\site-packages
Requires: botocore, jmespath, s3transfer
Required-by: aws-shell, kitten

# python code is working in command line but not in IDE (VSCode run)
Search the python path then
Setup build system in the IDE

Knowing from python
import sys
print(sys.version)
print(sys.executable)

# Linux and Mac - It shows python 2 even after installing python3
which python3
/usr/local/bin/python3
So we need to use python3

Another way to search
type python3
python3 is hashed in (/usr/local/bin/python3)

To know the PATH
echo $PATH

Adding into bash file (env details)
.bash_profile

To know about a pip
pip show django

which python





"""
