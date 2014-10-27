# Problem 64
# 

#
# Fraction_of_root_n = x / (root_n - y)
#   So we can compare x and y only to get what the perodic times of faction of 
#   the root n
#
def perodic(n):
    originx = 1  
    originy = int( n ** 0.5) # Get initial form
    x = originx
    y = originy
    count = 0
    while True:
        tmp = (n - y * y) / x          # The denominator
        num = int ((n ** 0.5 + y)/tmp) # Integral part
        y = tmp * num - y              # Get next form 
        x = tmp
        count += 1
        if y == originy and x == originx:
            return count
            
if __name__ == '__main__':
    odd = 0
    for i in range(2, 10001):
        r = i ** 0.5
        if r != int(r) and (perodic(i)&1):
            odd += 1
    print odd
    