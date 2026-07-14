"""Demonstrates Python keywords versus valid identifier names.
Shows the reserved keyword list and safe variable naming patterns.
Highlights why keywords like False cannot be reused as names.
"""

import keyword

# Print the list of Python reserved keywords
print(keyword.kwlist)  # Output: ['False', 'None', 'True', ...]

# Valid identifier starting with a letter
name = "Hanzala"
print(name)  # Output: Hanzala

# Valid identifier using underscore only
_ = "Hanzala"
print(_)  # Output: Hanzala

# Valid identifier containing an underscore
first_name = "Hanzala"
print(first_name)  # Output: Hanzala

# Invalid identifier example: keywords cannot be used as variable names
# False = 'Hanzala'  # This would raise a SyntaxError if uncommented
# print(False)
