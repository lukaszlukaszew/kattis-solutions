"""DVDs"""

# dvds

from sys import stdin

k = int(stdin.readline())

for i in range(k):
    n = int(stdin.readline())
    counter, current = 0, 1
    dvds = list(map(int, stdin.readline().rstrip().split()))

    for j in range(n):
        if dvds[j] != current:
            counter += 1
        else:
            current += 1

    print(counter)
