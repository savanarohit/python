# list - sequential , non duplicate, unordered data and Immutable data type
courses = ['math', 'science', 'physics', 'chemistry', 'geography']

# print list's items
print(courses)

# print the first item from the list (it starts from 0)
print(courses[1])

# print from the range
print(courses[1:5])

# add an item to the list this will add an item in the last
courses.append('art')
print(courses)

# add an item to specific location using insert function
courses.insert(0, 'biology')
print(courses)

# adding multiple items in main list using extend
# First create new item object
courses2 = ['it', 'social science', 'commerce']
# Then extend the main object
courses.extend(courses2)
print(courses)

# removing items from the list
courses.remove('it')
print(courses)

# pop method will by default removes last item from the list , we can store this method in an object to get the popped item as an output
popped = courses.pop()
print(popped)

# print the list in reverse order
courses.reverse()
print(courses)

# sorting the list alphabetically
courses.sort()
print(courses)

# sorting the list ascending
numbers = [5, 4, 3, 2, 1]
print(numbers)
numbers.sort()
print(numbers)

# sorting the  list in descending order
numbers.sort(reverse=True)
print(numbers)

# to get sorted version (alphabetically) of a list without changing the original list
# first create an object to store the sorted function the output the object
sorted_courses = sorted(courses)
print(sorted_courses)

# min , max and sum
number = [1, 4, 2, 9, 6]            # This list should be without any quotes
print(max(numbers))
print(min(number))
print(sum(number))

# Find the index of certain item in the list
number = [1, 4, 2, 9, 6, 12, 15]
print(number.index(9))

# print all items of a list using for loop
number = [1, 4, 2, 9, 6, 12, 15]
for num in number:
    print(num)

# print index and items both
for index, num in enumerate(number):
    print(index, num)           # index will start from 0

# print item from the list into into csv / hyphen values
mycourses = ['python', 'django', 'flask', 'fastAPI']
mycourses_str = ' , '.join(mycourses)           # ',' or ' - '
print(mycourses_str)

# print from string back into a list
new_list = mycourses_str.split(' - ')
print(new_list)

# crete an empty list
empty_list = []
print(empty_list)


# Tuples is a Immutable data type , use ()
tuple_1 = ('english', 'science', 'biology', 'arts')
tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Social Science'     # comment out this to see the error
print(tuple_1)
print(tuple_2)

# create an empty tuple
empty_tuple = ()
print(empty_tuple)

# Sets are value unordered and no duplicate
# since math is duplicate on it was removed
cs_course = {'python', 'java', 'perl', 'linux', 'history'}
art_course = {'history', 'math', 'design', 'commerce', 'arts'}
print(cs_course)

# to check if an item is in the set or not
print('python' in cs_course)
print('cloud' in cs_course)

# print common items from the sets
print(cs_course.intersection(art_course))

# print difference between the first set and the second set
print(cs_course.difference(art_course))

# print all the items from multiple sets
print(cs_course.union(art_course))

# create an empty set
empty_set = set()
print(type(empty_set))
