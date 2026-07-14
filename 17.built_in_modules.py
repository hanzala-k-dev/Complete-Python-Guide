"""Shows examples of Python built-in modules and their common usage.
Covers math, random, time, datetime, and os module helpers.
Includes clear printed outputs so learners can see module behavior.
"""

help("modules")

import math

# math constants and functions
print(math.pi)  # Output: 3.141592653589793
print(math.e)  # Output: 2.718281828459045
print(math.factorial(5))  # Output: 120
print(math.ceil(6.3))  # Output: 7
print(math.floor(6.9))  # Output: 6

import random

# random number generation and shuffling a list
print(random.randint(1, 100))  # Output: random integer between 1 and 100

a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)  # Output: shuffled list order

import time

# time functions
print(time.time())  # Output: current timestamp in seconds
print(time.ctime())  # Output: current time string
print("Hello")  # Output: Hello
time.sleep(5)
print("World")  # Output: World

import datetime

# current date and time
print(datetime.datetime.now())  # Output: current datetime

import os

# current working directory and top-level listing
print(os.getcwd())  # Output: current working directory path
print(os.listdir())  # Output: directory listing
