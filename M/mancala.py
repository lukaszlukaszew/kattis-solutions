"""Mancala"""

# mancala

cases = int(input())

for i in range(cases):
    case, counter = map(int, input().split())
    bins = [1]

    while counter - 1:
        if 0 not in bins:
            for j, val in enumerate(bins):
                bins[j] = val - 1
            bins.append(j + 2)
        else:
            if bins[0] == 0:
                bins[0] += 1
            else:
                for j in range(bins.index(0)):
                    bins[j] -= 1
                bins[j + 1] = j + 2

        counter -= 1

    print(case, len(bins))

    for j, val in enumerate(bins):
        print(val, end=" ")

        if not j % 10:
            print()
