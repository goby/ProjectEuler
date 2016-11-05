﻿#
# Problem 44 Pentagon numbers
#
# Pentagonal numbers are generated by the formula, P(n)=n(3n−1)/2. 
# The first ten pentagonal numbers are:
#   1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P(4) + P(7) = 22 + 70 = 92 = P(8). However, their 
# difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, P(j) and P(k), for which their sum 
# and difference are pentagonal and D = |P(k) − P(j)| is minimised; what 
# is the value of D?

import math

def pentagonal(n):
    # 2*k*k <= 2*P(k) <= 3*k*k
    n = 2 * n
    start = int(math.floor(math.sqrt(n/3)))
    end = int(math.ceil(math.sqrt(n/2)))
    for i in range(start, end + 1):
        if n == i * (3 * i - 1):
            return i
    return 0
    
def pentagonal2(n):
    # x = (sqrt(24n+1) + 1) / 6
    x = (math.sqrt(24 * n + 1)) / 6
    return x == int(x)

def p044(start, end):
    for i in range(start, end):
        for j in range(i - 1, 1, -1):
            pi = i * (3 * i - 1) / 2
            pj = j * (3 * j - 1) / 2
            s = pentagonal(pi + pj)
            m = pentagonal(pi - pj)
            if s and m:
                print i, j
                return pi - pj

if __name__ == '__main__':
    print 1020 * (3 * 1020 - 1) / 2
    print pentagonal(92)
    print p044(1, 10000)

    