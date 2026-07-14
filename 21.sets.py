"""Demonstrate Python set and frozenset usage.

 shows set creation, operations, and methods,
including immutability of frozensets and set comprehensions.
"""

# Empty set creation
S1 = set()
print(type(S1))  # <class 'set'>

# Set with integers
S1 = {1, 2, 3, 4, 5}
print(S1)  # {1, 2, 3, 4, 5}

# Set with mixed types
S2 = {"Hello", 4.5, True}
print(S2)  # order may vary, e.g. {'Hello', True, 4.5}

# Create a set from a list
s4 = set([1, 2, 3])
print(s4)  # {1, 2, 3}

# Duplicate values are removed in sets
S3 = {1, 1, 2, 2, 3, 3}
print(S3)  # {1, 2, 3}

# Sets can contain immutable elements like tuples
S4 = {(1, 2, 3), "Hello"}
print(S4)  # order may vary, e.g. {(1, 2, 3), 'Hello'}

# Order does not matter for equality
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2)  # True

# Converting set to list and back; set identity changes
S1 = {1, 2, 3, 4, 5}
print(id(S1))  # memory id of the set object

L = list(S1)
L[0] = 100
print(L)  # [100, 2, 3, 4, 5] or similar order depending on list conversion

S1 = set(L)
print(S1)  # {100, 2, 3, 4, 5}
print(id(S1))  # new memory id after rebuilding the set

# Adding elements to a set
S1.add(6)
print(S1)  # {100, 2, 3, 4, 5, 6}
print(id(S1))  # same set object id as before

S1.add(7)
print(S1)  # {100, 2, 3, 4, 5, 6, 7}
print(id(S1))  # same set object id as before

# Update from another iterable
S1.update([5, 6, 7])
print(S1)  # duplicates ignored, remains {100, 2, 3, 4, 5, 6, 7}

# Remove an element
S1 = {2, 3, 4, 5, 6, 7, 100}
S1.remove(100)
print(S1)  # {2, 3, 4, 5, 6, 7}

# pop removes and returns an arbitrary element
print(S1.pop())  # one arbitrary element, e.g. 2
print(S1)  # remaining elements
print(S1.pop())  # another arbitrary element
print(S1)  # remaining elements

# discard does not raise an error if the element is missing
S1.discard(7)
print(S1)  # 7 removed if present

# Clear all elements from the set
S1.clear()
print(S1)  # set()

# Iterate over a set
S1 = {1, 2, 3, 4, 5}
for i in S1:
    print(i)  # prints each element in arbitrary order

# Membership tests
print(1 in S1)  # True
print(1 not in S1)  # False

# Set algebra operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1 | s2)  # union, {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 & s2)  # intersection, {4, 5}
print(s1 - s2)  # difference, {1, 2, 3}
print(s2 - s1)  # difference, {6, 7, 8}
print(s1 ^ s2)  # symmetric difference, {1, 2, 3, 6, 7, 8}

# Additional set methods
S1 = {1, 2, 3, 4, 5}
S2 = {3, 4, 5, 6, 7}
print(len(S1))  # 5
print(min(S1))  # 1
print(max(S1))  # 5
print(sorted(S1))  # [1, 2, 3, 4, 5]
print(sorted(S1, reverse=True))  # [5, 4, 3, 2, 1]
print(S1.union(S2))  # {1, 2, 3, 4, 5, 6, 7}
print(S1.intersection(S2))  # {3, 4, 5}
print(S1.difference(S2))  # {1, 2}
print(S2.difference(S1))  # {6, 7}
print(S1.symmetric_difference(S2))  # {1, 2, 6, 7}
print(S1.isdisjoint(S2))  # False
print(S1.issubset(S2))  # False
print(S1.issuperset(S2))  # False

# Copying a set
s1 = {1, 2, 3}
s2 = s1.copy()
print(s1)  # {1, 2, 3}
print(s2)  # {1, 2, 3}

# frozensets are immutable sets
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(fs1 | fs2)  # frozenset({1, 2, 3, 4, 5})

fs = frozenset([1, 2, frozenset([3, 4])])
print(fs)  # frozenset({1, 2, frozenset({3, 4})})
