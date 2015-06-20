'''
Created on Jun 20, 2015

@author: richard
'''

import profile

import math

s = math.sqrt

def f1():
    
    return 2 ** 4

def f2():
    return pow(2, 4)

def main():
    
    for i in range(200000):
        f1()
        f2()


if __name__ == '__main__':
    profile.run("main()")