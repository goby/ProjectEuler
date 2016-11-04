########################################
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
#   and concatenating them in any order the result will always be prime. For 
#   example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these 
#   four primes, 792, represents the lowest sum for a set of four primes with 
#   this property.
# 
# Find the lowest sum for a set of five primes for which any two primes 
#   concatenate to produce another prime.
########################################

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
    
def validnum(n):
    n = str(n)
    if sum([int(x) for x in n]) % 3 != 1: return False
    for src in ['7','109', '673', '3']:
        if not (isprime(int(n)) and isprime(int(src+n)) and isprime(int(n+src))):
            return False
        if src == '673': print n
    return True
    
def getfiveprime():
    x = 677
    while True:
        if validnum(x):
            return 3+7+109+673+x
        x += 2

if __name__ == '__main__':
    print getfiveprime()
            