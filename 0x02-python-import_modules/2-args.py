#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    x = len(args)

    print(f"{x} argument{'s' if x != 1 else ''} {'.'if x == 0 else ':'}")

    if x > 0:
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")
