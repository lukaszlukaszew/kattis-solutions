"""Odd Gnome"""

# oddgnome

groups = int(input())

for i in range(groups):
    gnomes = list(map(int, input().split()))

    for j in range(1, len(gnomes)):
        if gnomes[j + 1] - gnomes[j] != 1:
            print(j + 1)
            break
