"""Jack-O'-Lantern Juxtaposition"""

# jackolanternjuxtaposition

from functools import reduce

print(reduce(lambda x, y: x * y, map(int, input().split())))
