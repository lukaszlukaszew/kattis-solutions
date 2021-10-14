"""Crne"""

cuts = int(input())
rows, columns = 1, 1

rows += int(cuts / 2)
columns += cuts - int(cuts / 2)

print(columns * rows)
