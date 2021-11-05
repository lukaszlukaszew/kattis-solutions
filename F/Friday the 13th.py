"""Friday the 13th"""

cases = int(input())

for i in range(cases):
    y = [int(x) for x in input().split()]
    m = [int(x) for x in input().split()]
    d, counter = 0, 0

    for j, val in enumerate(m):
        if val >= 13 and (d + 13) % 7 == 6:
            counter += 1

        d += val

    print(counter)
