"""Guess the Number"""

# guess

import sys

minimum, maximum, guess = 1, 1000, 500

for i in range(10):
    print(guess)
    answer = input()

    if answer != "correct":
        if answer == "lower":
            maximum = guess - 1
        elif answer == "higher":
            minimum = guess + 1

        guess = int((minimum + maximum) / 2)

    else:
        sys.exit()
