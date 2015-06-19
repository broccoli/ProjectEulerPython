
from time import time

import math


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
        test_num += 2
        if (test_num + 2) % 3 == 0:
            # skip multiples of 3
            test_num += 2
    
    return primes

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

def timewrap(switch='off'):
    def decorator(func):
        def new_func(*args, **kwargs):
            if switch == 'on':
                print "starting %s" % func.__name__
                start_time = time()
            result = func(*args, **kwargs)
            if switch == 'on':
                end_time = time() - start_time
                print "elapsed time: %f" % end_time
                print
            return result
        return new_func
    return decorator
