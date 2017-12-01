#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    T = 6
    sd, sc = 0, 20
    v = np.zeros((T+1, 21))
    print(v.shape)

    for s in range(sd, sc+1):
        if s == sd:
            v[T,s] = 0
        else:
            v[T,s] = 1
    for t in range(10, 0-1, -1):
        for s in range(sd, sc+1):
            if s == sd:



if __name__ == '__main__':
    main()
