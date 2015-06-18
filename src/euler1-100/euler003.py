

def main():
    """
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    num = 600851475143
    
    result = largest_prime_factor(num)
    
    print "largest prime: ", result
    
def largest_prime_factor(num):
    prime_factors = []    
    
    while(True):
        pf = smallest_prime_factor(num)
        print pf
        prime_factors.append(pf)
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
    for x in xrange(3, num/3, 2):
        if num % x == 0:
            return x
    return num

if __name__ == '__main__':
    main()