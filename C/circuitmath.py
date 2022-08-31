"""Circuit Math"""

# circuitmath

from string import ascii_uppercase

variable_count = int(input())

line = list(input().split())

variables_values = {}

for i in range(variable_count):
    variables_values[ascii_uppercase[i]] = bool(line[i] == "T")

line = list(input().split())

stack = []

for i, value in enumerate(line):
    if value == "-":
        stack.append(not stack.pop())
    elif value == "+":
        val1, val2 = stack.pop(), stack.pop()
        stack.append(val1 or val2)
    elif value == "*":
        val1, val2 = stack.pop(), stack.pop()
        stack.append(val1 and val2)
    else:
        stack.append(variables_values[value])

print(str(*stack)[0])
