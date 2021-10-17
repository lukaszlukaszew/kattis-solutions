"""Dice Game"""

emma = map(int, input().split())
gunnar = map(int, input().split())
result = sum(map(lambda x, y: x - y, emma, gunnar))

if result < 0:
    print('Emma')
elif result > 0:
    print('Gunnar')
else:
    print('Tie')
