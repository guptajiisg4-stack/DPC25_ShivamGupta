import math

def prime_factorization(n: int) -> list:
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 1:
        factors.append(n)
    
    return factors
