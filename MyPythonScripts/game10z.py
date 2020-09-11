import sys
e = sys.stdin

N = int(e.readline())
D = int(e.readline())
A = int(e.readline())
assert 3 <= N <= 100, 'Error'
assert 1 <= D <= N, 'Error'
assert 1 <= A <= N, 'Error'
dist = D-A
if dist < 0:
    dist = -dist
    print(N - dist)
else:
    print(dist)
