#!/usr/bin/python3
"""Defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Sqaure"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation
        of the square class"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Overrides the __str__ to return a custom message"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + (str(self.id)) + ")" + " " + str(self.x)\
                      + "/" + str(self.y)
        string += " - " + str(self.width)
        return string
