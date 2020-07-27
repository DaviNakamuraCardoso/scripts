import datetime
import time
import subprocess

print(datetime.datetime.now().strftime('%A, %H:%M'))
# You can lauch other programs with the Popen() function
while True:
    calc_open = subprocess.Popen('/usr/bin/gnome-calculator')
    calc_open.wait()
#print(calc_open.poll())
 # Doesn't return until calc closes
#print(calc_open.poll())

#cmd_line_arg = subprocess.Popen(['/bin/python3',
                              #   '/home/davi/Documents/Code/Projeto-ATMCP/C15-Documentos-em-PDF-e-Word/exercicio_pratico.py'])

#time.sleep(3)
alarm_clock = subprocess.Popen(['see', '/home/davi/Documents/Code/Projeto-ATMCP/C17-Monitorando-Tempo/alarm.wav'])
# On Linux, the see argument performs the default executable application

date = datetime.datetime(2019, 1, 7, 0, 0, 0)
print(date.strftime('%A'))