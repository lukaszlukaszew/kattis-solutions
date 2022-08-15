"""Sky Islands"""

# skyislands

from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

connected = set(stdin.readline().rstrip().split())
to_check = set()

for i in range(m-1):
    bridge = tuple(sorted(stdin.readline().rstrip().split()))
    if bridge in connected:
        connected.update(bridge)
    else:
        to_check.add(bridge)

while to_check:
    to_remove = set()
    for i in to_check:
        if connected.intersection(set(i)):
            connected.update(i)
            to_remove.add(i)

    if to_remove:
        to_check = to_check.difference(to_remove)
    else:
        print("NO")
        break

else:
    print("YES")
