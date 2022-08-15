"""Calculating Dart Scores"""

# calculatingdartscores


def calculate(n):
    """Calculate dart scores"""
    phrases = {1: "single ", 2: "double ", 3: "triple "}
    for a in range(21):
        for i in range(4):
            for b in range(21):
                for j in range(4):
                    for c in range(21):
                        for k in range(4):
                            if a * i + b * j + c * k == n:
                                result = ""
                                if i and a:
                                    result += phrases[i] + str(a) +"\n"
                                if j and b:
                                    result += phrases[j] + str(b) +"\n"
                                if k and c:
                                    result += phrases[k] + str(c)

                                return result


score = calculate(int(input()))
print(score) if score is not None else print("impossible")
