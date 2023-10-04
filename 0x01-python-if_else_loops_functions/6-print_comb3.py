#!/usr/bin/python3
for a in range(0, 9):
    for b in range((a + 1), 10):
        if (a == b):
            continue
        if (a != b):
            if (a != 8):
                print("{}{}, " .format(a, b), end="")
            if (a == 8 and b == 9):
                print("{}{}" .format(a, b))
            if (a == 1 and b == 0):
                continue
