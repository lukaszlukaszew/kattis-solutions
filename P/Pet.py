"""Pet"""

position, result = 0, 0

for i in range(5):
    line = sum(map(int, input().split()))
    if line > result:
        result = line
        position = i + 1

print(position, result)
