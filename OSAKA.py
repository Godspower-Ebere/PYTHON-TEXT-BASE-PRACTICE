import pyautogui
import time
pyautogui.hotkey("win","e")
time.sleep(5)
with pyautogui.hold("alt"):
    pyautogui.press("tab",presses=1,interval=0.25)
pyautogui.press("tab",presses=3,interval=0.25)
pyautogui.typewrite("osaka high",0.25)
time.sleep(10)
pyautogui.press("down",presses=2)
pyautogui.press("enter")
