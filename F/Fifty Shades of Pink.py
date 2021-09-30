counter = 0
words = ['pink', 'rose']

for i in range(int(input())):
    word = input().lower()
    for j in words:
        if j in word:
            counter += 1
            break

print(counter) if counter else print('I must watch Star Wars with my daughter')

