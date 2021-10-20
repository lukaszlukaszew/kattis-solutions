"""Kemija"""

line = input()
result = ""
i = 0

while i < len(line):
    result += line[i]

    if line[i] in "aeiou":
        i += 2

    i += 1

print(result)
