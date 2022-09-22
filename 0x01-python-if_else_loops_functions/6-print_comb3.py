#!/usr/bin/python3
for i in range(0, 9):
    for n in range(10):
        if int(str(n) + str(i)) > int(str(i) + str(n)):
            if int(str(i) + str(n)) < 89:
                print("{}".format(str(i) + str(n)), end=", ")
            else:
                print("{}".format(str(i) + str(n)))
