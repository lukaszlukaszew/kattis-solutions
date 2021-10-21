"""Line Them Up"""

cases = int(input())
words = []
increase = []
decrease = []

for i in range(cases):
    words.append(input())

for i in range(cases - 1):
    increase.append(int(words[i] < words[i + 1]))
    decrease.append(int(words[i] > words[i + 1]))

if any(increase) and any(decrease):
    print("NEITHER")
elif all(decrease):
    print("DECREASING")
elif all(increase):
    print("INCREASING")
