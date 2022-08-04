"""Thanos"""

# thanos

cases = int(input())

for i in range(cases):
    P, R, F = [int(x) for x in input().split()]
    years = 0
    while P <= F:
        P *= R
        years += 1

    print(years)
