#!/usr/bin/python3
"""
Model to test Square class
"""
import unittest
import io
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    class to test Square class
    """
    def setUp(self):
        self.s1 = Square(5, id=100)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def test_init(self):
        self.assertEqual(self.s1.id, 100)

        with self.assertRaises(TypeError) as context:
            self.bad_s1 = Square('5')
        self.assertRegex(str(context.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as context:
            self.bad_s2 = Square(5, '2', 3)
        self.assertRegex(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            self.bad_s3 = Square(5, 2, '0')
        self.assertRegex(str(context.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as context:
            self.bad_s4 = Square(-5)
        self.assertRegex(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            self.bad_s5 = Square(5, -1, 0)
        self.assertRegex(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            self.bad_s6 = Square(1, 0, -2)
        self.assertRegex(str(context.exception), 'y must be >= 0')

    def test_area(self):
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)

    def test_display(self):
        expected_output_s1 = "#####\n#####\n#####\n#####\n#####\n"
        expected_output_s2 = "  ##\n  ##\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output_s1)

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output_s2)

    def test__str(self):
        expected_str_s1 = '[Square] ({}) 0/0 - 5'.format(self.s1.id)
        expected_str_s2 = '[Square] ({}) 2/0 - 2'.format(self.s2.id)

        self.assertEqual(str(self.s1), expected_str_s1)

        self.assertEqual(str(self.s2), expected_str_s2)

    def test__update(self):
        self.s1.update(10)
        expected_output_s1 = '[Square] ({}) 0/0 - 5'.format(self.s1.id)
        self.assertEqual(str(self.s1), expected_output_s1)

        self.s1.update(1, 2, 3)
        expected_output_s1 = '[Square] ({}) 3/0 - 2'.format(self.s1.id)
        self.assertEqual(str(self.s1), expected_output_s1)

        self.s1.update(1, 2, 3, 4)
        expected_output_s1 = '[Square] (1) 3/4 - 2'
        self.assertEqual(str(self.s1), expected_output_s1)

        self.s1.update(x=12)
        expected_output_s1 = '[Square] (1) 12/4 - 2'
        self.assertEqual(str(self.s1), expected_output_s1)

        self.s1.update(size=7, id=89, y=1)
        expected_output_s1 = '[Square] (89) 12/1 - 7'
        self.assertEqual(str(self.s1), expected_output_s1)
