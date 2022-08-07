"""Watchdog"""

# watchdog

cases = int(input())

for i in range(cases):
    S, H = map(int, input().split())
    hatches, X, Y, result = [], [], [], "poodle"
    for j in range(H):
        x, y = map(int, input().split())
        hatches.append((x, y))
        X.append(x)
        Y.append(y)

    x0, x1, y0, y1 = min(X), max(X), min(Y), max(Y)
    x0, x1 = x0 // 2, min(S, x1 + (S - x1) // 2)
    y0, y1 = y0 // 2, min(S, y1 + (S - y1) // 2)

    for x in range(x0, x1):
        if result == "poodle":
            for y in range(y0, y1):
                if (x, y) not in hatches:
                    r = min(x, S - x, S - y, y)
                    if all(((hatch[1] - y) ** 2 + (hatch[0] - x) ** 2 <= r ** 2 for hatch in hatches)):
                        result = f'{x} {y}'
                        break

    print(result)
