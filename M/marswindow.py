"""Mars Window"""

# marswindow

year = int(input())

result = 0

for i in range(year * 12 + 1, (year + 1) * 12 + 1):
    result = max(result, int((i - 2018 * 12 - 4) % 26 == 0))

if result:
    print("yes")
else:
    print("no")
