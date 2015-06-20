'''
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?'''

import math
import profile

def smallest_multiple_b(num):
    
    
    # get a list of primes less than num and multiply product by prime.
    # For every time the prime squared, cubed, etc is lte the num,
    # multiple product by the prime.  That takes care of 4, 8, 9, etc.
    
    # seems to be some efficiency gains with ** instead of pow
    primes = []
    prod = 1
    for x in range(2, num + 1):
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            prod = prod * x
            exp = 2
            while x ** exp <= num:
                prod = prod * x
                exp += 1
    return prod    

def smallest_multiple(num):
    
    # get all the primes and multiply together
    primes = get_primes_less_than(num)
    base = 1
    for x in primes:
        base = base * x

    test_list = range(num, 0, -1)
    
    test_num = base
    
    ctr = 0
    
    while (True):
        
        stop = True
        for x in test_list:
            if test_num % x != 0:
                stop = False
                break
        if stop:
            break
        test_num += base    
#     for x in test_list:
#         while test_num % x != 0:
#             test_num += base
        
    return test_num

def get_primes_less_than(num):
    
    result = []
    if 2 < num:
        result.append(2)
        
    for x in range(3, num):
        if is_prime(x):
            result.append(x)
            
    return result

def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    if num % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


def test():
    
    reps = 10000
    val = 30
    for r in range(reps):
        smallest_multiple(val)
        smallest_multiple_b(val)
        

if __name__ == '__main__':
    
    print smallest_multiple(10)
    print smallest_multiple_b(10)
    
    profile.run("test()")
#     print get_primes_less_than(10)
