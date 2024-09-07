# Filename: comprehension_examples.py


'''

List Comprehensions: A concise way to generate lists by iterating over sequences and optionally adding conditions.

Tuple Comprehensions: Python doesn’t have direct tuple comprehensions, but you can achieve this using generator expressions and converting the result to a tuple using tuple().

Dictionary Comprehensions: These allow you to generate dictionaries from iterables by providing both keys and values, with optional conditions or transformations.

Set Comprehensions: Like list comprehensions, but they generate sets, which are unordered collections of unique elements.

String Comprehensions: You can create new strings by iterating over characters or generating filtered sequences and joining them into strings.

Nested Comprehensions: Used for working with complex structures like 2D lists or dictionaries of dictionaries, allowing you to perform nested iteration and transformations in a concise manner.

'''


# 1. List Comprehensions
# List comprehensions provide a concise way to create lists.

# Basic list comprehension (squares of numbers)
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# List comprehension with condition (only even numbers)
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# List comprehension with nested loops (cartesian product of two lists)
cartesian_product = [(x, y) for x in range(2) for y in range(3)]
print(cartesian_product)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# 2. Tuple Comprehensions (using generator expressions)
# There is no direct tuple comprehension in Python, but you can use a generator expression and convert it to a tuple.

# Generator expression for tuple (squares of numbers)
squares_tuple = tuple(x**2 for x in range(5))
print(squares_tuple)  # Output: (0, 1, 4, 9, 16)

# Generator expression with condition (only even numbers)
even_numbers_tuple = tuple(x for x in range(10) if x % 2 == 0)
print(even_numbers_tuple)  # Output: (0, 2, 4, 6, 8)

# 3. Dictionary Comprehensions
# Dictionary comprehensions allow for generating dictionaries in a concise way.

# Basic dictionary comprehension (mapping numbers to their squares)
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension with condition (only even numbers)
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Dictionary comprehension with transformation (keys are numbers, values are their cubes)
cube_dict = {x: x**3 for x in range(5)}
print(cube_dict)  # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# 4. Set Comprehensions
# Similar to list comprehensions, but they create a set instead of a list.

# Basic set comprehension (squares of numbers)
squares_set = {x**2 for x in range(5)}
print(squares_set)  # Output: {0, 1, 4, 9, 16}

# Set comprehension with condition (only even numbers)
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)  # Output: {0, 2, 4, 6, 8}

# 5. String Comprehension (joining characters)
# While there is no string comprehension directly, you can use list comprehensions or generator expressions to join strings.

# List comprehension to create a string by repeating characters
repeated_chars = ''.join([char*2 for char in 'hello'])
print(repeated_chars)  # Output: hheelllloo

# Generator expression to filter and create a string (only vowels)
vowels = ''.join(char for char in 'hello world' if char in 'aeiou')
print(vowels)  # Output: eo

# 6. Nested Comprehensions
# You can nest comprehensions for more complex operations.

# Nested list comprehension (flattening a 2D list)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# Nested comprehension for dictionary (pairwise combinations of two lists)
combinations_dict = {x: y for x in range(2) for y in range(3)}
print(combinations_dict)  # Output: {1: 2}

# Example outputs for each comprehension type:
print(f"List of squares: {squares}")
print(f"Tuple of even numbers: {even_numbers_tuple}")
print(f"Dictionary of squares: {squares_dict}")
print(f"Set of even numbers: {even_set}")
print(f"String with repeated characters: {repeated_chars}")
print(f"Flattened matrix: {flattened}")