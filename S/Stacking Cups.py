"""Stacking Cups"""

# cups

cups = int(input())
result = []

for i in range(cups):
    line = input().split()

    if line[0].isnumeric():
        result.append((int(line[0]) / 2, line[1]))
    else:
        result.append((int(line[1]), line[0]))

result.sort()

for i in result:
    print(i[1])
