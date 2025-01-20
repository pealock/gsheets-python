import pyautogui
from get_data import get_data
import time

screenWidth, screenHeight = pyautogui.size()

def wait(seconds):
    time.sleep(seconds)

while True:
    data = get_data()
    print(data)
    wait(3)
    pyautogui.click(960,540)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(data)
    wait(1)
    pyautogui.click(1080,880)
    wait(1)
    pyautogui.click(960,580)
    wait(5)

