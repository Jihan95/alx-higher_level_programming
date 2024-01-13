#!/usr/bin/python3
"""
This model contains tests for class base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Class to test base class model
    """
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(10)
        self.b3 = Base()

    def test_init_method(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 10)
        self.assertEqual(self.b3.id, 2)
