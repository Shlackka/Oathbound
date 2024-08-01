# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import time
import gspread
import os
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


def clear_terminal():
    """
    Clear the terminal screen.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def scroll_text(text, delay=0.015):
    """
    Print text with a scrolling effect
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def scroll_text_slow(text, delay=0.05):
    """
    Print text with a scrolling effect slow
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def normalise_and_check_input(input_text, keywords):
    """
    Normalise the input text
    and check if it contains any of the specified keywords
    """
    normalised_input = input_text.strip().lower()
    for keyword in keywords:
        if keyword in normalised_input:
            return True
    return False


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
     "In this adventure, you will embark on a journey through a fantasy world"
     "\n"
     "filled with danger and mystery. You will choose a character class, each"
     "\n"
     "with its own unique strengths and weaknesses. As you progress, you will"
     "\n"
     "encounter various challenges and make decisions that will shape your\n"
     "destiny.\n\n"
     "Are you ready to take the oath and begin your adventure?\n\n"
     "Press enter to proceed...\n"
    )

    scroll_text(introduction)

    input('\n')


def opening_text():
    """
    Display the opening narrative before the player makes their first move.
    """
    opening_narrative = (
        "You awaken to the first light of dawn, your body still weary from\n"
        "restless dreams. The world outside your shelter is still and quiet,\n"
        "the perfect moment to gather your thoughts. You pack your belongings,"
        "\n"
        "ensuring you have everything you need for the journey ahead. Taking a"
        "\n"
        "deep breath, you step outside, feeling the cool morning air fill your"
        "\n"
        "lungs. With a sense of determination, you prepare to take your first"
        "\n"
        "step into the unknown...\n\n"
        "Press Enter to begin your adventure."
    )
    scroll_text_slow(opening_narrative, delay=0.03)
    input("\n")


def get_player_info():
    """
    Get player name and class
    """
    clear_terminal()
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

    scroll_text("Outfitting Character")

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
    turns_until_end = random.randint(10, 30)

    x = 0
    y = 0
    location = (x, y)

    return turns_until_end, location


def start_game():
    title_scroll()
    player_info = get_player_info()
    print("")
    scroll_text_slow("Planning how many days you'll be adventuring...\n")
    turns_until_end, location = initialise_game()
    scroll_text_slow("Packing all the required provisions...\n")
    inventory = initialise_inventory(player_info)
    scroll_text_slow("Surveying for potential dangers that lie ahead...\n")
    areas = get_areas()
    encounters = get_encounter()
    scroll_text_slow("Making preperations for combat...\n")
    enemies = get_enemies()
    npcs = get_npcs()
    scroll_text_slow("Settling down for the night before setting out...\n")
    drops = initialise_potential_drops()
    location_area_map = {}
    location_encounter_map = {}
    clear_terminal()
    opening_text()
    clear_terminal()
    game_loop(
        player_info,
        location,
        turns_until_end,
        inventory,
        areas,
        location_area_map,
        encounters,
        location_encounter_map,
        drops,
        enemies,
        npcs
    )


def game_loop(
        player_info,
        location,
        turns_until_end,
        inventory,
        areas,
        location_area_map,
        encounters,
        location_encounter_map,
        drops,
        enemies,
        npcs
):
    """
    Main game loop where the player will take actions
    """

    visited_locations = [(0, 0)]

    if location not in location_area_map:
        location_area_map[location] = get_random_area(areas)
    area = location_area_map[location]

    while turns_until_end > 0:
        # TESTING
        # scroll_text(visited_locations)
        # scroll_text(f"\nCurrent Location: {location} ({area})")
        # scroll_text(f"\nTurns Remaining: {turns_until_end}")
        # TESTING
        scroll_text("\n1. Move")
        scroll_text("2. View Inventory")
        scroll_text("3. View Stats")
        scroll_text("4. Quit Game")

        action = input("Choose an action: \n").strip()
        clear_terminal()

        if action == "1":
            new_location, new_area, moved = move(
                location, areas, location_area_map)
            if moved:
                location = new_location
                area = new_area
                turns_until_end -= 1
                if new_location not in visited_locations:
                    visited_locations.append(new_location)
                if new_location != (0, 0) and check_for_encounter() and new_location not in location_encounter_map:
                    encounter = get_random_encounter(encounters)
                    location_encounter_map[new_location] = encounter
                    handle_encounter(
                        encounter,
                        inventory,
                        drops,
                        enemies,
                        location_encounter_map,
                        new_location,
                        npcs
                    )
                elif new_location in location_encounter_map:
                    previous_encounter = location_encounter_map[new_location]
                    if previous_encounter == "Chest":
                        scroll_text(
                            f"You see an empty chest. "
                            "It seems someone has already looted it.")
                    elif previous_encounter["type"] == "Enemy":
                        enemy = previous_encounter["details"]
                        scroll_text(
                            "You see signs of a previous "
                            f"battle with a {enemy['Enemy']}.")
                        scroll_text(
                            "You continue on your way "
                            "as there is nothing else for you here.")
                    elif previous_encounter['type'] == "NPC":
                        npc = previous_encounter["details"]
                        scroll_text(
                            f"You see {npc['Name']} just up ahead "
                            "but as you wave 'Hello' to "
                            "them they turn and dissapear from sight.")
                        scroll_text(
                            "You continue on your way "
                            "ignoring their rudeness.")
                else:
                    scroll_text(
                        f"You find yourself at a "
                        f"{area} but there appears to be "
                        "nothing of interest here...")

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
    direction = input(
        "Will you go North, South, "
        "East, or West? \n").strip().lower()

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
    Retrieve the list of areas from the Google Sheet
    """
    area_sheet = SHEET.worksheet('Areas')
    areas = area_sheet.col_values(1)
    return areas


