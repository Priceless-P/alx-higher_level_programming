#!/usr/bin/python3
"""Defines unittests for base.py.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instantiation(self):
        # Test instantiation of a Base object without specifying an ID
        base_obj = Base()
        # The first instance should have an ID of 1
        self.assertEqual(base_obj.id, 1)

        # Test instantiation of a Base object with a specific ID
        custom_id = 10
        base_obj_with_id = Base(id=custom_id)
        self.assertEqual(base_obj_with_id.id, custom_id)

        # Test instantiation of a Rectangle
        r = Rectangle(2, 3)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

        # Test instantiation of a Square
        s = Square(4)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 4)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.load(file), [r1.to_dictionary(),
                                               r2.to_dictionary()])
        s1 = Square(5)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(json.load(file), [s1.to_dictionary(),
                                               s2.to_dictionary()])

    def test_from_json_string(self):
        # self.assertEqual(Base.from_json_string(None), [])
        # self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

        # Test empty string
        # self.assertEqual(Base.from_json_string(""), [])
        # Test string with one dictionary
        self.assertEqual(Base.from_json_string('[{"id": 1, "x": 2, "y": 3}]'),
                         [{"id": 1, "x": 2, "y": 3}])
        # Test string with multiple dictionaries
        self.assertEqual(Base.from_json_string('[{"id": 1, "x": 2, "y": 3}, \
                                                {"id": 2, "x": 4, "y": 5}]'),
                         [{"id": 1, "x": 2, "y": 3},
                         {"id": 2, "x": 4, "y": 5}])

    def test_create(self):
        r_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        s_dict = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_load_from_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        r_list = Rectangle.load_from_file()
        self.assertEqual(r_list[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(r_list[1].to_dictionary(), r2.to_dictionary())
        s1 = Square(5)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        s_list = Square.load_from_file()
        self.assertEqual(s_list[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(s_list[1].to_dictionary(), s2.to_dictionary())

    def test_save_to_file_csv(self):
        # Test saving an empty list to CSV
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "")

        # Test saving a list of objects to CSV
        s1 = Square(2)
        s2 = Square(3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as file:
            data = file.read()
            self.assertIn("1,2,0,0", data)
            self.assertIn("2,3,0,0", data)

    def test_load_from_file_csv(self):
        # Test loading from a non-existent CSV file
        result = Square.load_from_file_csv()
        self.assertEqual(result, [])

        # Test loading from an existing CSV file
        s1 = Square(2)
        s2 = Square(3)
        Square.save_to_file_csv([s1, s2])
        result = Square.load_from_file_csv()
        self.assertIsInstance(result[0], Square)
        self.assertIsInstance(result[1], Square)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
