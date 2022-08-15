"""Snapper Chain (Hard)"""

# snapperhard

cases = int(input())

for i in range(cases):
    n, k = [int(x) for x in input().split()]

    if k - (2 ** n - 1) >= 0 and (k - (2 ** n - 1)) % (2 ** n) == 0:
        result = "ON"
    else:
        result = "OFF"

    print("Case #" + str(i + 1) + ":", result)
