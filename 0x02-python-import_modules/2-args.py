#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    position = 1
    if len(argv) == 1:
        print("0 arguments.".format())
    elif len(argv) == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format((len(argv) - 1)))
        for i in argv[1:]:
            print("{}: {}".format(position, i))
            position = position + 1
