import math

def lcm(n: int, m: int) -> int:
    return n * m // math.gcd(n, m)
