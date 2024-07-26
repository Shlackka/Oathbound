# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
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

def scroll_text(text, delay=0.015):
    """
    Print text with a scrolling effect.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
        time.sleep(0.01)

    introduction = (
        "Welcome to Oathbound,\n\n"
        "In this adventure, you will embark on a journey through a fantasy world\n"
        "filled with danger and mystery. You will choose a character class, each\n"
        "with its own unique strengths and weaknesses. As you progress, you will\n"
        "encounter various challenges and make decisions that will shape your\n"
        "destiny.\n\n"
        "Are you ready to take the oath and begin your adventure?\n\n"
        "Press enter to proceed...\n"
    )

    for char in introduction:
        print(char, end='', flush=True)
        time.sleep(0.02)

    input('\n')

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
    
    scroll_text("Please pick a class from the following:\n")
    scroll_text("1 - Warrior")
    scroll_text("2 - Archer")
    scroll_text("3 - Mage")
    scroll_text("4 - Peasant (HARD)")

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
        "Speed": stats[3],
        "Weapon": stats[4],
        "Armour": stats[5],
        "Relic": stats[6]
    }

    # Display player info
    scroll_text(f"\nPlayer Name: {name}")
    print("")
    scroll_text(f"Player Class: {class_name}")
    scroll_text("\nPlayer Stats and Equipment:")
    for stat, value in player_stats.items():
        scroll_text(f"{stat}: {value}")

    return {
        "name": name,
        "class": class_name,
        "stats": player_stats
    }

def initialise_game():
    turns_until_end = random.randint(5, 15)

    x = 0
    y = 0
    location = (x, y)

    return turns_until_end, location

def start_game():
    title_scroll()
    areas = get_areas()
    turns_until_end, location = initialise_game()
    player_info = get_player_info()
    inventory = initialise_inventory(player_info)
    location_area_map = {}
    game_loop(player_info, location, turns_until_end, inventory, areas, location_area_map)

def game_loop(player_info, location, turns_until_end, inventory, areas, location_area_map):
    """
    Main game loop where the player will take actions
    """

    visited_locations = [(0,0)]

    if location not in location_area_map:
        location_area_map[location] = get_random_area(areas)
    area = location_area_map[location]

    while turns_until_end > 0:
        # TESTING
        scroll_text(visited_locations)
        scroll_text(f"\nCurrent Location: {location} ({area})")
        scroll_text(f"\nTurns Remaining: {turns_until_end}")
        # TESTING
        scroll_text("\n1. Move")
        scroll_text("2. View Inventory")
        scroll_text("3. View Stats")
        scroll_text("4. Quit Game")

        action = input("Choose an action: \n").strip()

        if action == "1":
            new_location, new_area, moved = move(location, areas, location_area_map)
            if moved:
                location = new_location
                area = new_area
                turns_until_end -= 1
                if new_location not in visited_locations:
                    visited_locations.append(new_location)
        elif action == "2":
            view_inventory(inventory)
        elif action == "3":
            view_stats(player_info)
        elif action == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid action. Please try again.")

    return visited_locations
    
def move(location, areas, location_area_map):
    """
    Function to move the player in desired direction
    """
    x, y = location
    direction = input("Move North, South, East, or West: \n").strip().lower()

    if direction == "north":
        y += 1
    elif direction == "south":
        y -= 1
    elif direction == "east":
        x += 1
    elif direction == "west":
        x -= 1
    else:
        scroll_text("Invalid direction.")
        return location, None, False

    new_location = (x, y)

    if new_location not in location_area_map:
        location_area_map[new_location] = get_random_area(areas)

    return new_location, location_area_map[new_location], True

def get_areas():
    """
    Retrieve the list of areas from the Google Sheet.
    """
    area_sheet = SHEET.worksheet('Areas')
    areas = area_sheet.col_values(1)
    return areas

def get_random_area(areas):
    """
    Get a random area from the provided list of areas.
    """
    return random.choice(areas)

def initialise_inventory(player_info):
    """
    Initialise the players inventory
    """
    return {
        "Weapons": [],
        "Armours": [],
        "Relics": [],
        "Currently Equipped": {
            "Weapon": player_info["stats"]["Weapon"],
            "Armour": player_info["stats"]["Armour"],
            "Relic": player_info["stats"]["Relic"]
        }
    }

def view_inventory(inventory):
    scroll_text("Your inventory contains:")
    for category, items in inventory.items():
        if category != "Currently Equipped":
            scroll_text(f"{category}: {', '.join(items)}")
        else:
            scroll_text("\nCurrently Equipped:")
            for equip_category, item in items.items():
                scroll_text(f"{equip_category}: {item if item else 'None'}")

def view_stats(player_info):
    scroll_text(f"Player Name: {player_info['name']}")
    scroll_text(f"Player Class: {player_info['class']}")
    scroll_text("\nPlayer Stats:")
    for stat, value in player_info['stats'].items():
        scroll_text(f"{stat}: {value}")

def main():
    """
    Run all functions
    """
    start_game()

main()


