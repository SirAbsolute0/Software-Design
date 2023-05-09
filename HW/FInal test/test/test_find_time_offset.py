import unittest
from src.find_time_offset import calculate_time_difference, get_city_names, get_time_offset_service_response

class FinalTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_calculate_time_difference(self):
        self.assertEqual(2, calculate_time_difference(7200))
        
    def test_calculate_time_difference_with_zero_offset(self):
        self.assertEqual(0, calculate_time_difference(0))
        
    def test_get_city_name_with_no_city(self):
        self.assertEqual([], get_city_names("[]"))
        
    def test_get_city_names_with_three_cites(self):
        self.assertEqual(['London', 'Amsterdam', 'Riga'], get_city_names("[London, Amsterdam, Riga]"))
        
    def test_get_time_offset_service_response(self):
        self.assertTrue(len(get_time_offset_service_response('http://worldtimeapi.org/api/timezone/Europe/Riga.txt')) > 0)