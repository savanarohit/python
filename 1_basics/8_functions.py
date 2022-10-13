# In Python, a function is a group of related statements that performs a specific task.Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable. DRY - Do Not Repeat

# function definition without a value
from cmath import inf


def myfunction():
    pass                                        # pass the function without any return value


print(myfunction)                               # call the function


# function definition with print
def myfunction():
    print('myfunction')                         # task of the function


myfunction()                                    # call the function


# function definition with return value
def hello_func():
    return 'HELLO FUNCTION'


print(hello_func())                             # call the function
print(hello_func().lower())                     # working with function


# passing arguments to the function
def myfunction(greeting, name='Rohit'):
    # {} is placeholder for the greeting and name arguments
    return '{},{}'.format(greeting, name)
    # The format() method returns a formatted representation of the given value controlled by the format specifier.
    # to call {},{} with .format(greeting,name)


# without any positional arguments which is greeting is required to call the function
# greeting parameter is required value of the myfunction
print(myfunction('Hi', 'Savana'))
print(myfunction('Hi', name=''))


# function with positional arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# positional arguments - Math and Art       tuples
# Keyword arguments - name and age          dictionary
# student_info('Math', 'Art', name='savana', age=22)

# working with args and kwargs
courses = ['Math', 'Art', 'CompScience', 'Biology']
info = {'name': 'Savana', 'age': 22, 'address': 'Mumbai'}

# unpacking the list and dictionary values individually
student_info(*courses, **info)


# Leap year

# number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year"""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
print(days_in_month(2022, 2))
