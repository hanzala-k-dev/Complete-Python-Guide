"""Shows Python literal types and how their printed values appear.
Includes numeric, string, boolean, None, and collection-related examples.
Focuses on output behavior for learner clarity.
"""

# Numeric literals in various formats
a = 0b1010  # Binary literal (base 2)
b = 100  # Decimal literal (base 10)
c = 0o310  # Octal literal (base 8)
d = 0x12C  # Hexadecimal literal (base 16)

# Floating-point literals
float_1 = 10.5  # Standard decimal notation
float_2 = 1.5e2  # Exponential notation with positive exponent
float_3 = 2.5e-3  # Exponential notation with negative exponent

# Complex number literal
x = 3 + 4j

print(a, b, c, d)  # Output: 10 100 200 300
print(float_1, float_2, float_3)  # Output: 10.5 150.0 0.0025
print(x, x.imag, x.real)  # Output: (3+4j) 4.0 3.0

# String literals using double quotes, single quotes, and triple quotes
string = "\nThis is a python code"
stings = "\nThis is a python code"
char = "\nH"

multiline_string = """This is a multi line python code"""
raw_string = r"This is a raw string"  # Raw string keeps backslashes literal

# Unicode string literal
unicode_string = "\U0001f600\U0001f606\U0001f604"

print(
    string, stings, char
)  # Output: (newline)This is a python code (newline)This is a python code (newline)H
print(multiline_string)  # Output: This is a multi line python code
print(unicode_string)  # Output: 😀😆😄
print(raw_string)  # Output: This is a raw string

# Boolean values participate in arithmetic as 1 (True) and 0 (False)
a = True + 4
b = False + 10
print("a", a)  # Output: a 5
print("b", b)  # Output: b 10

# None literal represents the absence of a value
c = None
print(c)  # Output: None

# variable assigned to None can be used to indicate that it has no value or is uninitialized
k = None
