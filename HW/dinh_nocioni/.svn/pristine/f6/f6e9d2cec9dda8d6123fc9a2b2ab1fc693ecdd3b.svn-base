def validation_position(fibonacci):   
    def validate_and_call(position, *args):
        if(position < 0): 
            raise ValueError("Position must be a positive integer")
            
        return fibonacci(position, *args) 
        
    return validate_and_call
