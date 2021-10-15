"""Cryptographer's Conundrum"""

word = input()
result = 0

for i, w in enumerate(word):
    if not any(
        (i % 3 == 0 and w == "P", i % 3 == 1 and w == "E", i % 3 == 2 and w == "R")
    ):
        result += 1

print(result)
