"""Prozor"""

R, S, K = [int(x) for x in input().split()]
window, flies = [], 0

for i in range(R):
    window.append(input())

for i in range(R - K + 1):
    for j in range(S - K + 1):
        posibility = ""
        for k in range(K - 2):
            for l in range(K - 2):
                posibility += window[i + 1 + k][j + 1 + l]

        if flies < posibility.count("*"):
            flies = posibility.count("*")
            co = [i, j]

print(flies)

for i in range(R):
    if i in (co[0], co[0] + K - 1):
        window[i] = (
            window[i][: co[1]] + "+" + (K - 2) * "-" + "+" + window[i][co[1] + K:]
        )
    elif i in range(co[0] + 1, co[0] + K - 1):
        window[i] = (
            window[i][: co[1]]
            + "|"
            + window[i][co[1] + 1: co[1] + K - 1]
            + "|"
            + window[i][co[1] + K:]
        )

    print(window[i])
