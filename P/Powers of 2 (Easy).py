"""Powers of 2 (Easy)"""

# powersof2easy

n, e = map(int, input().split())
counter, power = 0, str(2**e)

for i in range(n+1):
    if power in str(i):
        counter += 1

print(counter)
