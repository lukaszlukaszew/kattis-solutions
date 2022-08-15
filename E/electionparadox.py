"""Election Paradox"""

# electionparadox

regions = int(input())
voters = sorted(map(int, input().split()))

print(sum(map(lambda x: x//2, voters[:regions//2 + 1]))+sum(voters[regions//2 + 1:]))
