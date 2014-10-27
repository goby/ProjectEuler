# Problem 66
#   Diophantine equation
#   Pell equation(http://en.wikipedia.org/wiki/Pell%27s_equation)
    
# the form diophantine equation: x^2 - Dy^2 = 1
# 无限序列公式

def pell(h, k, D):
    if h*h - D * k * k == 1:
        return h
    
def diophantine(h, k):
    y = 1
    while True:
        x = D * y * y + 1
        if ((x%10) in [0,1,4,5,6,9]) and issquare(x):
            return x
        y += 1
            
if __name__ == '__main__':
    result = 0
    maxium = 0
    for D in range(200, 1001):
        if D % 10 == 0: print D
        if not issquare(D):
            ret = diophantine(D)
            if ret > maxium:
                print ret, D
                maxium = ret
                result = D
                
    print result
