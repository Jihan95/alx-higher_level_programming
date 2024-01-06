#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integeri


class TestMaxInteger(unittest.TestCase):
    """
    class to test function max_integer
    """
    def test_normal_list(self):
        """
        Function to test the max_integer function
        normal positive numbers
        """
        lis = [5, 6, 10, 80, 3]
        self.assertEqual(max_integer(lis), max(lis))

    def test_list_negative_num(self):
        """
        Function to test the max_integer function
        in case of negative numbers
        """
        lis = [-5, -2, -10, -6]
        self.assertEqual(max_integer(lis), max(lis))

    def test_mixed_list(self):
        """
        Function to test max_integer function
        mixed types input
        """
        lis = [-1, 0, -8, 8, -2]
        self.assertEqual(max_integer(lis), max(lis))

    def test_none_list(self):
        """
        Function to test max_integer function
        in case of input is None
        """
        lis = None
        self.assertEqual(max_integer(lis), None)

    def test_not_list(self):
        """
        Function to test max_integer function
        in case of input is not alist or containing
        non numbers elements
        """
        not_list = (5, 10)
        lis = ['cat', '1', '2']
        self.assertRaises(TypeError, max_integer, not_list)
        self.assertRaises(ValueError, max_integer, lis)
