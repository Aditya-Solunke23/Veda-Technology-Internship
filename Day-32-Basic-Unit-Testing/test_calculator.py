"""
Unit tests for calculator.py
Run with: python -m unittest -v
"""

import unittest
from calculator import add, subtract, multiply, divide, is_even, get_square


class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    # Subtraction tests
    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_to_negative_result(self):
        self.assertEqual(subtract(4, 10), -6)

    # Multiplication tests
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)

    # Division tests
    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    # Even number tests
    def test_even_number(self):
        self.assertTrue(is_even(8))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    # Square tests
    def test_square_positive_number(self):
        self.assertEqual(get_square(5), 25)

    def test_square_negative_number(self):
        self.assertEqual(get_square(-4), 16)


if __name__ == "__main__":
    unittest.main()