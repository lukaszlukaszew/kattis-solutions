"""The Dragon of Loowater"""

# loowater

from sys import stdin

heads, knights = [int(x) for x in stdin.readline().split()]

while heads + knights:
    h, k = [], []
    cost = 0

    for i in range(heads):
        h.append(int(stdin.readline()))

    for i in range(knights):
        k.append(int(stdin.readline()))

    h.sort(reverse=True)
    k.sort(reverse=True)

    while h and k:
        kk = k.pop()
        if kk >= h[-1]:
            h.pop()
            cost += kk

    if h:
        print("Loowater is doomed!")
    else:
        print(cost)

    heads, knights = [int(x) for x in stdin.readline().split()]
