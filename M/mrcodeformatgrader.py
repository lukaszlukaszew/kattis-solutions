"""MrCodeFormatGrader"""

# mrcodeformatgrader

from sys import stdin


def prepare_result(container, result_type):
    """Output formatting"""
    result = [f"{result_type}:"]

    while container:
        next_one = container.pop()
        upper = next_one
        while container:
            if upper + 1 == container[-1]:
                upper += 1
                container.pop()
                continue

            if modify_result(next_one, upper, result):
                break

        else:
            if modify_result(next_one, upper, result):
                break

    if len(result) > 2:
        result[-2] = result[-2][:-1]
        result[-1] = result[-1][:-1]
        result.insert(-1, "and")

    return " ".join(result)


def modify_result(start, end, container):
    """Adding prepared values to result"""
    if start == end:
        container.append(f'{start},')
        return True

    if start != end:
        container.append(f"{start}-{end},")
        return True

    return False


C, N = map(int, stdin.readline().split())
errors = set(map(int, stdin.readline().split()))
correct = sorted(set(range(1, C + 1)) - errors, reverse=True)
errors = sorted(errors, reverse=True)


print(prepare_result(errors, "Errors"))
print(prepare_result(correct, "Correct"))
