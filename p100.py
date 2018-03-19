#!/bin/python
# -*- coding=utf-8 -*-

# If a box contains twenty-one coloured discs, composed of fifteen blue discs
# and six red discs, and two discs were taken at random, it can be seen that
# the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
# 
# The next such arrangement, for which there is exactly 50% chance of taking
# two blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.
# 
# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box would contain.

# P(BB) = x * (x - 1) / (n * (n - 1))
# so x^2 - x - n * (n  - 1)/ 2 = 0
# 2* x^2 - 2x - n^2 + n = 0
#  ref: https://www.alpertron.com.ar/QUAD.HTM
#

import decimal

def p100(upper):
    # X(n+1) = 3 Xn + 2 Nn
    # N(n+1) = 4 Xn + 3 Nn - 1
    # we got x0 = 15, n0 = 21
    x = 15
    n = 21
    while n < upper:
        next_x = 3 * x + 2 * n - 2
        next_n = 4 * x + 3 * n - 3

        x = next_x
        n = next_n

    return x


if __name__ == '__main__':
    print p100(10**12)
