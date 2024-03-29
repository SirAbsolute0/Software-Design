def get_vendor_price_ignore_exception(vendor_service): 
    try:
        return vendor_service()
    except Exception:
        pass 
    
def find_lowest_price_and_vendor(num_of_days, vendor_price_services=[]):
    vendors_available = filter(lambda response: isinstance(response, tuple) and type(response[1]) == int, list(map(get_vendor_price_ignore_exception, vendor_price_services)))
    
    price_details = list(vendors_available)
    
    if len(price_details) == 0:
        raise ValueError("No Vendor to Provide Service")
    
    lowest_price_per_day = min(price_details, key=lambda vendor: vendor[1])[1]    
    vendors_with_best_pricing = [vendor[0] for vendor in price_details if vendor[1] == lowest_price_per_day]
    
    return {'price_per_day': lowest_price_per_day, 'total_price': lowest_price_per_day * num_of_days, 'vendor_names' : vendors_with_best_pricing}



                    

    
