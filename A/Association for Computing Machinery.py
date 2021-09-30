N, ind = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]

time, penalty, counter = 0, 0, 0

if times[ind] <= 300:
    time += times[ind]
    counter += 1
    times.pop(ind)

    times.sort()

    for i in range(len(times)):
        if time + sum(times) > 300:
            times.pop()

    while times:
        penalty += time
        time += times[0]
        counter += 1
        times.pop(0)

print(counter, penalty+time)
