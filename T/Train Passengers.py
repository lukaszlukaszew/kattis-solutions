"""Train Passengers"""

capacity, stations = [int(x) for x in input().split()]
train, possibility = 0, 1

for i in range(stations):
    if possibility:
        out, in_, left = [int(x) for x in input().split()]

        train -= out

        if train < 0 or train + in_ > capacity or (left and capacity - train - in_):
            possibility = 0
        else:
            train += in_
    else:
        break

if possibility and not train:
    print("possible")
else:
    print("impossible")
