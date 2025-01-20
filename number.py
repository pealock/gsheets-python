import pyautogui
from get_data import get_number
import time

screenWidth, screenHeight = pyautogui.size()

def wait(seconds):
    time.sleep(seconds)

while True:
    data = get_number()
    print(data)
    wait(3)
    pyautogui.click(960,540)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(data)
    wait(3)
    pyautogui.click(1080,880)
    wait(3)
    pyautogui.click(960,580)
    wait(60)

