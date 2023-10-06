#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    arg = len(sys.argv) - 1
    for i in range(1, arg + 1):
        add = add + int(sys.argv[i])
    print("{:d}" .format(add))
