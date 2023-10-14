#!/usr/bin/python3
"""Defines the base class"""
import json
import csv
import turtle


class Base:
    """Represents the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is not None:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string
        representation json_string
        """
        if json_string is not None or json_string != []:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all
        attributes already set"""
        if dictionary and dictionary !={ }:
            if cls.__name__ == "Square":
                new = cls(1)
            else:
                new = cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                return []
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                w = csv.DictWriter(file, fieldnames=fields)
                for object in list_objs:
                    w.writerow(object.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of classes instantiated from a CSV file.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(file, fieldnames=fields)
                list_of_dicts = [dict([key, int(value)] for key, value in dict_.items()) \
                                                        for dict_ in list_of_dicts]
                return [cls.create(**dict_) for dict_ in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        my_turtle = turtle.Turtle()
        my_turtle.screen.bgcolor("black")
        my_turtle.pencolor("red")
        my_turtle.shape("turtle")
        my_turtle.pensize(4)
        for rectangle in list_rectangles:
            my_turtle.showturtle()
            my_turtle.up()
            my_turtle.goto(rectangle.x, rectangle.y)
            my_turtle.down()
            for i in range(2):
                my_turtle.forward(rectangle.width)
                my_turtle.left(90)
                my_turtle.forward(rectangle.height)
                my_turtle.left(90)
            my_turtle.hideturtle()

        my_turtle.color("#b5e3d8")
        for sq in list_squares:
            my_turtle.showturtle()
            my_turtle.up()
            my_turtle.goto(sq.x, sq.y)
            my_turtle.down()
            for i in range(2):
                my_turtle.forward(sq.width)
                my_turtle.left(90)
                my_turtle.forward(sq.height)
                my_turtle.left(90)
            my_turtle.hideturtle()
        turtle.exitonclick()
