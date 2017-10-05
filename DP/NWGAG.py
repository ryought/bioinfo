#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Needleman-Wunsch-Gotoh アルゴリスム
"""

import math

T = 'null'

MATCH = 1
MISMATCH = -1
d = 7
e = 1

S1 = 'GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG'
S2 = 'CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG'


_M  = [[T for _ in range(len(S2))] for _ in range(len(S1))]
_Ix = [[T for _ in range(len(S2))] for _ in range(len(S1))]
_Iy = [[T for _ in range(len(S2))] for _ in range(len(S1))]

_M[0][0] = 0

for i in range(len(S2)):
    


def c(x, y):
    if x == y:
        return MATCH
    else:
        return MISMATCH

def M(i, j):
    if _M[i][j] != T:
        return _M[i][j]
    if i < 0 or j < 0:
        return -1*math.inf
    _M[i][j] = max(
            M(i-1, j-1),
            Ix(i-1, j-1),
            Iy(i-1, j-1)
            ) + c(S1[i], S2[j])
    return _M[i][j]

def Ix(i, j):
    if _Ix[i][j] != T:
        return _Ix[i][j]
    if i < 0 or j < 0:
        return -1*math.inf
    _Ix[i][j] = max(
            M(i-1, j) - d,
            Ix(i-1, j) - e,
            Iy(i-1, j) - d
            )
    return _Ix[i][j]

def Iy(i, j):
    if _Iy[i][j] != T:
        return _Iy[i][j]
    if i < 0 or j < 0:
        return -1*math.inf
    _Iy[i][j] = max(
            M(i, j-1) - d,
            Iy(i, j-1) - e
            )
    return _Iy[i][j]


print(M(len(S1)-1, len(S2)-1))
