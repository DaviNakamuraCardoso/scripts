import sys
entrada = sys.stdin
compensacao_total = 0
M, N = [int(i) for i in entrada.readline()[:-1].split(' ')]
assert 1 <= M <= 1000000, 'Erro'
assert 2 <= N <= 1000, 'Erro'
contas = {}
for i in range(1, N+1):
    contas[i] = 0

for i in range(1, M+1):
    lista = list(entrada.readline().split())
    X, V, Y = [int(d) for d in lista]
    assert 1 <= X <= N, 'Erro'
    assert 1 <= Y <= N, 'Erro'
    assert 1 <= V <= 100, 'Erro'
    assert X != Y, 'Erro'
    contas[X] -= int(V)
    contas[Y] += int(V)
    compensacao_total += V
compensacao = 0
for i in range(1, N+1):
    if contas[i] > 0:
        compensacao += contas[i]


if compensacao_total == compensacao:
    print('N')
    print(compensacao)
else:
    print('S')
    print(compensacao)








