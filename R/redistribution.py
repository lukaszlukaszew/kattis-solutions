"""Exam Redistribution"""

# redistribution

room_count = int(input())
rooms = [int(x) for x in input().split()]
room_order = sorted([(rooms[i], i+1) for i in range(room_count)], reverse=True)

first_room, tests = room_order[0][0], room_order[0][0]

for i, val in enumerate(room_order):
    if i:
        if tests < val[0]:
            print("impossible")
            break
        first_room -= val[0]

else:
    if first_room > 0:
        print("impossible")
    else:
        print(*(x[1] for x in room_order))
