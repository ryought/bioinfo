#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Needleman-Wunsch-Gotoh アルゴリスム
"""

import math

#### 共通部分 #############
# 定数
T = 'null'
MATCH = 1
MISMATCH = -1
d = 7
e = 1

# 対象シークエンス
S1 = 'GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG'
S2 = 'CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG'

# S1 = 'ABCDEFGHI'
# S2 = 'AXXBCDQ'

# 配列宣言
_M  = [[T for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
_Ix = [[T for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
_Iy = [[T for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]


# 初期値
_M[0][0] = 0
for j in range(len(S2)+1):
    _M[0][j] = -d - (j-1)*e if j>0 else 0
    _Ix[0][j] = -1*math.inf
    _Iy[0][j] = -1*math.inf
for i in range(len(S1)+1):
    _M[i][0] = -d - (i-1)*e if i>0 else 0
    _Ix[i][0] = -1*math.inf
    _Iy[i][0] = -1*math.inf

# スコア
def c(x, y):
    if x == y:
        return MATCH
    else:
        return MISMATCH
## end of 共通部分 ##############


def run_hyoume():
    # 表を埋める
    for i in range(1,len(S1)+1):
        for j in range(1,len(S2)+1):
            _M[i][j] = max(_M[i-1][j-1],
                    _Ix[i-1][j-1],
                    _Iy[i-1][j-1]
                    ) + c(S1[i-1], S2[j-1])
            _Ix[i][j] = max(
                    _M[i-1][j] - d,
                    _Ix[i-1][j] - e,
                    _Iy[i-1][j] - d
                    )
            _Iy[i][j] = max(
                    _M[i][j-1] - d,
                    _Iy[i][j-1] - e
                    )
    # 配列の値を返すだけの関数
    def M(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _M[i][j]

    def Ix(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _Ix[i][j]

    def Iy(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _Iy[i][j]
    # 点数の確認
    x, y = len(S1), len(S2)
    print('score:', max(M(x,y), Ix(x,y), Iy(x,y)))

def run_memo():
    def M(i, j):
        if _M[i][j] != T:
            return _M[i][j]
        if i < 0 or j < 0:
            return -1*math.inf
        _M[i][j] = max(
                M(i-1, j-1),
                Ix(i-1, j-1),
                Iy(i-1, j-1)
                ) + c(S1[i-1], S2[j-1])
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

    # 実行
    x, y = len(S1), len(S2)
    print('score:', max(M(x,y), Ix(x,y), Iy(x,y)))




def argmax(List):
    return max(enumerate(List), key=lambda x: x[1])[0]


# トレースバック 2方式に共通
def traceback():
    # この配列にアラインメントを足していく
    alignment = []
    # 配列の値を返すだけの関数
    def M(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _M[i][j]

    def Ix(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _Ix[i][j]

    def Iy(i, j):
        if i < 0 or j < 0:
            return -1*math.inf
        return _Iy[i][j]

    x, y = len(S1), len(S2)
    origin = argmax([M(x,y), Ix(x,y), Iy(x,y)])
    alignment.append([x, y])

    while not(x==0 or y==0):
        # 由来を探す
        if origin == 0:
            origin = argmax([M(x-1,y-1), Ix(x-1,y-1), Iy(x-1,y-1)])
            alignment.append([x-1, y-1])
            x, y = x-1, y-1
        elif origin == 1:
            origin = argmax([M(x-1,y)-d, Ix(x-1,y)-e, Iy(x-1,y)-d])
            alignment.append([x-1, '-'])
            x, y = x-1, y
        elif origin == 2:
            origin = argmax([M(x,y-1)-d, -1*math.inf, Iy(x,y-1)-e])
            alignment.append(['-', y-1])
            x, y = x, y-1
    return alignment

# アライメントを綺麗に表示する
def print_alignment(a, size=40):
    prettified = []
    for (x,y) in reversed(a[1:]):
        if x != '-' and y != '-':
            prettified.append((S1[x], S2[y]))
        elif x == '-':
            prettified.append(('-', S2[y]))
        else:
            prettified.append((S1[x], '-'))

    for i in range(len(prettified) // size):
        # size(40)文字ごとに出力
        _X, _Y = '', ''
        for (x,y) in prettified[i*size:(i+1)*size]:
            _X += x
            _Y += y
        print(i*size)
        print(_X)
        print(_Y, '\n')

    # 最終行をプリント
    _X, _Y = '', ''
    i = len(prettified)//size
    for (x,y) in prettified[i*size:]:
        _X += x
        _Y += y
    print(i*size)
    print(_X)
    print(_Y, '\n')


# 実行
method = 'hyoume'

if method == 'memo':
    print(method)
    run_memo()
    a = traceback()
    print_alignment(a)
elif method == 'hyoume':
    print(method)
    run_hyoume()
    a = traceback()
    print_alignment(a)
