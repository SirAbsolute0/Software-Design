from functools import reduce
from src.validation_position import validation_position

def compute_next_fibonacci(fibonacci_number,_): 
    return fibonacci_number[1], sum(fibonacci_number)
    
@validation_position
def fibonacci(position):
    return reduce(compute_next_fibonacci, range(position-1), (1, 1))[-1] 
