"""Prsteni"""


def nwd(a, b):
    """Greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


N = int(input())
radius, *radiuses = map(int, input().split())

for i in range(1, N):
    nwd_result = nwd(radius, radiuses[i - 1])
    print(f"{int(radius / nwd_result)}/{int(radiuses[i-1] / nwd_result)}")
