"""Game of Throwns"""

# throwns

students, moves_count = [int(x) for x in input().split()]
moves = [
    0,
]
student = 0

commands = input().split()[::-1]

while commands:
    move = commands.pop()

    if move == "undo":
        move = int(commands.pop())

        for i in range(move):
            moves.pop()

        student = moves[-1]
        continue

    student = int((student + int(move)) % students)
    moves.append(student)

print(student)
