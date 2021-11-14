"""Tour de France"""

from sys import stdin

while True:
    try:
        f, r = [int(x) for x in stdin.readline().split()]
        front = [int(x) for x in stdin.readline().split()]
        rear = [int(x) for x in stdin.readline().split()]
        ratios, result = [], 0

        for f in front:
            for r in rear:
                ratios.append(r / f)

        ratios.sort()

        for i in range(len(ratios) - 1):
            result = max(result, ratios[i + 1] / ratios[i])

        print(f"{result:.2f}")

    except ValueError:
        break
