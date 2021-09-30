from sys import stdin

k = int(stdin.readline())

for i in range(k):
    n = int(stdin.readline())
    counter, current = 0, 1
    dvds = list(map(int, stdin.readline().rstrip().split()))

    for i in range(n):
        if dvds[i] == current:
            current += 1
            continue
        else:
            counter += 1

    print(counter)
