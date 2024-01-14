#!/usr/bin/python3
"""
Model to test Rectangle class
"""
import unittest
import io
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    class to test Rectangle class
    """
    def setUp(self):
        """setup function"""
        self.r1 = Rectangle(5, 2)
        self.r2 = Rectangle(5, 3, 0, 3, 15)
        self.r3 = Rectangle(2, 3, 1, 1)
        self.r4 = Rectangle(4, 4, 2, 1, 100)

    def test_init(self):
        """unit test for init function"""
        self.assertEqual(self.r2.id, 15)

        with self.assertRaises(TypeError) as context:
            self.bad_r1 = Rectangle('1', 3)
        self.assertRegex(str(context.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as context:
            self.bad_r2 = Rectangle(1, '5')
        self.assertRegex(str(context.exception), 'height must be an integer')

        with self.assertRaises(TypeError) as context:
            self.bad_r3 = Rectangle(1, 5, '2', 3)
        self.assertRegex(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            self.bad_r4 = Rectangle(1, 5, 2, '0')
        self.assertRegex(str(context.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as context:
            self.bad_r2 = Rectangle(-5, 1)
        self.assertRegex(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            self.bad_r2 = Rectangle(5, -1)
        self.assertRegex(str(context.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as context:
            self.bad_r2 = Rectangle(5, 1, -1, 0)
        self.assertRegex(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            self.bad_r2 = Rectangle(5, 1, 0, -2)
        self.assertRegex(str(context.exception), 'y must be >= 0')

    def test_area(self):
        """unit test for area function"""
        self.assertEqual(self.r1.area(), 10)
        self.assertEqual(self.r2.area(), 15)

    def test_display(self):
        """unit test for display function"""
        expected_output_r1 = "#####\n#####\n"
        expected_output_r2 = "\n\n\n#####\n#####\n#####\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output_r1)

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output_r2)

    def test__str(self):
        """unit test for __str__ function"""
        expected_str_r1 = '[Rectangle] ({}) 0/0 - 5/2'.format(self.r1.id)
        expected_str_r2 = '[Rectangle] ({}) 0/3 - 5/3'.format(self.r2.id)

        self.assertEqual(str(self.r1), expected_str_r1)

        self.assertEqual(str(self.r2), expected_str_r2)

    def test_update(self):
        """unit test for update function"""
        self.r4.update(89, 2, 3, 4, 5)
        expected_output_r4 = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(self.r4), expected_output_r4)

        self.r4.update(80, 10, height=5)
        expected_output_r4 = '[Rectangle] (80) 4/5 - 10/3'
        self.assertEqual(str(self.r4), expected_output_r4)

        self.r4.update(y=1, width=2, x=3, id=89)
        expected_output_r4 = '[Rectangle] (89) 3/1 - 2/3'
        self.assertEqual(str(self.r4), expected_output_r4)

    def test_to_dictionary(self):
        """unit test ifor to_dictionary function"""
        r4_dict = self.r4.to_dictionary()
        expected_dict = {'x': 2, 'y': 1, 'id': 100, 'height': 4, 'width': 4}
        self.assertEqual(r4_dict, expected_dict)
        self.assertIsInstance(r4_dict, dict)
        r5 = Rectangle(1, 1)
        r5.update(**r4_dict)
        self.assertIsNot(r5, self.r4)
