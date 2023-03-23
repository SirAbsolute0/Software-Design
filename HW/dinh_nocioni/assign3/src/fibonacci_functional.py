def checkPosition(position):
    if(position < 0):
        raise ValueError("Position must be a positive integer")
    
def fibonacci(position):
    def fibonacci_helper(position, fib1, fib2):
        return 1 if position <= 1 else fibonacci_helper(position - 1, fib2, fib1 + fib2)
    return fibonacci_helper(position, 0, 1)

