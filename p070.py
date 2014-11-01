# Problem 70

def isperm(x, y):
    dic = [0 for _ in range(10)]
    while x:
        dic[x%10] += 1
        x /= 10
        
    while y:
        if dic[y%10] == 0: return False
        dic[y%10] -= 1
        y /= 10
    for x in dic: 
        if x != 0: return False
    
    return True

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
            
if __name__ == '__main__':
    # 10000000 ** 0.5 = 3162.2776601683795
    prime_dict = []
    min = 2
    for n in range(6000, 2, -1):
        if prime(n): prime_dict.append(n)
    for i in range(len(prime_dict)):
        for j in range(i, len(prime_dict)):
            n = prime_dict[i] * prime_dict[j]
            if n > 10000000: continue
            p = (prime_dict[i] - 1)*(prime_dict[j] - 1)
            if isperm(n, p):
                if min > n * 1.0/p:
                    min = n*1.0/p
                    print n,p,min
        
    