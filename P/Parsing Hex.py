"""Parsing Hex"""

from re import findall
from sys import stdin

line = stdin.readline().lower().rstrip()

while line:
    result = findall(r'0x[abcdef0123456789]+', line)

    for i in result:
        print(i, int(i, 16))

    line = stdin.readline().lower().rstrip()
