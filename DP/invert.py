A = ['a', 'c', 'g', 'u']


def invert(A):
    B = {}
    for i, a in enumerate(A):
        print(i, a)
        B[a] = i
    return B

S = 'acguggc'

B  = invert(A)


C = list(map(lambda x:B[x], S))
print(S)
print(C)




