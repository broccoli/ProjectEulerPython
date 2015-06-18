'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def special_pythagorean_triplet():
    """
    Loop through a,b,c where they sum to 1000 and check for triple
    """
    
    for c in range(998, 1000/3, -1):
        remainder = 1000 - c
        
        for a in range(1, remainder / 2  + 1):
             
            b = remainder - a
            if is_triple(a, b, c):
                total = a + b + c
                if total == 1000:
                    return a * b * c
            
#     for a in range(1, 1001):
#          
#         for b in range (a, 1001):
#              
#             c = 1000 - a - b
#              
#             if b > c:
#                 break
#              
#             if is_triple(a, b, c):
#                 print (a, b, c)
#                 total = a + b + c
#                 if total == 1000:
#                     return a * b * c
#      
#      
#      

def is_triple(a, b, c):
    
    if a ** 2 + b **2 == c ** 2:
        return True
    return False

if __name__ == '__main__':
    
    print special_pythagorean_triplet()
