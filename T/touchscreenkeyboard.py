"""Touchscreen Keyboard"""

# touchscreenkeyboard

keyboard = ("qwertyuiop", "asdfghjkl", "zxcvbnm")

test_cases = int(input())

for i in range(test_cases):
    result = []

    word, words_count = input().split()

    for j in range(int(words_count)):
        entry, full_distance = input(), 0

        for k, val in enumerate(word):
            distance = [0, 0, 0, 0]
            for l, line in enumerate(keyboard):
                if val in line:
                    distance[0] = l
                    distance[1] = line.index(val)
                if entry[k] in line:
                    distance[2] = l
                    distance[3] = line.index(entry[k])

            full_distance += abs(distance[1] - distance[3]) + abs(distance[0] - distance[2])

        result.append((full_distance, entry))

    result.sort()

    for j in result:
        print(j[1], j[0])
