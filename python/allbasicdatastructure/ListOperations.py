# Filename: list_operations.py

'''
Accessing Elements: Uses indexing to access specific list elements.
Modifying Elements: Lists are mutable, so you can modify elements in place.
Appending Elements: Adds an item to the end of the list.
Inserting Elements: Adds an item at a specified position in the list.
Removing Elements by Value: Removes the first occurrence of a value from the list.
Removing Elements by Index: Uses pop() to remove an item from a specific position.
Clearing the List: Removes all elements from the list, making it empty.
Extending a List: Combines another list with the current list.
Slicing a List: Extracts a portion of the list using start and stop indexes.
Sorting a List: Sorts the list in ascending or descending order.
List Comprehension: Creates a new list by applying an operation to each item.
List Length: Uses len() to find the number of items in the list.
Element Existence: Checks if a specific item exists in the list.
Reversing a List: Reverses the order of elements in the list.
Copying a List: Creates a shallow copy of the list.
Counting Elements: Counts how many times a specific element appears.
Finding the Index of an Element: Locates the first occurrence of a value in the list.
'''



# List Creation
# A list is created by enclosing elements within square brackets [].
my_list = [1, 2, 3, 4, 5]

# 1. Accessing Elements
# You can access elements by their index. Indexing starts at 0.
first_element = my_list[0]  # Access first element (1)
last_element = my_list[-1]  # Access last element (5)

# 2. Modifying Elements
# Lists are mutable, meaning you can change their content.
my_list[1] = 20  # Modifies the second element to 20. Now list is [1, 20, 3, 4, 5]

# 3. Appending Elements
# Adds an element to the end of the list.
my_list.append(6)  # List becomes [1, 20, 3, 4, 5, 6]

# 4. Inserting Elements
# Insert an element at a specified index.
my_list.insert(2, 30)  # Inserts 30 at index 2. List becomes [1, 20, 30, 3, 4, 5, 6]

# 5. Removing Elements by Value
# Removes the first occurrence of a value.
my_list.remove(20)  # Removes 20 from the list. List becomes [1, 30, 3, 4, 5, 6]

# 6. Removing Elements by Index
# Removes an element by its index and returns the removed element.
removed_element = my_list.pop(2)  # Removes the element at index 2 (which is 3). List becomes [1, 30, 4, 5, 6]

# 7. Clearing the List
# Removes all elements from the list.
my_list.clear()  # Now the list is empty []

# 8. Extending a List
# You can extend a list by appending all the elements of another list.
my_list = [1, 2, 3]  # Reinitialize the list
my_list.extend([4, 5, 6])  # Extends the list to [1, 2, 3, 4, 5, 6]

# 9. Slicing a List
# Extract a part of the list (sublist) using slice notation: [start:stop].
sub_list = my_list[1:4]  # Extract elements from index 1 to 3 (excluding 4). Result: [2, 3, 4]

# 10. Sorting a List
# Sorts the list in ascending order. The list is modified in place.
my_list.sort()  # List becomes [1, 2, 3, 4, 5, 6]

# You can also sort a list in descending order by passing reverse=True
my_list.sort(reverse=True)  # List becomes [6, 5, 4, 3, 2, 1]

# 11. List Comprehension
# A concise way to create lists.
squared_list = [x**2 for x in my_list]  # Squares each element. Result: [36, 25, 16, 9, 4, 1]

# 12. List Length
# Returns the number of elements in the list.
length = len(my_list)  # Result: 6

# 13. Checking for Element Existence
# Use the `in` keyword to check if an element exists in the list.
exists = 3 in my_list  # Returns True if 3 is in the list, False otherwise

# 14. Reversing a List
# Reverses the list in place.
my_list.reverse()  # Now the list is [1, 2, 3, 4, 5, 6]

# 15. Copying a List
# To create a shallow copy of a list, use the copy method.
list_copy = my_list.copy()  # Creates a new list with the same elements [1, 2, 3, 4, 5, 6]

# 16. Counting Occurrences of an Element
# Returns the number of times an element appears in the list.
count_of_five = my_list.count(5)  # Result: 1 (5 appears once)

# 17. Finding the Index of an Element
# Returns the index of the first occurrence of an element. Raises an error if not found.
index_of_five = my_list.index(5)  # Result: 4 (index starts at 0)

# Example list printout after operations:
print(f"Final list: {my_list}")
print(f"Sublist (1:4): {sub_list}")
print(f"Squared list: {squared_list}")
print(f"Length of list: {length}")
print(f"Does 3 exist in list?: {exists}")
print(f"Copied list: {list_copy}")
print(f"Count of 5: {count_of_five}")
print(f"Index of 5: {index_of_five}")