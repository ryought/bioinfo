#!/usr/bin/env python
# -*- coding: utf-8 -*-

## random sampling of Gamma(x|a,b)  with Metropolis method

import numpy as np
import matplotlib.pyplot as plt

# 乱数発生の方法
# np.random.rand() # 0~1の一様乱数
# np.random.normal(mu, sigma)  # 正規分布

def gamma_23(x):
    """Gamma(x|a,b)を計算する x^{a-1} e^{-bx} に比例することを使う"""
    a, b = 2, 3
    return x**(a-1) * np.exp(-b * x)

def metropolis_sampling(q, sigma, N=100, init_x=0.1):
    """サンプリングをN回して結果を返す
    @param q:func サンプリングする確率分布の確率密度関数
    @param N:int サンプリング回数 
    @return xs:array サンプルの集合
    """
    # 初期化
    x = init_x
    xs = [init_x]
    # イテレーション
    for i in range(N):
        # 乱数発生
        y = np.random.normal(x, sigma)
        r = np.random.rand()
        # 採択
        if q(y) / q(x) > r:
            x = y
        else:
            pass
        xs.append(x)
    return xs

def compare(N=100000):
    plt.subplots_adjust(hspace=0.4)
    plt.suptitle('gamma(2,3) N={0}'.format(N))

    xs = metropolis_sampling(gamma_23, 0.2, N=2*N)
    xs = np.array(xs[N:2*N])
    plt.subplot(2, 1, 1)
    plt.xlim([0, 5])
    plt.title('metropolis')
    plt.hist(xs, bins=50)
    
    a, b = 2, 1/3
    # numpyのgamma分布との比較
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.gamma.html#numpy.random.gamma
    # p(x) = (x^{k-1} e^{-x/\theta}) / (\theta^k \Gamma(k)) という実装らしいので
    #  \theta = 1/b とした
    s = np.random.gamma(a, b, N)
    plt.subplot(2, 1, 2)
    plt.xlim([0, 5])
    plt.title('numpy.random.gamma')
    plt.hist(s, bins=50)

    plt.savefig('compare.png')

def main():
    trial = 300
    bin_size = 100
    ave = np.zeros(trial)
    var = np.zeros(trial)
    Ns = np.arange(bin_size, bin_size*(trial+1), bin_size)
    for i, N in enumerate(Ns):
        xs = metropolis_sampling(gamma_23, 0.2, N=N)
        xs = np.array(xs[N//2:N])
        ave[i], var[i] = np.average(xs), np.var(xs)

    print(Ns.shape, ave.shape, var.shape)
    plt.plot(Ns, ave, label='ave')
    plt.plot(Ns, var, label='var')
    
    # gamma(a,b) a=2, b=3の期待値分散は
    # E = a/b  V = a^2/b だから
    a, b = 2, 3
    E, V = a/b, (a)/(b**2)
    plt.plot([0, trial*bin_size], [E, E], label='ave expect')
    plt.plot([0, trial*bin_size], [V, V], label='var expect')

    plt.legend()
    plt.show()


# compare()
main()


