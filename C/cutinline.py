"""Cut in Line"""

# cutinline

people = int(input())
line = []

for i in range(people):
    line.append(input())

interactions = int(input())

for i in range(interactions):
    event = input().split()

    if event[0] == "cut":
        line.insert(line.index(event[2]), event[1])
    elif event[0] == "leave":
        line.remove(event[1])

for i in line:
    print(i)
