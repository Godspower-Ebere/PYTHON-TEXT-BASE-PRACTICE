import pyautogui
import time
move=200
pyautogui.press("win")
pyautogui.typewrite("paint",0.25)
time.sleep(2)
pyautogui.press("enter")

while move > 0:
    pyautogui.drag(move,0,0.25)
    move-=5
    pyautogui.drag(0,move,0.25)
    pyautogui.drag(-move,0,0.25)
    move-=5
    pyautogui.drag(0,-move,0.25)

