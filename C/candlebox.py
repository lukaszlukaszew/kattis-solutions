"""Candle Box"""

# candlebox

D = int(input())
R = int(input())
T = int(input())

ritas, theos = 0, 0
r, t = 4, 3

while ritas + theos != R + T:
    ritas += r

    if r - D == t:
        theos += t
        t += 1

    r += 1

print(R - ritas)
