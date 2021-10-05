"""Death Knight Hero"""

battles = int(input())
battles_lost = 0

for i in range(battles):
    if "CD" in input():
        battles_lost += 1

print(battles - battles_lost)
