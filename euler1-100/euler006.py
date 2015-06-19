'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''


"""
Using algebra, (a + b + c)^2 - a^2 - b^2 - c^2 =
2(ab + ac + bc)

I made two versions based on this principal.  But I found it is more
efficient to compute the answer directly, as in this solution from the
discussion board:

sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)])
"""

from utils import timewrap, timewrap2

switch = 'on'

@timewrap2
def sum_square_difference2(num):
    
    return sum([x * y for x in range(1, num + 1) for y in range(1, num + 1) if x != y])


@timewrap(switch)
def sum_square_difference(num):
    
    
    list1 = range(1, num + 1)
    
    total = 0
    
    list2 = list1[:-1]
    list3 = list1[:]
    
    for x in list2:
        list3 = list3[1:]
        for y in list3:
            if x != y:
                total += x * y
    return 2 * total

if __name__ == '__main__':
    

     print sum_square_difference2(100)





