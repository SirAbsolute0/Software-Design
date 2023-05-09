from price_finder import find_lowest_price_and_vendor
from dynamic_vendor_discovery import discover_services

def main():
    number_of_days = int(input("Please enter the number of days for the car rental: "))
    while number_of_days <= 0:
        number_of_days = int(input("Please enter an appropriate value: "))
        
    vendor_services = discover_services()
    
    try: 
        vendor_search_result = find_lowest_price_and_vendor(number_of_days, vendor_services)
        
        print("Price Per Day:", vendor_search_result["price_per_day"])
        print("Total Price:", vendor_search_result["total_price"])
        print("Vendor(s):", end=" ")
        for vendor in vendor_search_result["vendor_names"]:
            print(vendor, end=" ")
                
    except ValueError:
        print("No Vendor to Provide Service")
        
if __name__ == "__main__":
    main()
