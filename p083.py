#!/bin/python
'''
Path sum: four ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom
right by moving left, right, up, and down.

'''

import sys

class Infinity:
    def __init__(self, flag):
        self.__flag = flag

    def __neg__(self):
        return Infinity(-1)

    def __cmp__(self, i):
        return self.__flag

inf = Infinity(1)

class Matrix:
    '''
    A simple matrix create from col and row
    '''
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.data = [ None for _ in range(col * row) ]

    def __getitem__(self, (col, row)):
        self.__validate(col, row)
        return self.data[ row * self.col + col ]

    def __setitem__(self, (col, row), value):
        self.__validate(col, row)
        self.data[row * self.col + col ] = value

    def __str__(self):
        s = []
        for r in range(self.row):
            s.append(', '.join([str(e) for e in self.data[self.col * r : self.col * r + self.col]]))
        return '\n'.join(s)

    def __validate(self, col, row):
        if col >= self.col or row >= self.row or col < 0 or row < 0:
            raise ValueError("Invalid col or row")

def get_matrix(fname):
    matrix = []
    with open(fname) as f:
        for l in f.readlines():
            nums = l.strip().split(',')
            row = [int(n) for n in nums]
            matrix.append(row)

    return matrix

def extract_min(d, q):
    '''return x,y'''
    mind = -1
    minu = None
    for e in q:
        value = d[e[0]][e[1]]
        if (value > 0 and value < mind) or mind < 0:
            mind = value
            minu = e

    q.remove(minu)
    return minu

def dijistra(m):
    row = len(m)
    col = len(m[0])

    queue = set((r, c) for c in range(col) for r in range(row))
    score = [[ -1 for _ in range(col)] for _ in range(row)]
    score[0][0] = m[0][0]
    
    while len(queue) > 0:
        u = extract_min(score, queue)
        x = u[0]
        y = u[1]
        du = score[x][y]
        vs = []
        if x > 0:
            #left
            vs.append([x - 1, y])
        if x < row - 1:
            # right
            vs.append([x + 1, y])
        if y > 0:
            # up
            vs.append([x, y - 1])
        if y < col - 1:
            vs.append([x, y + 1])
        for v in vs:
            x = v[0]
            y = v[1]
            wv = m[x][y]
            if score[x][y] < 0 or (score[x][y] > du + wv):
                score[x][y] = du + wv

    return score[row - 1][col - 1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        m = get_matrix(sys.argv[1])
        print dijistra(m)
    else:
        print "Usage: p083.py <matrix file>"
