"""Speed Limit"""

# speedlimit

case = int(input())

while case != -1:
    distance, duration = 0, 0

    for j in range(case):
        s, t = map(int, input().split())

        distance += s * (t - duration)
        duration = t

    print(distance, "miles")
    case = int(input())
