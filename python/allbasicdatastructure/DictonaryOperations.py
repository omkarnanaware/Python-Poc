# Filename: DictionaryOperations.py

'''
Accessing Values: Retrieves the value associated with a specific key.
Adding/Updating Key-Value Pairs: Adds a new key-value pair or updates an existing one.
Checking if Key Exists: Checks whether a specific key exists in the dictionary.
Removing Key-Value Pairs: Deletes a key-value pair using del or pop().
Getting a Value Safely: Uses get() to retrieve a value without raising an error if the key is missing.
Dictionary Length: Gets the number of key-value pairs.
Iterating Over a Dictionary: Loops through keys, values, or key-value pairs.
Merging Dictionaries: Merges one dictionary into another using update() or the ** operator.
Dictionary Comprehension: Creates a dictionary dynamically using comprehension.
Clearing a Dictionary: Removes all key-value pairs from the dictionary.
Copying a Dictionary: Creates a shallow copy of the dictionary.
Nested Dictionaries: Accesses values inside nested dictionaries.
Default Values with setdefault(): Returns a value for a key or adds it with a default value.
Converting Keys/Values to Lists: Converts keys or values to lists.
Sorting a Dictionary (Keys): Sorts a dictionary by its keys using sorted().git a
'''


# Dictionary Creation
# Dictionaries are created using curly braces {}. They consist of key-value pairs.
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionaries are unordered (before Python 3.7) and mutable (values can be changed).

# 1. Accessing Values
# You can access a value by its key using the square bracket notation.
name = my_dict["name"]  # Access the value associated with key 'name'. Result: 'Alice'

# 2. Adding or Updating Key-Value Pairs
# You can add a new key-value pair or update an existing one.
my_dict["profession"] = "Engineer"  # Adds new key 'profession'. Dictionary becomes: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}
my_dict["age"] = 31  # Updates the value of key 'age'. Result: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}

# 3. Checking if Key Exists
# You can check if a key exists in the dictionary using the 'in' keyword.
exists = "city" in my_dict  # Returns True if 'city' exists in the dictionary

# 4. Removing Key-Value Pairs
# You can remove a key-value pair using the del statement or pop() method.
del my_dict["city"]  # Removes the key 'city'. Result: {'name': 'Alice', 'age': 31', 'profession': 'Engineer'}
profession = my_dict.pop("profession")  # Removes 'profession' and returns its value. Dictionary becomes: {'name': 'Alice', 'age': 31'}

# 5. Getting a Value Safely
# The get() method retrieves the value for a key, returning None if the key does not exist (or a default value).
age = my_dict.get("age")  # Returns 31
salary = my_dict.get("salary", "Not specified")  # Returns 'Not specified' since 'salary' key doesn't exist

# 6. Dictionary Length
# You can find the number of key-value pairs using the len() function.
length = len(my_dict)  # Result: 2 (because 'name' and 'age' remain)

# 7. Iterating Over a Dictionary
# You can loop through a dictionary's keys, values, or key-value pairs.
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")  # Iterates over keys

for value in my_dict.values():
    print(f"Value: {value}")  # Iterates over values

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Iterates over key-value pairs

# 8. Merging Two Dictionaries
# You can merge two dictionaries using the update() method or the ** operator.
other_dict = {"country": "USA", "hobby": "Reading"}
my_dict.update(other_dict)  # Merges 'other_dict' into 'my_dict'. Result: {'name': 'Alice', 'age': 31, 'country': 'USA', 'hobby': 'Reading'}

# 9. Dictionary Comprehension
# You can create a dictionary dynamically using dictionary comprehension.
squares = {x: x**2 for x in range(5)}  # Creates a dictionary of squares. Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 10. Clearing a Dictionary
# The clear() method removes all key-value pairs from the dictionary.
my_dict.clear()  # Empties the dictionary. Result: {}

# 11. Copying a Dictionary
# You can create a shallow copy of a dictionary using the copy() method.
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()  # Creates a copy of the dictionary. Result: {'a': 1, 'b': 2}

# 12. Nested Dictionaries
# Dictionaries can contain other dictionaries as values (nested dictionaries).
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
person1_name = nested_dict["person1"]["name"]  # Accessing nested dictionary value. Result: 'Alice'

# 13. Default Values with setdefault()
# The setdefault() method returns the value of a key if it exists. If not, it sets the key to a default value.
hobby = my_dict.setdefault("hobby", "No hobby")  # Adds 'hobby' with default value if it doesn't exist. Result: 'No hobby'

# 14. Converting Dictionary Keys or Values to Lists
# You can convert all keys or values of a dictionary into a list.
keys_list = list(my_dict.keys())  # Converts keys to a list. Result: ['name', 'age']
values_list = list(my_dict.values())  # Converts values to a list. Result: ['Alice', 31]

# 15. Sorting a Dictionary (Keys)
# You can sort a dictionary by its keys using the sorted() function.
sorted_dict = dict(sorted(my_dict.items()))  # Returns a dictionary sorted by keys.

# Example dictionary printout after operations:
print(f"Original dictionary: {my_dict}")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City exists: {exists}")
print(f"Updated dictionary: {my_dict}")
print(f"Length of dictionary: {length}")
print(f"Profession removed: {profession}")
print(f"Other dict merged: {my_dict}")
print(f"Dictionary of squares: {squares}")
print(f"Copied dictionary: {copied_dict}")
print(f"Nested dictionary access: {person1_name}")
print(f"Keys list: {keys_list}")
print(f"Values list: {values_list}")
print(f"Sorted dictionary by keys: {sorted_dict}")