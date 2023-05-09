import unittest
import os
from src.dynamic_vendor_discovery import discover_services
from vendors.Avis import Vendor as Avis_vendor
from vendors.Budget import Vendor as Budget_vendor
from vendors.Dollar import Vendor as Dollar_vendor
from vendors.National import Vendor as National_vendor

VENDOR_FILE_DIRECTORY = "vendors"
REMOVE_VENDOR_FILE_DIRECTORY = "removed_vendor"
class PriceFinderTests(unittest.TestCase):
     
    def test_discover_services(self):
         self.assertTrue(all(callable(function) for function in discover_services())) 
    
    def test_discover_services_having_at_least_three_vendors(self):
        self.assertTrue(len(discover_services()) >= 3)
        
    def test_discover_services_before_and_after_removing_one_vendor(self):

        self.assertTrue(all(isinstance(vendor, (Avis_vendor, Budget_vendor, Dollar_vendor, National_vendor)) for vendor in discover_services()))
        
        intial_vendor_location = os.path.join(VENDOR_FILE_DIRECTORY, 'National.py')
        temporary_vendor_location = os.path.join(REMOVE_VENDOR_FILE_DIRECTORY, 'National.py')
        os.rename(intial_vendor_location, temporary_vendor_location)
        
        self.assertTrue(all(isinstance(vendor, (Avis_vendor, Budget_vendor, Dollar_vendor)) for vendor in discover_services()))
        
        os.rename(temporary_vendor_location, intial_vendor_location)
        
        
        
