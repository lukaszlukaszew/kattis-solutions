"""Jury Jeopardy"""

# juryjeopardy

moves = {"L": ((1, 0), (0, -1), (-1, 0), (0, 1)), "R": ((1, 0), (0, 1), (-1, 0), (0, -1))}


def move(instruction):
    """Prepare maze according to moves"""
    global row, rows, column, columns, direction

    if instruction == "B":
        direction = tuple(-1 * d for d in direction)
    elif instruction in ("L", "R"):
        direction = moves[instruction][int((moves[instruction].index(direction) + 1) % 4)]

    row += direction[1]
    column += direction[0]

    if row < 0:
        maze.insert(0, ["#"] * column + ["."] + ["#"] * (columns - column - 1))
        row, rows = 0, rows + 1
    elif row == rows:
        maze.append(["#"] * column + ["."] + ["#"] * (columns - column - 1))
        rows = rows + 1
    elif column < 0:
        for k, value in enumerate(maze):
            if k == row:
                value.insert(0, ".")
            else:
                value.insert(0, "#")
        column, columns = 0, columns + 1
    elif column == columns:
        for k, value in enumerate(maze):
            if k == row:
                value.append(".")
            else:
                value.append("#")
        columns = columns + 1
    else:
        maze[row][column] = "."


cases = int(input())
print(cases)

for i in range(cases):
    path = input()
    maze, row, column, rows, columns, direction = [["."]], 0, 0, 1, 1, (1, 0)

    for j in path:
        move(j)

    maze_length = 0

    for j in maze:
        temp = len(j)
        if j[-1] == ".":
            temp += 1
        maze_length = max(maze_length, temp)

    for j, val in enumerate(maze):
        maze[j] = val + ["#"] * (maze_length - len(val))

    maze.insert(0, ["#"] * maze_length)
    maze.append(["#"] * maze_length)

    print(len(maze), maze_length)
    for j in maze:
        print("".join(j))
