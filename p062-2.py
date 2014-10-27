# Problem 62
# Cubic Permutations

def generatekey(n):
    d = [0 for _ in range(10)]
    while n:
        d[n % 10] += 1
        n /= 10
        
    return ''.join([str(x) for x in d])
    
if __name__ == '__main__':
    n = 345
    result = {}     # [smallest, times]
    while True:
        key = generatekey(n*n*n)
        if key in result: 
            result[key][1] += 1
        else: 
            result[key] = [n*n*n, 1]
        if result[key][1] == 5:
            print result[key][0]
            break
        n += 1
