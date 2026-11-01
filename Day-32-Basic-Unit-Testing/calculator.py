"""
Day 32 - Basic Unit Testing Project
A simple calculator module with functions to test.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the result of division."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


def get_square(number):
    """Return the square of a number."""
    return number ** 2