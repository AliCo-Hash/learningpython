import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(Calculator.add(10, 20), 30)
    self.assertEqual(Calculator.add(2.3, 4.2), 6.5)

  def test_subtract(self):
    self.assertEqual(Calculator.subtract(20, 5), 15)
    self.assertEqual(Calculator.subtract(12.5, -10.5), 23)

  def test_multiply(self):
    self.assertEqual(Calculator.multiply(10, 20), 200)
    self.assertEqual(Calculator.multiply(10.5, -2.5), -26.25)

  def test_divide(self):
    self.assertEqual(Calculator.divide(200, 20), 10)


if __name__ == '__main__':
  unittest.main()