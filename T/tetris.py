"""Tetris"""

# tetris

columns_count, piece = [int(x) for x in input().split()]
columns = [int(x) for x in input().split()]

counter = 0

if piece == 1:
    counter += columns_count
    if columns_count >= 4:
        for i in range(columns_count - 3):
            counter += columns[i] == columns[i + 1] == columns[i + 2] == columns[i + 3]

if columns_count >= 2:
    if piece == 2:
        for i in range(columns_count - 1):
            counter += columns[i] == columns[i + 1]
    elif piece == 3:
        for i in range(columns_count - 1):
            counter += columns[i] == columns[i + 1] + 1
        for i in range(columns_count - 2):
            counter += columns[i] + 1 == columns[i + 1] + 1 == columns[i + 2]
    elif piece == 4:
        for i in range(columns_count - 1):
            counter += columns[i] + 1 == columns[i + 1]
        for i in range(columns_count - 2):
            counter += columns[i] == columns[i + 1] + 1 == columns[i + 2] + 1
    elif piece == 5:
        for i in range(columns_count - 1):
            counter += columns[i] + 1 == columns[i + 1]
            counter += columns[i] == columns[i + 1] + 1
        for i in range(columns_count - 2):
            counter += columns[i] == columns[i + 1] == columns[i + 2]
            counter += columns[i] == columns[i + 1] + 1 == columns[i + 2]
    elif piece == 6:
        for i in range(columns_count - 1):
            counter += columns[i] == columns[i + 1]
            counter += columns[i] == columns[i + 1] + 2
        for i in range(columns_count - 2):
            counter += columns[i] == columns[i + 1] == columns[i + 2]
            counter += columns[i] + 1 == columns[i + 1] == columns[i + 2]
    elif piece == 7:
        for i in range(columns_count - 1):
            counter += columns[i] == columns[i+1]
            counter += columns[i] + 2 == columns[i + 1]
        for i in range(columns_count - 2):
            counter += columns[i] == columns[i + 1] == columns[i + 2]
            counter += columns[i] == columns[i + 1] == columns[i + 2] + 1

print(counter)
