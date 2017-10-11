#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
最短編集距離を計算する
"""

import math

T = 'null'

S1 = 'GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG'
S2 = 'CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG'

S1 = 'akfsfhskjfhsie'
S2 = 'akie'

d = [[T for _ in range(len(S2))] for _ in range(len(S1))]

d[0][0] = 0

print(d[len(S1)-1][len(S2)-2])

def c(x, y):
    if x == y:
        return 0
    else:
        return 1

def D(i, j):
    if d[i][j] != T:
        return d[i][j]
    if i < 0 or j < 0:
        return math.inf
    # d[i][j]: x[0:i)とy[0:j)のスコア
    d[i][j] = min(
            D(i-1, j-1) + c(S1[i-1], S2[j-1]),
            D(i-1, j  ) + 1,
            D(i  , j-1) + 1
            )
    return d[i][j]


def argmin(List):
    return min(enumerate(List), key=lambda x: x[1])[0]


def trackback():
    a = []
    x, y = len(S1)-1, len(S2)-1
    while x >= 1 and y >= 1:
        print(x,y)
        origin = argmin([
            D(x-1, y-1) + c(S1[x-1], S2[y-1]),
            D(x-1, y  ) + 1,
            D(x  , y-1) + 1 ])
        if origin == 0:
            a.append((x-1, y-1))
            x, y = x-1, y-1
        elif origin == 1:
            a.append((x-1, '-'))
            x, y = x-1, y
        elif origin == 2:
            a.append(('-', y-1))
            x, y = x, y-1
    return a

print(D(len(S1)-1,len(S2)-1))

print(trackback())



