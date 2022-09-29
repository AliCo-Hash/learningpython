import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(Calculator.add(10, 20), 30)
    self.assertEqual(Calculator.add(5, 4), 9)
    self.assertEqual(Calculator.add(2.3, 4.2), 6.5)


if __name__ == '__main__':
  unittest.main()