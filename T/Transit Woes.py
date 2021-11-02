"""Transit Woes"""

start, end, buses = map(int, input().split())

walking = [int(x) for x in input().split()]
riding = [int(x) for x in input().split()]
buses_intervals = [int(x) for x in input().split()]

travel_time = 0

for i in range(buses):
    travel_time += walking[i]
    travel_time += (
        buses_intervals[i] - ((start + travel_time) % buses_intervals[i])
    ) % buses_intervals[i]
    travel_time += riding[i]

travel_time += walking[-1]

if travel_time + start > end:
    print("no")
else:
    print("yes")
