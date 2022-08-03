"""Early Winter"""

# earlywinter

years, gap = [int(x) for x in input().split()]
gaps = [int(x) for x in input().split()]

if min(gaps) > gap:
    print("It had never snowed this early!")
else:
    for i in range(years):
        if gaps[i] <= gap:
            print(f"It hadn't snowed this early in {i} years!")
            break
