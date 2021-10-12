"""Backspace"""

import sys

line = sys.stdin.readline()
stack = []

for i in line:
    if stack and i == "<":
        stack.pop()
        continue

    stack.append(i)

sys.stdout.write("".join(stack))
