"""Islands in the Data Stream"""

# islands


def counter(num):
    """Count islands"""
    global c, stock

    if num > stock[-1]:
        stock.append(num)
        c += 1
    elif num < stock[-1]:
        stock.pop()
        c += 1
        counter(num)


cases = int(input())

for i in range(cases):
    c, stock = 0, [0]
    stream = [int(x) for x in input().split()][2:]

    for j in stream:
        counter(j)

    print(i + 1, int(c / 2))
