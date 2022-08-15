"""Beat the Spread!"""

# beatspread

cases = int(input())

for i in range(cases):
    summ, diff = map(int, input().split())

    x = diff + (summ - diff) / 2
    y = (summ - diff) / 2

    if any([y < 0, y % 1 != 0, x < 0, x % 1 != 0]):
        print("impossible")
    else:
        print(int(max(x, y)), int(min(x, y)))
