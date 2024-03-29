from src.validation_position import validation_position

@validation_position
def fibonacci(position): 
    current = previous = 1
    
    for _ in range(position - 1):  
        current, previous = current + previous, current
        
    return current
