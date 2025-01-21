import pyautogui
from get_data import get_number
import time
import pyfiglet
screenWidth, screenHeight = pyautogui.size()

def wait(seconds):
    time.sleep(seconds)

pysheetsLogo = pyfiglet.figlet_format('pySheets', font='slant')

print('')
print(pysheetsLogo)
print('')
wait(5)

while True:
    data = get_number()
    print('')
    print('New data has been fetched.')
    print('')
    wait(1)
    print('')
    print(f'Updated total is {data}')
    print('')
    wait(1)
    print('')
    print('Updating LED controller...')
    print('')
    wait(3)
    pyautogui.click(960,540)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(data)
    wait(3)
    pyautogui.click(1080,880)
    wait(3)
    pyautogui.click(960,580)
    wait(1)
    print('')
    print('LED controller updated.')
    print('')
    wait(1)
    print('')
    print('New data will be fetched in 60 seconds.')
    print('')
    wait(30)
    print('')
    print('New data will be fetched in 30 seconds.')
    print('')
    wait(20)
    print('')
    print('New data will be fetched in 10 seconds.')
    print('')
    wait(10)
    print('')
    print('Fetching new data.')
    print('')


