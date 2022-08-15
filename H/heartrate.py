"""Heart Rate"""

# heartrate

cases = int(input())

for i in range(cases):
    b, p = map(float, input().split())
    print(
        format(60 * b / p - 60 / p, ".4f"),
        format(60 * b / p, ".4f"),
        format(60 * b / p + 60 / p, ".4f"),
    )
