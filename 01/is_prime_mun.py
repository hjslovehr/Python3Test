import math
import time

def is_prime_v1(n):
    '''
    如果 n 是素数返回 True，否则返回 False
    '''
    if 1 == n:
        return False
    
    for i in range(2, n):
        if 0 == n % i:
            return False
    
    return True


def is_prime_v2(n):
    '''
    如果 n 是素数返回 True，否则返回 False
    '''
    if 1 == n:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_divisor):
        if 0 == n % i:
            return False
    
    return True


def is_prime_v3(n):
    '''
    如果 n 是素数返回 True，否则返回 False
    '''
    if 1 == n:
        return False
    
    if 2 == n:
        return True
    if n > 2 and 0 == n % 2:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor, 2):
        if 0 == n % i:
            return False
    
    return True


def test():
    '''
    Test function
    '''
    begin = time.time()
    for n in range(1, 1_000_000):
        # print(n, is_prime_v1(n))
        # is_prime_v1(n)
        # is_prime_v2(n)
        is_prime_v3(n)
        pass

    end = time.time()
    time_sub = end - begin
    print(time_sub, 's')

if __name__ == "__main__":
    test()
    input('Press any key to continue . . . ')


