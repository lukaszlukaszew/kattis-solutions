"""Pyramid Construction"""


def count_bricks(level):
    """Define required num of 1-sized bricks"""
    counter, bricks = 1, 1

    while counter < level:
        counter += 1
        bricks += 2 * (2 * counter - 2)

    return bricks * 2


def needed(required, n, m):
    """Define required number of bricks of each size"""
    possibles, result, x2 = {}, {}, 1

    while x2 * 2 <= required:
        if not (required - x2 * 2) % 4:
            x4 = int((required - x2 * 2) // 4)
            possibles[x2 + x4] = (x2, x4)
        x2 += 1

    for v in possibles.values():
        x, y = max(0, v[0] - n), max(0, v[1] - m)
        result[x + y] = x, y

    return result[min(result.keys())][0], result[min(result.keys())][1]


H, N, M = [int(x) for x in input().split()]
bricks_needed = count_bricks(H)

print(*needed(bricks_needed, N, M))
