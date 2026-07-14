"""Demonstrates user input and type conversion in Python.

This script shows how input values are read as strings and converted
into integers when required for numeric operations.
"""

# Ask for the user's name and ignore the value in this example
input("Enter your name: ")

# Read age as a string from input
age = input("Enter your age: ")

# Convert numeric input from string to integer for arithmetic
first_num = int(input("Enter first number:"))
second_num = int(input("Enter second number:"))

# Print the values entered
print(first_num)  # Output: first numeric input as integer
print(second_num)  # Output: second numeric input as integer

# Calculate and print the sum of the two numbers
result = first_num + second_num
print(
    "The sum of", first_num, "and", second_num, "is:", result
)  # Output: sum statement with numeric values

# Print the type of a literal value
print(type(4))  # Output: <class 'int'>

# Print the type of the converted input value
print(type(first_num))  # Output: <class 'int'>

# Input returns a string, so this type will be <class 'str'>
a = type(input("Enter a number:"))
print(a)  # Output: <class 'str'>

# Converting input to int before checking its type yields <class 'int'>
a = type(int(input("Enter your age:")))
print(a)  # Output: <class 'int'>

# Convert a floating-point number to integer; fractional part is discarded
a = int(2.5)
print(a)  # Output: 2

# Read two more values as strings and concatenate them
third_num = input("Enter third number:")
fourth_num = input("Enter fourth number:")

result = third_num + fourth_num
print(
    "The sum of", third_num, "and", fourth_num, "is:", result
)  # Output: string concatenation result

# Define a complex number and print it
b = 5 + 6 + 7j
print(b)  # Output: (11+7j)

# Convert a string into a list of characters
print(
    list("Hello World!")
)  # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# Convert a string into a tuple of characters
print(
    tuple("Hello World!")
)  # Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

# Convert a string into a set of unique characters
print(set("Hello World!"))  # Output: unique set of characters from the string
