"""Reverse"""

from sys import stdin, stdout

loop = int(stdin.readline())

lines = []

for i in range(loop):
    lines.append(stdin.readline())

for i in range(loop):
    stdout.write(lines.pop())
