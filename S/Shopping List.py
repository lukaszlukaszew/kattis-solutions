"""Shopping List"""

from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
base = set(stdin.readline().rstrip().split())

for i in range(n - 1):
    base = base & set(stdin.readline().rstrip().split())

base = sorted(base)

print(len(base))
for i in base:
    print(i)
