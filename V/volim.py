"""Volim"""

# volim

player = int(input())
questions = int(input())
boom = 0

for i in range(questions):
    time, answer = input().split()
    boom += int(time)

    if answer == "T" and boom < 210:
        if player == 8:
            player = 1
        else:
            player += 1

    elif boom >= 210:
        break

print(player)
