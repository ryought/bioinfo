#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
前向きアルゴリズム
"""

from math import log, exp, inf

#### 共通部分 #############
# 定数
T = 1
MATCH = 1
MISMATCH = -1
d = 7
e = 1
infty = 10000000000

# 対象シークエンス
S1 = 'GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG'
S2 = 'CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG'

# S1 = 'ABCDEFGHI'
# S2 = 'AXXBCDQ'


# スコア
def c(x, y):
    if x == y:
        return MATCH
    else:
        return MISMATCH
## end of 共通部分 ##############


# logsumexp adding
def add(logB, logC):
    m = max(logB, logC)
    logA = m + log(exp(logB-m) + exp(logC-m))
    return logA

def forward(x=len(S1), y=len(S2)):
    # 配列宣言
    fM  = [['null' for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
    fx  = [['null' for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
    fy  = [['null' for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
    f   = [['null' for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
# # 初期値
# fM[0][0] = 1
# for j in range(len(S2)+1):
#     fM[0][j] = 0 if j != 0  
#     fx[0][j] = 0
#     fy[0][j] = exp((-d-(j-1)e)/T) if j != 0
# for i in range(len(S1)+1):
#     fM[i][0] = 0 if i != 0  
#     fx[i][0] = exp((-d-(i-1)e)/T) if i != 0
#     fy[i][0] = 0
# のlogとったバージョン
    fM[0][0] = 0
    for j in range(len(S2)+1):
        fx[0][j] = -infty
        if j != 0:
            fM[0][j] = -infty  
            fy[0][j] = (-d-(j-1)*e)/T
    for i in range(len(S1)+1):
        if i != 0:
            fM[i][0] = -infty
            fx[i][0] = (-d-(i-1)*e)/T
        fy[i][0] = -infty
    # 表を埋める
    for i in range(1,len(S1)+1):
        for j in range(1,len(S2)+1):
            # fM(i,j) = fm(i-1,j-1)exp(c/t) + fx(i-1,j-1)exp(c/t) + fy(i-1,j-1)exp(c/t)
            _c = c(S1[i-1], S2[j-1])
            tmp = add(fM[i-1][j-1] + _c/T, fx[i-1][j-1] + _c/T)
            fM[i][j] = add(tmp, fy[i-1][j-1] + _c/T)

            # fx(i,j) = fm(i-1,j)exp(-d/t) + fx(i-1,j)exp(-e/t) + fy(i-1,j)exp(-d/t)
            tmp = add(fM[i-1][j] - d/T, fx[i-1][j] - e/T)
            fx[i][j] = add(tmp, fy[i-1][j] - d/T)

            # fy(i,j) = fm(i,j-1)exp(-d/t) + fy(i,j-1)exp(-e/t)
            fy[i][j] = add(fM[i][j-1] - d/T, fy[i][j-1] - e/T)

            # f(i,j) = fm(i,j) + fx(i,j) + fy(i,j)
            f[i][j] = fM[i][j] + fx[i][j] + fy[i][j]

    # 点数の確認
    print('Z:', f[len(S1)][len(S2)], exp(f[len(S1)][len(S2)]))
    return f[x][y]



def argmax(List):
    return max(enumerate(List), key=lambda x: x[1])[0]




logZ = forward()
# P = exp(S/T) / Z より、 logP = S/T - logZ
Score = -1  # NWG.pyの実行結果
logP = Score/T - logZ
print('probability: log=', logP, 'p=', exp(logP))
