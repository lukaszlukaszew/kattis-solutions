"""Relocation"""

# relocation

N, Q = map(int, input().split())
locations = list(map(int, input().split()))

for i in range(Q):
    request = list(map(int, input().split()))

    if request[0] == 1:
        locations[request[1] - 1] = request[2]
    elif request[0] == 2:
        print(abs(locations[request[1] - 1] - locations[request[2] - 1]))
