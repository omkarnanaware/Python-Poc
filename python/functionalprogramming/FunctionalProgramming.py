# Filename: FunctionalProgramming.py

'''
Lambda Functions: Anonymous functions written using the lambda keyword. Useful for small, short-lived operations.

map(): Applies a function to every item of an iterable (list, tuple, etc.) and returns an iterator.

filter(): Filters an iterable based on a condition and returns only elements that meet the condition.

reduce(): Applies a binary function to the items of an iterable, reducing them to a single value. It’s in the functools module.

Higher-Order Functions: Functions that either take other functions as arguments or return a function.

Function Composition: Combining two or more functions where the output of one function is the input to another.

Partial Functions: Allows you to "fix" certain arguments of a function and create a new function with those arguments predefined (from the functools module).

Using map(), filter(), and reduce() Together: Combining functional programming tools to perform complex transformations and computations in a functional way.
'''

from functools import reduce  # reduce() is part of functools module

# 1. Lambda Functions (Anonymous Functions)
# Lambda functions are small anonymous functions defined using the 'lambda' keyword.

# Example: A lambda function that squares a number
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Example: Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# 2. Map Function
# The map() function applies a function to every item in an iterable (like a list) and returns an iterator.

# Example: Using map() to square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example: Using map() to convert a list of strings to uppercase
names = ['alice', 'bob', 'charlie']
uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']

# 3. Filter Function
# The filter() function filters an iterable based on a function that returns True or False.

# Example: Using filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example: Using filter() to get names longer than 3 characters
long_names = list(filter(lambda name: len(name) > 3, names))
print(long_names)  # Output: ['alice', 'charlie']

# 4. Reduce Function
# The reduce() function is used to apply a binary function to the items of an iterable and reduces it to a single value.
# It is not part of the built-in functions; it's in the functools module.

# Example: Using reduce() to compute the product of all numbers in a list
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Example: Using reduce() to concatenate all strings in a list
concatenated_names = reduce(lambda x, y: x + " " + y, names)
print(concatenated_names)  # Output: 'alice bob charlie'

# 5. List Comprehension vs map() + filter()
# List comprehensions can often be used instead of map() and filter().

# Example: List comprehension for squaring numbers
squares_list_comprehension = [x ** 2 for x in numbers]
print(squares_list_comprehension)  # Output: [1, 4, 9, 16, 25]

# Example: List comprehension for filtering even numbers
even_list_comprehension = [x for x in numbers if x % 2 == 0]
print(even_list_comprehension)  # Output: [2, 4]

# 6. Higher-Order Functions
# A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result.

# Example: Higher-order function that returns a function
def create_multiplier(n):
    return lambda x: x * n

# Using the higher-order function to create different multipliers
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# Example: Higher-order function that accepts a function as argument
def apply_function(func, value):
    return func(value)

# Passing a lambda function as an argument
result = apply_function(lambda x: x ** 2, 6)
print(result)  # Output: 36

# 7. Function Composition
# Function composition is combining two or more functions to produce a new function.

# Example: Composing two functions
def add_one(x):
    return x + 1

def square_number(x):
    return x ** 2

# Composing functions using lambda
composed_function = lambda x: square_number(add_one(x))
print(composed_function(4))  # Output: 25 (4 + 1 = 5, 5^2 = 25)

# 8. Partial Functions (from functools)
# Partial functions allow you to fix a certain number of arguments of a function and generate a new function.

from functools import partial

# Example: Partial function to create a power function with a fixed exponent
def power(base, exponent):
    return base ** exponent

# Creating a square function (exponent is fixed to 2)
square_partial = partial(power, exponent=2)
print(square_partial(5))  # Output: 25

# Creating a cube function (exponent is fixed to 3)
cube_partial = partial(power, exponent=3)
print(cube_partial(3))  # Output: 27

# 9. Using map(), filter(), and reduce() Together
# Functional programming often involves combining these functions.

# Example: Filtering even numbers, squaring them, and then calculating their product
result = reduce(lambda x, y: x * y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: 64 (squares of 2 and 4: 4 * 16 = 64)

# Example: Converting a list of strings to uppercase, filtering those with more than 3 characters, and concatenating them
result = reduce(lambda x, y: x + " " + y, filter(lambda name: len(name) > 3, map(lambda name: name.upper(), names)))
print(result)  # Output: 'ALICE CHARLIE'

# Example outputs for each functional programming operation:
print(f"Squares using map: {squared_numbers}")
print(f"Even numbers using filter: {even_numbers}")
print(f"Product using reduce: {product}")