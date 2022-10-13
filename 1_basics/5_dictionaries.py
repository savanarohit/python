#  A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value. You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:  In other programming languages it is known as hashmap and associative arrays. key is unique identifier and vale is the data  (like an actual dictionary).

student = {'name': 'rohit',
           'age': '33',
           'courses': ['Math', 'CompSci']
           }

# print all the items from the dictionary
print(student['courses'])

# print an item from the dictionary
print(student['age'])
print(student['courses'])

# print null or default value when a key does not exist
print(student.get('savana', 'Not Found'))

# add a entry in the dictionary
student['phone'] = '829191'
student['laptop'] = 'Dell'
print(student)

# updating multiple keys
student.update({'name': 'savana', 'age': '34', 'phone': '123456'})
print(student)

# delete a specific value
del student['age']

# delete a specific value using pop
popped = student.pop('name')
print(popped)
# we can see that name key was popped out from the dictionary
print(student)

# how many keys are in dict
print(len(student))

# print all of keys from the dict
print(student.keys())

# print all values of the keys
print(student.values())

# print keys and values
print(student.items())

# loop though keys and their values using .items() function
for key, value in student.items():
    print(key, value)
