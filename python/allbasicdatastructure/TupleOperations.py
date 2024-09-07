# Filename: TupleOperations.py

'''
Accessing Elements: Uses indexing to access elements of the tuple.
Slicing a Tuple: Extracts a subtuple from the original tuple.
Tuple Concatenation: Combines two tuples to form a new one.
Tuple Repetition: Repeats the tuple a specified number of times.
Checking Element Existence: Checks if an element exists in the tuple using the in keyword.
Finding Tuple Length: Uses len() to find the number of elements in the tuple.
Finding the Index of an Element: Locates the first occurrence of a value in the tuple.
Counting Elements: Counts how many times a specific element appears in the tuple.
Tuple Unpacking: Assigns the elements of a tuple to variables.
Nested Tuples: Tuples can contain other tuples, and their elements can be accessed using double indexing.
Immutable Nature: Tuples are immutable, so attempting to modify them will result in an error.
Conversion to List: You can convert a tuple to a list to make it mutable.
Conversion from List to Tuple: You can convert a list back into a tuple.
Minimum and Maximum Values: Finds the smallest and largest elements in a tuple.
Sorting a Tuple: You can indirectly sort a tuple by converting it to a list, sorting it, and then converting it back.
'''



# Tuple Creation
# Tuples are created by enclosing elements in parentheses ().
my_tuple = (1, 2, 3, 4, 5)

# Tuples are immutable, meaning once created, their elements cannot be modified.

# 1. Accessing Elements
# Elements can be accessed by their index (indexing starts at 0).
first_element = my_tuple[0]  # Access first element (1)
last_element = my_tuple[-1]  # Access last element (5)

# 2. Slicing a Tuple
# Slices a portion of the tuple using [start:stop] notation.
sub_tuple = my_tuple[1:4]  # Extracts elements from index 1 to 3. Result: (2, 3, 4)

# 3. Tuple Concatenation
# You can concatenate two tuples to form a new one.
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple  # Combines tuples. Result: (1, 2, 3, 4, 5, 6, 7, 8)

# 4. Tuple Repetition
# You can repeat the elements of a tuple using the * operator.
repeated_tuple = my_tuple * 2  # Repeats the tuple. Result: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 5. Checking for Element Existence
# Use the 'in' keyword to check if an element exists in the tuple.
exists = 3 in my_tuple  # Returns True if 3 is in the tuple, False otherwise

# 6. Finding the Length of a Tuple
# The length of a tuple (i.e., the number of elements) can be found using the len() function.
length = len(my_tuple)  # Result: 5

# 7. Finding the Index of an Element
# The index() method returns the first occurrence of the specified element.
index_of_four = my_tuple.index(4)  # Result: 3 (index starts at 0)

# 8. Counting Occurrences of an Element
# The count() method returns the number of times a specified element appears in the tuple.
count_of_two = my_tuple.count(2)  # Result: 1 (2 appears once)

# 9. Tuple Unpacking
# You can unpack a tuple into individual variables.
a, b, c, d, e = my_tuple  # a = 1, b = 2, c = 3, d = 4, e = 5

# 10. Nested Tuples
# Tuples can contain other tuples as elements, forming a nested tuple.
nested_tuple = (1, 2, (3, 4), (5, 6))  # Nested tuples

# You can access elements of the inner tuple by double indexing.
inner_tuple_element = nested_tuple[2][1]  # Accesses the second element of the third tuple (which is 4)

# 11. Immutable Nature
# Trying to modify a tuple element will result in an error.
# Uncommenting the line below will raise a TypeError.
# my_tuple[1] = 10  # ERROR: 'tuple' object does not support item assignment

# 12. Conversion to List
# Since tuples are immutable, you may want to convert them to lists if you need mutability.
tuple_as_list = list(my_tuple)  # Converts the tuple to a list: [1, 2, 3, 4, 5]
tuple_as_list[1] = 20  # Now we can modify the list. List becomes [1, 20, 3, 4, 5]

# 13. Conversion from List to Tuple
# You can also convert a list back into a tuple.
new_tuple = tuple(tuple_as_list)  # Converts the list back to a tuple: (1, 20, 3, 4, 5)

# 14. Minimum and Maximum Values
# You can find the smallest and largest elements in a tuple with min() and max().
min_value = min(my_tuple)  # Result: 1
max_value = max(my_tuple)  # Result: 5

# 15. Sorting a Tuple (Indirectly)
# You can't sort a tuple directly since it's immutable, but you can convert it to a list, sort it, and then convert it back to a tuple.
sorted_tuple = tuple(sorted(my_tuple))  # Result: (1, 2, 3, 4, 5)

# Example tuple printout after operations:
print(f"Original tuple: {my_tuple}")
print(f"Subtuple (1:4): {sub_tuple}")
print(f"Combined tuple: {combined_tuple}")
print(f"Repeated tuple: {repeated_tuple}")
print(f"Length of tuple: {length}")
print(f"Does 3 exist in tuple?: {exists}")
print(f"Index of 4: {index_of_four}")
print(f"Count of 2: {count_of_two}")
print(f"Unpacked elements: a={a}, b={b}, c={c}, d={d}, e={e}")
print(f"Nested tuple access: {inner_tuple_element}")
print(f"Modified list from tuple: {tuple_as_list}")
print(f"New tuple from list: {new_tuple}")
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
print(f"Sorted tuple: {sorted_tuple}")