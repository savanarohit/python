# Modules refer to a file containing Python statements and definitions. We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

# Define a function
def output():
    print("Hello World!")


# Function with arguments
def addition():
    print(5+4)


# Function with arguments
print('Imported mymodule')
test = 'Test String'


def find(to_search, target):
    '''Find the index of a value in a string'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
