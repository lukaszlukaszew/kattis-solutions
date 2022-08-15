"""Radio Commercials"""

# commercials

from sys import stdin

N, P = [int(x) for x in stdin.readline().split()]
breaks = [int(x) - P for x in stdin.readline().split()]

local = total = breaks[0]

for x in breaks[1:]:
    local = max(x, local + x)
    total = max(total, local)

print(total)
