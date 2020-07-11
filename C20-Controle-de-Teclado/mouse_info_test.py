import pyautogui

pyautogui.screenshot()
print(pyautogui.pixel(x=0, y=0))
print(pyautogui.pixel(x=1000, y=50)) # Pyautogui pixel method will return the pixel's RGB
print(pyautogui.pixelMatchesColor(x=83, y=400, expectedRGBColor=(253, 253, 253))) # This method will return False if
# the pixel doesn't match the given color

b = pyautogui.locateOnScreen('tools.png')
print(b)
pyautogui.click(b) # Pyautogui image recognition method is such a great form of getting a element in a page
#fw = pyautogui.getActiveWindow()
# pyautogui.getAllWindows()
# pyautogui.getWindowsWithTitle(title)
# The isActive(), isMinimized(), isMaximized() methods return booleans. maximize(), minimize() and close() will change
# the window's state

# Unfortunately, this attribute works in Windows only






