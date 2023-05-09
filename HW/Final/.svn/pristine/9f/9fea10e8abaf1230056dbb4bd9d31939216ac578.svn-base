import unittest
from src.find_prime_numbers import get_prime_numbers, sieve_of_eratosthenes_method

class FinalTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_sieve_of_eratosthenes_method(self):
        responses = [[[False, False, True, True, False, True], 5],
                     [[False, False, True, True, False, True, False], 6]]
        
        for test in responses:
              response, number = test
              with self.subTest():
                self.assertEqual(response, sieve_of_eratosthenes_method(number))
                
    def test_get_prime_numbers(self):
        responses = [[[2, 3, 5, 7, 11], 11],
                     [[2, 3, 5, 7], 8],
                     [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 100]]
        
        for test in responses:
              response, number = test
              with self.subTest():
                self.assertEqual(response, get_prime_numbers(number))
                
    def test_get_prime_numbers_with_large_range(self):
        self.assertTrue(len(get_prime_numbers(10000000)) > 2)