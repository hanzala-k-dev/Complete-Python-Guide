"""Demonstrates Python variable assignment, reassignment, and dynamic typing.
Shows how a single name can hold string, integer, and boolean values.
Includes multiple assignment styles used in practical code.
"""

name = "Hanzala"
print(name)  # Output: Hanzala

# Python can't parse bare identifiers as strings
# name = Saad
# print(name)

# Reassign name to an integer value
name = 4
print(name)  # Output: 4

# Reassign name to a boolean value
name = True
print(name)  # Output: True

# A variable can change type freely in Python
a = 5
print(a)  # Output: 5

a = "Ameen"
print(a)  # Output: Ameen

# Multiple assignments on one line
a = 5
b = 10
c = 20
print(a, b, c)  # Output: 5 10 20

# Parallel assignment from a tuple-like list of values
a, b, c = 5, 10, 20
print(a)  # Output: 5
print(b)  # Output: 10
print(c)  # Output: 20

# Assign the same value to multiple variables
a = b = c = 9
print(a, b, c)  # Output: 9 9 9
