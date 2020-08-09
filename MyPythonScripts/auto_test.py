import os, shelve, random

# Os dados para as provas, em um dicionário no qual as chaves são os estados e os valores, as capitais
os.chdir('..\capitals_quiz')
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California':
            'Sacramento', 'Colorado': 'Denver', 'Conecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahasse',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana':
            'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rougue', 'Maine': 'Annapolis', 'Massaschussets': 'Boston', 'Michigan': 'Lansing', 'Minessota':
            'Saint Paul', 'Mississipi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
            'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
            'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tenesse': 'Nashville', 'Texas': 'Austin', 'Utah':
            'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
            'Charleston', 'Wisconsin': 'Madison', 'Wyomin': 'Cheyenne'}
for quiz_number in range(35):
    quiz_file = open('capitalsquiz%s.txt' % (quiz_number + 1), 'w')
    answer_key_file = open('capitalsquiz_answers%s.txt' % (quiz_number + 1), 'w')
    quiz_file.write('Nome:\nData:__/__/____\n\nTurma:\n\n')
    quiz_file.write((' ' * 20) + 'Quiz das Capitais dos Estados (Formulário %s)' % (quiz_number + 1))
    quiz_file.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question_num in range(49):

        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write('%s. Qual é a capital de %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write('   %s. %s\n' % ('ABCD'[i], answer_options[i]))
            quiz_file.write('\n')

        answer_key_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()


