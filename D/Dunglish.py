"""Dunglish"""

# dunglish

from sys import stdin
from collections import defaultdict

trans = {"correct": defaultdict(list), "incorrect": defaultdict(list)}
correct, incorrect = 1, 1

stdin.readline()
sentence = stdin.readline().split()

for i in range(int(stdin.readline())):
    dutch, english, translation = stdin.readline().split()
    trans[translation][dutch].append(english)

for i in sentence:
    for j in range(2):
        globals()["in" * j + "correct"] *= len(trans["incorrect"][i]) * j + len(trans["correct"][i])

incorrect -= correct

if correct + incorrect == 1:
    print(
        *[
            trans[incorrect * "in" + "correct"][i][0]
            if trans[incorrect * "in" + "correct"][i]
            else trans[correct * "in" + "correct"][i][0]
            for i in sentence
        ]
    )
    print(incorrect * "in" + "correct")
else:
    for i in range(2):
        print(globals()[i * "in" + "correct"], i * "in" + "correct")
