#!/usr/bin/env python
# -*- coding: utf-8 -*-

def computeSupport(p, T):
    """supportを計算する
    Args:
            p : パターン
            T : データベース
    Returns:
        n : int 出現回数
    """
    n = 0
    for t in T:
        if t & p == p:
            n += 1
    return n

def computeDenotation(P, T):
    """外延 denotation T(P) = { t \in T : P \subset t } を計算する
    @params P(set): パターン
    @params T(list): データベース．ここに含まれるsetのうち，Pを含むものを返す
    @return list: パターンを含む要素の集合 データベースの部分集合
    """
    return [t for t in T if P.issubset(t)]

def computeClosure(p, T):
    """closure(pを含むTの要素全てが共通に含むパターン，つまり全てのandをとったもの)を計算する
    @params p(set) pattern
    @params T(list) database
    @return c(set) closure
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
    print('ppc', c1, c2, i)
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
        print(computeClosure(P&Z, T), P)
        if computeClosure( P & Z, T ) == P:
            print('tail', i)
            return i
    print('not found')

def is_ppc2(C1, C2, i, T):
    """
    C1: P
    C2: H = closure(P U {i})
    """
    tail = computeClosureTail(C1, T)
    L = set([j for j in range(1, i-1+1)])
    # print(C1, C2, L, i, tail)
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
    print('\033[31m[track]', C, '\033[m')
    # print(list(range(i+1, M+1)))
    for j in range(i+1, M+1):
        # print('j=', j, C, i, T)
        if j in C:
            continue
        P = C | set([j])
        n = computeSupport(P, T)
        if n < theta:
            continue
        C2 = computeClosure(P, T)
        if is_ppc2(C, C2, j, T) == False:
            # if is_ppc(C, C2, j) == False:
            continue
        # print('induce', C2, 'from', C, 'in', j)
        backtrack(C2, j, computeDenotation(P, T), M, theta=theta)


def computeFreq(T):
    backtrack2(set(), 0, T)


def computeLCM(T, M, theta):
    C = computeClosure({}, T)
    backtrack(C, 0, T, theta=theta, M=M)

def read_db_from_file(path):
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
    T = [{1,2,5,6,7,9},
         {2,3,4,5},
         {1,2,7,8,9},
         {1,7,9},
         {2,7,9},
         {2}]
    M = 9
    for t in T:
        print(t)
    print(T[1])
    for x in T[4]:
        print('a', x)
    print(T[4], sorted(T[4]))
    print({1,2,3,4} == {1,2,3,4})
    print({1,2} == {2})
    print(T[1] | T[2])
    print(T[1] & T[2])
    print('support', computeSupport({1,2}, T))
    print('support', computeSupport({1}, T))
    print('support', computeSupport({2}, T))
    print('support', computeSupport(set(), T))
    print('closure', computeClosure({1,2}, T))
    print('closure', computeClosure({1,9}, T))
    print('closure', computeClosure({4}, T))
    print('closure of empty set', computeClosure(set(), T))
    print('denota', computeDenotation({1}, T))
    print('denota', computeDenotation(set(), T))
    print('ppc', is_ppc({1,7,9}, {1,2,5,6,7,9}, 3))
    print('ppc', is_ppc({1,2,7,9}, {1,2,5,6,7,9}, 5))
    print('ppc', is_ppc({1,2,7,9}, {1,2,5,6,7,9}, 10))
    print('ppc', is_ppc({1,2,7,9}, {1,2,5,6,7,9}, 10))
    computeFreq(T)

    computeLCM(T, M, theta=1)

    print('ppc', is_ppc({2}, {2,3,4,5}, 2))
    print('ppc', is_ppc({2}, {2,3,4,5}, 3))
    print('closure', computeClosure({2,3}, T))


    for i in range(1, M-1):
        print('closure', i, computeClosure(set([i]), T))
        print('ppc', is_ppc(set(), computeClosure(set([i]), T), i))

    print('ppc2', is_ppc2({2}, {2,3,4,5}, 2, T))
    print('ppc2', is_ppc2({2}, {2,3,4,5}, 3, T))
    print('closure', computeClosure({4}, T))
    print('closuretail', computeClosureTail({2,3,4,5}, T))
    print('closuretail', computeClosureTail({1,2,7,9}, T))

    T2, M = read_db_from_file('../data/itemset_mining/retail_1based.txt')
    # computeLCM(T2, M, theta=10)

if __name__ == '__main__':
    main()
