#!/usr/bin/python3
# 3_infinite.py

if __name__ == "__main__":
    """ Prints the result of the addition of all arguments """
    import sys
    argvs = imt(sys.argv)
    count = 0
    for i in range (len(sys.argv) - 1):
        count += 1
        print("{}", count)
