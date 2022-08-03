"""Skener"""

# skener

r, c, y, x = map(int, input().split())

for i in range(r):
    line = input()
    for j in range(y):
        result_line = ""
        for k in line:
            result_line += k * x
        print(result_line)
