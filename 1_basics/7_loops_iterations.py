# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

# For loop
from operator import le

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break statement - stop and exit the loop when condition is true
for num in nums:
    if num == 3:
        print('Found 3')
        break
    print(num)

# continue statement - stop and continue the loop when condition is true
for num in nums:
    if num == 3:
        print('Found 3')
        continue
    print(num)

# loop within a loop
nums = [1, 2, 3, 4, 5, ]
for num in nums:                        # 1st loop
    for letter in 'abc':                # 2nd loop inside the 1st loop
        print(num, letter)              # print both loops

# loop using range (nth times)
for i in range(10):             # starts with 0 and end at 9
    print(i)

for i in range(1, 11):          # starts with 1 and ends at 10
    print(i)

# while loop - continue till the condition is met or break
x = 0
while x < 10:
    print(x)
    # if we use x == 1 it will go into infinite and won't stop
    x += 1
    # press ctrl+c to exit out of infinite loop
