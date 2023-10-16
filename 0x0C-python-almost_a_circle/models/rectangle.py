#!/usr/bin/python3
"""Defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y of A rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with '#' character"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(1, self.__width):
                print("#", end="")
            print("#")

    def __str__(self):
        """Overrides the __str__ to return a custom message"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + (str(self.id)) + ")" + " " + str(self.__x)\
                      + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for id, arg in enumerate(args):
                if id < len(attributes):
                    setattr(self, attributes[id], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation
        of the rectangle class"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
