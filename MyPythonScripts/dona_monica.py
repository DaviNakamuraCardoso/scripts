import sys
entrada = sys.stdin
M, A, B = [int(i) for i in entrada.readlines()]

assert 40 <= M <= 110, 'Erro'
assert 1 <= A < M, 'Erro'
assert 1 <= B < M, 'Erro'
assert A != B, 'Erro'
C = M - (A + B)

idades = []

idades.append(A)
idades.append(B)
idades.append(C)
idades.sort()
print(idades[-1])
