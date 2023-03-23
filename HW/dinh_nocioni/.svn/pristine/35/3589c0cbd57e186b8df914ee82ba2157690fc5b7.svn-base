import unittest
from src.fibonacci_functional import fibonacci

class FibonacciImperativeTests(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_fibonacci_positions(self):
    responses = [[0, 1], 
                 [1, 1],
                 [2, 2],
                 [5, 8],
                 [10, 89],
                 [50, 20365011074]]
    
    for test in responses:
      position, value = test
      with self.subTest():
        self.assertEqual(value, fibonacci(position))

  def test_fibonacci_exception(self):
    with self.assertRaises(ValueError):
      fibonacci(-1)

if __name__ == '__main__': 
  unittest.main()
