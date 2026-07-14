"""Shows `for` loop behavior with range and iterable examples.
Demonstrates loop output sequences and a simple factorial series.
Includes explicit results for learners to follow line by line.
"""

# Examples of `range()` converted to lists for visualization
print(list(range(1, 11)))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
print(list(range(1, 11, 2)))  # Output: [1, 3, 5, 7, 9]
print(list(range(10, 0, -1)))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Simple for-loops using range
for i in range(1, 11):
    print(i)  # Output: 1..10

for i in range(1, 11, 2):
    print(i)  # Output: odd numbers 1..9

for i in range(10, 0, -1):
    print(i)  # Output: countdown 10..1

# Iterate over a string (prints each character)
for ch in "Islamabad":
    print(ch)  # Output: each character in Islamabad

# Iterate over different iterable types
for item in [1, 2, 3, 5]:
    print(item)  # Output: list item values

for item in (1, 2, 3, 5):
    print(item)  # Output: tuple item values

for item in {1, 2, 3, 5}:
    print(item)  # Output: set item values (order may vary)

# Compute a series: sum_{i=1..n} i / i!  (demonstrates loop with accumulator)
num = int(input("Enter a Num: "))
result = 0.0
fact = 1
for i in range(1, num + 1):
    fact *= i
    result += i / fact
print(result)  # Output: computed series sum
