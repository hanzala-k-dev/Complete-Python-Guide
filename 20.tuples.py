"""Shows tuple creation, immutability, and common tuple operations.
Includes indexing, slicing, conversion from iterables, and tuple functions.
Keeps the original style while documenting output for learners.
"""

# Empty tuple
T1 = ()
print(T1)  # Output: ()

# Tuple with integer elements
T2 = (1, 2, 3, 4, 5)
print(T2)  # Output: (1, 2, 3, 4, 5)

# Tuple with mixed element types
T3 = ("Hello", 4, 5, 6)
print(T3)  # Output: ('Hello', 4, 5, 6)

# Nested tuple containing another tuple
T4 = (1, 2, 3, (4, 5))
print(T4)  # Output: (1, 2, 3, (4, 5))

# A single element tuple requires a trailing comma
T5_wrong = 1
print(type(T5_wrong))  # Output: <class 'int'>
T5_correct = ("Hello",)
print(type(T5_correct))  # Output: <class 'tuple'>

# Create tuples from other iterable types
T6_from_str = tuple("Karachi")
print(T6_from_str)  # Output: ('K', 'a', 'r', 'a', 'c', 'h', 'i')

T6_from_list = tuple([1, 2, 3, 4])
print(T6_from_list)  # Output: (1, 2, 3, 4)

# Indexing and slicing tuples
print(T2[0])  # Output: 1
print(T2[-1])  # Output: 5
print(T2[:4])  # Output: (1, 2, 3, 4)
print(T4[-1][0])  # Output: 4

# Lists are mutable, unlike tuples
L = [1, 2, 3, 4, 5]
L[0] = 100
print(L)  # Output: [100, 2, 3, 4, 5]

# Tuples are immutable, so deleting a tuple variable is possible,
# but individual tuple elements cannot be changed
del T1

# Tuple concatenation and repetition
print(T2 + T3)  # Output: (1, 2, 3, 4, 5, 'Hello', 4, 5, 6)
print(T2 * 3)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Iterate through tuple elements
for i in T2:
    print(i)  # Output: one element per line from T2

# Membership and tuple functions
print(1 in T2)  # Output: True
print(len(T2))  # Output: 5
print(min(T2))  # Output: 1
print(max(T2))  # Output: 5
print(sum(T2))  # Output: 15

# Sorted returns a list
print(sorted(T2))  # Output: [1, 2, 3, 4, 5]
print(sorted(T2, reverse=True))  # Output: [5, 4, 3, 2, 1]

# Tuple methods
t = (1, 2, 3, 4, 5)
print(t.count(50))  # Output: 0
print(t.index(3))  # Output: 2
