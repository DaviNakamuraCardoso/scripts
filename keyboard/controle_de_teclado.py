import pyautogui
import subprocess
import time

subprocess.Popen('/usr/bin/gnome-text-editor')
time.sleep(8)
pyautogui.typewrite("Hello World!", 0.25) # The second argument sets the time between each type
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.drag(0, 50, duration=2)
pyautogui.hotkey('ctrl', 'c')
