#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Represents MyInt class that inherits the int class"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, __value):
        """Override != operator with == behavior."""
        return super().__eq__(__value)
