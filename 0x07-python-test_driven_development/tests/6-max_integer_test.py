#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


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

    def test_empty_list(self):
        """
        Function to test max_integer function
        in case of input is empty
        """
        lis = []
        self.assertEqual(max_integer(lis), None)

    def test_one_el_list(self):
        """
        Function to test one element list
        """
        lis = [1]
        self.assertEqual(max_integer(lis), max(lis))
