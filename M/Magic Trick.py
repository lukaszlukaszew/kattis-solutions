"""Magic Trick"""

from collections import Counter

print(int(not max(Counter(input()).values()) > 1))
