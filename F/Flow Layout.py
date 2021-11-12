"""Flow Layout"""

width = int(input())

while width:
    current_width, result_width = 0, 0
    current_height, result_height = 0, 0

    w, h = [int(x) for x in input().split()]

    while w != -1 and h != -1:
        if current_width + w > width:
            result_height += current_height
            result_width = max(current_width, result_width)
            current_width, current_height = w, h
        else:
            current_width += w
            current_height = max(current_height, h)

        w, h = [int(x) for x in input().split()]

    print(max(current_width, result_width), "x", result_height + current_height)

    width = int(input())
