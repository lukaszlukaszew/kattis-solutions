"""The Grand Adventure"""

cases = int(input())

for i in range(cases):
    adventure, counter = input().replace(".", ""), 0

    while counter <= 2 and adventure:
        if "|t" in adventure:
            adventure, counter = adventure.replace("|t", ""), 0
        elif "*j" in adventure:
            adventure, counter = adventure.replace("*j", ""), 0
        elif "$b" in adventure:
            adventure, counter = adventure.replace("$b", ""), 0
        else:
            counter += 1

    if adventure:
        print("NO")
    else:
        print("YES")
