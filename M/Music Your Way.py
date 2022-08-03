"""Music Your Way"""

# musicyourway

headers = input().split()

songs_count = int(input())
songs = []

for i in range(songs_count):
    songs.append(input().split())

attributes_count = int(input())
attributes = []

for i in range(attributes_count):
    attributes.append(input())

for i in range(attributes_count):
    print(*headers)
    songs.sort(key=lambda x: (x[headers.index(attributes[i])]))
    for j in songs:
        print(*j)
    print()
