# list - sequential , non duplicate & unordered data
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
