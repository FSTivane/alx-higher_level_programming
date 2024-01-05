#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from add_0 import add

    count = len(sys.argv) - 1
    sum = 0

    for i in range(count):
        sum = add(sum, int(sys.argv[i+1]))
    print(sum)
