"""Alphabet Spam"""

# alphabetspam

import string

line = input()
counter = 0

check = ["_", string.ascii_lowercase, string.ascii_uppercase]

for i in check:
    current = 0
    for j in i:
        current += line.count(j)
    print(float(format(current / len(line), ".6f")))
    counter += current

print(float(format((len(line) - counter) / len(line), ".6f")))
