#!/usr/bin/env python
# -*- coding=utf-8 -*-

#
# 
# Let f(N) be the number of points with integer coordinates that are on a circle
# passing through (0,0), (N,0),(0,N), and (N,N).
# 
# It can be shown that f(10000) = 36.
# 
# What is the sum of all positive integers N ≤ 10**11 such that f(N) = 420 ?
# 
# analysis formula: (x - r)^2 + (y - r)^2 = 2*r^2, which r = N/sqrt(2)
# ==> x^2 + y^2 - 2(x+y)r = 0
#
# Get integers result numbers. Right?
#
# More read: http://mathworld.wolfram.com/CircleLatticePoints.html
#
# Where this problem is a Gauss's Circle Problem: http://mathworld.wolfram.com/GausssCircleProblem.html
# As the number N(R) = r_2(R^2), and the r_2 is a Sum of Square function: http://mathworld.wolfram.com/SumofSquaresFunction.html
#
# So this problem turn to solve sum of square function.(Clearly...)
#
# n can be represented as:
#   n = 2^(a0) p1^(2a1)... pr^(2ar) q1^(b1)...qs^(bs),
#       pi is primes of form 4k+3, qi is primes of form 4k+1
#   B -= (b1+1)(b2+1)...(bs+1)
#
# r_2(n) = 4B, if all a(i) is integer
#
# For the problem, we need to find out all sum of N for r_2(N^2/2) = 420, and N <= 10**11
# And B = 420/4 = 105 = 3 * 5 * 7  = 15 * 7 = 21 * 5 = 3 * 35
# So found out follow solution with B = 2, 4, 6 = 14, 6 = 20, 4 = 2, 34
# And the N should in form with sqrt(B) = 1, 2, 3 = 7, 3 = 10, 2 = 1, 17
# 
# Smallest qn is 5, and log5(10^11) < 16, so we remove last condition.
#
# qn = [5, 13, 17, 29, 37, 41, ...]
# 
# 1) 1,2,3, we only concern all prime in qn and with 1 2 3 <- core
#     the first is  ((10**11)/2/(5**3)/(13**2)) < 2366864
#     the second is ((10**11)/2/13/(5**3))**0.5 < 5548
#     the third is  ((10**11)/2/(5**2)/13)**(1/3) < 536
# 2) 3, 7, log37(10^11/2) < 7, so the second largest is 29, and (10**11/(5**7)/2)**0.333 < 87, the first most is smaller than 87
# 3) 2, 10, log13(10^11/2) < 10, so the second is only [5], and (10^11/2/(5^10))^0.5 < 72, the first most is smaller than 72
#

import math

pn = [3,  7, 11]
qn = [5, 13, 17]

def load_prime(n):
    i = 19
    while i < n:
        flag = False
        root = i**0.5
        for k in pn:
            if k > root: break
            if i % k == 0:
                flag = True
                break
        for k in qn:
            if k > root: break
            if i % k == 0:
                flag = True
                break
        if not flag:
            if (i - 3) % 4 == 0:
                pn.append(i)
            else:
                qn.append(i)
        i += 2
    print pn[-1], qn[-1]

def problem1():
    upper = [
             ((10**11)/2/(5**3)/(13**2)),
             ((10**11)/2/(5**3)/(13))**(0.5),
             ((10**11)/2/(5**2)/(13))**(1.0/3)
            ]
    result = []
    for a in qn:
        if a > upper[0]: break
        for b in qn:
            if a == b or b > upper[1]: break
            for c in qn:
                if c == a or c == b or c > upper[2]: break
                rt = a * (b**2) * (c**3)
                if 2*rt > (10**11):
                    break
                result.append(rt)
    print len(result)
    return result

# 2) 3, 7, log37(10^11/2) < 7, so the second largest is 29, and (10**11/(5**7)/2)**0.333 < 87, the first most is smaller than 87
def problem2():
    upper = [
             ((10**11)/2/(5**7))**(1.0/3),
             ((10**11)/2/(5**3))**(1.0/7),
            ]
    result = []
    for a in qn:
        if a > upper[0]: break
        for b in qn:
            if a == b or b > upper[1]: break
            rt = (a**3) * (b**7)
            if 2*rt > (10**11):
                break
            print a, b
            result.append(rt)

    print len(result)
    return result

# 3) 2, 10, log13(10^11/2) < 10, so the second is only [5], and (10^11/2/(5^10))^0.5 < 72, the first most is smaller than 72
def problem3():
    upper = [
             ((10**11)/2/(5**10))**(1.0/2),
             ((10**11)/2/(5**2))**(1.0/10),
            ]
    result = []
    for a in qn:
        if a > upper[0]: break
        for b in qn:
            if a == b or b > upper[1]: break
            rt = (a**2) * (b**10)
            if 2*rt > (10**11):
                break
            print a, b
            result.append(rt)

    print len(result)
    return result

def main():
    max_n = 2366864
    load_prime(max_n)
    print "loaded prime"
    problem1()
    problem2()
    problem3()
    return

if __name__ == '__main__':
    main()
