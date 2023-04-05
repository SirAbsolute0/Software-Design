import unittest
from src.fibonacci_imperative import fibonacci
from test_fibonacci import FibonacciTests

class FibonacciImperativeTests(FibonacciTests, unittest.TestCase):
  
  def fibonacci_implementation(self):
    return fibonacci
  
if __name__ == '__main__': 
  unittest.main()

