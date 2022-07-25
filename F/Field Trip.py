"""Field Trip"""

# fieldtrip

from sys import stdin

N = int(stdin.readline())
sections = list(map(int, stdin.readline().split()))
result, current = [], 0

all_students = sum(sections)

for i, section in enumerate(sections):
    current += section
    if current == all_students // 3:
        current = 0
        result.append(i + 1)
    elif current > all_students // 3:
        result = [-1]
        break

print(*result[:2])
