"""Shows how indentation defines blocks and nested conditionals in Python.
Demonstrates the outer if case and how nested indentation controls flow.
Focuses on clear output behavior for each executed print statement.
"""

# Variable to compare in the conditional
name = "abc"

if name == "abc":
    # These lines are inside the first if-block
    print("line1")  # Output: line1
    print("line2")  # Output: line2

    # Nested if: further indented, so it runs only when the outer if is true
    if 4 == 4:
        print("line5")  # Output: line5
else:
    # This else matches the outer if and runs when name != 'abc'
    print("line3")  # Output: line3
