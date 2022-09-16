"""Musical Notation"""

# musicalnotation

input()
notation = list(input().split())

dashes = ("F", "D", "B", "g", "e", "a")
notes = ("G", "F", "E", "D", "C", "B", "A")
result = {}

for note in notes:
    result[note] = [f"{note}: "]
    result[note.lower()] = [f"{note.lower()}: "]

for note in notation:
    count = 1 if len(note) == 1 else int(note[1:])

    for k, v in result.items():
        if k == note[0]:
            v.append(f'{"*" * count}{"-" * (k in dashes)}{" " * (k not in dashes)}')
        else:
            v.append(f'{"-" * (k in dashes)*(count+1)}{" "*(k not in dashes)*(count+1)}')

for note in notes:
    print("".join(result[note])[:-1])

for note in notes:
    print("".join(result[note.lower()])[:-1])
