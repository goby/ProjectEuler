#!/usr/bin/env python

def isValid(n):
    DICT=(1<<10)-2
    while n:
        i = 1 << (n % 10)
        if not (i & DICT):
            return False
        DICT = DICT & (~i)
        n = n / 10
    return not DICT

KNOWN_MAX =  918273645
MAX       = 1000000000

def getNumberLen(n):
    l = 0
    while n:
        l = l + 1
        n = n / 10
    return l
    
def getFirst(n):
    while n > 10:
        n = n / 10
    return n

def getMinDec(n):
    d = 1
    while n:
        d = d * 10
        n = n / 10
    return d

def getValue(bit):
    v = 9/bit
    f = 1
    for i in range(v):
        f = f*10
    f = f - 1
    print f
    max = KNOWN_MAX
    for i in range(f, 0, -1):
        if getFirst(i) < 9: return max
        v = 0
        for k in range(bit):
            k = k + 1
            r = k * i
            v = v * getMinDec(r) + r
            l = getNumberLen(v)
            if l > 9:
                break
            elif l == 9 and isValid(v):
                print bit, f, i, k, v
                if v > max:
                    max = v
    
    return max
    
    
def pandigital():
    max = KNOWN_MAX
    for i in range(2, 9):
        curr = getValue(i)
        if curr > max:
            max = curr
    return max

if __name__ == '__main__':
    r = pandigital()
    print "MAX=", r