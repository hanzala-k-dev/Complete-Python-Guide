"""Shows Python operator usage across common operator categories.
Includes arithmetic, comparison, logical, bitwise, assignment, identity, and membership.
Ends with a simple interactive digit-sum exercise for learner practice.
"""

# Arithmetic operators
x = 5
y = 8

print(x + y)  # Output: 13
print(x - y)  # Output: -3
print(x * y)  # Output: 40
print(x / y)  # Output: 0.625
print(x % y)  # Output: 5
print(x**y)  # Output: 390625
print(x // y)  # Output: 0

# Comparison operators
print(x > y)  # Output: False
print(x < y)  # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True
print(x == y)  # Output: False
print(x != y)  # Output: True

# Logical operators
x = True
y = False
print(x or y)  # Output: True
print(x and y)  # Output: False
print(not x)  # Output: False
print(not y)  # Output: True

# Bitwise operators
x = 3
y = 5
print(x & y)  # Bitwise AND -> Output: 1
print(x | y)  # Bitwise OR -> Output: 7
print(3 ^ 5)  # Bitwise XOR -> Output: 6
print(x >> 2)  # Output: 0
print(y << 3)  # Output: 40
print(~x)  # Bitwise NOT -> Output: -4

# Assignment operators
a = 3
print(a)  # Output: 3

a += 3
print(a)  # Output: 6

a -= 3
print(a)  # Output: 3

a *= 3
print(a)  # Output: 9

a /= 3
print(a)  # Output: 3.0

# Identify Operator
a = 3
b = 3
print(a is b)  # Output: True

a = "Hello"
b = "Hello"
print(a is b)  # Output: True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, because they are different objects in memory

a = "Hello-World"
b = "Hello-World"
print(a is b)  # Output: True
print(a is not b)  # Output: False

# Membership Operatores
x = "Karachi"
print("D" in x)  # Output: False
print("D" not in x)  # Output: True

x = [1, 2, 3, 4, 5]
print(1 in x)  # Output: True
print(6 not in x)  # Output: True
print(5 in x)  # Output: True

# Sum of digits of a 3-digit number
number = int(input("Enter a 3 digit number: "))

# Units digit
a = number % 10
number //= 10

# Tens digit
b = number % 10
number //= 10

# Hundreds digit
c = number % 10

print(a + b + c)  # Output: sum of the three digits
