"""Numbers On a Tree"""

# numbertree


def tree_max_num(max_level):
    """Count all tree nodes"""
    max_num = 0
    for j in range(max_level + 1):
        max_num += 2**j

    return max_num


def next_move(move, current_level, current_position, current_root):
    """Calculate next move"""
    current_position = current_position * 2 - int(move == "L")
    current_root = current_root - 2**current_level - current_position // 2
    current_level += 1

    return current_level, current_position, current_root


line = input()

try:
    height, path = line.split()
    root = tree_max_num(int(height))
    level, position = 0, 1

    for i in path:
        level, position, root = next_move(i, level, position, root)

except ValueError:
    root = tree_max_num(int(line))

print(root)
