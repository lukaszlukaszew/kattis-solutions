"""Wood Cutting"""

from sys import stdin, stdout

test_cases = int(stdin.readline())

for i in range(test_cases):
    customers = int(stdin.readline())
    all_time, local, times = 0, 0, []
    for j in range(customers):
        times.append(sum([int(x) for x in stdin.readline().split()[1:]]))

    times.sort()

    for j in times:
        local += j
        all_time += local

    stdout.write(str(all_time/customers)+'\n')
