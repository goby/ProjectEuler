# Problem 47 Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
#   14 = 2 × 7
#   15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
#   644 = 2^2 × 7 × 23
#   645 = 3 × 5 × 43
#   646 = 2 × 17 × 19
# Find the first four consecutive integers to have four distinct prime factors 
# each. What is the first of these numbers?
#
#
# Distinct Prime Factor: http://mathworld.wolfram.com/DistinctPrimeFactors.html
#

MAX = 1000000

w = [0 for _ in range(MAX)]

def p047():
    for i in range(2, MAX):
        if w[i] == 0:
            # this is a prime, so we add this count 
            for j in range(i, MAX, i):
                w[j] = w[j] + 1
   
    # found consecutive 4
    count = 0
    for i in range(10, MAX):
        if w[i] != 4:
            count = 0
        else:
            count = count + 1
            if count == 4:
                return i - 3

if __name__ == '__main__':
    print p047()
        
            
