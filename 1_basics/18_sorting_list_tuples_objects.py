# sorting a list in ascending order using sorted function
from operator import attrgetter
list = [10, 8, 9, 5, 6, 3, 1, 7, 4, 2, ]

sorted_list = sorted(list)
print('Original list:\t\t', list)
print('Sorted list:\t\t', sorted_list)

# sorting a list using sort method
list.sort()
print('Sorted list:\t\t', list)

# sorting a list in descending order
descending_sorted_list = sorted(list, reverse=True)
print('Descending list:\t', descending_sorted_list)


# sorting a tuple
my_tuple = (1, 4, 9, 2, 7, 5, 6, 8, 10, 3)
sorted_tuple = sorted(my_tuple)
print('Sorted tuple:\t\t', sorted_tuple)


# sorting negative numbers
list = [-3, -5, -1, -4]
sorted_list = sorted(list)
print('Sorted list:\t\t', sorted_list)  # default is from negative to positive

# sorting based on absolute value
list = [-4, -9, -3, -5, -1]
sorted_list = sorted(list, key=abs)
print('Sorted list:\t\t', sorted_list)  # absolute sort ignoring negative


# Employee class example with absolute sorting
class Employee():  # class
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):  # method
        # placeholder
        return '({},{},${})'.format(self.name, self.age, self.salary)


# creating employee objects from the Employee class
e1 = Employee('Rohit', 34, 50000)
e2 = Employee('Amit', 35, 60000)
e3 = Employee('Savana', 32, 40000)

# sorting without absolute
employees = [e1, e2, e3]

# create a sort function that will be used as key in sorted()


def e_sort(employees):
    return employees.salary


# using key and also reverse
sorted_employees = sorted(employees, key=e_sort)
print(sorted_employees)


# using lambda function
sorted_employees = sorted(employees, key=lambda e: e.salary)
print(sorted_employees)


# using attrgetter module
sorted_employees = sorted(employees, key=attrgetter('salary'))
print(sorted_employees)
