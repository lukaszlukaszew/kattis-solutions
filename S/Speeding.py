"""Speeding"""

from sys import stdin

photos = int(stdin.readline())
last_time, last_dist, velocity = 0, 0, 0

for i in range(photos):
    time, dist = [int(x) for x in stdin.readline().split()]
    if i:
        velocity = max(velocity, (dist - last_dist) / (time - last_time))
        last_time, last_dist = time, dist

print(int(velocity))
