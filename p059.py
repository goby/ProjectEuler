##############
# Problem 59
#
#############

from itertools import product
import sys
def check(lst):
    index = 0
    sum   = 0
    key   =  [0, 0, 0]
    for key[0], key[1], key[2] in product(range(97, 123), repeat = 3):
        sum = 0
        line = ''
        for index in range(len(lst)):
            value = lst[index] ^ key[index % 3]
            if (value > 122 or value < 32) or value in [35, 36, 37, 38]:
                break
            sum += value
            line += chr(value)
        if index == len(lst) - 1:
            print chr(key[0])+chr(key[1])+chr(key[2])
            print line
            return sum
            
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        line = f.readline().strip().split(',')
        print check([int(x) for x in line])
                
        