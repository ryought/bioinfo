#!/usr/bin/env python
# -*- coding: utf-8 -*-

def computeSupport(p, T):
    """supportを計算する
    p: パターン
    T: データベース
    n: int 出現回数
    """
    n = 0
    for t in T:
        if t & p == p:
            n += 1
    return n

def computeDenotation(P, T):
    """外延 denotation T(P) = { t \in T : P \subset t } を計算する
    P(set): パターン
    T(list): データベース．ここに含まれるsetのうち，Pを含むものを返す
    list: パターンを含む要素の集合 データベースの部分集合
    """
    return [t for t in T if P.issubset(t)]

def computeClosure(p, T):
    """closure(pを含むTの要素全てが共通に含むパターン，つまり全てのandをとったもの)を計算する
    p(set) pattern
    T(list) database
    c(set) closure
    """
    C = {}
    for t in T:
        if t.issuperset(p):
            if C == {}:
                C = t
            else:
                C = C & t
            if C == {}:
                break
    return C

def is_ppc(C1, C2, i):
    """ check if C2 is prefix preserving closure extension of C1
    """
    c1, c2 = sorted(C1), sorted(C2)
    for k in range(len(c1)):
        if i <= c2[k]:
            # return False
            break
        if c1[k] != c2[k]:
            return False
    return True

def computeClosureTail(P, T):
    global M
    for i in range(1, M+1):
        Z = set([j for j in range(1, i+1)])
        if computeClosure( P & Z, T ) == P:
            return i
    print('not found')

def is_ppc2(C1, C2, i, T):
    """
    C1: P
    C2: H = closure(P U {i})
    """
    tail = computeClosureTail(C1, T)
    L = set([j for j in range(1, i-1+1)])
    if i >= tail and (C1 & L == C2 & L):
        return True
    else:
        return False

M = 9
# 単純に多いパターンを見つける
def backtrack2(C, i, T):
    global M
    theta = 4
    print(C)
    for j in range(i+1, M+1):
        C2 = C | set([j])
        if computeSupport(C2, T) >= theta:
            backtrack2(C2, j, T)

# LCM
def backtrack(C, i, T, M, theta=3):
    global patternDB
    support = computeSupport(C, T)
    patternDB.append((C, support))
    print('\033[31m[track]', C, '\033[m', support)
    for j in range(i+1, M+1):
        if j in C:
            continue
        P = C | set([j])
        n = computeSupport(P, T)
        if n < theta:
            continue
        C2 = computeClosure(P, T)
        if is_ppc2(C, C2, j, T) == False:
            continue
        backtrack(C2, j, computeDenotation(P, T), M, theta=theta)


def computeFreq(T):
    """supportの大きいpatternをDFSで見つける"""
    backtrack2(set(), 0, T)


def computeLCM(T, M, theta):
    """LCMアルゴリズムでfrequentなclosed patternを見つける
    グローバル変数patternDBに出現頻度について降順に格納される"""
    global patternDB
    patternDB = []
    C = computeClosure({}, T)
    backtrack(C, 0, T, theta=theta, M=M)
    patternDB = sorted(patternDB, key=lambda x: x[1], reverse=True)
    print(patternDB)

def read_db_from_file(path):
    """トランザクションデータベースをテキストファイルから作る
    """
    d = []
    do = []
    di = {}
    with open(path, 'rt') as f:
        for line in f:
            z = line.split()
            for x in z:
                if x not in di:
                    di[x] = len(di) + 1
            do.append(z)
    for d2 in do:
        d.append(set(map(lambda x: di[x], d2)))
    return d, len(di)

def main():
    # スライドのサンプルデータ
    T = [{1,2,5,6,7,9},
         {2,3,4,5},
         {1,2,7,8,9},
         {1,7,9},
         {2,7,9},
         {2}]
    M = 9
    computeLCM(T, M, theta=1)


    # 実データ 時間計測する
    import timeit
    T2, M = read_db_from_file('../data/itemset_mining/retail_1based_500.txt')
    print(timeit.timeit(lambda: computeLCM(T2, M, theta=10), number=10)/10, 's')


if __name__ == '__main__':
    main()
