'''
Created on Jun 20, 2015

@author: richard
'''

import profile

import math

s = math.sqrt

def f1(i):
    return math.sqrt(i)

def f2(i):
    return s(i)

def main():
    
    for i in range(200000):
        f1(i)
        f2(i)


if __name__ == '__main__':
    profile.run("main()")