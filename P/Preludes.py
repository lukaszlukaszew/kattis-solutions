"""Preludes"""

import sys

pre1 = ("A#", "C#", "D#", "F#", "G#")
pre2 = ("Bb", "Db", "Eb", "Gb", "Ab")
preludes, case = {}, 1

for i in range(5):
    preludes[pre1[i]] = pre2[i]
    preludes[pre2[i]] = pre1[i]

try:
    while True:
        pre, tonality = input().split()
        result = preludes.get(pre, "UNIQUE")
        print(f"Case {case}:", result, tonality * int(result != "UNIQUE"))
        case += 1

except EOFError:
    sys.exit()
