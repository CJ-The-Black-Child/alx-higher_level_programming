#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_regular_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result,4)

    def test_reversed_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reversed_list(self):
        """Test max_integer with a reversed list"""
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_duplicate_values(self):
        """Test max_integer with a list containing duplicate values"""
        result = max_integer([1, 3, 4, 4])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

if __name__ == "__main__":
        unittest.main()
