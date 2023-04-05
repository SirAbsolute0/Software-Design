import unittest
from src.price_finder import find_lowest_price_and_vendor

class PriceFinderTests(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_find_lowest_price_and_vendor_with_no_vendor(self):
        with self.assertRaises(ValueError) : find_lowest_price_and_vendor(2)
        
