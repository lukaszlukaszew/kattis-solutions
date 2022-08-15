"""Eb Alto Saxophone Player"""

# saxophone

notes = {
    "c": {1, 2, 3, 6, 7, 8, 9},
    "d": {1, 2, 3, 6, 7, 8},
    "e": {1, 2, 3, 6, 7},
    "f": {1, 2, 3, 6},
    "g": {1, 2, 3},
    "a": {1, 2},
    "b": {1},
    "C": {2},
    "D": {0, 1, 2, 3, 6, 7, 8},
    "E": {0, 1, 2, 3, 6, 7},
    "F": {0, 1, 2, 3, 6},
    "G": {0, 1, 2, 3},
    "A": {0, 1, 2},
    "B": {0, 1},
}

songs = int(input())

for i in range(songs):
    result, pressed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], set()
    song = input()

    for j in song:
        for x in notes[j] - pressed:
            result[x] += 1
        pressed = notes[j]

    print(*result)
