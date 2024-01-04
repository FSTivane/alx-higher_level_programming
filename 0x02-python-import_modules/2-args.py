#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    x = len(args)

    if x == 0:
        print("0 arguments")

    elif x == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(x))

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
