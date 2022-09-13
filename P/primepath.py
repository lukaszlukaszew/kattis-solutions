"""Prime Path"""

# primepath

from sys import stdin
from collections import deque


def primes(limit):
    """Generate all needed prime numbers"""
    tab = []
    for num in range(2, limit):
        for j in tab:
            if num % j == 0:
                break
        else:
            yield num
            tab.append(num)


def check(queue, prime_nums, visited, end):
    """Check possible paths"""
    temporary_nums = prime_nums.copy()

    while queue and temporary_nums:
        num, cost = queue.popleft()

        for j in temporary_nums:
            if j in visited:
                continue

            letters = 0
            for k in range(4):
                if num[k] == j[k]:
                    letters += 1

            if letters == 3:
                if j == end:
                    return cost + 1

                queue.append((j, cost + 1))
                visited.add(j)

        temporary_nums = temporary_nums - visited

    return "Impossible"


prime_numbers = list(primes(10000))
nums = {str(x) for x in prime_numbers[prime_numbers.index(997) + 1 :]}
cases = int(stdin.readline())

for i in range(cases):
    start, stop = stdin.readline().split()

    if start == stop:
        print(0)
    else:
        primes_visited, working_queue = set(), deque()
        working_queue.append((start, 0))
        print(check(working_queue, nums, primes_visited, stop))
