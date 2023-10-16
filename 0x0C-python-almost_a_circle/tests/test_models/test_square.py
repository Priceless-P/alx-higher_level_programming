#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

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
