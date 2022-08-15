"""A Rank Problem"""

# rankproblem

teams, matches = map(int, input().split())

order = [f"T{x+1}" for x in range(teams)]


for i in range(matches):
    team1, team2 = input().split()

    if order.index(team1) > order.index(team2):
        order.remove(team2)
        order.insert(order.index(team1) + 1, team2)

print(*order)
