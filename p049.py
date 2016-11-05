# Problem 49 Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
# increases by 3330, is unusual in #two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this 
# sequence?


w = [0 for _ in range(10000)]

def p049():
    w[2] = 1
    for i in range(3, 10000, 2): w[i] = 1

    for i in range(5, 10000, 2):
        for j in range(3, i, 2):
            if i % j == 0: w[i] = 0

    for i in range(1001, 10000, 2):
        if w[i] == 1:
            step = (9999 - i) / 2
            for j in range(2, step, 2):
                if w[i+j] == 1 and w[i + j + j] == 1 and isPerm(i, i+j) and isPerm(i, i + j + j):
                    print i, i + j, i + j + j

if __name__ == '__main__':
    p049()