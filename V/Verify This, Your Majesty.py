"""Verify This, Your Majesty"""

# queens

from sys import stdin

size = int(stdin.readline())
rows, columns, one, two = set(), set(), set(), set()

for i in range(size):
    x, y = [int(x) for x in stdin.readline().split()]
    rows.add(y)
    columns.add(x)
    one.add(x - y)
    two.add(7 - x - y)

result = {len(rows), len(columns), len(one), len(two)}
result.discard(size)

if result:
    print("INCORRECT")
else:
    print("CORRECT")
