"""Keep it cool"""

n, m, s, d = [int(x) for x in input().split()]
slots = [int(x) for x in input().split()]
refill = [0 for x in range(s)]

while n:
    ind = slots.index(min(slots))
    for i in range(d - slots[ind]):
        if n:
            refill[ind] += 1
            slots[ind] += 1
            n -= 1

if sum(map(lambda x, y: x * int(not y), slots, refill)) >= m:
    print(*refill)
else:
    print("impossible")
