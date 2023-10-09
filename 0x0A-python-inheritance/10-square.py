#!/usr/bin/python3
"""Defines class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square using BaseGeometry."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            width (int): The width of the new Square.
            height (int): The height of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
