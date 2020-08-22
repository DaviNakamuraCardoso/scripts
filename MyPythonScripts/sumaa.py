import sys

entrada = sys.stdin
N, K = [int(i) for i in entrada.readline()[0:-1].split(' ')]
sequencia = list(entrada.readline()[:-1].split())
for i in range(len(sequencia)):
    sequencia[i] = int(sequencia[i])
    assert 0 <= sequencia[i] <= 100, 'Error'

assert 1 <= N <= 500000, 'Erro'
assert 0 <= K <= 1000000, 'Erro'

count = 0
for d in range(N):
    for j in range(d, N):
        soma = sum(sequencia[d:j+1])
        if soma == K:
            count += 1

print(count)