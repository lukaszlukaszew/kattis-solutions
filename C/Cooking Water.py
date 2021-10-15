"""Cooking Water"""

cases = int(input())
result = 0

range_start, range_finish = [int(x) for x in input().split()]
range_finish += 1

for i in range(cases - 1):
    away_start, away_stop = [int(x) for x in input().split()]

    if (away_start >= range_start and away_start >= range_finish) or (
        range_finish <= away_stop + 1 <= range_start
    ):
        result = 1
        break

if result:
    print("edward is right")
else:
    print("gunilla has a point")
