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


# Utility functions
def clear_terminal():
    """
    Clear the terminal screen
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


def scroll_text_slow(text, delay=0.035):
    """
    Print text with a scrolling effect slow
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def normalise_and_check_input(input_text, keywords):
    """
    Normalise the input text and check if it contains any of the specified keywords
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
    Display the opening narrative before the player makes their first move
    """
    opening_narrative = (
        "\n"
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

    while True:
        name = input("\nEnter your character's name:\n").strip()
        if name:
            break
        else:
            scroll_text("Name cannot be empty. Please enter a valid name.")

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

    scroll_text("\nPlease pick a class from the following:\n")
    scroll_text("1 - Warrior")
    scroll_text("2 - Archer")
    scroll_text("3 - Mage")
    scroll_text("4 - Peasant (HARD)")

    player_class = input("\n").strip().lower()

    while player_class not in class_lookup:
        scroll_text("Invalid class selected. Please try again.\n")
        scroll_text("Please pick a class from the following:\n")
        scroll_text("1 - Warrior")
        scroll_text("2 - Archer")
        scroll_text("3 - Mage")
        scroll_text("4 - Peasant (HARD)")

        player_class = input("\n").strip().lower()

    class_name = class_lookup[player_class]

    # Retrieve player stats from the Google Sheet
    class_sheet = SHEET.worksheet('Classes')
    headers = class_sheet.row_values(1)
    stats = class_sheet.col_values(headers.index(class_name) + 1)

    base_stats = {
        "MaxHealth": int(stats[1]),
        "Health": int(stats[1]),
        "Attack": int(stats[2]),
        "Speed": int(stats[3])
    }

    current_stats = base_stats.copy()

    scroll_text("Outfitting Character")

    # Display player info
    scroll_text(f"\nPlayer Name: {name}")
    scroll_text(f"Player Class: {class_name}")
    scroll_text("\nPlayer Stats and Equipment:")
    for stat, value in base_stats.items():
        if stat != "MaxHealth":
            scroll_text(f"{stat}: {value}")

    return {
        "name": name,
        "class": class_name,
        "base_stats": base_stats,
        "current_stats": current_stats,
        "equipment": {
            "Weapon": stats[4],
            "Armour": stats[5],
            "Relic": stats[6]
        }
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
    Main game loop where the player will take actions.
    """

    visited_locations = [(0, 0)]
    encountered_npcs = set()

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
        scroll_text("4. View Map")
        scroll_text("5. Quit Game")

        action = input("Choose an action: \n").strip()
        clear_terminal()

        if action == "1":
            new_location, new_area, moved = move(
                location, areas, location_area_map, player_info)
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
                        player_info,
                        encounter,
                        inventory,
                        drops,
                        enemies,
                        location_encounter_map,
                        new_location,
                        npcs,
                        encountered_npcs
                    )
                elif new_location in location_encounter_map:
                    previous_encounter = location_encounter_map[new_location]
                    if previous_encounter == "Chest":
                        scroll_text(
                            f"You see an empty chest. "
                            "It seems someone has already looted it.")
                    elif isinstance(previous_encounter, dict) and previous_encounter["type"] == "Enemy":
                        enemy = previous_encounter["details"]
                        scroll_text(
                            "You see signs of a previous "
                            f"battle with a {enemy['Enemy']}.")
                        scroll_text(
                            "You continue on your way "
                            "as there is nothing else for you here.")
                    elif isinstance(previous_encounter, dict) and previous_encounter['type'] == "NPC":
                        npc = previous_encounter["details"]
                        scroll_text(
                            f"You see {npc['Name']} just up ahead "
                            "\nbut as you wave 'Hello' to "
                            "them they turn and disappear from sight.")
                        scroll_text(
                            "\nYou continue on your way "
                            "ignoring their rudeness.")
                    elif previous_encounter == "No Encounter":
                        scroll_text(
                            "You have been here before but there is still "
                            "nothing of interest here...")
                else:
                    scroll_text(
                        f"You find yourself at a {area} "
                        "\n but there appears to be "
                        "nothing of interest here...")
                    location_encounter_map[new_location] = "No Encounter"

        elif action == "2":
            view_inventory(inventory, player_info["current_stats"])
        elif action == "3":
            view_stats(player_info)
        elif action == "4":
            view_map(location, visited_locations, location_area_map, location_encounter_map)
        elif action == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid action. Please try again.")

    return visited_locations


def move(location, areas, location_area_map, player_info):
    """
    Function to move the player in desired direction
    """
    x, y = location
    direction = input(
        "Will you go North, South, "
        "East, or West? \n").strip().lower()

    if direction == "north":
        y += 1
        clear_terminal()
    elif direction == "south":
        y -= 1
        clear_terminal()
    elif direction == "east":
        x += 1
        clear_terminal()
    elif direction == "west":
        x -= 1
        clear_terminal()
    else:
        scroll_text("Invalid direction.")
        return location, None, False

    new_location = (x, y)

    if new_location not in location_area_map:
        location_area_map[new_location] = get_random_area(areas)

    # Heal the player by 10% of their max health each move
    heal_amount = int(player_info["current_stats"]["MaxHealth"] * 0.10)
    player_info["current_stats"]["Health"] = min(
        player_info["current_stats"]["MaxHealth"],
        player_info["current_stats"]["Health"] + heal_amount
    )

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
    player_info,
    encounter,
    inventory,
    drops,
    enemies,
    location_encounter_map,
    location,
    npcs,
    encountered_npcs
        ):
    """
    Handle the encounter logic
    """
    if encounter == "Chest":
        print("")
        scroll_text(
            f"You come across a chest in front of "
            "you, \nthere is no lock on the chest "
            "and nobody around, what will you do?\n")
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
                result = fight_enemy(player_info["current_stats"], mimic, drops, inventory)
                if result == "Victory":
                    drop = get_random_drop(drops)
                    scroll_text(f"The enemy dropped {drop['Item Name']}!"
                    "\n"
                    "You pick up the item and continue on your journey.")
                    inventory[drop['Category'] + 's'].append(drop['Item Name'])
                location_encounter_map[location] = {"type": "Enemy", "details": enemy}


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
        result = fight_enemy(player_info["current_stats"], enemy, drops, inventory)
        if result == "Victory":
            drop = get_random_drop(drops)
            scroll_text(f"The enemy dropped {drop['Item Name']}!"
            "\n"
            "You pick up the item and continue on your journey.")
            inventory[drop['Category'] + 's'].append(drop['Item Name'])
        location_encounter_map[location] = {"type": "Enemy", "details": enemy}
    elif encounter == "NPC":
        npc = get_unique_npc(npcs, encountered_npcs)
        if npc:
            talk_to_npc(npc)
            location_encounter_map[location] = {"type": "NPC", "details": npc}
            encountered_npcs.add(npc['Name'])
        else:
            scroll_text(
                "There appears to be nothing here, "
                "you carry on your way.")


def fight_enemy(player_stats, enemy, drops, inventory):
    """
    Handle the fight with enemy
    """
    print("")
    scroll_text(f"A {enemy['Enemy']} attacks you! Prepare for battle.")

    while player_stats["Health"] > 0 and enemy["Health"] > 0:
        # Display player and enemy stats
        scroll_text("\nPlayer Stats:\n")
        for stat, value in player_stats.items():
            if stat != "Effects" and stat != "MaxHealth":
                scroll_text(f"{stat}: {value}")

        scroll_text("\n")
        scroll_text(f"Enemy: {enemy['Enemy']}")
        scroll_text(f"Health: {enemy['Health']}")

        # Player action
        scroll_text("\n1. Attack")
        scroll_text("2. Flee")

        action = input("Choose your action: \n").strip()

        if action == "1":
            player_attack(player_stats, enemy)
        elif action == "2":
            if attmept_flee(player_stats, enemy):
                scroll_text("You successfully fled the battle!")
                return
            else:
                scroll_text("You failed to flee!")
        else:
            scroll_text("Invalid action. Please choose again.")

        if enemy["Health"] > 0:
            enemy_attack(player_stats, enemy)

        # Check for player defeat
        if player_stats["Health"] <= 0:
            scroll_text("You have been defeated!")
            if "ReviveWithHalfHealth" in player_stats["Effects"]:
                scroll_text("Your relic revives you with half health!")
                player_stats["Health"] = player_stats["MaxHealth"] // 2
                player_stats["Effects"].remove("ReviveWithHalfHealth")
            else:
                return "Defeat"

    scroll_text(f"You have defeated the {enemy['Enemy']}!"
    "\n")
    return "Victory"


def player_attack(player_stats, enemy):
    """
    Handle the player's attack on the enemy
    """
    damage = player_stats["Attack"]

    # Check for increased critical chance effect
    if "IncreasedCriticalChance" in player_stats["Effects"]:
        if random.random() < 0.25:  # Assuming a 25% critical hit chance
            damage *= 2
            scroll_text("Critical hit!")

    scroll_text(f"\nYou attack the {enemy['Enemy']} for {damage} damage."
    "\n")
    enemy["Health"] -= damage


def enemy_attack(player_stats, enemy):
    """
    Handle the enemy's attack on the player
    """
    damage = enemy["Attack"]
    scroll_text(f"\nThe {enemy['Enemy']} attacks you for {damage} damage.")
    player_stats["Health"] -= damage


def attempt_flee(player_stats, enemy):
    """
    Attempt to flee from the battle
    """
    player_speed = player_stats["Speed"]
    enemy_speed = enemy["Speed"]

    if player_speed > enemy_speed:
        return True
    else:
        return random.random() < 0.5


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
    for npc in npcs_data:
        npc['Description'] = npc['Description'].replace('\\n', '\n')
        npc['Dialogue'] = npc['Dialogue'].replace('\\n', '\n')
        npc['More Dialogue'] = npc['More Dialogue'].replace('\\n', '\n')
        npc['Exit Reason'] = npc['Exit Reason'].replace('\\n', '\n')
        npc['Exit Dialogue'] = npc['Exit Dialogue'].replace('\\n', '\n')
    return npcs_data


def get_unique_npc(npcs, encountered_npcs):
    """
    Get a unique NPC that has not been encountered yet
    """
    remaining_npcs = [npc for npc in npcs if npc['Name'] not in encountered_npcs]
    if remaining_npcs:
        return random.choice(remaining_npcs)
    else:
        return None


def talk_to_npc(npc):
    """
    Handle the interaction with the NPC
    """
    print("")
    scroll_text_slow(
        f"You encounter {npc['Name']}, {npc['Description']}.")
    scroll_text("\n")
    scroll_text_slow(
        f"{npc['Name']} says: {npc['Dialogue']}")

    has_more_to_say = True
    talked_more = False

    while True:
        if has_more_to_say:
            scroll_text("\n1. Talk more")
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


def view_map(current_location, visited_locations, location_area_map, location_encounter_map):
    """
    Display a dynamic map showing the player's current location and visited locations
    """

    scroll_text("Map Legend:")
    scroll_text("P: Player's current location")
    scroll_text("V: Visited location")
    scroll_text("C: Chest")
    scroll_text("E: Enemy encounter")
    scroll_text("N: NPC encounter")
    scroll_text("")

    map_radius = 5  # Adjust the radius of the visible map area
    map_size = map_radius * 2 + 1
    map_grid = [[' ' for _ in range(map_size)] for _ in range(map_size)]

    cx, cy = current_location

    def translate_coords_to_index(coords):
        x, y = coords
        return x - cx + map_radius, map_radius - (y - cy)

    def is_within_map(coords):
        x, y = translate_coords_to_index(coords)
        return 0 <= x < map_size and 0 <= y < map_size

    # Mark visited locations
    for loc in visited_locations:
        if is_within_map(loc):
            x_idx, y_idx = translate_coords_to_index(loc)
            map_grid[y_idx][x_idx] = 'V'

    # Mark encounters
    for loc, encounter in location_encounter_map.items():
        if is_within_map(loc):
            x_idx, y_idx = translate_coords_to_index(loc)
            if encounter == "Chest":
                map_grid[y_idx][x_idx] = 'C'
            elif isinstance(encounter, dict) and encounter["type"] == "Enemy":
                map_grid[y_idx][x_idx] = 'E'
            elif isinstance(encounter, dict) and encounter["type"] == "NPC":
                map_grid[y_idx][x_idx] = 'N'

    # Mark the player's current location
    px, py = translate_coords_to_index(current_location)
    map_grid[py][px] = 'P'

    # Display the map with borders
    print(' ' + '-' * map_size * 2)
    for row in map_grid:
        print('|' + ' '.join(row) + '|')
    print(' ' + '-' * map_size * 2)

    input("Press Enter to continue...")


def initialise_inventory(player_info):
    """
    Initialise the player's inventory.
    """
    # Retrieve all item stats from the Google Sheet
    drops_sheet = SHEET.worksheet('Drops')
    items_data = drops_sheet.get_all_records()

    # Create a dictionary to store item stats
    items_stats = {}
    for item in items_data:
        items_stats[item['Item Name'].strip()] = {
            "Health": int(item['Health']),
            "Attack": int(item['Attack']),
            "Speed": int(item['Speed']),
            "Effect": item['Effect'],
            "Description": item['Description']
        }

    inventory = {
        "Weapons": [],
        "Armours": [],
        "Relics": [],
        "Currently Equipped": {
            "Weapon": player_info["equipment"]["Weapon"],
            "Armour": player_info["equipment"]["Armour"],
            "Relic": player_info["equipment"]["Relic"]
        }
    }

    # Apply the stats of the default equipment to the player's stats
    for equip_slot, item_name in inventory["Currently Equipped"].items():
        if item_name:
            item_stats = items_stats.get(item_name)
            if item_stats:
                apply_item_stats(player_info["current_stats"], item_stats)
            else:
                print(f"Warning: {item_name} not found in item stats.")

    return inventory


def view_inventory(inventory, player_stats):
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
        equip_item(inventory, player_stats)
    elif choice == "2":
        unequip_item(inventory, player_stats)
    else:
        scroll_text("Exiting inventory.")


def equip_item(inventory, player_stats):
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
        while True:
            scroll_text(f"\n{category} available to equip:")
            for item in inventory[category]:
                scroll_text(item)

            scroll_text("\nOptions:")
            scroll_text("1. Equip an item")
            scroll_text("2. View item description")
            scroll_text("3. Exit")

            option = input("Choose an option: \n").strip().lower()

            if option == "1":
                scroll_text(f"\n{category} available to equip:")
                for idx, item in enumerate(inventory[category], 1):
                    scroll_text(f"{idx}. {item}")

                item_choice = input("Choose an item to equip (number): \n").strip()

                if item_choice.isdigit() and 1 <= int(item_choice) <= len(inventory[category]):
                    item_choice = int(item_choice) - 1
                    new_item = inventory[category][item_choice]
                    currently_equipped_item = inventory["Currently Equipped"][equip_slot]

                    if currently_equipped_item:
                        inventory[category].append(currently_equipped_item)
                        remove_item_stats(player_stats, get_item_stats(currently_equipped_item))

                    inventory["Currently Equipped"][equip_slot] = new_item
                    player_stats[equip_slot] = new_item  # Update player stats with the new item name
                    inventory[category].pop(item_choice)
                    apply_item_stats(player_stats, get_item_stats(new_item))
                    scroll_text(f"{new_item} has been equipped as your {equip_slot}.")
                    break
                else:
                    scroll_text("Invalid item choice.")
            elif option == "2":
                scroll_text(f"\n{category} available to equip:")
                for idx, item in enumerate(inventory[category], 1):
                    scroll_text(f"{idx}. {item}")

                item_choice = input("Choose an item to view description (number): \n").strip()

                if item_choice.isdigit() and 1 <= int(item_choice) <= len(inventory[category]):
                    item_choice = int(item_choice) - 1
                    item_name = inventory[category][item_choice]
                    item_stats = get_item_stats(item_name)
                    scroll_text(f"Description of {item_name}: {item_stats['Description']}")
                else:
                    scroll_text("Invalid item choice.")
            elif option == "3":
                scroll_text("Exiting equip menu.")
                break
            else:
                scroll_text("Invalid option. Please try again.")
    else:
        scroll_text(f"No items available in {category} to equip.")


def unequip_item(inventory, player_stats):
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
        player_stats[equip_slot] = "None"  # Update player stats with the unequipped state
        remove_item_stats(player_stats, get_item_stats(item_to_unequip))
        scroll_text(f"{item_to_unequip} has been unequipped.")
    else:
        scroll_text(f"No item equipped in {equip_slot} slot.")


def get_item_stats(item_name):
    """
    Retrieve the stats for a given item, including a description
    """
    drops_sheet = SHEET.worksheet('Drops')
    item_row = drops_sheet.find(item_name).row
    item_stats = drops_sheet.row_values(item_row)
    return {
        "Health": int(item_stats[2]),
        "Attack": int(item_stats[3]),
        "Speed": int(item_stats[4]),
        "Effect": item_stats[5],
        "Description": item_stats[6]
    }


def apply_item_stats(player_stats, item_stats):
    """
    Apply the stats of an item to the player's stats.
    """
    player_stats["MaxHealth"] += item_stats["Health"]
    player_stats["Health"] += item_stats["Health"]
    player_stats["Attack"] += item_stats["Attack"]
    player_stats["Speed"] += item_stats["Speed"]
    # Apply any additional effects based on the item's effect description
    if item_stats["Effect"]:
        if "Effects" not in player_stats:
            player_stats["Effects"] = []
        player_stats["Effects"].append(item_stats["Effect"])


def remove_item_stats(player_stats, item_stats):
    """
    Remove the stats of an item from the player's stats.
    """
    player_stats["MaxHealth"] -= item_stats["Health"]
    player_stats["Health"] -= item_stats["Health"]
    player_stats["Attack"] -= item_stats["Attack"]
    player_stats["Speed"] -= item_stats["Speed"]
    # Remove any additional effects based on the item's effect description
    if item_stats["Effect"] and "Effects" in player_stats:
        if item_stats["Effect"] in player_stats["Effects"]:
            player_stats["Effects"].remove(item_stats["Effect"])


def heal_player(player_info, percentage):
    """
    Heal the player by a certain percentage of their maximum health.
    """
    max_health = player_info["base_stats"]["MaxHealth"]
    healing_amount = int(max_health * (percentage / 100))
    new_health = player_info["current_stats"]["Health"] + healing_amount
    player_info["current_stats"]["Health"] = min(new_health, max_health)
    scroll_text(f"You heal for {healing_amount} health.")


def view_stats(player_info):
    scroll_text(f"Player Name: {player_info['name']}")
    scroll_text(f"Player Class: {player_info['class']}")
    scroll_text("\nPlayer Stats:")
    for stat, value in player_info['current_stats'].items():
        if stat != "Effects" and stat != "MaxHealth":
            scroll_text(f"{stat}: {value}")


def main():
    """
    Run all functions
    """
    start_game()


main()
