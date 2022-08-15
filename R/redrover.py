"""Red Rover"""

# redrover

line = input()
minimum = len(line)


for i in range(len(line)):
    for j in range(len(line) - i):
        minimum = min(
            minimum,
            len(line) - ((line.count(line[i: i + j]) - 1) * len(line[i: i + j])) + line.count(line[i: i + j]),
        )

print(minimum)
