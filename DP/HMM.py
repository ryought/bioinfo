#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HMM vitervi algorithm
"""

import math

######## 読み込み部分 ###############
params = []
with open('param.txt') as f:
    for line in f:
        params.append(line.split())
K = int(params[1][0])  # アルファベット数
Z = params[2][0:K]
N = int(params[3][0])  # 状態数


def invert(A):
    B = {}
    for i, a in enumerate(A):
        print(i, a)
        B[a] = i
    return B

B = invert(Z)


a = [[math.log(float(x)) if float(x)!=0 else -1*math.inf for x in line[0:N]] for line in params[4:4+N]]
e2 = [[math.log(float(x)) if float(x)!=0 else -1*math.inf for x in line[0:K]] for line in params[9:9+K]]
e = [[0.0 for _ in range(K)]]
for ee in e2:
    e.append(ee)
print(e)

sequence = ''
with open('sample.fasta') as f:
    for line in f:
        if line[0] != '>':
            sequence += line[:-1]

# sequence = 'aaa'
X = list(map(lambda x:B[x], sequence))

# 配列宣言
# V[t][i] t:時刻 i:隠れ状態の番号  
lV  = [['null' for _ in range(N)] for _ in range(len(sequence)+1)]


# 初期値
for i in range(N):
    lV[0][i] = 0 if i == 0 else -1*math.inf
for j in range(1, len(sequence)+1):
    lV[j][0] = -1*math.inf


def run_hyoume(lV):
    # 表を埋める
    for t in range(1,len(sequence)+1):
        for i in range(1,N):
            prev = [lV[t-1][k] + a[k][i] for k in range(N)]
            lV[t][i] = e[i][X[t-1]] + max( prev )

    # 配列の値を返すだけの関数
    def _lV(t,i):
        if i < 0 or j < 0:
            return -1*math.inf
        return lV[t][i]

    # 点数の確認
    print(lV[len(sequence)])




def argmax(List):
    return max(enumerate(List), key=lambda x: x[1])[0]


# トレースバック 2方式に共通
def traceback(lV):
    # この配列にアラインメントを足していく
    alignment = []
    # 配列の値を返すだけの関数

    t = len(sequence)
    print(lV[t])
    i = argmax(lV[t])
    alignment.append(i)

    while t != 0:
        i = argmax([lV[t-1][k] + a[k][i] for k in range(N)])
        t -= 1
        alignment.append(i)
        
    return list(reversed(alignment))



# 実行
run_hyoume(lV)
print(traceback(lV))
