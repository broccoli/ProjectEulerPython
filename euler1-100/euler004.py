'''
Created on Jun 17, 2015

@author: richard
'''



def largest_palindrome():
    
    for x in range(999, 100, -1):
        pal = get_palindrome(x)
        if is_three_digit_product(pal):
            return pal

    return 0

def is_three_digit_product(num):
    for x in range(999, 100, -1):
        if num / x >= 100 and num / x <= 999:
            if num % x == 0:
                return True
    return False

def get_palindrome(x):
    
    ones = x % 10
    tens = (x - ones) % 100 / 10
    huns = x / 100
    return x * 1000 + ones * 100 + tens * 10 + huns
    

if __name__ == '__main__':
    
    
    print largest_palindrome()
