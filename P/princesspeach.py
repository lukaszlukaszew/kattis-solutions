"""Saving Princess Peach"""

# princesspeach

obstacles_count, mario = [int(x) for x in input().split()]

obstacles = set(range(obstacles_count))
mario_obstacles = set()

for i in range(mario):
    mario_obstacles.add(int(input()))

obstacles = sorted(list(obstacles.difference(mario_obstacles)))

for i in obstacles:
    print(i)

print('Mario got', len(mario_obstacles), 'of the dangerous obstacles.')
