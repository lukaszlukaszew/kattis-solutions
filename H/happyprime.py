"""Happy Happy Prime Prime"""

# happyprime

cases = int(input())
numbers = []


def primes(limit):
    """Prime numbers generator"""
    tab = []
    for i in range(2, limit):
        for j in tab:
            if i % j == 0:
                break
        else:
            yield i
            tab.append(i)


for num in primes(10000):
    numbers.append(num)

for _ in range(cases):
    case, candidate = [int(x) for x in input().split()]
    result = "NO"

    if candidate in numbers:
        current, nums = candidate, []

        while len(str(current**2)) > 1:
            temporary = 0
            for num in str(current):
                temporary += int(num) ** 2

            current = temporary

            if current in nums:
                break

            nums.append(current)

        if current == 1:
            result = "YES"

    print(case, candidate, result)
