
#from Utilities import Timer
from utils import timewrap

switch = 'on'

@timewrap(switch)
def solution1():
    
#    timer = Timer()
#    timer.start()
    top = 1000
    total = 0
    for x in range(1, top):
        if x % 3 == 0:
            total = total + x
        elif x % 5 == 0:
            total = total + x

#    print timer.etime()
    print total

@timewrap(switch)
def solution2():
#    timer = Timer()
#    timer.start()

    
    top = 1000
    total = 0
    for x in range(3, top , 3):
        total = total + x
    for x in range(5, top, 5):
        if x % 3 != 0:
            total = total + x
#    print timer.etime()
    print total



if __name__ == '__main__':
    solution1()
    solution2()
    
