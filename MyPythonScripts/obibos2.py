import sys
e = sys.stdin
L = int(e.readline())
C = int(e.readline())
assert 1 <= L <= 100, 'Erro'
assert 1 <= C <= 100, 'Erro'

t1 = (C * L) + ((C-1) * (L-1))
t2 = 2 * (C-1) + 2 * (L-1)

print(t1)
print(t2)



