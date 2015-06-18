


def main():
    
    top = 4000000
    total = 0
    a, b = 0, 1

    while total < top:
        term = a + b
        if term % 2 == 0:
            total = total + term
        a = b
        b = term
        
    print total
    
if __name__ == '__main__':
    main()
