"""Pachyderm Peanut Packing"""

# pachydermpeanutpacking

box_count = int(input())

while box_count:
    boxes, x, y = {}, [], []

    for i in range(box_count):
        x1, y1, x2, y2, size = input().split()
        boxes[i] = (float(x1), float(x2), float(y1), float(y2), size)

    peanut_count = int(input())

    for i in range(peanut_count):
        X, Y, size = input().split()
        X, Y = float(X), float(Y)

        for k, v in boxes.items():
            if (v[0] <= X <= v[1]) and (v[2] <= Y <= v[3]):
                if size == v[4]:
                    print(size, "correct")
                elif size != v[4]:
                    print(size, v[4])
                break
        else:
            print(size, "floor")

    print()
    box_count = int(input())
