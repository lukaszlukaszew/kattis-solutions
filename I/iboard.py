"""iBoard"""

# iboard

from sys import stdin

line = stdin.readline().rstrip()

while line:
    counts = [0, 0]

    for i in line:
        char = "0" * (7 - len(bin(ord(i))[2:])) + bin(ord(i))[2:]

        for j in range(2):
            counts[j] += char.count(str(j))

    if counts[0] % 2 or counts[1] % 2:
        print("trapped")
    else:
        print("free")

    line = stdin.readline().rstrip()
