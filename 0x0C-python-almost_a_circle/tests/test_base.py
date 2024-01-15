#!/usr/bin/python3
"""
This model contains tests for class base
"""
import unittest
from json import loads, load
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Class to test base class model
    """
    def setUp(self):
        """setup function"""
        self.b1 = Base()
        self.b2 = Base(10)
        self.b3 = Base()
        self.r1 = Rectangle(3, 2, 1, 1, 50)
        self.s1 = Square(5, 1, 1, 55)

    def test_init_method(self):
        """Method init unittest"""
        self.assertEqual(self.b2.id, 10)

    def test_to_json_string(self):
        """ unittest for to_json_string function"""
        self.assertEqual(Base.to_json_string(None), '[]')

        self.assertEqual(Base.to_json_string([]), '[]')

        r1_dict = self.r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        expected_dict = sorted([
            {'x': 1, 'width': 3, 'id': 50, 'height': 2, 'y': 1}
            ])
        self.assertEqual(sorted(loads(
            json_dict.replace("'", "\"")
            )), expected_dict)
        self.assertIsInstance(json_dict, str)

        s1_dict = self.s1.to_dictionary()
        json_dict = Base.to_json_string([s1_dict])
        expected_dict = sorted([{'x': 1, 'size': 5, 'id': 55, 'y': 1}])
        self.assertEqual(sorted(loads(
            json_dict.replace("'", "\"")
            )), expected_dict)
        self.assertIsInstance(json_dict, str)

    def test_from_json_string(self):
        """unit test for from_json_string method"""
        input_list = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]

        self.assertEqual(Rectangle.from_json_string(None), [])

        self.assertEqual(Rectangle.from_json_string([]), [])

        json_list = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_list)
        self.assertEqual(input_list, output_list)

        input_list = [
                {'id': 89, 'size': 5},
                {'id': 7, 'size': 7}
                ]

        self.assertEqual(Square.from_json_string(None), [])

        self.assertEqual(Square.from_json_string([]), [])

        json_list = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_list)
        self.assertEqual(input_list, output_list)

    def test_create(self):
        """unit test for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

        s1 = Square(5, 3, 2)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """unit test for load from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(
                sorted(
                    (r.width, r.height, r.x, r.y)
                    for r in list_rectangles_input
                    ),
                sorted(
                    (r.width, r.height, r.x, r.y)
                    for r in list_rectangles_output
                    )
                )

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(
                sorted((s.size, s.x, s.y) for s in list_squares_input),
                sorted((s.size, s.x, s.y) for s in list_squares_output)
                )

    def test_save_to_file(self):
        """unit test for save_to_file method"""

        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
