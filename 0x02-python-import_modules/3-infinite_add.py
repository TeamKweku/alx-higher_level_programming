#!/usr/bin/python3
if __name__ == "__main__":
    """ print the total of all commandline args """
    import sys

    total = 0
    argc = len(sys.argv) - 1
    for i in range(argc):
        total += int(sys.argv[i + 1])
    print("{:d}".format(total))
