# Filename: looping_operations.py

'''
Basic For Loop: Loops through a sequence (like a list or string).
For Loop with Range: Iterates over a sequence of numbers.
For Loop with Step in Range: Skips values based on a step size.
For Loop with Else: Executes the else block after the loop finishes without break.
Looping Over Strings: Iterates over characters in a string.
Looping Over Dictionaries: Loops over keys, values, or key-value pairs of a dictionary.
Nested For Loops: Loops inside loops, commonly used for multi-dimensional data.
Using Break in a Loop: Exits the loop when a specific condition is met.
Using Continue in a Loop: Skips the current iteration and moves to the next one.
While Loop: Loops while a condition remains True.
While Loop with Else: Executes the else block after the while loop finishes.
Infinite While Loop: A loop that runs indefinitely until manually stopped.
Using Break in While Loop: Exits the loop early when a condition is met.
Using Continue in While Loop: Skips the current iteration in the while loop.
Looping with List Comprehensions: Creates lists using compact loops.
Looping with Dictionary Comprehensions: Creates dictionaries using compact loops.
Enumerate in Loops: Iterates over both index and value at the same time.
Looping Over Multiple Lists with Zip: Combines two or more lists into pairs of values.
Looping with a Step: Iterates with a custom step interval.
Unpacking Tuples in For Loops: Iterates over a list of tuples and unpacks values.
'''



# 1. Basic For Loop
# The 'for' loop is used to iterate over a sequence (like a list, tuple, string, or range).
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)  # Iterates over each number in the list and prints it

# 2. For Loop with Range
# The range() function generates a sequence of numbers, which can be used to loop over a specific range.
for i in range(5):
    print(i)  # Prints numbers from 0 to 4 (range generates numbers from 0 to n-1)

for i in range(2, 7):
    print(i)  # Prints numbers from 2 to 6

# 3. For Loop with Step in Range
# You can specify a step value to skip numbers in the range.
for i in range(0, 10, 2):
    print(i)  # Prints even numbers: 0, 2, 4, 6, 8

# 4. For Loop with Else
# The else block is executed when the for loop completes without hitting a break statement.
for i in range(3):
    print(i)
else:
    print("Loop finished")  # Prints this after the loop ends

# 5. Looping Over Strings
# You can loop through each character of a string.
text = "Hello"
for char in text:
    print(char)  # Prints each character in the string "Hello"

# 6. Looping Over Dictionaries
# You can loop through keys, values, or both in a dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key)  # Prints each key in the dictionary

for value in person.values():
    print(value)  # Prints each value in the dictionary

for key, value in person.items():
    print(f"{key}: {value}")  # Prints each key-value pair

# 7. Nested For Loops
# You can use a for loop inside another for loop (common in working with 2D arrays or matrices).
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for item in row:
        print(item)  # Prints each element in the matrix

# 8. Using Break in a Loop
# The 'break' statement exits the loop immediately.
for i in range(10):
    if i == 5:
        break  # Loop stops when i equals 5
    print(i)

# 9. Using Continue in a Loop
# The 'continue' statement skips the current iteration and moves to the next.
for i in range(5):
    if i == 3:
        continue  # Skips printing 3
    print(i)  # Prints 0, 1, 2, 4

# 10. While Loop
# The 'while' loop repeats as long as the condition is True.
count = 0
while count < 5:
    print(count)
    count += 1  # Increments count by 1 each time

# 11. While Loop with Else
# Similar to for loops, you can use an else block with a while loop.
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop finished")  # Prints after the loop ends

# 12. Infinite While Loop
# Be careful with conditions that always remain True, as they create infinite loops.
# Uncommenting the code below will create an infinite loop
# while True:
#     print("This will run forever")

# 13. Using Break in While Loop
# The 'break' statement exits a while loop immediately.
count = 0
while count < 10:
    if count == 6:
        break  # Loop stops when count equals 6
    print(count)
    count += 1

# 14. Using Continue in While Loop
# The 'continue' statement skips the rest of the code in the current iteration and moves to the next iteration.
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skips printing 3
    print(count)  # Prints 1, 2, 4, 5

# 15. Looping with List Comprehensions
# List comprehensions offer a concise way to loop and generate lists.
squares = [x**2 for x in range(5)]  # Creates a list of squares of numbers from 0 to 4
print(squares)  # Output: [0, 1, 4, 9, 16]

# 16. Looping with Dictionary Comprehensions
# You can also use dictionary comprehensions to generate dictionaries with loops.
squares_dict = {x: x**2 for x in range(5)}  # Creates a dictionary of squares
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 17. Enumerate in Loops
# The enumerate() function provides both the index and the value during iteration.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")  # Prints both index and color

# 18. Looping Over Multiple Lists with Zip
# The zip() function allows you to loop over multiple sequences in parallel.
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for num, letter in zip(list1, list2):
    print(f"Number: {num}, Letter: {letter}")  # Prints paired items from both lists

# 19. Looping with a Step Using Range
# By using the step argument in range, you can iterate in custom intervals.
for i in range(10, 0, -2):  # Loops from 10 to 2 with a step of -2
    print(i)  # Prints 10, 8, 6, 4, 2

# 20. Unpacking Tuples in For Loops
# When looping over a list of tuples, you can unpack the values into separate variables.
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x: {x}, y: {y}")  # Prints the x and y coordinates for each tuple

# Example output for each loop:
print(f"List of numbers: {numbers}")
print(f"Squares of numbers: {squares}")
print(f"Dictionary of squares: {squares_dict}")
print(f"Enumerate example: Colors = {colors}")
print(f"Zipped lists: {list(zip(list1, list2))}")