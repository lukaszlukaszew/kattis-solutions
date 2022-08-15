"""ASCII Figure Rotation"""

# asciifigurerotation

counter = 0

while True:
    lines = int(input())

    if not lines:
        break

    if counter:
        print()

    shape, max_len = [], 0

    for i in range(lines):
        line = input()
        max_len = max(max_len, len(line))
        line = line.replace("|", "x")
        line = line.replace("-", "|")
        line = line.replace("x", "-")
        shape.append(line)

    for i in range(max_len):
        line = ""
        for j in range(lines - 1, -1, -1):
            try:
                line += shape[j][i]
            except IndexError:
                line += " "

        print(line.rstrip())

    counter += 1
