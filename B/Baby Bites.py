"""Baby Bites"""

bites = int(input())
words = input().split()
counter = 1

for i in range(bites):
    if words[i] == 'mumble':
        counter += 1
    elif int(words[i]) == counter:
        counter += 1
    else:
        print('something is fishy')
        break

if counter == bites + 1:
    print('makes sense')
