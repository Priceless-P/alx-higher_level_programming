#!/usr/bin/python3
# 3_infinite.py

if __name__ == "__main__":
    """Prints the result of the addition of 
    all arguments. """
    import sys
    count = 0
    for i in range(len(sys.argv) - 1):
        count += int(sys.argv[i + 1])
        print("{}".format(count))
