"""Sum Kind of Problem"""

cases = int(input())

for i in range(cases):
    K, N = map(int, input().split())
    print(K, int((1 + N) / 2 * N), N ** 2, (1 + N) * N)
