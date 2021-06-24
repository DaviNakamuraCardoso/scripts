import random, os
os.chdir('..\capitals_quiz')
# Definição de um dicionário que contém as referências como chaves e os textos como valores
textos = {'Ácido Sulfúrico': 'H2SO4', 'Ácido Nítrico': 'HNO3', 'Ácido clorídrico': 'HCl', 'Ácido Fosfórico': 'H3PO4',
          'Ácido Acético': 'CH3-COOH', 'Ácido Fluorídrico': 'HF', 'Ácido Carbônico': 'H2CO3', 'Ácido Sulfuroso':
          'H2SO3', 'Ácido Nitroso': 'HNO2', 'Ácido Perclórico': 'HClO4', 'Ácido Clórico': 'HClO3', 'Ácido Cloroso':
          'HClO2', 'Ácido Hipocloroso': 'HClO', 'Ácido Bromídrico': 'HBr', 'Ácido Perbrômico': 'HBrO4', 'Ácido Brômico':
          'HBrO3', 'Ácido Bromoso': 'HBrO2', 'Ácido Hipobromoso': 'HBrO', 'Hidróxido de Sódio': 'NaOH',
          'Hidróxido de Magnésio': 'Mg(OH)2', 'Hidróxido de Manganês II': 'Mn(OH)2', 'Hidróxido Ferroso': 'Fe(OH)2',
          'Hidróxido Férrico': 'Fe(OH)3', 'Hidróxido de Lítio': 'LiOH', 'Hidróxido de Potássio': 'KOH'}
rev_textos = {}
keys = list(textos.keys())
values = list(textos.values())
for value, key in zip(values, keys):
    rev_textos[value] = key


for file_number in range(38):
    quiz_file = open('QuizdaQuímicaReverso%s.txt' % (file_number + 1), 'w')
    gabarito_file = open('GabaritodoQuizReverso%s.txt' % (file_number + 1), 'w')
    quiz_file.write(' '*40 + 'Quiz Reverso de Número %s' % (file_number + 1) + '\n\n')
    quiz_file.write('Nome:\nData:__/__/____\n\n')
    compostos = list(rev_textos.keys())
    random.shuffle(compostos)
    for question_num in range(len(compostos)):
        resposta_correta = rev_textos[compostos[question_num]]
        respostas_erradas = list(rev_textos.values())
        del respostas_erradas[respostas_erradas.index(resposta_correta)]
        respostas_erradas = random.sample(respostas_erradas, 4)
        opcoes = respostas_erradas + [resposta_correta]
        random.shuffle(opcoes)
        quiz_file.write('\n%s - Qual é o nome do %s ? \n\n' % (question_num + 1, compostos[question_num]))
        for i in range(5):
            quiz_file.write('%s. %s' % ('ABCDE'[i], opcoes[i]))
            quiz_file.write('\n')

        gabarito_file.write('%s . %s' % (question_num + 1, 'ABCDE'[opcoes.index(resposta_correta)]))
    gabarito_file.close()
    quiz_file.close()