def get_random_area(areas):
    """
    Get a random area from the provided list of areas
    """
    return random.choice(areas)


def get_encounter():
    """
    Get list of encounters from Google Sheet
    """
    encounter_sheet = SHEET.worksheet('Encounters')
    encounters = encounter_sheet.col_values(1)
    return encounters


def get_random_encounter(encounters):
    """
    Get a random encounter from list of encounters
    """
    return random.choice(encounters)


def check_for_encounter():
    """
    Determine if an encounter should occur (65% chance)
    """
    return random.random() < 0.65


def handle_encounter(
    encounter,
    inventory,
    drops,
    enemies,
    location_encounter_map,
    location,
    npcs
        ):
    """
    Handle the encounter logic
    """
    if encounter == "Chest":
        print("")
        scroll_text(
            f"You come across a chest in front of "
            "you, \nthere is no lock on the chest "
            "and nobody around, what will you do?")
        scroll_text("\n1. Open the chest")
        scroll_text("2. Leave the chest alone")

        choice = input("")

        open_keywords = [
            "open",
            "open the chest",
            "open it", "open up", "look inside", "open chest", "1"]

        if normalise_and_check_input(choice, open_keywords):
            if random.random() < 0.1:  # 10% chance for the chest to be a mimic
                # Add logic to handle the fight with the mimic
                mimic = {
                    "Enemy": "Mimic",
                    "Health": 50,
                    "Attack": 12,
                    "Speed": 4}
                fight_enemy(mimic, drops, inventory)
            else:
                drop = get_random_drop(drops)
                scroll_text(
                    f"You open the chest and find: {drop['Item Name']}!")
                # Add logic to add the drop to inventory
                inventory[drop['Category'] + 's'].append(drop['Item Name'])
        else:
            scroll_text(
                "You leave the chest alone and continue on your journey.")
    elif encounter == "Enemy":
        enemy = get_random_enemy(enemies)
        fight_enemy(enemy, drops, inventory)
        location_encounter_map[location] = {"type": "Enemy", "details": enemy}
    elif encounter == "NPC":
        npc = get_random_npc(npcs)
        talk_to_npc(npc)
        location_encounter_map[location] = {"type": "NPC", "details": npc}


def fight_enemy(enemy, drops, inventory):
    """
    Handle the fight with enemy
    """
    print("")
    scroll_text(f"A {enemy['Enemy']} attacks you! Prepare for battle.")
    # Add detailed fight mechanics here
    # Assume enemy is defeated for now
    drop = get_random_drop(drops)
    scroll_text(
        f"You defeat the {enemy['Enemy']}, they drop "
        f"{drop['Item Name']}! "
        "You pick up the loot and continue on your journey.")
    inventory[drop['Category'] + 's'].append(drop['Item Name'])


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


def initialise_potential_drops():
    """
    Retrieve list of potential drops to use in game
    """
    drops_sheet = SHEET.worksheet('Drops')
    drops_data = drops_sheet.get_all_records()
    return drops_data


def get_random_drop(drops):
    """
    Get a random drop from the list of drops
    """
    return random.choice(drops)


def get_enemies():
    """
    Get list of enemies from worksheet
    """
    enemies_sheet = SHEET.worksheet('Enemies')
    enemies_data = enemies_sheet.get_all_records()
    return enemies_data


def get_random_enemy(enemies):
    """
    Get a random enemy from the list of enemies
    """
    return random.choice(enemies)


def get_npcs():
    """
    Get list of npcs from worksheet
    """
    npcs_sheet = SHEET.worksheet("NPCs")
    npcs_data = npcs_sheet.get_all_records()
    return npcs_data


