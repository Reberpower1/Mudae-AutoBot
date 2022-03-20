import pyautogui
import time
time.sleep(5)
f = open('mudae 2.txt', 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1.5)