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



from utils import timewrap, timewrap2

import profile

def sum_square_difference2(num):
    
    return sum(range(num + 1))**2 - sum([x**2 for x in range(num + 1)])


def sum_square_difference(num):
    """
    Using algebra, (a + b + c)^2 - a^2 - b^2 - c^2 =
    2(ab + ac + bc)
    
    
    This method is slower than doing it explicitly with sum and range.
    """
    
    
    list1 = range(1, num + 1)
    
    total = 0
    
    list2 = list1[:-1]
    
    for x in list2:
        list1 = list1[1:]
        for y in list1:
            total += x * y
    return 2 * total

def sum_square_difference3(num):
    """
    Computes 2(ab + ac + bc).
    Slowest method of all.
    """
    
    a = range(1, num + 1)
    
    return sum([x * y for x in a for y in a if x != y])


def test():
    reps = 10000
    num = 100
    for r in range(reps):
        sum_square_difference(num)
        sum_square_difference2(num)
        sum_square_difference3(num)

if __name__ == '__main__':
    

    print sum_square_difference(100)
    print sum_square_difference2(100)
    print sum_square_difference3(100)

    profile.run("test()")




