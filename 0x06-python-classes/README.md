## README for 0x06. Python - Classes and Objects

This directory contains solutions to various Python tasks related to classes and objects. The tasks cover different aspects of Python classes, such as attribute management, method implementation, and operator overloading. Below is a brief description of each task along with the associated files.

### Task 0: My first square
- File: [0-square.py](0-square.py)
- Description: This task requires the creation of an empty Python class named `Square`.

### Task 1: Square with size
- File: [1-square.py](1-square.py)
- Description: In this task, a Python class named `Square` is created with a private instance attribute `size`. The `size` attribute is initialized through the constructor, and attempts to access it directly or with a different name should raise an AttributeError.

### Task 2: Size validation
- File: [2-square.py](2-square.py)
- Description: The `Square` class from Task 1 is extended to add validation for the `size` attribute. The `size` attribute must be an integer and should not be negative. If an invalid `size` is provided, it raises TypeError or ValueError accordingly.

### Task 3: Area of a square
- File: [3-square.py](3-square.py)
- Description: In this task, the `Square` class is further enhanced with a method `area` that calculates and returns the area of the square.

### Task 4: Access and update private attribute
- File: [4-square.py](4-square.py)
- Description: The `Square` class is modified to include getter and setter methods for the `size` attribute. These methods allow controlled access and modification of the private attribute, enforcing data type and value validation.

### Task 5: Printing a square
- File: [5-square.py](5-square.py)
- Description: The `Square` class is extended to include a method `my_print` that prints a square pattern of '#' characters. The size of the square determines the number of '#' characters printed.

### Task 6: Coordinates of a square
- File: [6-square.py](6-square.py)
- Description: In this task, the `Square` class is further modified to include a private instance attribute `position`, which represents the position of the square. The `my_print` method is adjusted to account for the position of the square.

### Task 7: Singly linked list (Advanced)
- File: [100-singly_linked_list.py](100-singly_linked_list.py)
- Description: This advanced task involves creating a singly linked list using two classes: `Node` to represent individual nodes and `SinglyLinkedList` to represent the entire linked list. The `SinglyLinkedList` class includes a `sorted_insert` method to insert nodes in a sorted order.

### Task 8: Print Square instance (Advanced)
- File: [101-square.py](101-square.py)
- Description: The `Square` class is extended to have a custom string representation such that printing a `Square` instance displays a square pattern using '#' characters.

### Task 9: Compare 2 squares (Advanced)
- File: [102-square.py](102-square.py)
- Description: In this advanced task, the `Square` class is modified to support comparison operators (==, !=, >, >=, <, <=) based on the area of the squares.

### Task 10: ByteCode -> Python #5 (Advanced)
- File: [103-magic_class.py](103-magic_class.py)
- Description: This advanced task requires creating a Python class `MagicClass` that replicates the behavior of a given Python bytecode. The bytecode defines an `__init__` method for initializing a radius and methods for calculating the area and circumference of a circle.

#### NB:
Each task is contained in its respective Python file, and you can find example usage of the classes and methods in the associated main files (e.g., 0-main.py, 1-main.py, etc.).