import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope for authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('./.creds/sheets-python-447900-cff818541424.json', scope)

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


def get_data():
    data = sheet.acell('F1').numeric_value
    return data
