"""Simplicity"""

# simplicity

from collections import Counter

word = Counter(input())
simplicity = 0

while len(word) > 2:
    for k, v in word.items():
        if v == min(word.values()):
            simplicity += v
            word.pop(k)
            break

print(simplicity)
