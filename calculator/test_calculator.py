import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(Calculator.add(10, 20), 30)
    self.assertEqual(Calculator.add(2.3, 4.2), 6.5)

  def test_subtract(self):
    self.assertEqual(Calculator.subtract(20, 5), 15)


if __name__ == '__main__':
  unittest.main()