#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """
        The `size` property returns the value of the private `__size` attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Get/set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
