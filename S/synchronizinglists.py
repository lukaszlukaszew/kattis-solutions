"""Synchronizing Lists"""

# synchronizinglists

length_of_lists = int(input())

while length_of_lists:
    first_list, second_list = [], []

    for i in range(length_of_lists):
        first_list.append(int(input()))

    for i in range(length_of_lists):
        second_list.append(int(input()))

    reordered_second_list = second_list.copy()
    second_list.sort(reverse=True)

    for i, val in enumerate(sorted(first_list, reverse=True)):
        reordered_second_list[first_list.index(val)] = second_list[i]

    for i in reordered_second_list:
        print(i)

    print()

    length_of_lists = int(input())
