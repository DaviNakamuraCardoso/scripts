import random, os

os.chdir('..\\documentos')
for filename in os.listdir():
    if filename.endswith('.txt'):
     os.unlink(filename)

i = 0
while i < 2000:
    num = random.randint(1,2)
    file = open('fjkf%s.txt' % i, 'a')
    i += num


