#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if lastDigit > 5:
    if number < 0:
        print(
            "Last digit of {} is {} and is greater than {}"
            .format(-number, 10-lastDigit, 5))
    else:
        print(
            "Last digit of {} is {} and is greater than {}"
            .format(number, lastDigit, 5))
if lastDigit == 0:
    print("Last digit of {} is {} and is {}".format(number, lastDigit, 0))
if lastDigit < 6 and lastDigit != 0:
    if number < 0:
        print(
            "Last digit of {} is {} and is less than {} and not {}"
            .format(number, -(10-lastDigit), 6, 0))
    else:
        print(
            "Last digit of {} is {} and is less than {} and not {}"
            .format(number, lastDigit, 6, 0))
