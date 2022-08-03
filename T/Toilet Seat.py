"""Toilet Seat"""

# toilet

queue = input()

print(2 * queue[1:].count("D") + queue.startswith("DU") - queue.startswith("DD"))
print(2 * queue[1:].count("U") + queue.startswith("UD") - queue.startswith("UU"))
print(queue.count('UD') + queue.count('DU'))
