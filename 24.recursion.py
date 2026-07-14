"""
This file shows recursive function examples alongside an iterative multiplication example.
Each example includes comments and output notes so learners can clearly follow the behavior.
"""

import time


def multiply(a, b):
    # Multiply a by b using repeated addition.
    result = 0
    for _ in range(b):
        result += a
    print(result)  # prints 12 for multiply(3, 4)


multiply(3, 4)


def mul(a, b):
    # Multiply a by b using recursion.
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)


print(mul(3, 4))  # prints 12


def fact(number):
    # Compute factorial of number using recursion.
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)


print(fact(5))  # prints 120


def palin(text):
    # Check whether a string is a palindrome using recursion.
    if len(text) <= 1:
        print("palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("not a palindrome")


palin("madam")  # palindrome
palin("malayalam")  # palindrome
palin("python")  # not a palindrome
palin("abba")  # palindrome


def fib(m):
    # Recursive Fibonacci definition.
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)


print(fib(12))  # prints 233

start = time.time()
print(fib(12))  # prints 233 again
print(time.time() - start)  # time taken for the first recursive call

print(fib(24))  # prints 75025
print(time.time() - start)  # cumulative time since start

print(fib(36))  # prints 2971215073
print(time.time() - start)  # cumulative time since start


def memo(m, d):
    # Use memoization to compute Fibonacci values efficiently.
    if m in d:
        return d[m]
    else:
        d[m] = memo(m - 1, d) + memo(m - 2, d)
        return d[m]


d = {0: 1, 1: 1}
print(memo(48, d))  # prints 4807526976

print(memo(48, d))  # prints 4807526976, retrieved from memo
print(time.time() - start)  # cumulative time since start

print(memo(500, d))  # prints a large Fibonacci number quickly with memoization
print(time.time() - start)  # cumulative time since start

print(memo(1000, d))  # prints an even larger Fibonacci number quickly
print(time.time() - start)  # cumulative time since start

print(d)  # prints the memo dictionary with all computed Fibonacci entries


def powerset1(xs):
    # Generate the power set of a sequence recursively.
    res = [[]]
    if len(xs) <= 0:
        return "Please Enter a parameter"
    if len(xs) == 1:
        res.append([xs[0]])
        return res
    else:
        z = []
        for i in powerset1(xs[1:]):
            z.append(i)
            z.append([xs[0]] + i)
        return z


final = powerset1("123")
print(
    final
)  # prints [[], ['3'], ['2'], ['2', '3'], ['1'], ['1', '3'], ['1', '2'], ['1', '2', '3']]
print(len(final))  # prints 8 because power set of 3 items has 2^3 subsets
