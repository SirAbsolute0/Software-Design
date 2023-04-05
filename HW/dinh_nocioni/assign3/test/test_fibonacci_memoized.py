import unittest
from src.fibonacci_memoized import fibonacci
from test_fibonacci import FibonacciTests

class FibonacciMemoizedTests(FibonacciTests, unittest.TestCase):
  
  def fibonacci_implementation(self):
    return fibonacci
  
if __name__ == '__main__': 
  unittest.main()

