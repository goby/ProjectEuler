#!/bin/python
# -*- coding=utf-8 -*-
#
# ellipse formula: 4x^2 + y^2 = 100
#
# The light beam in this problem starts at the point (0.0,10.1) just outside
# the white cell, and the beam first impacts the mirror at (1.4,-9.6)
# The slope m of the tangent line at any point (x,y) of the given ellipse is: 
#     m = -4x/y
#
# we know the start lasor:
#    (x - x1)(y2 - y1) = (y - y1)(x2 - x1) which slope: m=(y2-y1)/(x2-x1)
# the slope of the normal line:
#    m = y0/4x0
# so slope of the mirror line:
#   θ_o = θ_n + θ_n - θ_i 
#   tan(out) = tan(normal + normal - in)
#            = (tan(2n) - tan(i))/(1 + tan(2n)tan(i))
#

def formulaRoot(a, b, c):
    rt = (b * b - 4. * a * c)**0.5
    return (rt - b)/2/ a, (-rt - b)/2/a


def p144():
    tx = 0
    ty = 10.1
    x = 1.4
    y = -9.6
    upper = (100 - 4 * 0.01)**0.5
    count = 0
    while x > -0.1 or x < 0.1 or y > upper:
        tani = (y - ty)/(x - tx)
        tann =  y / 4 / x
        tan2n = 2 * tann / ( 1 - tann * tann)
        tano = (tan2n - tani)/(1 + tan2n * tani)
        
        # y = tano * (x -x0) + y0
        # 4x^2 + y^2 = 100
        # 4x^2 + (tano * x + y0 - tano * x0)^2 = 100
        # (4 + tano * tano)x^2 + 2*tano*(y0 - tano*x0)x + (y0 - tano * x0)^2 - 100 = 0
        nx = formulaRoot(4 + tano * tano, 2 * tano * (y - tano * x), (y - tano * x) * (y - tano * x) - 100)

        tx = x
        ty = y
        if abs(nx[0] -x) > abs(nx[1] -x):
            x = nx[1]
        else:
            x = nx[0]
        y = tano * (x - tx) + ty

        count+= 1

    return count

if __name__ == "__main__":
    print p144()

        
   
