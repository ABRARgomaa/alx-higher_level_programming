#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    else:
        print(f"{arg} argument {'s' if arg > 1 else ''}:")
        for i in range(1, arg + 1):
            print(f"{i}: {sys.argv[i]}")
