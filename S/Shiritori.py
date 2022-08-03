"""Shiritori"""

# shiritori

from sys import stdin

words = int(stdin.readline())
letter, playable, data = "", True, set()

for i in range(words):
    word = stdin.readline().rstrip()

    if word.startswith(letter) and word not in data and playable:
        letter = word[-1]
        data.add(word)
    else:
        if playable:
            if i % 2:
                result = "Player 2 lost"
            else:
                result = "Player 1 lost"

            playable = False

if "result" not in globals():
    result = "Fair Game"

print(result)
