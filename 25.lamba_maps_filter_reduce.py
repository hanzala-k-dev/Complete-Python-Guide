"""
This file shows how to use lambda functions, map, filter and functools.reduce.
Examples include small predicates, higher-order functions, and aggregation patterns.
"""

import functools

# Simple lambda that squares its input
x = lambda x: x**2
print(x(9))  # 81


# Lambda adding two numbers and its type
a = lambda x, y: x + y
print(a(4, 5))  # 9
print(type(a))  # <class 'function'>


# Predicate lambda: checks whether the first character is 'a'
b_apple = lambda s: s[0] == "a"
print(b_apple("apple"))  # True
print(b_apple("banana"))  # False


# Ternary lambda returning 'Even'/'Odd'
b_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(b_even_odd(3))  # Odd
print(b_even_odd(2))  # Even


L = [11, 14, 27, 21, 23, 56, 78, 39, 45, 29, 28, 30]


def return_sum_basic(L):
    # Compute sums with explicit loops (beginner-friendly)
    even_sum = 0
    odd_sum = 0
    div3_sum = 0
    for i in L:
        if i % 2 == 0:
            even_sum += i
    for i in L:
        if i % 2 != 0:
            odd_sum += i
    for i in L:
        if i % 3 == 0:
            div3_sum += i
    return (even_sum, odd_sum, div3_sum)


print(return_sum_basic(L))  # (206, 195, 162)


def return_sum_hof(func, L):
    # Higher-order function: sum items where func(item) is True
    result = 0
    for i in L:
        if func(i):
            result += i
    return result


x_even = lambda x: x % 2 == 0
y_odd = lambda x: x % 2 != 0
z_div3 = lambda x: x % 3 == 0

print(return_sum_hof(x_even, L))  # 206 (sum of evens)
print(return_sum_hof(y_odd, L))  # 195 (sum of odds)
print(return_sum_hof(z_div3, L))  # 162 (sum of multiples of 3)


L_map = [1, 2, 3, 4, 5, 6, 7]
print(L_map)  # [1, 2, 3, 4, 5, 6, 7]

# map returns an iterator object in Python 3
map_obj = map(lambda x: x * 2, L_map)
print(map_obj)  # <map object ...>
print(list(map(lambda x: x * 2, L_map)))  # [2, 4, 6, 8, 10, 12, 14]
print(
    list(map(lambda x: x % 2 == 0, L_map))
)  # [False, True, False, True, False, True, False]


students = [
    {
        "name": "Jacob Martin",
        "Father name": "Ros Martin",
        "Address": "123 Hills Street",
    },
    {
        "name": "Angela Stevens",
        "Father name": "Robert Stevens",
        "Address": "3 Upper Street London",
    },
    {"name": "Ricky Smart", "Father name": "William Smart", "Address": "Unknown"},
]

print(list(map(lambda student: student["name"], students)))
# ['Jacob Martin', 'Angela Stevens', 'Ricky Smart']


print(list(filter(lambda x: x > 4, L_map)))  # [5, 6, 7]

fruits = ["Apple", "Orange", "Mango", "Guava"]
print(list(filter(lambda fruit: "e" in fruit, fruits)))  # ['Apple', 'Orange']


# functools.reduce to aggregate a sequence
print(functools.reduce(lambda x, y: x + y, L_map))  # 28 (sum of 1..7)


L1 = [12, 34, 56, 11, 21, 58]
print(L1)  # [12, 34, 56, 11, 21, 58]

# find max and min using reduce
print(functools.reduce(lambda x, y: x if x > y else y, L1))  # 58
print(functools.reduce(lambda x, y: x if x < y else y, L1))  # 11
