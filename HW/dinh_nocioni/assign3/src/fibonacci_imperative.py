def fibonacci(position):
    if(position < 0):
        raise ValueError("Position must be a positive integer")
    
    current = previous = 1
    
    for _ in range(position - 1):  
        current, previous = current + previous, current
        
    return current
