import random

#for i in range(10):
    #spam = random.randint(0, 20)
    #print(spam)
    #assert spam < 10, 'Erro!'

for i in range(10):
    words = ['Hello', 'heLLo', 'davi', 'DAVI', 'goodbye', 'gOodBye']
    egg = random.choice(words)
    bacon = random.choice(words)
    assert str(bacon.lower()) != str(egg.lower()), 'AssertionError'

