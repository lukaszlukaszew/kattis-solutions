"""Basketball One-on-One"""

match = input()
points = {"A": 0, "B": 0}

for i in range(0, len(match), 2):
    points[match[i]] += int(match[i + 1])

    if max(points.values()) >= 11 and max(points.values()) - min(points.values()) >= 2:
        if points["A"] > points["B"]:
            print("A")
        else:
            print("B")
        break
