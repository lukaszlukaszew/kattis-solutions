"""Booking a Room"""

rooms, unavailable = map(int, input().split())
booked = set()

for i in range(unavailable):
    booked.add(int(input()))

available = set(range(1, rooms + 1)).difference(booked)

if available:
    print(available.pop())
else:
    print("too late")
