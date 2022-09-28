import unittest
import calculator

class TestCalc(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(calculator.add(10, 20), 30)