##############################
# Problem 53
# Combinatoric selections
##############################

def Ccount(x):
    ret = x
    end = x / 2
    for r in range(2, end+1):
        ret = ret*(x-r+1)/r
        if ret > 1000000:
            print r
            return x - 2*r + 1
    return 0
            
if __name__ == '__main__':
    ret = 0
    for i in range(2, 101):
        c = Ccount(i)
        if c: print i,c
        ret += c
        
    print ret