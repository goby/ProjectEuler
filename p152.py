#!/usr/bin/env python

# sum of inverse squals to 1/2
# count how many distinct sum(1/i^2) = 1/2, which i in [2, 80]
# there are 3 ways for [2,45]:
#
# * {2,3,4,5,7,12,15,20,28,35}          <- seed
# * {2,3,4,6,7,9,10,20,28,35,36,45}     <- {-5, -15, +6, +9, +10, +36, +45}
# * {2,3,4,6,7,9,12,15,28,30,35,36,45}  <- {-10,-20, +12,+15,+30}
#
# f(n+1) = f(n) + ?
#
