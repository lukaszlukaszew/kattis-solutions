"""Zyxab"""

# zyxab

from sys import maxsize

lines = int(input())
current_len, current_word = maxsize, "neibb!"

for i in range(lines):
    word = input()
    letters = list(word)

    if not (len(letters) < 5 or len(letters) != len(set(letters))):
        if len(letters) < current_len:
            current_word, current_len = word, len(letters)
        elif len(letters) == current_len:
            current_word = max(word, current_word)

print(current_word)
