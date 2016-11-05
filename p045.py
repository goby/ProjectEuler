
import math

if __name__ == '__main__':
    # http://mathworld.wolfram.com/HexagonalPentagonalNumber.html
    # And the Hexgonal number is always a triangular number
    #    H(n) = n(2n-1) = 1/2(2n - 1)[(2n - 1) + 1] = T(2n-1)
    # So we need find next hexagonal & pentagonal number
    # (1,1), (165, 143), (31977, 27693)
    n = 27693
    print n * (2 * n - 1)