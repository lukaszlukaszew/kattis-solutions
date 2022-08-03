"""Bus"""

# bus

cases = int(input())

for i in range(cases):
    stops = int(input())

    passengers = 0

    for j in range(stops):
        passengers = passengers * 2 + 1

    print(passengers)
