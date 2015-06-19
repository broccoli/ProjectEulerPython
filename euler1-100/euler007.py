'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13. What is the 10 001st prime number?
'''

import math

def find_prime(num):
    
    """
    This method keeps a running list of primes, tests numbers against the list,
    adds the number to the list if they are not divisible by primes.
    """
    
    if num == 1:
        return 2
    
    ctr = 1
    test_num = 3
    primes = [2]
    while(True):
        is_prime = False
        top = math.sqrt(test_num)
        for prime in primes:
            if test_num % prime == 0:
                is_prime = False
                break
            if prime > top:
                # don't need to test primes that are larger than square root
                is_prime = True
                break
        if is_prime:
            primes.append(test_num)
            ctr += 1
        if ctr >= num:
            break
        else:
            test_num += 2
    return test_num
        




if __name__ == '__main__':
    print find_prime(10001)
