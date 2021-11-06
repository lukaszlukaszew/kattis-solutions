"""Driver's Dilemma"""

capacity, leak, distance = map(float, input().split())

table, result = [], 0

for i in range(6):
    table.append(tuple(map(float, input().split())))

for i in range(5, -1, -1):
    max_speed = table[i][0]

    if max_speed * ((capacity / 2) / (max_speed / table[i][1] + leak)) >= distance:
        print("YES", int(max_speed))
        break

else:
    print("NO")
