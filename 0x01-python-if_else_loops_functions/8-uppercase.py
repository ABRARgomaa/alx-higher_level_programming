#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            upper_c = chr(ord(c) - 32)
            upper += upper_c
        else:
            upper += c
    print("{}" .format(upper))
