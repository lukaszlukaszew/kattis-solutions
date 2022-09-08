"""Glitch Bot"""

# glitchbot

from collections import deque


def make_move(k, start, azimuth):
    """Make desired move"""
    if k == "Forward":
        start[:] = [start[0] + azimuth[0], start[1] + azimuth[1]]
    else:
        azimuth[:] = turns[k][int((turns[k].index(azimuth) + 1) % 4)][:]


turns = {"Left": ([-1, 0], [0, -1], [1, 0], [0, 1]), "Right": ([1, 0], [0, -1], [-1, 0], [0, 1]), "Forward": [0, 1]}

moves = deque()
current = [0, 0]
destination = [int(x) for x in input().split()]
instructions = int(input())
instruction = 1

for i in range(instructions):
    moves.append(input())

while moves:
    move = moves.popleft()
    for key in turns.keys():
        if key != move:
            check, direction = current.copy(), turns["Forward"].copy()
            make_move(key, check, direction)
            for m in moves:
                make_move(m, check, direction)

            if check == destination:
                print(instruction, key)
                break

    else:
        make_move(move, current, turns["Forward"])
        instruction += 1
        continue

    break
