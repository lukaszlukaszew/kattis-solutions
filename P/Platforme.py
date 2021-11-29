"""Platforme"""

from sys import stdin

N = int(stdin.readline())
platforms, length = [], 0

for i in range(N):
    platforms.append(tuple(map(int, stdin.readline().split())))

platforms.sort(reverse=True)

while platforms:
    height, *columns = platforms.pop(0)

    for i, val in enumerate(columns):
        for platform in platforms:
            if platform[1] <= val + 0.5 - 1 * i <= platform[2]:
                length += height - platform[0]
                break
        else:
            length += height

print(length)
