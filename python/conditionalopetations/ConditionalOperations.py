# Filename: conditional_statements.py

# 1. Basic If Statement
# The simplest conditional statement. Executes code only if the condition is True.
x = 10
if x > 5:
    print("x is greater than 5")  # This will be printed because x = 10

# 2. If-Else Statement
# Provides an alternative action if the condition is False.
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # This will be printed because y = 3

# 3. If-Elif-Else Statement
# Adds multiple conditions to be checked in order.
z = 8
if z > 10:
    print("z is greater than 10")
elif z == 8:
    print("z is equal to 8")  # This will be printed
else:
    print("z is less than 10 but not 8")

# 4. Nested If Statements
# You can nest if statements within other if statements to add more complexity.
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")  # This will be printed
    else:
        print("a is greater than or equal to 20")
else:
    print("a is 10 or less")

# 5. One-Liner If Statement
# The if statement can be written in a single line if it's simple enough.
b = 25
if b > 20: print("b is greater than 20")  # One-liner if statement

# 6. One-Liner If-Else (Ternary Operator)
# The if-else statement can be written in one line using the ternary operator.
c = 5
result = "Positive" if c > 0 else "Non-Positive"  # If c > 0, result is "Positive", else "Non-Positive"
print(result)  # This will print "Positive"

# 7. Using Boolean Operators in Conditionals
# You can combine conditions with boolean operators: 'and', 'or', and 'not'.
d = 7
if d > 5 and d < 10:
    print("d is between 5 and 10")  # Both conditions are True, so this will be printed

if d < 5 or d == 7:
    print("d is either less than 5 or equal to 7")  # The second condition is True, so this will be printed

if not d < 5:
    print("d is not less than 5")  # Since d is 7, the condition is False, so this is printed

# 8. Multiple Conditions in If (Chained Conditions)
# You can use parentheses to group complex conditions.
e = 50
if (e > 40 and e < 60) or (e == 100):
    print("e is in the range 40-60 or is exactly 100")  # This will be printed because e = 50

# 9. Checking Membership with 'in'
# You can use 'in' to check if a value is in a list, tuple, or string.
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banana is in the list")  # This will be printed

if "grape" not in fruits:
    print("grape is not in the list")  # This will be printed

# 10. Comparing Objects
# You can use comparison operators like ==, !=, >, <, >=, <= to compare values.
f = 100
if f == 100:
    print("f is equal to 100")  # This will be printed

if f != 50:
    print("f is not equal to 50")  # This will be printed

if f >= 100:
    print("f is greater than or equal to 100")  # This will be printed

# 11. Checking Object Type with 'isinstance()'
# You can check the type of an object using the isinstance() function.
g = "Hello"
if isinstance(g, str):
    print("g is a string")  # This will be printed

h = [1, 2, 3]
if isinstance(h, list):
    print("h is a list")  # This will be printed

# 12. Empty Values as False
# In Python, empty values like [], {}, "", 0, and None are considered False.
empty_list = []
if not empty_list:
    print("The list is empty")  # This will be printed because the list is empty

empty_string = ""
if not empty_string:
    print("The string is empty")  # This will be printed

# 13. Conditional Statements with Functions
# You can use conditional statements inside functions to create dynamic behavior.
def check_number(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

print(check_number(10))  # Calls the function, prints 'Positive'
print(check_number(0))   # Calls the function, prints 'Zero'
print(check_number(-5))  # Calls the function, prints 'Negative'

# 14. Using 'pass' in Conditionals
# The 'pass' keyword is used as a placeholder for future code when no action is required.
i = 10
if i > 5:
    pass  # No action is taken, but the condition is valid

# Example conditional outputs:
print(f"x is greater than 5: {x > 5}")
print(f"y is greater than 5: {y > 5}")
print(f"Result of ternary operation: {result}")
print(f"d is between 5 and 10: {d > 5 and d < 10}")