"""Babelfish"""

dictionary = {}

while True:
    try:
        value, key = input().split()
        dictionary[key] = value
    except ValueError:
        break

while True:
    try:
        print(dictionary.get(input(), "eh"))
    except EOFError:
        break
