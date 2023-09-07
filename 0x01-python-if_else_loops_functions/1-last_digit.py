#!/usr/bin/python3
"""This program will assign a random signed number to the variable
number each time it is executed and  print the last
digit of the number stored in the variable number."""
import random
number = random.randint(-10000, 10000)
last_num = number % 10
if last_num > 5:
    if number < 0:
        print(
            "Last digit of {} is {} and is greater than {}"
            .format(-number, 10 - last_num, 5))
    else:
        print("Last digit of {} is {} and is greater than 5"
              .format(number, last_num))
if last_num == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, last_num))
if last_num < 6 and last_num != 0:
    if number < 0:
        print(
            "Last digit of {} is {} and is less than {} and not {}"
            .format(number, -(10 - last_num), 6, 0))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, last_num))
