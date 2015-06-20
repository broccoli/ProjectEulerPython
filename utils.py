
from time import time

from math import sqrt


def get_primes_below(num):
    
    """
    method starts with a list of primes and then test other numbers against the list
    to see if it is prime.  If so, it is added to the list
    """
    
    if num < 2:
        return []
    primes = [2]
    if num == 3:
        return primes

    test_num = 3
    while(test_num < num):
        is_prime = False
        top = sqrt(test_num)
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
        test_num += 2
        if (test_num + 2) % 3 == 0:
            # skip multiples of 3
            test_num += 2
    
    return primes



class Primes:
    
    
    """
    Utility functions used in 012
    """
    def __init__(self):
        self.primes = [2, 3]
        self.fill_primes(65500)
        # a list of prime factor is initialized for 012
        
    
    def get_prime_factors(self, val):
        prime_factors = []
        top = val / 2

#         if self.primes[-1] < val / 2:
#             self.fill_primes(val)
            
            
        for prime in self.primes:
            if val % prime == 0:
                prime_factors.append(prime)
                val = val / prime
                while (val % prime == 0):
                    val = val / prime
            if prime > val or prime > top:
                break
        
        return prime_factors
    
    
    def fill_primes(self, limit):
        """
        fill the existing primes list up to the  limit
        """
        
        if self.primes[-1] + 1 >= limit:
            # get out if the limit is less than or equal to the
            # last prime or the next even integer up
            return
        test_num = self.primes[-1] + 2
        while(test_num <= limit):
            is_prime = False
            top = sqrt(test_num)
            for prime in self.primes:
                if test_num % prime == 0:
                    is_prime = False
                    break
                if prime > top:
                    # don't need to test primes that are larger than square root
                    is_prime = True
                    break
            if is_prime:
                self.primes.append(test_num)
            test_num += 2
            while(test_num % 3 == 0 or test_num % 5 == 0):
                # skip multiples of 3 and 5
                test_num += 2
    
    
    def primes_generator(self):
        
        self.primes.append(2)
        yield 2
        self.primes.append(3)
        yield 3
        test_num = 5
        
        while(True):
            is_prime = False
            top = sqrt(test_num)
            for prime in self.primes:
                if test_num % prime == 0:
                    is_prime = False
                    break
                if prime > top:
                    # don't need to test primes that are larger than square root
                    is_prime = True
                    break
            if is_prime:
                self.primes.append(test_num)
                #print self.primes
                yield(test_num)
            test_num += 2
            if (test_num) % 3 == 0:
                # skip multiples of 3
                test_num += 2
    
    

class Timer:
    
    def start(self):
        self.start_time = time()
    def etime(self):
        return time() - self.start_time


def timewrap2(func):
    def new_func(*args, **kwargs):
        print "starting %s" % func.__name__
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time() - start_time
        print "elapsed time: %f" % end_time
        print
        return result
    return new_func

def timewrap(switch='off', times = 1):
    if switch == 'off':
        times = 1
    def decorator(func):
        def new_func(*args, **kwargs):
            total_time = 0
            if switch == 'on':
                print "starting %s" % func.__name__
            for rep in range(times):
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time() - start_time
                total_time += end_time
            if switch == 'on':
                ave_time = total_time / times
                print ave_time
                print "{} reps, ave. time: {:.20f}".format(times, ave_time)
                #print "elapsed time: %f" % end_time
                print
            return result
        return new_func
    return decorator
