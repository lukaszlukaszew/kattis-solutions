"""Musical Scales"""

notes = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#") * 3
indices = (0, 2, 4, 5, 7, 9, 11, 12)
scales, result = {}, []

for i in range(int(len(notes)/3)):
    scale = tuple()

    for j in indices:
        scale += (notes[i + j],)

    scales[scale] = notes[i]

notes_count = int(input())
case = input().split()

for k, v in scales.items():
    counter = 0

    for j in case:
        counter += int(j in k)

    if counter == notes_count:
        result.append(v)

if result:
    print(*result)
else:
    print("none")
