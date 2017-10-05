#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
最短編集距離を計算する
"""

import math

T = 'null'

S1 = 'GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG'
S2 = 'CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG'

S1 = 'hoge'
S2 = 'hoge'

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
    d[i][j] = min(
            D(i-1, j-1) + c(S1[i], S2[j]),
            D(i-1, j  ) + 1,
            D(i  , j-1) + 1
            )
    return d[i][j]

print(D(len(S1)-1,len(S2)-1))
