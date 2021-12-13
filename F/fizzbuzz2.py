"""FizzBuzz"""

from sys import stdin

N, M = map(int, stdin.readline().split())
cursor, maximum, correct = 0, -1, 0

for i in range(N):
    line = stdin.readline().split()

    for j in range(1, M + 1):
        correct += int(
            any(
                [
                    j % 3 and j % 5 and line[j - 1] == str(j),
                    j % 3 == 0 and j % 5 == 0 and line[j - 1] == "fizzbuzz",
                    j % 3 == 0 and j % 5 and line[j - 1] == "fizz",
                    j % 3 and j % 5 == 0 and line[j - 1] == "buzz",
                ]
            )
        )

    if maximum < correct:
        maximum = correct
        cursor = i + 1

    correct = 0

print(cursor)
