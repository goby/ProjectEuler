# Problem 60
# Prime pair sets
# Use dfs to get result. It is slowly. Running 144s in my laptop

def isprime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    count = 5
    while count * count <= n:
        if n % count == 0 or n % (count + 2) == 0: return False
        count = count + 6
    
    return True

def valid(n,x):
    return isprime(x) and isprime(int(str(x)+str(n))) and  isprime(int(str(n)+str(x)))
    
def getprimepair(n):
    ret = []
    for i in range(3, 10000):
        if valid(n, i):
            ret.append(i)
            
    return ret
    
def getallpair():
    all = {}
    for i in range(3, 10000):
        if isprime(i):
            all[i] = getprimepair(i)
    
    return all

def dfs(pair, li):
    current = li[-1]
    level = len(li)
    for i in li[:-1]: 
        if not (i in pair[current]): return 0;
        
    if (level == 5):
        print li
        return sum(li)
        
    min = 9999999
    if level < 5:
        for i in pair[current]:
            if i in li or i < current: continue
            r = dfs(pair, li+[i])
            if r and r < min:
                min = r
        if min != 9999999:
            return min
    return 0 # not found
    
if __name__ == '__main__':
    pair = getallpair()
    min = 9999999
    for i in pair:
        r = dfs(pair, [i])
        if r and r < min:
            min = r
    
    print min
