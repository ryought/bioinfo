#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import csv
# tsv = csv.reader(file(r""))


# tsvの読み込み
# https://qiita.com/lethe2211/items/6cbade2bc547649bc040
# 実行時は python opt.py < data.tsv とせよ
import sys
a = []
for line in sys.stdin:
    if line[0] != '#':
        a.append(line.split())


print('loaded', len(a))
N = len(a) # datasize
#b[N] # input array
#A[N] # 構造のデータ

# 配列を数える
# input: 'CCGG'
# output: [0, 0, 0, 0]
def count(seq):
    x = [0,0,0,0]
    # 最初の文字
    if seq[0] in {'A', 'U'}:
        x[2] += 1
    elif seq[0] in {'C', 'G'}:
        x[3] += 1
    # 最後の文字
    if seq[-1] in {'A', 'U'}:
        x[2] += 1
    elif seq[-1] in {'C', 'G'}:
        x[3] += 1
    # その間は普通に数数える
    for i in seq[1:-1]:
        if i in {'A', 'U'}:
            x[0] += 1
        elif i in {'C', 'G'}:
            x[1] += 1
    return x


A = [count(seq) for (_, seq, energy) in a]
b = [float(energy) for (_, _ , energy) in a]

print(b)

def f(x):
    S = 0
    for i in range(N):
        S += b[i] - (A[i][0]*x[0] + A[i][1]*x[1] + A[i][2]*x[2] + A[i][3]*x[3])
    return S

print(f([1.0,1.0,1.0,1.0]))

    

def grad_f(x):
    # xを受けて$-\frac{\Delta f}{\Delta x}$ を返す
    # とりあえず数値微分
    # h =  TODO
    h = []
    # return [ 


def run(alpha=1, initial_x = [1,1,1,1]):
    xs = [] # 途中経過の集合
    x = initial_x  # 各部分のエネルギー [G(AU) G(GC) G(tAU) G(tGC)]
    print(alpha) # ステップサイズ

    for k in range(100):  # 勾配降下回数
        x = x + alpha * grad_f(x)
        xs.append(x)
    return xs


