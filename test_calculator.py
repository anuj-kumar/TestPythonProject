import unittest
from calculator import Calculator as Calc


class TestCalculator(unittest.TestCase):

    def test_add_positive_integers(self):
        self.assertEqual(Calc.add(5, 10), 15, "Add two integers")
        self.assertEqual(Calc.add(5, 10, 15), 30, "Add three positive integers")

    def test_add_positive_and_negative_integers(self):
        self.assertEqual(Calc.add(5, -10), -5, "Add two integers")
        self.assertEqual(Calc.add(5, 10, -15), 0, "Add three positive integers")

    def test_multiply_non_integers(self):
        self.assertEqual(Calc.multiply(5.5, 1.3), 5.5 * 1.3, "Add three positive integers")
        self.assertEqual(Calc.multiply(5.5, -1.3), 5.5 * -1.3, "Add three positive integers")
