"""Curse the Darkness"""

# cursethedarkness

cases = int(input())

for i in range(cases):
    bookX, bookY = [float(x) for x in input().split()]

    candles_count = int(input())
    result = 0

    for j in range(candles_count):
        candX, candY = [float(x) for x in input().split()]

        if (bookX - candX) ** 2 + (bookY - candY) ** 2 - 8 ** 2 <= 0:
            result = 1

    if result:
        print("light a candle")
    else:
        print("curse the darkness")
