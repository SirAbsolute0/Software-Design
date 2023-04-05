from functools import lru_cache
from sample2 import compute


#print(compute(10))

@lru_cache(maxsize=None)
def compute_memoized(n):
 print(f"compute_memoized called for {n}")

 return 1 if n < 2 else compute(n, lambda n: compute_memoized(n))

print(compute_memoized(10))

