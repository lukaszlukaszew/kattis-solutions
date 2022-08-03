"""Another Candies"""

# anothercandies

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    stdin.readline()
    children = int(stdin.readline())
    candies = 0
    for j in range(children):
        candies += int(stdin.readline())

    if candies % children:
        print("NO")
    else:
        print("YES")
