"""Just a Minute"""

# justaminute

observations = int(input())
minutes, seconds = [], []

for i in range(observations):
    m, s = map(int, input().split())

    minutes.append(m)
    seconds.append(s)

avg = sum(seconds) / sum(minutes) / 60

if avg <= 1:
    print("measurement error")
else:
    print(avg)
