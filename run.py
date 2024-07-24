# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Oathbound')

# Test for title
def title_scroll():

    title = r"""
      ____          _    _      _                               _ 
     / __ \        | |  | |    | |                             | |
    | |  | |  __ _ | |_ | |__  | |__    ___   _   _  _ __    __| |
    | |  | | / _` || __|| '_ \ | '_ \  / _ \ | | | || '_ \  / _` |
    | |__| || (_| || |_ | | | || |_) || (_) || |_| || | | || (_| |
     \____/  \__,_| \__||_| |_||_.__/  \___/  \__,_||_| |_| \__,_|
                                                                """
                                                                
    title_lines = title.split('\n')

    for line in title_lines:
        print(line)
        time.sleep(0.4)


def main():
    """
    Run all functions
    """
    title_scroll()

main()


