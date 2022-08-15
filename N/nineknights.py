"""Nine Knights"""

# nineknights

board, knights, moved, ops = [], set(), set(), set()
ops_a, ops_b = (1, -1), (2, -2)

for i in range(5):
    board.append(input())
    for j in range(5):
        if board[i][j] == "k":
            knights.add((i, j))

if len(knights) == 9:
    for i in ops_a:
        for j in ops_b:
            ops.add((i, j))
    for i in ops_b:
        for j in ops_a:
            ops.add((i, j))

    for knight in knights:
        for op in ops:
            if knight[0] + op[0] >= 0 and knight[1] + op[1] >= 0:
                moved.add((knight[0] + op[0], knight[1] + op[1]))

    if moved.intersection(knights):
        print("invalid")
    else:
        print("valid")

else:
    print("invalid")
