"""DRM Messages"""

# drmmessages

from string import ascii_uppercase

drm = input()
letters, result = ascii_uppercase, ""
drms, shifts, new_drms = {}, {}, {}

for i in range(2):
    if i:
        drms[i] = drm[int(len(drm) / 2):]
    else:
        drms[i] = drm[: int(len(drm) / 2)]

    for j in drms[i]:
        shifts[i] = shifts.get(i, 0) + letters.index(j)

    for j in drms[i]:
        new_drms[i] = (
            new_drms.get(i, "") + letters[(letters.index(j) + shifts[i]) % len(letters)]
        )

for i, val in enumerate(new_drms[0]):
    result += letters[
        (letters.index(val) + letters.index(new_drms[1][i])) % len(letters)
    ]

print(result)
