"""Tower Construction"""

# tornbygge

brick_count = int(input())
bricks = [int(x) for x in input().split()]

counter = 1

for i in range(1, brick_count):
    if bricks[i - 1] < bricks[i]:
        counter += 1

print(counter)
