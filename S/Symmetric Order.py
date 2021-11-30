"""Symmetric Order"""

case = 1
names_count = int(input())

while names_count:
    names = []

    for i in range(names_count):
        names.append(input())

    ascending = [names[x] for x in range(names_count) if not x % 2]
    descending = [names[x] for x in range(names_count) if x % 2][::-1]

    print("SET", case)

    for i in ascending:
        print(i)

    for i in descending:
        print(i)

    names_count = int(input())
    case += 1
