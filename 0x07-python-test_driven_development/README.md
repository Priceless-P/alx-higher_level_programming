# 0x07. Python - Test-driven development

## Description
This repository contains Python scripts that demonstrate the principles of test-driven development (TDD). Each script corresponds to a specific task and is thoroughly tested to ensure its correctness.

## List of Tasks

1. [Integers addition](0-add_integer.py)
   - Write a function that adds 2 integers.
   - Prototype: `def add_integer(a, b=98):`
   - Requirements:
     - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message "a must be an integer" or "b must be an integer".
     - `a` and `b` must be first casted to integers if they are float.
     - Returns an integer: the addition of `a` and `b`.
     - You are not allowed to import any module.

2. [Divide a matrix](2-matrix_divided.py)
   - Write a function that divides all elements of a matrix.
   - Prototype: `def matrix_divided(matrix, div):`
   - Requirements:
     - `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message "matrix must be a matrix (list of lists) of integers/floats".
     - Each row of the matrix must be of the same size, otherwise raise a `TypeError` exception with the message "Each row of the matrix must have the same size".
     - `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message "div must be a number".
     - `div` can't be equal to 0, otherwise raise a `ZeroDivisionError` exception with the message "division by zero".
     - All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
     - Returns a new matrix.
     - You are not allowed to import any module.

3. [Say my name](3-say_my_name.py)
   - Write a function that prints "My name is <first name> <last name>".
   - Prototype: `def say_my_name(first_name, last_name=""):`
   - Requirements:
     - `first_name` and `last_name` must be strings, otherwise raise a `TypeError` exception with the message "first_name must be a string" or "last_name must be a string".
     - You are not allowed to import any module.

4. [Print square](4-print_square.py)
   - Write a function that prints a square with the character `#`.
   - Prototype: `def print_square(size):`
   - Requirements:
     - `size` is the size length of the square.
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
     - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
     - If `size` is a float and is less than 0, raise a `TypeError` exception with the message "size must be an integer".
     - You are not allowed to import any module.

5. [Text indentation](5-text_indentation.py)
   - Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.
   - Prototype: `def text_indentation(text):`
   - Requirements:
     - `text` must be a string, otherwise raise a `TypeError` exception with the message "text must be a string".
     - There should be no space at the beginning or at the end of each printed line.
     - You are not allowed to import any module.

6. [Max integer - Unittest](6-max_integer.py)
   - Write a function to find and return the max integer in a list of integers.
   - Prototype: `def max_integer(list=[]):`
   - Requirements:
     - If the list is empty, the function returns `None`.
     - You are not allowed to import any module.
   - Includes unit tests using the `unittest` module.

7. [Matrix multiplication](100-matrix_mul.py)
   - Write a function that multiplies 2 matrices.
   - Prototype: `def matrix_mul(m_a, m_b):`
   - Requirements:
     - `m_a` and `m_b` must meet various validation requirements.
     - You are not allowed to import any module.
   - Includes doctests to ensure functionality.

8. [Lazy matrix multiplication](101-lazy_matrix_mul.py)
   - Write a function that multiplies 2 matrices using the NumPy module.
   - Prototype: `def lazy_matrix_mul(m_a, m_b):`
   - Requirements:
     - The same validation requirements as in task 7 apply.
     - You are allowed to use the NumPy module.
   - Includes doctests to ensure functionality.

## Usage
To run each script, simply execute it using Python3, e.g., `python3 0-add_integer.py`.

