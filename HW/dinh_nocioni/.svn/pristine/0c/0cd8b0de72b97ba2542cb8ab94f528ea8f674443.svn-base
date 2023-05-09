import importlib
import glob
import os, sys

sys.path.append(os.getcwd())

VENDOR_FILE_DIRECTORY = "vendors"

def discover_services():
    vendor_services = []
    
    for vendor_file in glob.glob(VENDOR_FILE_DIRECTORY + "/*.py"):
        module_name = os.path.basename(vendor_file)[:-3]
        my_module = importlib.import_module(VENDOR_FILE_DIRECTORY + "." + module_name)
        vendor_services.append(my_module.Vendor())
        
    return vendor_services

vendor_services = []

