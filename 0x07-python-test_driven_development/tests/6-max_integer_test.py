#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for integers"""

    def test_max_integer(self):
        """cases"""
        self.assertEqual(max_integer([13, 10, 9]), 13)
        self.assertEqual(max_integer([13, -25, -10, -50]), 13)
        self.assertEqual(max_integer([40, 32, -9]), 40)
        self.assertEqual(max_integer([-11, -24, -26]), -11)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([20]), 20)
        self.assertEqual(max_integer([27, 26, 10]), 27)
        self.assertEqual(max_integer([999999, 25852, -56521]), 999999)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
