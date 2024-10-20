print("Hello World First SonarQube Running")
# test_calculator.py

import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test class
class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)

# Run the tests
if __name__ == '__main__':
    unittest.main()
