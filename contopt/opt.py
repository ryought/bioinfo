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

# Ax = b, A:結合本数のデータ x:結合エネルギーのパラメータ b:エネルギーの実験値
A = [count(seq) for (_, seq, energy) in a]
b = [float(energy) for (_, _ , energy) in a]


# object function
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

def run(alpha=0.0001, initial_x = [1,1,-1, -1], iteration=100):
    fs = []
    x = initial_x  # 各部分のエネルギー [G(AU) G(GC) G(tAU) G(tGC)]
    print(alpha) # ステップサイズ
    print(x)

    for k in range(iteration):  # 勾配降下回数
        fs.append(f(x))
        x = add(x, scalar(-alpha, grad_f(x)))
        # x = x + alpha * grad_f(x)
    print(x)
    return x, fs

def estimation(x):
    b0 = [0 for _ in range(N)]
    for i in range(N):
        b0[i] = A[i][0]*x[0] + A[i][1]*x[1] + A[i][2]*x[2] + A[i][3]*x[3]
    return b0


alphas = [0.00001, 0.00005,  0.0001, 0.0005]

for i, alpha in enumerate(alphas):
    x, fs = run(alpha=alpha)
    log = np.array(fs)

    print(len(alphas))
    # 収束の様子
    plt.plot(log, label='alpha={0}'.format(alpha))
plt.legend()
plt.show()

# 散布図
# b0(予測値) vs b(実験値)でプロットの作成
b0 = np.array(estimation(x))
plt.scatter(b0, b)
plt.xlabel('predicted')
plt.ylabel('actual experimental')
plt.show()

## 最終的な収束値を見つける
x, _ = run(alpha=0.0001, iteration=10000)

## numpyを使って解析的に求める
AA = np.array(A)
bb = np.array(b)
x_analytic = np.dot(np.dot(np.linalg.inv(np.dot(AA.T, AA)), AA.T),  bb)
print('by numpy', x_analytic, 'original',  x)

