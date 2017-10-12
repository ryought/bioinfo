
params = []
with open('param.txt') as f:
    for line in f:
        params.append(line.split())

K = int(params[1][0])

Z = params[2][0:4]
print(Z)

N = int(params[3][0])

print(K,N)

A = [[float(x) for x in line[0:N]] for line in params[4:4+N]]

print(A)

e = [[float(x) for x in line[0:K]] for line in params[9:9+K]]
print(e)

e2 = [[0 for _ in range(K)]]
for ee in e:
    e2.append(ee)
print(e2[0], e2[1])


sequence = ''
with open('sample.fasta') as f:
    for line in f:
        if line[0] != '>':
            sequence += line[:-1]
print(sequence)

