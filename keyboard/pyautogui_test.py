import pyautogui

wh = pyautogui.size() # Obtain the screen resolution
print(wh)
print(wh[0])
print(wh[1])
print(wh.width)
print(wh.height)

for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25) # moveTo() moves the c
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25) # Move the mouse in a square

for i in range(10):
    pyautogui.move(100, 0, duration=0.25) # right
    pyautogui.move(0, 100, duration=0.25) # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up

print(pyautogui.position())  # Get the current mouse position
print(pyautogui.position()[0]) # The x coordinate is at index 0
print(pyautogui.position()[1]) # The y coordinante is at index 1
pyautogui.click(10, 5, button='left', clicks=5)
pyautogui.middleClick(700, 200)
pyautogui.doubleClick(700, 300)
pyautogui.dragTo(700, 600)
pyautogui.scroll(200)
pyautogui.mouseInfo()
