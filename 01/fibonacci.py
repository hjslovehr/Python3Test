import sys
sys.path.append('..\\common')
from helpers import *

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    value = 1
    if 1 == n:
        value = 1
    elif 2 == n:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    
    fibonacci_cache[n] = value
    return value

@func_use_time
def test():
    for n in range(1000):
        print(n, " : ", fibonacci(n))

if __name__ == "__main__":
    test()
