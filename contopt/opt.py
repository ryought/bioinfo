#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

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



def f(x):
    S = 0
    for i in range(N):
        S += (b[i] - (A[i][0]*x[0] + A[i][1]*x[1] + A[i][2]*x[2] + A[i][3]*x[3]))**2
    return S

print(f([0,0.1,0.2,2]))

def add(x, y):
    assert len(x) == len(y)
    z = [0 for _ in range(len(x))]
    for i in range(len(x)):
        z[i] = x[i] + y[i]
    return z



def scalar(c, x):
    z = [0 for _ in range(len(x))]
    for i in range(len(x)):
        z[i] = c * x[i]
    return z


def grad_f(x):
    # xを受けて$-\frac{\Delta f}{\Delta x}$ を返す
    # とりあえず数値微分
    h = 0.00001
    return [(f(add(x, [h, 0, 0, 0])) - f(x))/h,
            (f(add(x, [0, h, 0, 0])) - f(x))/h,
            (f(add(x, [0, 0, h, 0])) - f(x))/h,
            (f(add(x, [0, 0, 0, h])) - f(x))/h] 


f([0,0,0,0])
print(grad_f([0,0,0,0]))

def run(alpha=0.0001, initial_x = [0,0,0,0]):
    fs = []
    x = initial_x  # 各部分のエネルギー [G(AU) G(GC) G(tAU) G(tGC)]
    print(alpha) # ステップサイズ
    print(x)

    for k in range(10000):  # 勾配降下回数
        fs.append(f(x))
        x = add(x, scalar(-alpha, grad_f(x)))
        # x = x + alpha * grad_f(x)


    print(x)
    return fs


fs = run()
log = np.array(fs)
print(log.shape)
plt.plot(log)
plt.show()
