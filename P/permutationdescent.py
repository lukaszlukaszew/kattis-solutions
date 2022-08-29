"""Permutation Descent Counts"""

# permutationdescent

tree = [[1, 0]]

for i in range(1, 101):
    for j in range(i):
        if j == 0:
            tree.append([1] * i)
        elif j == i - 1:
            tree[i][j] = 1
        else:
            tree[i][j] = tree[i - 1][j - 1] * (i - j) + tree[i - 1][j] * (j + 1)

cases = int(input())

for i in range(cases):
    case, x, y = [int(x) for x in input().split()]
    print(case, int(tree[x][y] % 1001113))
