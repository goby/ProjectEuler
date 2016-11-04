##############################
# Problem 52
#
# It can be seen that the number, 125874, and its double, 251748, contain 
#   exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#   contain the same digits.
##############################

def checksame(x, y):
    dict = [0 for _ in range(10)]
    for c in str(x): dict[int(c)] += 1
    for c in str(y): 
        if not dict[int(c)]: return False
        dict[int(c)] -= 1
    return sum(dict) == 0
    
def check():
    x = 9
    idx = 10
    while True:
        x += 1
        if str(x)[:2] > '16': 
            idx *= 10
            x = idx
        if not checksame(x, 2*x): continue
        if not checksame(x, 3*x): continue
        if not checksame(x, 4*x): continue
        if not checksame(x, 5*x): continue
        if not checksame(x, 6*x): continue
        
        return x
        
if __name__ == '__main__':
    print check()