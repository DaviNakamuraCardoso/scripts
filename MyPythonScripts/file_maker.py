import os, random
os.chdir('..\\datas')
i = 0
for filename in os.listdir():
    os.unlink(filename)
while i < 1000:
    mes = random.randint(1, 12)
    dia = random.randint(1, 31)
    ano = random.randint(1901, 2060)
    file = open('%d-%d-%d.txt' % (mes, dia, ano), 'a')
    file.write('È dSDvi')
    i += 1
