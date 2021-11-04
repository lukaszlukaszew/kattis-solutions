"""Shattered Cake"""

width = int(input())
pieces = int(input())
area = 0

for i in range(pieces):
    wi, li = map(int, input().split())
    area += wi * li

print(int(area / width))
