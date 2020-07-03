
i = 0
import os
os.chdir('../down')
for i in range(10000):
    filename = open('edavi%s' % i, 'a')
    filename.close()

for filename in os.listdir('../down'):
    if filename.startswith('edavi'):
        print('Deletando', filename)
        os.unlink('../down/%s' % filename)

