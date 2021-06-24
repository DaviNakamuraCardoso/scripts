def davi(i, j):
    grade[i][j] = 'o'

    if (i == L-1):return

    if (grade[i + 1][j] == '.'): davi(i + 1, j)
    if (grade[i + 1][j] == '#'):
        if (grade[i][j - 1] == '.'): davi(i, j - 1)
        if (grade[i][j + 1] == '.'): davi(i, j + 1)


import sys
f = sys.stdin
sys.setrecursionlimit(50000)


A, L = [int(i) for i in f.readline()[:-1].split(" ")]

grade = []
for i in range(A):
    grade.append(list(f.readline()[:-1]))

davi(0, grade[0].index('o'))
for i in range(L):
    print("".join(grade[i]))

