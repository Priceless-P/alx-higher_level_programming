# 0x05. Python - Exceptions
In this project, i learnt how to effectively handle errors and exceptions in Python code, and how to use try-except blocks to gracefully manage exceptions, handle division by zero, and print informative error messages.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All code files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All code files should end with a new line.
- The first line of all code files should be `#!/usr/bin/python3`.
- A README.md file, at the root of the project folder, is mandatory.
- The code should use the pycodestyle (version 2.8.*).
- All code files must be executable.
- The length of code files will be tested using wc.

## Tasks

1. [Safe list printing](0-safe_print_list.py)
   - Write a function that prints x elements of a list.
   - Prototype: `def safe_print_list(my_list=[], x=0)`

2. [Safe printing of an integers list](1-safe_print_integer.py)
   - Write a function that prints an integer with "{:d}".format().
   - Prototype: `def safe_print_integer(value)`

3. [Print and count integers](2-safe_print_list_integers.py)
   - Write a function that prints the first x elements of a list containing integers.
   - Prototype: `def safe_print_list_integers(my_list=[], x=0)`

4. [Integers division with debug](3-safe_print_division.py)
   - Write a function that divides two integers and prints the result.
   - Prototype: `def safe_print_division(a, b)`

5. [Divide a list](4-list_division.py)
   - Write a function that divides two lists element-wise.
   - Prototype: `def list_division(my_list_1, my_list_2, list_length)`

6. [Raise exception](5-raise_exception.py)
   - Write a function that raises a type exception.
   - Prototype: `def raise_exception()`

7. [Raise a message](6-raise_exception_msg.py)
   - Write a function that raises a name exception with a message.
   - Prototype: `def raise_exception_msg(message="")`

8. [Safe integer print with error message](100-safe_print_integer_err.py)
   - Write a function that prints an integer and handles exceptions.
   - Prototype: `def safe_print_integer_err(value)`

9. [Safe function](101-safe_function.py)
   - Write a function that executes a function safely and handles exceptions.
   - Prototype: `def safe_function(fct, *args)`

10. [ByteCode -> Python #4](102-magic_calculation.py)
    - Implement a Python function that performs the same operations as given Python bytecode.

11. [CPython #2: PyFloatObject](103-python.c)
    - Create C functions that print information about Python lists, bytes, and float objects.
