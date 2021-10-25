"""Quick Brown Fox"""

from string import ascii_lowercase

cases = int(input())

for j in range(cases):
    alphabet = set(ascii_lowercase)
    line = set(input().lower())

    if not alphabet.difference(line):
        print("pangram")
    else:
        print("missing " + "".join(sorted(alphabet.difference(line))))
