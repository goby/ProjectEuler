# Problem 62
# Cubic Permutations

def same(x, y):
    d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while x:
        d[x % 10] += 1
        x /= 10
    while y:
        d[y % 10] -= 1
        if d[y % 10] < 0: return False
        y /= 10
    return sum(d) == 0