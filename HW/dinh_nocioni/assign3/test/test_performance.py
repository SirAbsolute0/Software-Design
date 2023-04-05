import time
import unittest
from src.fibonacci_recursion import fibonacci as fibonacci_recursive
from src.fibonacci_memoized import fibonacci as fibonacci_memoized

class PerformanceTests(unittest.TestCase):

    def time_taken(self, fibonacci):
        start = time.time()
        fibonacci(30)
        return time.time() - start

    def test_performance_memoized_against_recursion(self):
        recursion_time = self.time_taken(fibonacci_recursive)
        memoized_time = self.time_taken(fibonacci_memoized)

        self.assertTrue(memoized_time * 10 < recursion_time)

        
        
