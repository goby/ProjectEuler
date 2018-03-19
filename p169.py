#!/usr/bin/env python

#
# A Number can be present by sum of 2^(k), which k in [0..N], and k can be
# existed twice at most. For example:
#  10
#     = 1 + 1 + 2 + 2 + 4, k = 0, 0, 1, 1, 2
#     = 1 + 1 + 4 + 4, k = 0, 0, 2, 2
#     = 1 + 1 + 8, k = 0, 0, 3
#     = 2 + 4 + 4, k = 1, 2, 2
#     = 2 + 8, k = 1, 3
# So f(10) = 5, five forms. f(1e25) = ???
#
# f(x) = f((x-1)/2), if x % 2 == 1
#      = f(x/2) + f(x/2 - 1), otherwise
# f(0) = 1
#
# this recursive formula is very interesting, rule by number's
#
# If last_bit(n) == 1, remove last bit is (n-1)/2, so remove last bit does not change value of f.
# If last_bit(n) == 0, suppose n has N-0s in suffix,
#   so, n/2 has (N-1)-0s suffix ---- (1)
#       n/2-1 should change (N-1)-0s to (N-1)-1s, and change last-N's 1 = 0. ---- (2) = g(n)
#
# For example:
#   [100]0 ==> [100] + [011] = [100] + [0]11 = [100] + [0]
#
# Another more obvious ep.,
#   f(y100) = f(y10)         + f(y01)
#   f(y100) = f(y10)         + f(y0)
#   f(y100) = f(y1)  + f(y0) + f(y0)
#   f(y100) = f(y)   + f(y0) * 2
#
# We forcus on (1), we can get the conclusion that the last N+1 should change
#   N times.
#
# So f(n) = f(n/2^N) + N * f(n/2^N - 1)
#

import math

def zerocount(n):
    i = 0
    e = 1
    while (n & 0x1) == 0:
        n /= 2
        i += 1
        e *= 2
    return i,e

def p169(n):
    while (n & 0x1) == 1:
        n = n/2
    if n <= 0: return 1
    zc,e = zerocount(n)
    return p169(n/(2 * e)) + zc * p169(n/e - 1)

if __name__ == '__main__':
    print p169(10**25)
