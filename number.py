import pyautogui
from get_data import get_number
import time
from pysheets_logo import pysheets_logo
screenWidth, screenHeight = pyautogui.size()

# Define timeout
def wait(seconds):
    time.sleep(seconds)

# Print pySheets logo
pysheets_logo()

# Sequence loop for fetching new data and updated LED control software
while True:
    # Call data fetch function
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
    # Select main text/ number input box
    pyautogui.click(960,540)
    # Select all text
    pyautogui.hotkey("ctrl", "a")
    # Replace previous text with new data
    pyautogui.write(data)
    wait(3)
    # Select 'Send' button
    pyautogui.click(1080,880)
    wait(3)
    # Confirm prompt
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


