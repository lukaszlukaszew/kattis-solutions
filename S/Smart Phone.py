"""Smart Phone"""

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    word = stdin.readline().rstrip()
    cost = float("inf")
    for j in range(4):
        suggestion = stdin.readline().rstrip()

        for k in range(len(suggestion) + 1):
            if word.startswith(suggestion[: len(suggestion) - k]):
                cost = min(
                    cost,
                    int(bool(j))
                    + k
                    + len(word)
                    - (len(suggestion[: len(suggestion) - k])),
                )
                break

    print(cost)
