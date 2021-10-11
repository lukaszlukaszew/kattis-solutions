"""Buka"""

from ast import literal_eval

result = ""
for i in range(3):
    result += input()

print(literal_eval(result))
