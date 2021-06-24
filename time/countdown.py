import time
import subprocess

for i in range(60, 0, -1):
    print(i)
    time.sleep(1)

subprocess.Popen(['see', '/home/davi/Documents/Code/Projeto-ATMCP/C17-Monitorando-Tempo/alarm.wav'])
