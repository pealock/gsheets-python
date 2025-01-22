import pyautogui
from get_data import get_number, wait, text_box, update_led_sign
from pysheets_logo import pysheets_logo

# Get current screen dimensions
screenWidth, screenHeight = pyautogui.size()

# Print pySheets logo
pysheets_logo()

# Sequence loop for fetching new data and updated LED control software
while True:
    # Call data fetch function
    data = get_number()
    text_box('New data has been fetched.')
    wait(1)
    text_box(f'Updated total is {data}')
    wait(1)
    text_box('Updating LED controller.')
    wait(3)

    # Call update function
    update_led_sign(data, 3)

    # Countdown timer
    wait(1)
    text_box('LED controller updated.')
    wait(1)
    text_box('New data will be fetched in 60 seconds.')
    wait(30)
    text_box('New data will be fetched in 30 seconds.')
    wait(20)
    text_box('New data will be fetched in 10 seconds.')
    wait(10)
    text_box('Fetching new data.')


