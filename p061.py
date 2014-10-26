# Cyclical figurate numbers
# Problem 61


funs = [
    [lambda x : x * (x + 1) / 2, 44, 141], 
    [lambda x : x * x, 32, 100], 
    [lambda x : x * (3 * x - 1) / 2, 25, 82], 
    [lambda x : x * (2 * x - 1), 22, 70],
    [lambda x : x * (5 * x - 3) / 2, 20 , 63],
    [lambda x : x * (3 * x - 2), 18, 58],
]

def dfs(first, current, level):
    if level == 3:
        print first, current
        return current if (funs[0][0](first)/100 == funs[-1][0](current) % 100) else 0
    
    m = funs[level - 1][0](current) % 100
    for i in range(funs[level][1]-10, funs[level][2]+10):
        if funs[level][0](i) < 1000: continue
        if funs[level][0](i) > 10000: continue
        if m == funs[level][0](i) / 100:
            r = dfs(first, i, level+1)
            if r: return r
            
    return 0

if __name__ == '__main__':
#    for i in range(funs[0][1]-10, funs[0][2]+1):
#        if funs[0][0](i) < 1000: continue
#        r = dfs(i, i, 1)
#        if r: 
#            print r
#            break 
    for i in range(6):
        c = set()
        for x in range(funs[i][1], funs[i][2]+1):
            c.add(funs[i][0](x) % 100)
        print i,c
        for x in range(funs[i][1], funs[i][2]+1):
            c.add(funs[i][0](x) / 100)
        print i,c