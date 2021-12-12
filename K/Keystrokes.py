"""Keystrokes"""

from sys import stdin

line = stdin.readline().rstrip()
result, ind = [], 0

for i in line:
    if i == "L":
        ind -= 1
    elif i == "R":
        ind += 1
    elif i == "B":
        result.pop(ind - 1)
        ind -= 1
    else:
        result.insert(ind, i)
        ind += 1

print("".join(result))
