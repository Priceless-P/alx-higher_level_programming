#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json: The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
