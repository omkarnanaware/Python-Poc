# Filename: StringOperations.py

'''
Accessing Characters: Uses indexing to access individual characters in a string.
Slicing a String: Extracts a substring using start and stop indices.
String Concatenation: Combines two strings using the + operator.
String Repetition: Repeats a string using the * operator.
Checking Substring: Uses in to check if a substring exists.
String Length: Uses len() to find the number of characters.
Changing Case: Converts a string to lowercase, uppercase, or capitalizes the first character.
Splitting a String: Splits a string into a list based on a delimiter.
Joining a List of Strings: Joins a list of strings into one with a specified delimiter.
Finding Substring: Finds the index of the first occurrence of a substring.
Replacing Substrings: Replaces occurrences of a substring with another.
Removing Whitespace: Strips leading and trailing whitespace.
Counting Substring Occurrences: Counts how many times a substring appears in a string.
Checking Start and End: Checks if a string starts or ends with a specific substring.
String Formatting: Formats strings dynamically using format() or f-strings.
String Reversal: Reverses a string using slicing.
Checking if String is Numeric: Checks if all characters in the string are digits.
Checking if String is Alphanumeric: Checks if all characters are letters or numbers.
'''


# String Creation
# Strings are created by enclosing text in either single quotes (' ') or double quotes (" ").
my_string = "Hello, World!"

# Strings are immutable, meaning you cannot change individual characters directly.

# 1. Accessing Characters
# You can access characters of a string using their index (indexing starts at 0).
first_char = my_string[0]  # Access first character ('H')
last_char = my_string[-1]  # Access last character ('!')

# 2. Slicing a String
# Slices a portion of the string using [start:stop] notation.
sub_string = my_string[0:5]  # Extracts characters from index 0 to 4 (exclusive). Result: 'Hello'

# 3. String Concatenation
# You can concatenate strings using the + operator.
another_string = " Welcome to Python!"
combined_string = my_string + another_string  # Result: "Hello, World! Welcome to Python!"

# 4. String Repetition
# Repeats the string using the * operator.
repeated_string = my_string * 2  # Result: "Hello, World!Hello, World!"

# 5. Checking for Substring
# You can check if a substring exists in a string using the `in` keyword.
exists = "World" in my_string  # Returns True

# 6. String Length
# The length of a string (i.e., the number of characters) can be found using the len() function.
length = len(my_string)  # Result: 13

# 7. Changing Case
# You can convert the string to lower case, upper case, or capitalize it.
lower_case = my_string.lower()  # Converts the string to lower case. Result: "hello, world!"
upper_case = my_string.upper()  # Converts the string to upper case. Result: "HELLO, WORLD!"
capitalized = my_string.capitalize()  # Capitalizes the first character. Result: "Hello, world!"

# 8. Splitting a String
# Splits the string into a list of substrings based on a delimiter (space is default).
words = my_string.split()  # Splits by spaces. Result: ['Hello,', 'World!']
split_by_comma = my_string.split(",")  # Splits by comma. Result: ['Hello', ' World!']

# 9. Joining a List of Strings
# Joins elements of a list into a single string with a specified delimiter.
words = ['Python', 'is', 'fun']
joined_string = " ".join(words)  # Joins the list with space delimiter. Result: "Python is fun"

# 10. Finding a Substring
# The find() method returns the index of the first occurrence of a substring, or -1 if not found.
index_of_world = my_string.find("World")  # Result: 7 (index of 'W')

# 11. Replacing Substrings
# The replace() method replaces all occurrences of a substring with another substring.
replaced_string = my_string.replace("World", "Python")  # Result: "Hello, Python!"

# 12. Removing Whitespace
# You can remove leading and trailing whitespace using strip(). Use lstrip() for left side, rstrip() for right side.
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()  # Result: "Hello, World!"

# 13. Counting Substring Occurrences
# The count() method counts how many times a substring occurs in the string.
count_of_l = my_string.count('l')  # Result: 3 (three 'l' characters in "Hello, World!")

# 14. Checking String Start and End
# You can check if a string starts or ends with a particular substring using startswith() and endswith().
starts_with_hello = my_string.startswith("Hello")  # Returns True
ends_with_exclamation = my_string.endswith("!")  # Returns True

# 15. String Formatting
# You can use format() or f-strings to format strings dynamically.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)  # Using format(). Result: "My name is Alice and I am 30 years old."
f_string = f"My name is {name} and I am {age} years old."  # Using f-string. Result: "My name is Alice and I am 30 years old."

# 16. String Reversal (using slicing)
# You can reverse a string using slicing with a step of -1.
reversed_string = my_string[::-1]  # Result: "!dlroW ,olleH"

# 17. Checking if String Contains Only Digits
# The isdigit() method checks if all characters in the string are digits.
numeric_string = "12345"
is_digit = numeric_string.isdigit()  # Returns True

# 18. Checking if String is Alphanumeric
# The isalnum() method checks if all characters in the string are alphanumeric (letters and numbers).
alphanumeric_string = "Hello123"
is_alnum = alphanumeric_string.isalnum()  # Returns True

# Example string printout after operations:
print(f"Original string: {my_string}")
print(f"First character: {first_char}")
print(f"Last character: {last_char}")
print(f"Substring (0:5): {sub_string}")
print(f"Combined string: {combined_string}")
print(f"Repeated string: {repeated_string}")
print(f"Length of string: {length}")
print(f"Lowercase: {lower_case}")
print(f"Uppercase: {upper_case}")
print(f"Capitalized: {capitalized}")
print(f"Words in string: {words}")
print(f"Joined string: {joined_string}")
print(f"Index of 'World': {index_of_world}")
print(f"Replaced string: {replaced_string}")
print(f"Stripped string: {stripped_string}")
print(f"Count of 'l': {count_of_l}")
print(f"Starts with 'Hello': {starts_with_hello}")
print(f"Ends with '!': {ends_with_exclamation}")
print(f"Formatted string: {formatted_string}")
print(f"Reversed string: {reversed_string}")
print(f"Is numeric: {is_digit}")
print(f"Is alphanumeric: {is_alnum}")