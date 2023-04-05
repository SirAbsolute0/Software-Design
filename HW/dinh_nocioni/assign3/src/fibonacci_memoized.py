from functools import lru_cache
from src.fibonacci_recursion import fibonacci as fibonacci_recursive

@lru_cache()
def fibonacci(position):  
    return 1 if 0 < position < 2 else fibonacci_recursive(position, fibonacci) 
