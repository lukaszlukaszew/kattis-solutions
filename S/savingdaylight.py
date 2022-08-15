"""Saving Daylight"""

# savingdaylight

while True:
    try:
        a = input().split()
        sr = list(map(int, a[-2].split(":")))
        ss = list(map(int, a[-1].split(":")))

        duration = 60 * ss[0] + ss[1] - (60 * sr[0] + sr[1])

        print(
            " ".join(a[:3]) + f" {int(duration//60)} hours {int(duration%60)} minutes"
        )

    except EOFError:
        break
