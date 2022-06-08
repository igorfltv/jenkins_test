import unittest
from functions import Functions

class TestFunction(unittest.TestCase):
    def setUp(self):
        self.functions = Functions()
    def test_add(self):
        self.assertEqual(self.functions.plus(4,7), 11)
    def test_minus(self):
        self.assertEqual(self.functions.minus(10,2), 8)
    def test_divide(self):
        self.assertEqual(self.functions.div(20,4), 5)

if __name__ == "__main__":
  unittest.main()