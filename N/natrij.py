"""Natrij"""

# natrij

h, m, s = map(int, input().split(":"))
start = 3600 * h + 60 * m + s

h, m, s = map(int, input().split(":"))
end = 3600 * h + 60 * m + s
end += int(end <= start) * 24 * 3600

h = int((end - start) // 3600)
m = int((end - start - h * 3600) // 60)
s = end - start - h * 3600 - m * 60

print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), sep=":")
