"""Show common Python built-in functions with their printed results.
Demonstrates type checking, numeric helpers, sequence operations, and introspection.
Keeps examples direct so learners can connect each built-in to its output.
"""

print("Hello World")  # Output: Hello World

# Read a name from the user (returned value is ignored here)
input("Enter your name: ")

# type() shows the type of a value
a = 3
print(type(a))  # Output: <class 'int'>

a = 3.5
print(type(a))  # Output: <class 'float'>

a = True
print(type(a))  # Output: <class 'bool'>

# Convert string to integer
print(int("5"))  # Output: 5

# Numeric built-in functions
print(abs(4))  # absolute value -> Output: 4
print(abs(-4))  # Output: 4
print(pow(2, 3))  # exponentiation -> Output: 8
print(pow(2, -3))  # Output: 0.125

# min() and max() work on iterables and strings
print(min([2, 1, 3, 0]))  # Output: 0
print(max([2, 1, 3, 0]))  # Output: 3
print(min("kolkata"))  # Output: a
print(max("kolkata"))  # Output: t

# round() rounds to nearest integer or to a fixed number of decimals
c = 22 / 7
print(c)  # Output: 3.142857142857143
print(round(c))  # Output: 3
print(round(c, 2))  # Output: 3.14

# divmod() returns quotient and remainder as a tuple
print(divmod(5, 2))  # Output: (2, 1)

# Convert integers to binary, octal, hexadecimal strings
print(bin(4))  # Output: 0b100
print(oct(4))  # Output: 0o4
print(hex(4))  # Output: 0x4

# id() returns the identity of an object
a = 3
print(id(a))  # Output: memory address identifier

# ord() returns the Unicode code point of a character
print(ord("A"))  # Output: 65
print(ord("a"))  # Output: 97

# len() returns the length of sequences
print(len("Kolkata"))  # Output: 7
print(len([1, 2, 3]))  # Output: 3

# sum() adds numbers in an iterable
print(sum([1, 2, 3, 4, 5]))  # Output: 15
print(sum({1, 2, 3, 4, 5}))  # Output: 15

# help() shows the documentation for print()
help(print)  # Output: help text for print()
