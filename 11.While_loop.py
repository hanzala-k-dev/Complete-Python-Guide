"""Examples using while-loops: repetition, while-else, and break.

Shows multiplication tables, sum of digits, and average computation using while.
"""

# 1) Simple multiplication table (prints number * i for i = 1..10)
number = int(input("Enter a number: "))
i = 1
while i < 11:
    print(number * i)  # Output: product of the number and current multiplier
    i = i + 1

# 2) Formatted multiplication table (more readable output)
num = int(input("Enter a number: "))
i = 1
while i < 11:
    print(f"{num} x {i} = {num * i}")  # Output: formatted multiplication line
    i += 1

# 3) while-else example: else executes when loop finishes normally
x = 1
while x < 4:
    print(x)  # Output: loop counter values 1, 2, 3
    x = x + 1
else:
    print("limit reached")  # Output: limit reached

# 4) Sum of digits of a positive integer
number = int(input("Enter the number: "))
sum_digits = 0
while number > 0:
    digit = number % 10  # get the last digit
    sum_digits += digit  # add it to the running total
    number //= 10  # remove the last digit
print("sum of digits is:", sum_digits)  # Output: sum of the digits

# 5) Read numbers until 0 is entered; then compute the average
count = 0
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break  # exit loop when sentinel value is entered
    total += number
    count += 1

if count > 0:
    average = total / count
    print(
        "Average of the entered numbers is:", average
    )  # Output: average of entered numbers
else:
    print("No numbers were entered.")  # Output: No numbers were entered.
