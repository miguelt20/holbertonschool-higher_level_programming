#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([-1, 3, -7]), 3)
        self.assertAlmostEqual(max_integer([-4, -2, -1, -8, -9]), -1)
        self.assertAlmostEqual(max_integer([105, 89, -7]), 105)
