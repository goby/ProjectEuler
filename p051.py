###########################
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-
#   digit number is the first example having seven primes among the ten generated 
#   numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
#   56993. Consequently 56003, being the first member of this family, is the 
#   smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily 
#   adjacent digits) with the same digit, is part of an eight prime value family.
###########################

_5_pattern = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1]
]

_6_pattern = [
    [1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1]
]

def isprime(n):
    if n <=1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    counter = 5
    while counter * counter <= n:
        if n % counter == 0 or n % (counter + 2) == 0: return False
        counter += 6

    return True
    
def fillpattern(pattern, n):
    '''fill digits of n in pattern, and return filled array'''
    filled = [-1 for i in range(len(pattern))]
    for i in range(len(pattern), 0, -1):
        if pattern[i - 1] == 1:
            filled[i - 1] = n % 10
            n /= 10
            
    return filled
    
def generatenum(repnum, filled):
    tmp = 0
    for i in range(len(filled)):
        tmp *= 10
        tmp += repnum if filled[i] == -1 else filled[i]
        
    return tmp
    
def familysize(repnum, pattern):
    size = 1
    for i in range(repnum+1, 10):
        if isprime(generatenum(i, pattern)): size += 1
        
    return size
    
if __name__ == '__main__':
    result = 99999999999999999
    for i in range(11, 1000, 2):
        if i % 5 == 0: continue
        
        pattern = _5_pattern if i < 100 else _6_pattern
        
        for j in range(len(pattern)):
            for k in range(3):
                if pattern[j][0] == 0 and k ==0: continue
                
                filled = fillpattern(pattern[j], i)
                candidate = generatenum(k, filled)
                
                if candidate < result and isprime(candidate):
                    if familysize(k, filled) == 8:
                        result = candidate
                    break
                    
    print result