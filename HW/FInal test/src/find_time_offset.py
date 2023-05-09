import requests

def calculate_time_difference(time_raw_offset):
    return time_raw_offset / 3600

def get_city_names(city_list_text):
    cities = list(city_name.strip() for city_name in city_list_text.strip('[]').split(','))
    return [] if cities == [''] else cities

def get_time_offset_service_response(URL):
    return requests.get(URL).text

def check_time_offset_service_response_error():
    
    