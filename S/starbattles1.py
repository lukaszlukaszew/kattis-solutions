"""Star Battles I"""

# starbattles1

areas, stars = {}, set()
checks = {"rows": {}, "columns": {}, "areas": {}}

for i in range(2):
    for r in range(10):
        row = input()
        for c in range(10):
            if i:
                if row[c] == "*":
                    stars.add((r, c))
                    checks["rows"][r] = checks["rows"].get(r, 0) + 1
                    checks["columns"][c] = checks["columns"].get(c, 0) + 1
                    checks["areas"][areas[(r, c)]] = checks["areas"].get(areas[(r, c)], 0) + 1
                    continue
            else:
                areas[(r, c)] = row[c]


for k, v in checks.items():
    if not all((value == 2 for value in v.values())):
        print("invalid")
        break
else:
    for r, c in stars:
        for R, C in stars:
            if (abs(r - R) == 1 and abs(c - C) == 1) or (abs(r - R) == 1 and c == C) or (abs(c - C) == 1 and r == R):
                break
        else:
            continue

        print("invalid")
        break
    else:
        print("valid")
