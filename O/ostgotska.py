"""Östgötska"""

# ostgotska

counter = 0
line = input().split()
for i in line:
    counter += int("ae" in i)

if counter/len(line) >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
