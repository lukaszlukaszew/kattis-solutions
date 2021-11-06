"""I've Been Everywhere, Man"""

cases = int(input())

for i in range(cases):
    cities_count = int(input())
    cities = set()
    for j in range(cities_count):
        cities.add(input())

    print(len(cities))