def get_random_npc(npcs):
    """
    Get random NPC from list of NPCs
    """
    return random.choice(npcs)


def talk_to_npc(npc):
    """
    Handle the interaction with the NPC
    """
    print("")
    scroll_text_slow(
        f"You encounter {npc['Name']}, {npc['Description']}.")
    scroll_text_slow(
        f"{npc['Name']} says: {npc['Dialogue']}")

    has_more_to_say = True
    talked_more = False

    while True:
        if has_more_to_say:
            scroll_text("1. Talk more")
            scroll_text("2. Leave\n")

            choice = input("What will you do? \n").strip().lower()

            talk_keywords = ["talk", "talk more", "speak", "1"]
            leave_keywords = ["leave", "go", "bye", "2"]

            if normalise_and_check_input(choice, talk_keywords):
                scroll_text_slow(f"{npc['Name']} says: {npc['More Dialogue']}")
                has_more_to_say = False
                talked_more = True
            elif normalise_and_check_input(choice, leave_keywords):
                if talked_more:
                    print("")
                    scroll_text_slow(
                        f"{npc['Name']} has nothing "
                        "more to say, it would seem.")
                print("")
                scroll_text_slow(npc['Exit Reason'])
                print("")
                scroll_text_slow(npc['Exit Dialogue'])
                break
            else:
                scroll_text("Invalid choice. Please try again.")
        else:
            if talked_more:
                print("")
                scroll_text_slow(
                    f"{npc['Name']} has nothing more to say, it would seem.")
            print("")
            scroll_text_slow(npc['Exit Reason'])
            print("")
            scroll_text_slow(npc['Exit Dialogue'])
            break


def view_inventory(inventory):
    scroll_text("Your inventory contains:")
    for category, items in inventory.items():
        if category != "Currently Equipped":
            scroll_text(f"{category}: {', '.join(items)}")
        else:
            scroll_text("\nCurrently Equipped:")
            for equip_category, item in items.items():
                scroll_text(f"{equip_category}: {item if item else 'None'}")
    
    scroll_text("\n1. Equip Item")
    scroll_text("2. Unequip Item")
    scroll_text("3. Exit")

    choice = input("Choose an action: \n").strip().lower()

    if choice == "1":
        equip_item(inventory)
    elif choice == "2":
        unequip_item(inventory)
    else:
        scroll_text("Exiting inventory.")


def equip_item(inventory):
    scroll_text("\nChoose a category to equip from:")
    scroll_text("1. Weapons")
    scroll_text("2. Armours")
    scroll_text("3. Relics")

    category_choice = input("Choose a category: \n").strip().lower()

    if category_choice == "1":
        category = "Weapons"
        equip_slot = "Weapon"
    elif category_choice == "2":
        category = "Armours"
        equip_slot = "Armour"
    elif category_choice == "3":
        category = "Relics"
        equip_slot = "Relic"
    else:
        scroll_text("Invalid category.")
        return

    if inventory[category]:
        scroll_text(f"\n{category} available to equip:")
        for idx, item in enumerate(inventory[category], 1):
            scroll_text(f"{idx}. {item}")

        item_choice = int(input("Choose an item to equip: \n").strip()) - 1

        if 0 <= item_choice < len(inventory[category]):
            new_item = inventory[category][item_choice]
            currently_equipped_item = inventory["Currently Equipped"][equip_slot]

            if currently_equipped_item:
                inventory[category].append(currently_equipped_item)

            inventory["Currently Equipped"][equip_slot] = new_item
            inventory[category].pop(item_choice)
            scroll_text(f"{new_item} has been equipped as your {equip_slot}.")
        else:
            scroll_text("Invalid item choice.")
    else:
        scroll_text(f"No items available in {category} to equip.")

def unequip_item(inventory):
    scroll_text("\nChoose a category to unequip from:")
    scroll_text("1. Weapons")
    scroll_text("2. Armours")
    scroll_text("3. Relics")

    category_choice = input("Choose a category: \n").strip().lower()

    if category_choice == "1":
        equip_slot = "Weapon"
        category = "Weapons"
    elif category_choice == "2":
        equip_slot = "Armour"
        category = "Armours"
    elif category_choice == "3":
        equip_slot = "Relic"
        category = "Relics"
    else:
        scroll_text("Invalid category.")
        return

    if inventory["Currently Equipped"][equip_slot]:
        item_to_unequip = inventory["Currently Equipped"][equip_slot]
        inventory[category].append(item_to_unequip)
        inventory["Currently Equipped"][equip_slot] = None
        scroll_text(f"{item_to_unequip} has been unequipped.")
    else:
        scroll_text(f"No item equipped in {equip_slot} slot.")


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
