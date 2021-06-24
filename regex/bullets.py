# bullet_point_adder é um programa que adiciona bullet points em um texto da Wikipédia

import pyperclip, sys

text = pyperclip.paste()
lines = text.split('\n')
bullet = sys.argv[1]
ask = sys.argv[2]
del lines[-1]


def nominal_bullets():
    global bullet, lines, ask
    for i in range(len(lines)):
        if ask == 'ce':
            lines[i] = bullet + ' ' + lines[i]
        else:
            lines[i] = bullet + lines[i]


def numeral_bullet():
    global bullet, lines, ask
    count = len(lines)
    for i in range(len(lines)):
        if ask == 'd':
            lines[i] = '    ' + str(count) + '.    ' + lines[i]
            count = count - 1
        else:
            lines[i] = '    ' + str(bullet) + '.    ' + lines[i]
            bullet += 1


def bullet_making():
    global bullet, lines, ask
    if bullet.isdecimal():
        bullet = int(bullet)
        numeral_bullet()
    else:
        nominal_bullets()


bullet_making()
text = '\n'.join(lines)
pyperclip.copy(text)
