#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """mports all functions from the file calculator_1.py
     and handles basic operations"""
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(argv[1])
    operator = argv[2]
    num2 = int(argv[3])
    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '+':
        print("{} {} {} = {}".format(num1, operator, num2, add(num1, num2)))
    if operator == '-':
        print("{} {} {} = {}".format(num1, operator, num2, sub(num1, num2)))
    if operator == '*':
        print("{} {} {} = {}".format(num1, operator, num2, mul(num1, num2)))
    if operator == '/':
        print("{} {} {} = {}".format(num1, operator, num2, div(num1, num2)))
