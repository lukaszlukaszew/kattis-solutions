"""Parking"""

# parking

prices = list(map(int, input().split()))
times, cars, result, current = [], set(), 0, 0

for i in range(3):
    a, d = map(int, input().split())
    times.append((a, i))
    times.append((d, i))

times.sort()

for i, (time, car) in enumerate(times):
    result += len(cars) * (time - current) * prices[len(cars)-1]

    if car not in cars:
        cars.add(car)
    else:
        cars.remove(car)

    current = time

print(result)
