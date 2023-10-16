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
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_instantiation(self):
        base_obj = Base()
        self.assertEqual(base_obj.id, 1)

    def test_with_custom_id(self):
        custom_id = 10
        base_obj_with_id = Base(id=custom_id)
        self.assertEqual(base_obj_with_id.id, custom_id)

    def test_rectangle_instantiation(self):
        r = Rectangle(2, 3)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_square_instantiation(self):
        s = Square(4)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 4)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(1, 7, 5, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 9, 2, 8)
        s2 = Square(8, 2, 5, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_one_rectangle(self):
        self.assertEqual(Base.from_json_string('[{"id": 1, "x": 2, "y": 3}]'),
                         [{"id": 1, "x": 2, "y": 3}])

    def test_from_json_string_two_rectangles(self):
        self.assertEqual(Base.from_json_string('[{"id": 1, "x": 2, "y": 3}, \
                                                {"id": 2, "x": 4, "y": 5}]'),
                         [{"id": 1, "x": 2, "y": 3},
                         {"id": 2, "x": 4, "y": 5}])

    def test_create_rectangle(self):
        r_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_create_square(self):
        s_dict = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_load_empty_files(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_saved_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        r_list = Rectangle.load_from_file()
        self.assertEqual(r_list[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(r_list[1].to_dictionary(), r2.to_dictionary())

    def test_load_saved_squares(self):
        s1 = Square(5)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        s_list = Square.load_from_file()
        self.assertEqual(s_list[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(s_list[1].to_dictionary(), s2.to_dictionary())

    def test_load_files_that_do_not_exist(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_save_to_file_csv(self):
        # Test saving an empty list to CSV
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "")
        s1 = Square(2)
        s2 = Square(3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as file:
            data = file.read()
            self.assertIn("1,2,0,0", data)
            self.assertIn("2,3,0,0", data)

    def test_load_from_file_csv(self):
        result = Square.load_from_file_csv()
        self.assertEqual(result, [])
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
