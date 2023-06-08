#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1

    if argc == 0:
        print("{:d} arguments.".format(0))
    elif argc == 1:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    for i in range(argc):
        print("{:d}: {:s}".format(i + 1, argv[i + 1]))
