import unittest
from src.fibonacci_functional import fibonacci
from test_fibonacci import FibonacciTests

class FibonacciFunctionalTests(FibonacciTests, unittest.TestCase):

  def fibonacci_implementation(self):
    return fibonacci

if __name__ == '__main__': 
  unittest.main()
