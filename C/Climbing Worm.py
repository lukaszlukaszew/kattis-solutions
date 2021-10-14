"""Climbing Worm"""

crawl, fall, height = [int(x) for x in input().split()]
distance, counter = 0, 0

while distance < height:
    distance += crawl
    counter += 1

    if distance >= height:
        break

    distance -= fall

print(counter)
