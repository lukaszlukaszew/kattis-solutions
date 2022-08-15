"""Keylogger"""

# keylogger

from sys import stdin, stdout

sounds = {"clank": "a", "bong": "b", "click": "c", "tap": "d", "poing": "e", "clonk": "f", "clack": "g", "ping": "h",
          "tip": "i", "cloing": "j", "tic": "k", "cling": "l", "bing": "m", "pong": "n", "clang": "o", "pang": "p",
          "clong": "q", "tac": "r", "boing": "s", "boink": "t", "cloink": "u", "rattle": "v", "clock": "w", "toc": "x",
          "clink": "y", "tuc": "z", "whack": " "}

keys = {"bump": 1, "dink": 1, "thumb": -1}

taps, result, caps = int(stdin.readline()), [], 0

for i in range(taps):
    sound = stdin.readline().rstrip()
    if keys.get(sound, 0):
        caps += keys.get(sound, 0)
    elif sound == "pop" and result:
        result.pop()
    else:
        if caps % 2:
            result.append(sounds.get(sound, "").upper())
        else:
            result.append(sounds.get(sound, "").lower())

stdout.write("".join(result))
