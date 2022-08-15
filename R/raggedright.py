"""Ragged Right"""

# raggedright

penalty, max_len = 0, 0
lens = []

try:
    while True:
        line = input()
        lens.append(len(line))
except EOFError:
    max_len = max(lens)
    lens.pop()

while lens:
    penalty += (max_len - lens.pop()) ** 2

print(penalty)
