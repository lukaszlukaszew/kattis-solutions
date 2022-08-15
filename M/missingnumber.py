"""Missing Number"""

# missingnumber

from sys import stdin

nums = int(stdin.readline())
line = stdin.readline()
start = 0

for i in range(1, nums + 1):
    if str(i) != line[start: start + len(str(i))]:
        print(i)
        break

    start += len(str(i))
