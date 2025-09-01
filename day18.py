import math

def count_divisors(n: int) -> int:
    if n == 1:
        return 1

    count = 1
    temp = n

    power = 0
    while temp % 2 == 0:
        power += 1
        temp //= 2
    if power > 0:
        count *= (power + 1)

    for i in range(3, int(math.isqrt(temp)) + 1, 2):
        power = 0
        while temp % i == 0:
            power += 1
            temp //= i
        if power > 0:
            count *= (power + 1)

    if temp > 1:
        count *= 2

    return count
