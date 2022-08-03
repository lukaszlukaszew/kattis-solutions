"""Chanukah Challenge"""

# chanukah

data_sets = int(input())

for i in range(data_sets):
    K, N = map(int, input().split())

    if N == 1:
        print(K, 2)
    else:
        print(K, int((3 + N) / 2 * N))
