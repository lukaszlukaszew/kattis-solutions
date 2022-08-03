"""Imperial Measurement"""

# measurement

val, start, _, stop = input().split()
val = int(val)

names_long = ["thou", "inch", "foot", "yard", "chain", "furlong", "mile", "league"]
names_short = ["th", "in", "ft", "yd", "ch", "fur", "mi", "lea"]
values = [1, 1000, 12, 3, 22, 10, 8, 3]

start = names_long.index(start) if start in names_long else names_short.index(start)
stop = names_long.index(stop) if stop in names_long else names_short.index(stop)

while start != stop:
    if start < stop:
        val /= values[start + 1]
        start += 1
    elif start > stop:
        val *= values[start]
        start -= 1

print(val)
