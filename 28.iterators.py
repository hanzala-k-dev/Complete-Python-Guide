"""
This file explores Python iteration mechanics, iterables, and custom iterators.
Examples include memory comparisons, for-loop internals, and a bespoke range iterator.
"""

import sys

# Basic iteration over a list using for-loop
num = [1, 2, 3]
for i in num:
    print(i)  # prints 1, 2, 3 each on its own line


# ITERATORS VS ITERABLES: memory differences between list and range
L = [x for x in range(1, 100)]
for i in L:
    print(i * 2, end=",")
print()
print(f"list size (KB): {sys.getsizeof(L) / 1024}")

# range is an iterable that is memory-efficient (lazy sequence)
x = range(1, 100)
for i in x:
    print(i * 2, end=",")
print()
print(f"range size (KB): {sys.getsizeof(x) / 1024}")

print(type(L))  # <class 'list'>
print(iter(L))  # <list_iterator object at ...>
print(type(iter(L)))  # <class 'list_iterator'>


# PROBING ITERABILITY: some objects are not iterable
a = 2
try:
    for i in a:
        print(i)
except TypeError as e:
    print(f"Error: {e}")  # 'int' object is not iterable


# Inspecting available attributes for common containers
T_tuple = (1, 2, 3)
T_set = {1, 2, 3}
T_dict = {1: 2, 3: 4}
L_list = [1, 2, 3]

print(dir(T_tuple))  # shows tuple methods
print(dir(T_set))  # shows set methods
print(dir(T_dict))  # shows dict methods
print(dir(L_list))  # shows list methods
print(dir(iter(L_list)))  # shows iterator methods (like __next__)


# UNDERSTANDING the for-loop: manual iteration using next()
num_list = [1, 2, 3]
iter_num = iter(num_list)
print(next(iter_num))  # 1
print(next(iter_num))  # 2
print(next(iter_num))  # 3
try:
    print(next(iter_num))
except StopIteration:
    print("StopIteration Raised")  # reached end of iterator


# EMULATING a for-loop with an explicit iterator
def mera_khudka_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


e_dict = {0: 1, 1: 1}
mera_khudka_for_loop(e_dict)  # prints keys 0 and 1


# ITERATOR ALIASING: calling iter() on an iterator returns the same iterator
num_seq = [1, 2, 3]
iter_obj = iter(num_seq)
print(id(iter_obj), "Address of iterator 1")
iter_obj2 = iter(iter_obj)
print(id(iter_obj2), "Address of iterator 2")
# expected: both ids are the same because iter(iterator) returns iterator itself


# BUILDING a custom iterable and iterator: mera_range
class mera_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # return a fresh iterator tied to this iterable
        return mera_range_iterator(self)


class mera_range_iterator:
    def __init__(self, iterable_obj):
        # hold reference to the iterable so we can mutate its state
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start += 1
        return current


for i in mera_range(1, 11):
    print(i)  # prints numbers 1 through 10

x_custom = mera_range(1, 11)
print(type(x_custom))  # <class '...mera_range'>
print(iter(x_custom))  # <mera_range_iterator object at ...>
