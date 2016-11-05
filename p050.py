#
# Problem 50
#
# pi(1M) ~ 80k+
# pi(100k) ~ 9k+

PRIME_COUNT = 80000

w = [0] * PRIME_COUNT
s = [0] * PRIME_COUNT

def prime():
    w[0] = s[0] = 2
    w[1] = 3
    curr = 1
    for i in range(3, 100000, 2):
        flag = True
        for j in range(curr):
            if i % w[j] == 0:
                flag = False
                break
        if flag:
            w[curr] = i
            curr = curr + 1
    
    for i in range(1, curr):
        s[i] = s[i-1] + w[i]
    return curr
    
def isPrime(x, c):
    r = x**.5
    for i in range(c):
        if w[i] > r:
            return True
        if x % w[i] == 0:
            return False

def p050():
    maxSum = 0
    total = prime()
    print total
    for i in range(total):
        if isPrime(s[i], total) and maxSum < s[i]:
            maxSum = s[i]
        for j in range(i):
            sum = s[i] - s[j]
            if isPrime(sum, total) and maxSum < sum:
                maxSum = sum
                print i - j, w[j + 1], sum
    return maxSum
    
if __name__ == '__main__':
    print p050()