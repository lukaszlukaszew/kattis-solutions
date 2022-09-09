"""Playfair Cipher"""

# playfair

from re import sub

keyphrase, phrase = input(), input()
key, one, two, alphabet = "", {}, {}, "abcdefghijklmnoprstuvwxyz"

for i in keyphrase:
    if i in key or i == " ":
        continue

    key += i
    alphabet = sub(i, "", alphabet)

key += alphabet

for i in range(25):
    one[key[i]] = (i // 5, int(i % 5))
    two[(i // 5, int(i % 5))] = key[i]

phrase = list(sub(" ", "", phrase))

left, right = 0, 1

while len(phrase) > left:
    if len(phrase[left:]) == 1 or phrase[left] == phrase[right]:
        phrase.insert(right, "x")
        continue

    if one[phrase[left]][0] == one[phrase[right]][0]:
        phrase[left] = two[(one[phrase[left]][0], int((one[phrase[left]][1] + 1) % 5))]
        phrase[right] = two[(one[phrase[right]][0], int((one[phrase[right]][1] + 1) % 5))]
    elif one[phrase[left]][1] == one[phrase[right]][1]:
        phrase[left] = two[(int((one[phrase[left]][0] + 1) % 5), one[phrase[left]][1])]
        phrase[right] = two[(int((one[phrase[right]][0] + 1) % 5), one[phrase[right]][1])]
    else:
        lft = (one[phrase[left]][0], one[phrase[right]][1])
        rgt = (one[phrase[right]][0], one[phrase[left]][1])
        phrase[left] = two[lft]
        phrase[right] = two[rgt]

    left += 2
    right += 2

print("".join(phrase).upper())
