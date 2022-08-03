"""Delimiter Soup"""

# delimitersoup

input()
delimiters = {"}": "{", "]": "[", ")": "("}
line = input()
check = []

for i, val in enumerate(line):
    if val in "({[":
        check.append(val)
    elif val in ")}]":
        if check and check[-1] == delimiters[val]:
            check.pop()
        else:
            print(val, i)
            break
else:
    print("ok so far")
