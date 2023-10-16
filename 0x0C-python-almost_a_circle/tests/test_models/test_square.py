#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_valid_instantiation(self):
        s = Square(10, 1, 2, 5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            s = Square("invalid", 1, 2, 5)

    def test_invalid_size_value(self):
        with self.assertRaises(ValueError):
            s = Square(0, 1, 2, 5)

    def test_area(self):
        s = Square(10, 1, 2, 5)
        self.assertEqual(s.area(), 100)

    def test_str(self):
        s = Square(10, 1, 2, 5)
        self.assertEqual(str(s), "[Square] (5) 1/2 - 10")

    def test_update_args(self):
        s = Square(10, 1, 2, 5)
        s.update(1, 20, 3, 4, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(10, 1, 2, 5)
        s.update(id=1, size=20, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        s = Square(10, 1, 2, 5)
        expected_dict = {
            'id': 5,
            'size': 10,
            'x': 1,
            'y': 2
        }
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
