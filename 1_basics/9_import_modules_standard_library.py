# Modules refer to a file containing Python statements and definitions. We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

# Import hello module
from cmath import sin
import mymodule
import sys
import random
import math
import calendar
import datetime
import os
import antigravity          # some fun

# We can also do like this sys.path.append('/Users/nixmin/python_modules/')
# We can also add python modules path into .bash_profile file located in home dir as below
# export = PYTHONPATH="Users/nixmin/python_modules/" after updating run source .bash_profile

# We can also import module using as different name in the program
import mymodule as mm

# We can also use few functions from mymodule
from mymodule import output, addition, find, test

# We can use all functions from mymodule  (We don't know how many functions used) , So better not used
from mymodule import *

# Call function
mymodule.output()

# Call function
mymodule.addition()

# List on which we will use mymodule.find()
courses = ['Math', 'History', 'Physics', 'CompSci']

# Call function
index = mymodule.find(courses, 'Physics')
print(index)

# Call function  (Now we can use module name mm)
mm.addition()
print(test)

# System will know your module location
print(sys.path)

rand_courses = random.choice(courses)
print(rand_courses)

rads = math.radians(80)
sine = math.sin(10)
print(rads)
print(sine)

today = datetime.date.today()
print(today)

month = calendar.month(2022, 10)
print(month)

print(calendar.isleap(2020))

print(os.getcwd())

# __file__ (A double underscore variable in Python is usually referred to as a dunder) to know where this module is
print(os.__file__)
