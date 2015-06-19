
"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


from utils import timewrap, timewrap2

switch = 'on'
reps = 1

@timewrap(switch, reps)
def multiples_of_3_and_5_a(top):
    
    total = 0
    for x in range(3, top, 2):
        if x % 3 == 0:
            total = total + x
        elif x % 5 == 0:
            total = total + x

    return total

#@timewrap(switch, reps)
@timewrap2
def multiples_of_3_and_5_b(top):
    
    total = 0
    for x in range(3, top , 3):
        total = total + x
    for x in range(5, top, 5):
        if x % 3 != 0:
            total = total + x
    return total


@timewrap(switch, reps)
def multiples_of_3_and_5_c(top):
    """
    multiples of 3 and 5 appear in a pattern that repeats every 15 numbers
    """

    series = [3, 5, 6, 9, 10, 12, 15]
    base = 0 #start at 0
    total = 0
    stop = False
    while not stop:
        
        for i in series:
            num = base + i
            if num >= top:
                stop = True
                break
            else:
                total = total + num
                
        base = num
        
    return total



if __name__ == '__main__':
    print multiples_of_3_and_5_a(1000)
    print multiples_of_3_and_5_b(1000)
    print multiples_of_3_and_5_c(1000)
    
