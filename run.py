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
    """
    Main title page and introduction
    """

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

    introduction = r"""
    Welcome to Oathbound,
    
    In this adventure, you will embark on a journey through a fantasy world filled with danger and mystery.
    You will choose a character class, each with its own unique strengths and weaknesses. 
    As you progress, you will encounter various challenges and make decisions that will shape your destiny.
    
    Are you ready to take the oath and begin your adventure?
    
    Press enter to proceed...
    """

    for char in introduction:
        print(char, end='', flush=True)
        time.sleep(0.02)

    input('')

def get_player_info():
    """
    Get player name and class
    """
    name = input("Enter your character's name:\n")

    class_lookup = {
        "1": "Warrior",
        "2": "Archer",
        "3": "Mage",
        "4": "Peasant",
        "warrior": "Warrior",
        "archer": "Archer",
        "mage": "Mage",
        "peasant": "Peasant"
    }
    
    print("Please pick a class from the following:\n")
    print("1 - Warrior")
    print("2 - Archer")
    print("3 - Mage")
    print("4 - Peasant (HARD)")

    player_class = input("\n").strip().lower()

    while player_class not in class_lookup:
        print("Invalid class selected. Please try again.\n")
        print("Please pick a class from the following:\n")
        print("1 - Warrior")
        print("2 - Archer")
        print("3 - Mage")
        print("4 - Peasant (HARD)")

        player_class = input("\n").strip().lower()

    class_name = class_lookup[player_class]

    # Retrieve player stats from the Google Sheet
    class_sheet = SHEET.worksheet('Classes')
    headers = class_sheet.row_values(1)
    stats = class_sheet.col_values(headers.index(class_name) + 1)

    player_stats = {
        "Health": stats[1],
        "Attack": stats[2],
        "Speed": stats[3]
    }

    # Display player info
    print(f"\nPlayer Name: {name}")
    print(f"Player Class: {class_name}")
    print("Player Stats:")
    for stat, value in player_stats.items():
        print(f"  {stat}: {value}")

    return {
        "name": name,
        "class": class_name,
        "stats": player_stats
    }

def start_game():
    

def main():
    """
    Run all functions
    """
    title_scroll()
    player_info = get_player_info()

main()


