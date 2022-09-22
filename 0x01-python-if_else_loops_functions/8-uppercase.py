#!/usr/bin/python3
def uppercase(str):

    string = ""
    for i in str:
        test = chr(ord(i)-32)
        if ord(i) >= 97 and ord(i) <= 122:
            string += test
        else:
            string += i
    print("{}".format(string))
