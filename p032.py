# Problem 32

def swap(n ,i, j):
    temp = n[i]
    n[i] = n[j]
    n[j] = temp

def getnext(n):
    N = len(n)
    i = N - 1
    while n[i - 1] >= n[i]: 
        i -=1
        if i == 0: 
            return 0
    j = N
    while n[j - 1] < n[i - 1]: 
        j -= 1
        
    swap(n, i - 1, j - 1)
    
    i += 1
    j = N
    while i < j:
        swap(n, i - 1, j - 1)
        i += 1
        j -= 1
    
    return n
    
def productable(n):
    m1 = 0
    m2 = 0
    pd = 0
    delta = 10000
    for i in range(5):
        m2 = m2*10+n[i]
    for i in range(5,9):
        pd = pd*10+n[i]
        
    for i in range(4):
        m1 = m1*10 + n[i]
        m2 = m2 % delta
        delta /= 10
        if m2 * m1 == pd:
            print m1, m2, pd
            return pd
    return 0
    
if __name__ == '__main__':
    ori = [i for i in range(1, 10)]
    result = set()
    while True:
        a = productable(ori)
        if a: result.add(a)
        ori = getnext(ori)
        if not ori: break
        
    print sum(result)