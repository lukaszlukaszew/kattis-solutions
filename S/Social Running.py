"""Social Running"""

# socialrunning

number = int(input())
distances, minimum = [], float("inf")

for i in range(number):
    distances.append(int(input()))

for i in range(number):
    check = distances[i] + distances[(number - 2 + i) % number]
    if check < minimum:
        minimum = check

print(minimum)
