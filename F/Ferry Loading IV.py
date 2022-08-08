"""Ferry Loading IV"""

# ferryloading4

cases = int(input())
for i in range(cases):
    l, m = map(int, input().split())
    left, right, crossings = [], [], 0

    for j in range(m):
        L, bank = input().split()
        if bank == "left":
            left.append(int(L))
        else:
            right.append(int(L))

    left, right = left[::-1], right[::-1]

    while left or right:

        load = l * 100
        while load and left:
            if load >= left[-1]:
                load -= left.pop()
            else:
                break

        crossings += 1

        if not (left or right):
            break

        load = l * 100
        while load and right:
            if load >= right[-1]:
                load -= right.pop()
            else:
                break

        crossings += 1

    print(crossings)
