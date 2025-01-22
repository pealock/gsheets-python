import pyfiglet
import time
from colorama import Fore, Back, Style

def pysheets_logo():
    pysheets = pyfiglet.figlet_format('pySheets', font='slant')
    print('')
    print(Fore.GREEN + pysheets)
    print(Style.RESET_ALL + 'v0.01 by AMP Studios')
    print('')
    time.sleep(3)