#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    else:
        if (arg == 1):
            print("{} argument:" .format(arg))
        if (arg > 1):
            print("{} arguments:" .format(arg))
        for i in range(1, arg + 1):
            print("{:d}: {:s}" .format(i, sys.argv[i]))
