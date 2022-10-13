# Python Tutorial for Beginners 2: Strings - Working with Textual Data
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2

# Python welcome message

# Use double quote "" if anything inside is single '' content
message = "Hello World"

# Use single '' if anything inside it double quote ""  content
print(message)

# Finding how many characters in our string (message)
print(len(message))

# Accessing our strings characters individually (index will start from 0 it means  H is 0...)
print(message[0])
print(message[5])

# Getting range of characters from string like 0 to 4
print(message[0:5])

# We can leave : blank, So it will continue to the end of string
print(message[6:])

# Using methods (function of an object)
# First create an object
alert = 'power failure'

# using method on object alert
print(alert.upper())
print(alert.count('r'))
print(alert.find('failure'))

# using replace method  (need to set a new variable)
print(alert.replace('failure', 'okay'))

# concatenating multiple strings
greeting = 'Hello'
name = 'Savana'
# using another string with blank space in between different strings
message = greeting + ' ' + name
print(message)


# concatenate multiple strings (old way)
# message = '{},{} Welcome to Python programming'.format(greeting, name)
# print(message)

# concatenate multiple strings (new way)
message = f'{greeting},{name} Welcome to Python programming'
print(message)

# To know the methods available
print(dir(name))

# To get the help
print(help(str))
