"""Bounding Robots"""

width, length = map(int, input().split())

while width + length:
    actual, robot = [0, 0], [0, 0]

    moves = int(input())

    for i in range(moves):
        instruction, distance = input().split()

        if instruction == "u":
            actual[1] = min(actual[1] + int(distance), length - 1)
            robot[1] += int(distance)
        elif instruction == "d":
            actual[1] = max(0, actual[1] - int(distance))
            robot[1] -= int(distance)
        elif instruction == "l":
            actual[0] = max(0, actual[0] - int(distance))
            robot[0] -= int(distance)
        elif instruction == "r":
            actual[0] = min(actual[0] + int(distance), width - 1)
            robot[0] += int(distance)

    print("Robot thinks", *robot)
    print("Actually at", *actual, "\n")

    width, length = map(int, input().split())
