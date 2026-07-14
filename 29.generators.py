"""
This file demonstrates generator use and contrasts them with full in-memory sequences.
Examples show generator creation, lazy evaluation, and memory advantages.
"""

import sys
import os


# Legacy custom iterable/iterator implementation (stateful)
class mera_range_old:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return mera_iterator_old(self)


class mera_iterator_old:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start += 1
        return current


# Demonstrate memory usage difference between list and range
L = [x for x in range(100000)]
print(f"list size (bytes): {sys.getsizeof(L)}")

x = range(10000000)
print(f"range object size (bytes): {sys.getsizeof(x)}")


# Basic generator function that yields fixed values
def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"


gen = gen_demo()
print(gen)  # <generator object gen_demo at ...>
print(next(gen))  # first statement
print(next(gen))  # second statement
print(next(gen))  # third statement
try:
    print(next(gen))
except StopIteration:
    print("StopIteration Raised")


# Iterate directly over a fresh generator
gen2 = gen_demo()
for i in gen2:
    print(i)  # prints three yielded statements in order


# Generator that yields squares lazily
def square(num):
    for i in range(1, num + 1):
        yield i**2


gen_sq = square(10)
print(next(gen_sq))  # 1
print(next(gen_sq))  # 4
print(next(gen_sq))  # 9
print(next(gen_sq))  # 16
for i in gen_sq:
    print(i)  # prints remaining squares 25..100


# mera_range implemented as a generator (stateless, lazy)
def mera_range(start, end):
    for i in range(start, end):
        yield i


gen_range = mera_range(15, 26)
for i in gen_range:
    print(i)  # prints 15..25

for i in mera_range(15, 26):
    print(i)  # same as above, fresh generator each time


# List comprehension vs generator expression
L_comp = [i**2 for i in range(1, 11)]
print(L_comp)  # full list of squares

gen_exp = (i**2 for i in range(1, 11))
for i in gen_exp:
    print(i)  # prints squares lazily


# Example: generator yielding fake image batches (lazy reader)
def dummy_image_data_reader(folder_path):
    # would normally read image files from folder_path lazily
    yield [1, 2, 3]
    yield [4, 5, 6]


gen_img = dummy_image_data_reader("fake_path")
print(next(gen_img))  # [1, 2, 3]
print(next(gen_img))  # [4, 5, 6]


# Memory comparison of list vs generator for large ranges
L_mem = [x for x in range(100000)]
gen_mem = (x for x in range(100000))
print("Size of L in memory", sys.getsizeof(L_mem))  # large (bytes)
print("Size of gen in memory", sys.getsizeof(gen_mem))  # small (bytes)


# Infinite generator producing even numbers
def all_even():
    n = 0
    while True:
        yield n
        n += 2


even_num_gen = all_even()
print(next(even_num_gen))  # 0
print(next(even_num_gen))  # 2


# Composable generators: fibonacci generator and a squaring chain
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square_chain(nums):
    for num in nums:
        yield num**2


# Sum of squares of first 10 Fibonacci numbers
print(sum(square_chain(fibonacci_numbers(10))))  # 4895
