#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    x = len(args)

    if x == 0:
        print("{:d} arguments.".format(x))

    elif x == 1:
        print("{:d} argument:".format(x))

    else:
        print("{:d} arguments:".format(x))

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
