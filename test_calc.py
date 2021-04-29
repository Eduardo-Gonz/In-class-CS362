import unittest
import calc

class TestCase(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc.add(2,5), 7)
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.division(20, 5), 4)

if __name__ == "__main__":
    unittest.main()