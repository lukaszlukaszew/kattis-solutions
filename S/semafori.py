"""Semafori"""

# semafori

lights, road = [int(x) for x in input().split()]
timer, road_driven = 0, 0

for i in range(lights):
    D, R, G = [int(x) for x in input().split()]

    timer += D - road_driven
    road_driven = D

    if timer % (R + G) < R:
        timer += R - (timer % (R + G))

print(timer + road - road_driven)
