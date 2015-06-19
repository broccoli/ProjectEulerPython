'''
Created on Jun 18, 2015

@author: richard
'''
import unittest

from utils import get_primes_below


print "aaaaaaaa"
class Test(unittest.TestCase):

    print "asdfasdf"

    def testget_primes_below(self):
        
        print "asdf"
        expected = [2, 3, 5, 7, 11]
        result = get_primes_below(12)
        self.assertEqual(expected, result)
        
        expected = [2, 3, 5, 7, 11]
        result = get_primes_below(13)
        self.assertEqual(expected, result)

        expected = [2, 3, 5, 7, 11, 13]
        result = get_primes_below(14)
        self.assertEqual(expected, result)

        expected = [2, 3, 5, 7, 11, 13, 17]
        result = get_primes_below(19)
        self.assertEqual(expected, result)

        print "llllllll"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    
    print "rrrrrrrrr"
    unittest.main()