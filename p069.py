# Problem 69


def prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    current = 5
    while current * current <= n:
        if n % current == 0 or n % (current + 2) == 0:
            return False
        current += 6
        
    return True
    
def phi(d):
    n = 1
    for x in d: n *= x
    p = 0
    for i in range(1, n):
        flag = True
        for k in d:
            if i % k == 0: 
                flag = False
                break
        if flag:
            p += 1
    print p,n
    return n * 1. / p
            
if __name__ == '__main__':
    d = [2,3,5,7,11,13,17]
    for i in range(1,len(d)+1):
        print phi(d[:i])
        
