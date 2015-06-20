
"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

import profile


def largest_prime_factor_b(num):
    
    """
    Repeatedly factor a number and go on to next prime.
    Cache the square root to boost efficiency significantly.
    """
    
    while (num % 2 == 0):
        num = num / 2
    test_num = 3
    top = math.sqrt(num)
    while (test_num <= top):
        while num % test_num == 0 and num > test_num:
            num = num / test_num
            top = math.sqrt(num)    
        test_num += 2
        if test_num % 3 == 0:
            test_num += 2

    return num

    
def largest_prime_factor(num):
    
    """
    Repeatedly factor a number starting with its smallest prime.
    In the case of 600851475143, this method is faster. In other cases,
    it is slower.
    """
    
    while(True):
        pf = smallest_prime_factor(num)
        if pf == num:
            break
        num = num / pf
    return num
    
def smallest_prime_factor(num):
    """
    return smallest prime factor, which may be itself
    """
    
    if num % 2 == 0:
        return 2
#     for x in xrange(3, num/3, 2):
    for x in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return x
    return num

def test(num):

    reps = 1000
    for r in range(reps):        
        largest_prime_factor(num)
        largest_prime_factor_b(num)

if __name__ == '__main__':
    num = 600851475143
#     num = 3 ** 10
#     num = 2 * 3 * 5 * 7 * 11 * 17 * 6857
#     num = 18
    
    print largest_prime_factor(num)
    print largest_prime_factor_b(num)
    
    profile.run("test({})".format(num))

