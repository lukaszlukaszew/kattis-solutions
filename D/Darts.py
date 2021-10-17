"""Darts"""

cases = int(input())

for i in range(cases):
    score = 0
    throws = int(input())

    for j in range(throws):
        x, y = [int(x) for x in input().split()]

        for k in range(10, 0, -1):
            if x ** 2 + y ** 2 <= (20 * (11 - k)) ** 2:
                score += k
                break

    print(score)
