#!/usr/bin/python3
# 2_args.py

if __name__ == "__main__":
    """ Prints the number of and the list of its arguments """
    import sys
    total = len(sys.argv)-1
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 arguments:")
    else:
        print(f"{total} arguments:")
    for i in range(total):
        print("{}: {}".format(i + 1, sys.argv[i+1]))
