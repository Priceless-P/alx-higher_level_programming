#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_valid_instantiation(self):
        r = Rectangle(10, 20, 1, 2, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 20, 1, 2, 5)

    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20, 1, 2, 5)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid", 1, 2, 5)

    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0, 1, 2, 5)

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "invalid", 2, 5)

    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -1, 2, 5)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 1, "invalid", 5)

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 1, -2, 5)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_str(self):
        r = Rectangle(10, 20, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 10/20")

    def test_update_args(self):
        r = Rectangle(10, 20, 1, 2, 5)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 1, 2, 5)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 1, 2, 5)
        expected_dict = {
            'id': 5,
            'width': 10,
            'height': 20,
            'x': 1,
            'y': 2
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
