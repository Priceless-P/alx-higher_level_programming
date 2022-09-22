#!/usr/bin/python3
# 1_calculation.py

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    print(f"{a} + {b} = {add(a,b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
