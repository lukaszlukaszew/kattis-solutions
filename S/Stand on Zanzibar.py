"""Stand on Zanzibar"""

# zanzibar

cases = int(input())

for i in range(cases):
    turtles = list(map(int, input().split()))
    result = 0

    for j in range(len(turtles) - 1):
        if turtles[j + 1] - 2 * turtles[j] > 0:
            result += turtles[j + 1] - 2 * turtles[j]

    print(result)
