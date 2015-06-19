'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from ProjectEulerPython.src.utils import get_primes_below

def summation_of_primes():
    
    primes = get_primes_below(10)
    return sum(primes)
    
    pass

if __name__ == '__main__':
    
    print summation_of_primes()