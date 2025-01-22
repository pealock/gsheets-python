import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui

# Define the scope for authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('../.creds/sheets-python-447900-cff818541424.json', scope)

# Authenticate the gspread client
client = gspread.authorize(credentials)

# Open the Google Sheet by its name or URL
sheet = client.open('python-sheets').sheet1

#while True:
    # Get all values from the sheet
    #data = sheet.acell('F1').numeric_value
    # Print the data
    #print(data)
    # Sleep
    #time.sleep(10)

def get_name():
    data = sheet.col_values(8)
    return data

def get_number():
    data = sheet.acell('F1').value
    return data

def wait(seconds):
    time.sleep(seconds)

def text_box(text):
    print('')
    print(text)
    print('')

def update_led_sign(input):
    # Select main text/ number input box
    pyautogui.click(960, 540)

    # Select all text
    pyautogui.hotkey("ctrl", "a")

    # Replace previous text with new data
    pyautogui.write(input)
    wait(3)

    # Select 'Send' button
    pyautogui.click(1080, 880)
    wait(3)

    # Confirm prompt
    pyautogui.click(960, 580)
    wait(1)