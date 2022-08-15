"""Pig Latin"""

# piglatin

import sys

try:
    while True:
        line = input().split()

        for i, word in enumerate(line):
            if word[0] in "aeiouy":
                line[i] = word + "yay"
            else:
                for j, letter in enumerate(word):
                    if letter in "aeiouy":
                        line[i] = word[j:] + word[:j] + "ay"
                        break

        print(*line)

except EOFError:
    sys.exit()
