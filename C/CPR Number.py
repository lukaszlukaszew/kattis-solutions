"""CPR Number"""

# cprnummer

values = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
print(int(not bool(sum(map(lambda x, y: x * y, values, map(int, list(input().replace("-", ""))))) % 11)))
