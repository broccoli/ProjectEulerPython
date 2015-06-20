
"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


import profile

def multiples_of_3_and_5_a(top):
    
    total = 0
    for x in range(3, top):
        if x % 3 == 0:
            total = total + x
        elif x % 5 == 0:
            total = total + x

    return total

def multiples_of_3_and_5_b(top):
    
    total = 0
    for x in range(3, top , 3):
        total = total + x
    for x in range(5, top, 5):
        if x % 3 != 0:
            total = total + x
    return total


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

def multiples_of_3_and_5_d(top):
    """
    multiples of 3 and 5 appear in a pattern that repeats every 15 numbers
    
    This approach did very poorly until I cached the len().
    Array access still appears to slow it down.
    """

    series_diff = [3, 2, 1, 3, 1, 2, 3]
    length = len(series_diff)
    base = 0 #start at 0
    total = 0
    stop = False

    num = 3
    i = 1
    while num < top:
        total += num        
        num = num + series_diff[i]
        if i < length - 1:
            i += 1
        else:
            i = 0
            
    return total


def multiples_of_3_and_5_e(top):
    """
    multiples of 3 and 5 appear in a pattern that repeats every 15 numbers
    """

    series_diff = [3, 2, 1, 3, 1, 2, 3]
    num = 0 #start at 0
    total = 0
    stop = False

    while not stop:
        
        for i in series_diff:
            num = num + i
            if num >= top:
                stop = True
                break
            else:
                total = total + num
                
        
    return total


def multiples_of_3_and_5_f(top):
    """
    multiples of 3 and 5 appear in a pattern that repeats every 15 numbers
    
    The generator approach profiles badly.
    """
    series_diff = [3, 2, 1, 3, 1, 2, 3]
    
    def diff_gen():
        while(True):
            for diff in series_diff:
                yield diff
        
    num = 0 #start at 0
    total = 0
    stop = False
    
    diff = diff_gen()
    
    num = diff.next()

    while num < top:
        
        total = total + num
        num = num + diff.next()
        
    return total


def test():
    val = 1000
    reps = 1000
    for r in range(reps):
        multiples_of_3_and_5_a(val)
        multiples_of_3_and_5_b(val)
        multiples_of_3_and_5_c(val)
        multiples_of_3_and_5_d(val)
        multiples_of_3_and_5_e(val)
        multiples_of_3_and_5_f(val)



if __name__ == '__main__':
     val = 1000
     print multiples_of_3_and_5_a(val)
     print multiples_of_3_and_5_b(val)
     print multiples_of_3_and_5_c(val)
     print multiples_of_3_and_5_d(val)
     print multiples_of_3_and_5_e(val)
     print multiples_of_3_and_5_f(val)

     profile.run("test()")