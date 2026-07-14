"""Simple number guessing game with user feedback and attempt counting.
The program generates a secret number and prompts until the user wins.
Includes hints and a final attempt count for learner clarity.
"""

import random

# Secret number chosen uniformly from 1 to 100
jackpot = random.randint(1, 100)

# Get the first guess from the user and initialize attempt counter
guess = int(input("Guess a number between 1 and 100: "))
counter = 1

while guess != jackpot:
    # Give a hint whether to guess higher or lower
    if guess < jackpot:
        print("guess higher")  # Output: guess higher when guess is too low
    else:
        print("guess lower")  # Output: guess lower when guess is too high

    # Read the next guess and increment the counter
guess = int(input("Guess a number between 1 and 100: "))
counter += 1

print("Right Guess")  # Output: Right Guess
print("you took", counter, "attempts")  # Output: you took <count> attempts
