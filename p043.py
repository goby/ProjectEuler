#!/usr/bin/env python

import itertools

PRIME = [1, 2,3,5,7,11,13,17]

def getNumTen(n):
    r = 1
    while n:
        r = r * 10
        n = n - 1
    return r

def getSub(v, i):
    return v / getNumTen(7 - i) % 1000

def isInterestingString(v):
    for i in range(1, 8):
        if getSub(v, i) % PRIME[i]:
            return False
    return True
    
    
if __name__ == '__main__':
    s = 0
    for i in itertools.permutations('0123456789',10):
        v = long(''.join(i))
        if isInterestingString(v):
            print v
            s = s + v
    print s