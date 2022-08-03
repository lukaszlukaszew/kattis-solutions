"""Battle Simulation"""

# battlesimulation

from sys import stdin
import re

battle = stdin.readline().rstrip()
responses = {"R": "S", "B": "K", "L": "H"}

battle = re.sub("RBL|RLB|BLR|BRL|LRB|LBR", "C", battle)

for k, v in responses.items():
    battle = re.sub(k, v, battle)

print(battle)
