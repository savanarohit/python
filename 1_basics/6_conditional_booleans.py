# Comparisons
# Equal                 ==
# Not Equal             !=
# Greater Than          >
# Less Than             <
# Greater or Equal      >=
# Less or Equal         <=
# Object Identity       is

# if statement
if True:
    print('conditional was true')
else:
    print('conditional was false')

# print true if the condition is true else print false
language = 'java'

if language == 'python':
    print('Language is python')
else:
    print('No match')

# multiple condition statement using else if
language = 'javascript'

if language == 'python':
    print('This is python')
elif language == 'Java':
    print('This is Java')
elif language == 'javascript':
    print('This is javascript')
else:
    print('No match')

# Boolean operation - AND , OR , NOT
user = 'admin'
logged_in = False

# AND - if both the condition are true
if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad credentials')

# OR - if any one of the condition is true
user = 'nixmin2'
logged_in = True
if user == 'nimxin' or logged_in:
    print('nixmin page')
else:
    print('bad credential')

# NOT - if none of the condition is true
user = 'Admin'
logged_in = False
if not logged_in:
    print('Please login')
else:
    print('Welcome')


# Object Identity is Equal (same object in the memory)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

# check if the a object is equal to b
print(a is b)
print(id(a))        # a object location in memory
print(id(b))        # b object location in memory

a = [1, 2, 3]
b = a               # same object in memory
print(a is b)
print(id(a))        # a object location in memory
print(id(b))        # b object location in memory


# False Values:
# False
condition = False
if condition:
    print('evaluated to True')
else:
    print('evaluated to False')

# None
condition = None
if condition:
    print('evaluated to True')
else:
    print('evaluated to False')

# Zero or any numeric type
condition = 0
if condition:
    print('evaluated to True')
else:
    print('evaluated to False')

# Any empty sequence - '' , () , []   (empty string,tuples,list)
condition = []
if condition:
    print('evaluated to True')
else:
    print('evaluated to False')

# Any empty mapping - {}        (empty dictionary)
condition = {}
if condition:
    print('evaluated to True')
else:
    print('evaluated to False')
