"""Demonstrates nested loops with coordinate output and pyramid patterns.
Includes a star pyramid and numeric palindrome pyramid for visual practice.
Keeps loop structure clear and shows output behavior at each stage.
"""

# 1) Nested loops printing coordinate pairs (i, j)
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)  # Output: coordinate pairs 1 1 through 4 4


# 2) Star pyramid pattern
rows = int(input("Enter rows for star pyramid: "))
for i in range(1, rows + 1):
    # print i stars separated by a space on the same line
    for j in range(i):
        print("*", end=" ")
    print()  # Output: one pyramid row of stars


# 3) Numeric palindrome pyramid
# Example for rows=4:
# 1
# 121
# 12321
# 1234321
rows = int(input("Enter rows for numeric pyramid: "))
for i in range(1, rows + 1):
    # ascending part 1..i
    for j in range(1, i + 1):
        print(j, end="")
    # descending part i-1..1
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()  # Output: one row of the numeric palindrome pyramid
