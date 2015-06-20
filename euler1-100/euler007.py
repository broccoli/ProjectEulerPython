'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13. What is the 10 001st prime number?
'''

import math
import profile

def find_prime(num):
    
    """
    This method keeps a running list of primes, tests numbers against the list,
    adds the number to the list if they are not divisible by primes.
    """
    
    primes = [2, 3, 5]
    if num < 4:
        return primes[num - 1]
    
    ctr = 3
    test_num = 7
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
            while (test_num % 3 == 0 or test_num % 5 == 0):
                test_num += 2
    return test_num
        

def test():
    
    reps = 10
    num = 10001
    for r in range(reps):
        find_prime(num)


if __name__ == '__main__':
    num = 10001
    print find_prime(num)
    
    profile.run("test()")
