# 0x0A. Python - Inheritance

This repository contains solutions to the tasks in the "0x0A. Python - Inheritance" project.

## Tasks

1. [Lookup](0-lookup.py)
   - Write a function that returns the list of available attributes and methods of an object.
   - Prototype: `def lookup(obj)`.
   - Returns a list object.
   - You are not allowed to import any module.

2. [My List](1-my_list.py), [Test](tests/1-my_list.txt)
   - Write a class `MyList` that inherits from `list`.
   - Public instance method: `def print_sorted(self)` that prints the list, but sorted in ascending order.
   - You can assume that all the elements of the list will be of type int.
   - You are not allowed to import any module.

3. [Exact same object](2-is_same_class.py)
   - Write a function that returns True if the object is exactly an instance of the specified class; otherwise, False.
   - Prototype: `def is_same_class(obj, a_class)`.
   - You are not allowed to import any module.

4. [Same class or inherit from](3-is_kind_of_class.py)
   - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, False.
   - Prototype: `def is_kind_of_class(obj, a_class)`.
   - You are not allowed to import any module.

5. [Only sub class of](4-inherits_from.py)
   - Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, False.
   - Prototype: `def inherits_from(obj, a_class)`.
   - You are not allowed to import any module.

6. [Geometry module](5-base_geometry.py)
   - Write an empty class `BaseGeometry`.
   - You are not allowed to import any module.

7. [Improve Geometry](6-base_geometry.py)
   - Write a class `BaseGeometry` with a public instance method `def area(self)` that raises an Exception with the message "area() is not implemented."
   - You are not allowed to import any module.

8. [Integer validator](7-base_geometry.py), [Test](tests/7-base_geometry.txt)
   - Write a class `BaseGeometry` with public instance methods:
     - `def area(self)` that raises an Exception with the message "area() is not implemented."
     - `def integer_validator(self, name, value)` that validates `value`:
       - You can assume `name` is always a string.
       - If `value` is not an integer, raise a TypeError exception with the message `<name> must be an integer`.
       - If `value` is less than or equal to 0, raise a ValueError exception with the message `<name> must be greater than 0`.
   - You are not allowed to import any module.

9. [Rectangle](8-rectangle.py)
   - Write a class `Rectangle` that inherits from `BaseGeometry` and has an instantiation with width and height.
   - `width` and `height` must be private attributes with no getter or setter.
   - `width` and `height` must be positive integers, validated by the `integer_validator` method.
   - You are not allowed to import any module.

10. [Full rectangle](9-rectangle.py)
    - Write a class `Rectangle` that inherits from `BaseGeometry` (task based on 8-rectangle.py).
    - Instantiation with width and height: `def __init__(self, width, height)`:
      - `width` and `height` must be private attributes with no getter or setter.
      - `width` and `height` must be positive integers, validated by the `integer_validator` method.
    - The `area()` method must be implemented.
    - `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`.

11. [Square #1](10-square.py)
    - Write a class `Square` that inherits from `Rectangle` (task based on 9-rectangle.py).
    - Instantiation with size: `def __init__(self, size)`:
      - `size` must be a private attribute with no getter or setter.
      - `size` must be a positive integer, validated by the `integer_validator` method.
    - The `area()` method must be implemented.

12. [Square #2](11-square.py)
    - Write a class `Square` that inherits from `Rectangle` (task based on 10-square.py).
    - Instantiation with size: `def __init__(self, size)`:
      - `size` must be a private attribute with no getter or setter.
      - `size` must be a positive integer, validated by the `integer_validator` method.
    - The `area()` method must be implemented.
    - `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`.

13. [My integer](100-my_int.py)
    - Write a class `MyInt` that inherits from `int`.
    - `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted.
    - You are not allowed to import any module.

14. [Can I?](101-add_attribute.py)
    - Write a function `add_attribute` that adds a new attribute to an object if it’s possible.
    - Raise a TypeError exception with the message "can't add new attribute" if the object can’t have a new attribute.
    - You are not allowed to use try/except.
    - You are not allowed to import any module.

