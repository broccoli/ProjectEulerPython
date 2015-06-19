'''
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?'''

import math

def smallest_multiple(num):
    
    # get all the primes and multiply together
    primes = get_primes_less_than(num)
    base = 1
    for x in primes:
        base = base * x

    test_list = range(1, num + 1)
    test_list.reverse()

    
    test_num = base
    while (True):
        
        stop = True
        for x in test_list:
            if test_num % x != 0:
                stop = False
                break
        if stop:
            break
        test_num += base
        
        
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

if __name__ == '__main__':
    
    print smallest_multiple(20)

