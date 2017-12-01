import numpy as np

nuc      = ["A", "C", "G", "T"]

def nuc_to_code(nuc):
    return {'A': [1, 0, 0, 0],
            'C': [0, 1, 0, 0],
            'G': [0, 0, 1, 0],
            'T': [0, 0, 0, 1],
    }.get(nuc, [0, 0, 0, 0])

def write_dataset(outfile, x, y):
    with open(outfile, 'w') as fo:
        fo.write("y\tx\n")
        for i in range(len(y)):
            fo.write("%s\t%s\n" % (y[i], x[i]))

def read_dataset(infile):
    x, y = [], []
    with open(infile) as fi:
        next(fi)
        for s in fi:
            y1, x1 = s.strip().split("\t")
            x1 = [nuc_to_code(nuc) for nuc in x1]
            x.append(x1)
            y.append(int(y1))
    x, y = np.array(x), np.array(y)
    return (x, y)

def generate_dataset(n_p, n_n, length, motif, nuc):
    m    = len(motif)
    y    = ([1] * n_p + [0] * n_n)
    x    = [None] * (n_p + n_n)
    for i in range(n_p + n_n):
        seq = np.random.choice(nuc, size=length) # random seq
        if i < n_p: # embed motif at random position
            j = np.random.randint(length - m + 1)
            for k in range(m):
                seq[j + k] = np.random.choice(nuc, p=motif[k])
        x[i] = ''.join(seq)
    return (x, y)


motif    = [[0.0, 1.0, 0.0, 0.0], # C
            [0.5, 0.0, 0.0, 0.5], # A/T
            [0.0, 0.5, 0.5, 0.0], # C/G
            [0.0, 0.0, 1.0, 0.0], # G
            [0.0, 0.0, 0.0, 1.0]] # T

# motif    = [[0.0, 1.0, 0.0, 0.0], # C
#             [1.0, 0.0, 0.0, 0.0], # A/T
#             [0.0, 1.0, 0.0, 0.0], # C/G
#             [0.0, 0.0, 1.0, 0.0], # G
#             [0.0, 0.0, 0.0, 1.0]] # T

seq_len  = 20
np_train = 10000
nn_train = 10000
np_test  = 1000
nn_test  = 1000

if __name__ == '__main__':
    x_train, y_train = generate_dataset(np_train, nn_train, seq_len, motif, nuc)
    x_test, y_test   = generate_dataset(np_test, nn_test, seq_len, motif, nuc)
    write_dataset("motif_data_train.txt", x_train, y_train)
    write_dataset("motif_data_test.txt" , x_test , y_test )



