#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def main(number):
    # parse argument
    # psr = argparse.ArgumentParser()
    # psr.add_argument('-f', '--file', default='', type=int)
    # args = psr.parse_args()

    # main function

    # d = {0: (price, [items])}
    d = {}
    with open('ca-data/{0}.txt'.format(number), 'rt') as f:
        for line in f:
            t = line.split()
            bid_id, price, items = int(t[0]), int(t[1]), t[2:]
            items = filter(lambda x: not(x.startswith('#')), items)
            d[bid_id] = (price, items)

    item_occur = {}
    for bid_id, (price, items) in d.items():
        for x in items:
            if x in item_occur:
                item_occur[x].append(bid_id)
            else:
                item_occur[x] = [bid_id]

    # 1 object
    obj = "Maximize\n obj: "
    for bid_id, (price, _) in d.items():
        obj += "{0} x{1} + ".format(price, bid_id)
    obj = obj[:-2]
    obj += '\n'

    # 2 subject
    subject = "Subject To\n"
    i = 1
    for _, bidids in item_occur.items():
        subject += " c{0}: ".format(i)
        for bidid in bidids:
            subject += " x{0} + ".format(bidid)
        subject = subject[:-2] # strip tailing "+ "
        subject += ' <= 1\n'

        i += 1

    # 3 bounding
    bound = "Bounds\n"
    for bid_id, _ in d.items():
        bound += " 0 <= x{0} <= 1\n".format(bid_id)
    bound += "End"

    # combine all
    cplex_out = "" + obj + subject + bound

    with open('data_out_{0}.txt'.format(number), 'wt') as f:
        f.write(cplex_out)


if __name__ == '__main__':
    for i in range(1,12):
        main(i)
