'''
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

from utils import Primes

import profile

def highly_divisible_triangular_number(num):
    
    """
    Find first triangular number with num divisors.
    
    function gets a list of 65500 primes and then gets the
    prime factors of triangles using the list.  The "frequency"
    of each prime factor is found, which is used to determine
    the number of factors.
    """
    
    p = Primes()
    tval = 1
    ctr = 1
    while(True):
        pfs = p.get_prime_factors(tval)
        freq = get_prime_factor_frequence(tval, pfs)
        
        total = 1
        for f in freq:
            # get total number of divisors from the frequency
            total = total * (f + 1)
    
        if total == 1 and tval != 1:
            # val is a prime number, so has 2 divisors
            total = 2
        if total > num:
            break
    
        ctr += 1
        tval = tval + ctr
        
    return tval
    

def get_prime_factor_frequence(val, primes):

    result = [0 for p in primes]
    for index, prime in enumerate(primes):
        exp = 1
        while(True):
            if val % (prime ** exp) == 0:
                result[index] = exp
                exp += 1
            else:
                break

    return result


def triangle_number_generator():
    total = 0
    num = 1
    while(True):
        total += num
        num += 1
        yield total
        

def get_num_divisors(val):

    pfs = get_prime_factors(val)
    freq = get_prime_factor_frequence(val, pfs)
    result = 1
    for f in freq:
        result = result * (f + 1)
    return result
    


if __name__ == '__main__':
    
    
    val = 500
    print highly_divisible_triangular_number(val)
    
#     profile.run('highly_divisible_triangular_number(500)')
    
