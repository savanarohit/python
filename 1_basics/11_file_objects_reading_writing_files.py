# File  Objects
f = open('test.txt', 'r')
print(f.name)           # file name
print(f.mode)           # file mode
f.close()               # must otherwise you will get leaks

# using context manager
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# when we want to read large files
with open('test.txt', 'r') as f:
    f_read = f.readlines()
    print(f_read)
