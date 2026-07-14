"""Show break, continue, and pass in loop control flow.
Demonstrates exiting loops early, skipping iterations, and placeholder usage.
Includes a prime number example to show loop else behavior.
"""

# break exits the loop when a condition is met
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # Output: 1 2 3 4

# prime number checker using nested loops and break
lower = int(input("lower: "))
upper = int(input("upper: "))
for i in range(lower, upper + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)  # Output: prime numbers in the range

# continue skips the rest of the current iteration
for i in range(1, 11):
    if i == 5:
        continue
    print(i)  # Output: 1 2 3 4 6 7 8 9 10

# continue skips the iteration, so "Hello" is not printed for i == 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)  # Output: i values except 5
    print("Hello")  # Output: Hello for each value except 5

# pass does nothing; often used as a placeholder
for i in range(1, 11):
    pass
