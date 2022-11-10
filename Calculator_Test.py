import unittest
import Calculator

# Run "python -m unittest <path_to_text_file>" on command line to run test manually"

class MultiplierTest(unittest.TestCase):

	def test_multiply_success(self):
		actual = Calculator.multiply(10, 2)
		expected = 20
		self.assertEqual(actual, expected)

	def test_add_success(self):
		actual = Calculator.add(5, 3)
		expected = 8
		self.assertEqual(actual, expected)

	def test_subtract_success(self):
		actual = Calculator.subtract(15, 5)
		expected = 10
		self.assertEqual(actual, expected)

	def test_exponent_success(self):
		actual = Calculator.exponent(2, 4)
		expected = 16
		self.assertEqual(actual, expected)

	def test_multiply_failure(self):
		actual = Calculator.multiply(20, 4)
		expected = 100
		self.assertEqual(actual, expected)