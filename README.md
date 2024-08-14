# Oathbound

A link to the deployed app is **[here](https://oathbound-53135a23d9e9.herokuapp.com/)**.

Oathbound is a straightforward text-based adventure game that immerses players in a fantasy world where they take on the role of a chosen character class. Players will navigate different environments, face various enemies, and make choices that affect their journey. While the game offers strategic elements like resource management and combat, it’s designed to be accessible and engaging without being overly complex. Oathbound provides a simple yet immersive experience, suitable for players who enjoy a blend of exploration and decision-making in a classic fantasy setting.

## Deployed App

  - This image shows the initial page the player sees

![Deployed App](assets/images/readme/deployed-app.png)

**Table of contents:**

- [Title](#guess-the-god)
- [User Experience](#user-experience-ux)
  - [Expectation](#expectation)
  - [User Journey](#user-journey)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Languages Used](#languages-used)
  - [Flowcharts](#flowcharts)
- [Features](#features)
  - [Languages Used](#languages-used)
  - [Existing Features](#existing-features)
  - [Features Not Yet Implemented](#features-not-yet-implemented)
- [Testing](#testing)
  - [Testing Table](#testing-table)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Tools and Libraries](#tools-and-libraries)
  - [Acknowledgements](#acknowledgements)

## User Experience (UX)

  - ### Expectation
    - **Clear Instructions**: Users expect straightforward and detailed instructions on how to navigate and engage with the game’s various features.

    - **Simple Navigation**: Navigation of the game is simple and intuitive.

    - **Feedback**: Users anticipate immediate and meaningful feedback on their actions during gameplay, helping them understand the impact of their choices and strategies.

    - **Immersive Experience**: The game is designed to immerse players in a richly detailed fantasy world, with an emphasis on exploration, decision-making, and combat.

  - ### User Journey
    - **Title Screen**: Upon starting the game, users are introduced to the game’s world with a compelling title screen and an introductory narrative, setting the stage for the adventure ahead.

    - **Character Creation**: Users select their character’s name and class, with clear options to help them make a choice.

    - **Game Setup**: The game automatically generates the number of turns and starting location, creating a sense of unpredictability and excitement for the journey ahead.

    - **Main Gameplay Loop**: Players navigate through the world, encountering various challenges, enemies, and NPCs.  
    They are presented with options to move, view inventory, check stats, view the map, or quit the game.  
    The exploration is dynamic, with each move revealing new areas, encounters, and opportunities for strategic decisions.

    - **Combat and Encounters**: During encounters, users engage in combat with enemies or interact with NPCs.  
    The game provides clear choices and immediate feedback on the outcome of each action, whether it be battling a foe or discovering a hidden item.

    - **Boss Battle**: As the game progresses, users will face a final boss encounter, with the stakes clearly outlined.  
    The battle is a culmination of the player’s journey, testing their accumulated skills and resources.

    - **Completion**: Upon defeating the final boss or meeting an untimely end, users are presented with a concluding narrative and the option to restart the game or exit.

    - **Restart Option**: After the game concludes, users are given a clear option to restart their adventure or exit, ensuring a satisfying end to their experience.

## Design

  - ### Colour Scheme
    - The game is played entirely within a terminal so the colour scheme is simply the white text on a black background.

  - ### Typography
    - The game utilises the default monospace font typically associated with terminal environments.  
    
    - This font ensures that the text is easily readable and aligns with the retro, immersive aesthetic commonly associated with text-based adventure games.

  - ### Languages Used
    - **Python**: The game is built entirely in Python, a powerful programming language well-suited for developing interactive text-based games.  
      - Python's simplicity and readability make it an excellent choice for both game logic and narrative flow.
    
    - **Google Sheets API**: Google Sheets is used as a database to store and retrieve game data, such as character stats, enemies, items, and more. 
      - The Google Sheets API allows for dynamic interaction with this data, making the game adaptable and expandable.
    
    - **Markdown**: Used to write the README.

  - ### Flowcharts 

Please see below the flowcharts for the game, made using **[Miro](https://miro.com/)**.

- #### Original Flowchart (Simple)

![Simple Flowchart](assets/images/readme/flowchart.png)

- #### Final Flowchart (Full)

The full flowchart can be found **[Here.](https://miro.com/app/board/uXjVKq_bneI=/?share_link_id=965597782529)**

## Features

Below I will go into a brief explanation of the features I have encorporated into the game.

### Existing Features

- __Game Setup Features__

    - Title Screen:
      - The game starts with a title screen that displays the game's name in a stylized ASCII format, setting the mood for the adventure.
    
    - Character Creation: 
      - Player are prompted to enter their character's name.
      - Players choose a class from options (e.g. Warrior, Archer, Mage, Peasant), each with its own unique stats and starting equipment.

    - Initialisation:
      - The game randomly determines the number of turns until the final boss encounter.
      - The player's inventory is intialised with basic equipment based on the chosen class.

- __Gameplay Features__

    - Game Loop:
      - The core loop of the game where the player makes decisions each turn until the final encounter.
      - Actions Menu: 
        - Move: Players can move their character in one of four directions (North, South, East, West).
        - View Inventory: Players can view and manage their inventory.
        - View Stats: Players can check their current stats and equipment.
        - View Map: Players can view the map of visited locations and encounters.
        - Quit Game: Players can exit the game at any point.
    
    - Exploration:
      - As the player moves around, the game generates random areas (e.g. forests, lakes, mountains).
      - The player can revisit areas, and previously encountered locations are stored.
    
    - Encounters:
      - Random Encounters: As the player explores, they  have a chance of encountering chests, enemies, or NPCs.
      - Chests: Players can choose to open them, which might result in finding items or triggering a mimic battle.
      - Enemies: Players engage in turn-based combat with various enemies.
      - NPCs: Players can interact with NPCs to receive hints, lore and items.

    - Combat System:
      - Turn-Based Combat: Players choose to attack or flee. Players and enemies take turns based on their speed stat.
      - Player Attack: Players attack enemies, with a chance of critical hit if applicable.
      - Enemy Attack: Enemies retaliate, dealing damage to the player.
      - Fleeing: PLayers can attempt to flee from the battle, though it may not always succeed.
      - Defeat and Revival: If the player is defeated but has a revival item, they are revived with partial health. Otherwise, the game ends.

- __Final Encounter Features__

  - Boss Encounter:
    - Upon reaching the final turn, the player encounters a randomly selected boss.
    - Boss Battle: The boss battle operates similarly to regular combat but with stronger enemies and no possibility to flee successfully.
    - Victoy: Upon defeating the boss, the player is presented with a victory screen and congratulatory message.
    - Defeat: If the player is defeated, they are given the option to restart the game.

- __Inventory Management Features__

  - Inventory System:
    - Players can view their collected items, including weapons, armour and reclics.
    - Equip Items: Players cna equip new items from their inventory, which will modify their stats.
    - Unequip Items: Players can remove currently equipped items and store them back in their inventory.
    - Item Stats: Each item in the inventory effects the player's stats, such as health, attack and speed.

- __Map and Navigation Features__

  - Dynamic Map:
    - The game features a dynamic map that updates based on the player's exploration.
    - Map Symbols: Symbols represent different locations: 'P' for player, 'V' for visited locations, 'C' for chests, 'E' for enemies and 'N' for NPCs.
    - Map Legend: A legend explains the symbols used on the map as above.

- __User Interface and Feedback Features__

  - Scrolling Text:
    - Important messages and narrative text are displayed with a scrolling effect, enhancing immersion.
  - Immediate Feedback:
    - Players receive immediate feedback on their actions, such as the outcome of battles, successful escapes, or loot from chests.
  - Restart Option:
    - Upon game over, players are given the option to restart the game or exit.

- __Miscellaneous Features__

  - Healing Mechanism:
    - The player heals 10% of their maximum health each time they move to a new location.
  - Item Drops:
    - Enemies and chests can drop items that are added to the player's inventory.
  - Character Stats:
    - Players can view detailed stats that update as they progress and acquire new items.
  - Event Logging:
    - Key events in the game, such as battles and encounters, are logged and influence subsequent gameplay.

- __Customisation and Randomisation Features__

  - Randomised Boss Encounters:
    - The final boss is selected randomly from a list of potential bosses, adding replayability.
  - Random Areas and Encounters:
    - Each playthrough offers a unique experience due to the random generation of areas and encounters.

- __Endgame and Replayability Features__

  - Endgame Options:
    - After defeating the boss or dying, the player can choose to restart the game or quit.
  - Replayability:
    - With randomised encounters, bosses, and loot, each playthrough offers a different experience.

### Features Not Yet Implemented

- __Visuals__

  - My intention was to implement ASCII art to improve the storytelling aspect of the game but due to time constraints and complexity of other features this was sidelined.

- __Comprehensive Combat__

  - The combat aspect was planned to be expanded upon to include an order of battle which would have taken advantage of the already implemented speed attribute.

- __Consumable Items__

  - I had intended to include consumable items such as health potions and enhancement items but I ended up using the heal per move feature that is in the finished game.

- __Expanded NPC Interactions__

  - Inclusion of NPC specific interactions such as unique combat encounters were planned to be included but again had to be dropped due to time constraints.

## Testing

### Testing Table

| **Feature**            | **Test Description**                                                   | **Pass/Fail** | **Comments**                                |
|------------------------|------------------------------------------------------------------------|---------------|---------------------------------------------|
| Character Creation     | Tested the character creation process, ensuring the user can choose a class and the correct stats are assigned. | Pass          | All classes were selectable, and stats were correctly applied. |
| Movement System        | Verified that the player can move in all four directions and that the map updates correctly. | Pass          | Movement worked as expected, and the map updated correctly. |
| Encounter System       | Ensured that encounters trigger correctly and that the correct encounter (enemy, chest, or NPC) appears. | Pass          | All encounters triggered appropriately based on the conditions. |
| Combat System          | Tested combat mechanics, including attacking, taking damage, and defeating enemies. | Pass          | Combat worked as expected, with correct health deductions and enemy defeat. |
| Inventory Management   | Verified that the player can view, equip, and unequip items from the inventory. | Pass          | Inventory management functioned correctly, with items equipping/unequipping as expected. |
| Boss Encounter         | Ensured the final boss fight triggers correctly, and tested the combat mechanics specific to the boss. | Pass          | The boss encounter triggered correctly, and combat mechanics worked as expected. |
| Chest Encounter        | Tested to check that the interaction with the chest encounter worked correctly, both opening the chest, leaving the chest and also the mimic fight interaction. | Pass          | The chest encounter worked each time without any issues. |  
| Game Over Sequence     | Tested the game-over sequence, ensuring that the player is prompted to restart or quit the game. | Pass          | The game-over sequence worked as expected, with correct options for restarting or quitting. |
| Map Display            | Verified that the dynamic map displays correctly, showing visited locations and the player’s current position. | Pass          | The map displayed correctly, with accurate representation of the player’s location and visited areas. |
| Healing Mechanics      | Tested the healing system, ensuring that health regenerates appropriately after each move. | Pass          | Healing worked as intended, with health regenerating correctly. |
| NPC Interaction        | Verified that interactions with NPCs trigger dialogue and continue the game loop correctly. | Pass          | NPCs interacted correctly, with appropriate dialogue and effects. |
| Random Events          | Tested the randomness of encounters and item drops to ensure variability in gameplay. | Pass          | Random events occurred as expected, providing varied gameplay experiences. |
| Equipment Effects      | Verified that equipping different items changes the player's stats and abilities as intended. | Pass          | Equipment effects applied correctly, with stats adjusting based on the items equipped. |
| Turn Counter           | Tested the turn counter to ensure the game tracks and limits the number of turns correctly before triggering the boss fight. | Pass          | Turn counter functioned correctly, triggering the boss fight at the appropriate time. |
| Flee Mechanism         | Verified that the flee option works correctly in normal combat but is disabled or fails during the boss fight. | Pass          | Flee mechanics worked as expected, with fleeing possible in normal encounters but not during the boss fight. |
| Text and Dialogue Display | Ensured that all text and dialogue throughout the game displays correctly and at the appropriate speed. | Pass          | Text and dialogue displayed as intended, with correct timing and no overflow issues. |


### Validator Testing

- __Python__
    - No errors were returned when passing through the [CI Python Linter](https://pep8ci.herokuapp.com/#)
    ![Python Validator](assets/images/readme/python-validator.png)

### Unfixed Bugs

To the best of my knowledge after testing all aspects of the game I have been unable to find any unfixed bugs.

## Deployment

### **Deployment to Heroku**

The "Oathbound" game was deployed to Heroku by following these steps:

1. **Log In or Sign Up:** First, log in to your Heroku account. If you don’t have one, you’ll need to sign up.

2. **Access the Dashboard:** Click on the dashboard option from the menu in the top-right corner to navigate to the apps page.

3. **Create a New App:**
   - Click on the “New” button located in the top-right corner of the page.
   - Choose the “Create new app” option from the dropdown menu.

4. **Name Your App:**
   - Enter a unique name for your app (e.g., “oathbound-game”).
   - After selecting a name, choose your preferred region.

5. **Create the App:**
   - Click on the "Create App" button to proceed to the app’s dashboard.

6. **Configure Environment Variables:**
   - Navigate to the "Settings" tab.
   - Scroll down to the "Config Vars" section.
   - Click on "Reveal Config Vars" and add a key-value pair:
     - Key: `PORT`
     - Value: `8000`
   - Click the "Add" button to save the configuration.

7. **Add Buildpacks:**
   - Still in the "Settings" tab, scroll to the "Buildpacks" section.
   - Click on "Add buildpack," select Python, and save the changes.
   - Repeat the process to add Node.js as the second buildpack.
   - Ensure that Python is listed first, followed by Node.js.

8. **Connect to GitHub:**
   - Navigate to the "Deploy" tab.
   - In the "Deployment method" section, select GitHub.
   - Confirm your connection to GitHub and search for the repository containing the "Oathbound" project.
   - Click the "Connect" button next to the correct repository.

9. **Deploy the App:**
   - In the "Manual deploy" section, select the branch you wish to deploy from the dropdown menu.
   - Click the "Deploy Branch" button to initiate the deployment.
   - Alternatively, you can enable "Automatic Deploys" to automatically deploy any updates pushed to the connected GitHub branch.

If you wish to fork the repo this can be achieved by using the "Fork" button at the top of the repo and following the onscreen prompts to set up the forked repo as you wish.

If you wish to clone the repo this can be achieved by using the drop down on the green "code" button and copying the URL into a workspace of your choosing such as **[Gitpod](https://www.gitpod.io/)** or **[CodeAnywhere](https://codeanywhere.com/)**.

## Credits 

In the below section I will go over all of the external sources where I either drew inspiration or used their tools to assist in the development of Guess the God.

### Content

- All text included within Guess the God has been typed out by myself with hint and god facts first being found with the use of **[ChatGPT](https://chatgpt.com/?oai-dm=1)** before being reworded into the game.

- **[ChatGPT](https://chatgpt.com/?oai-dm=1)** has been used to help explain certain JavaScript concepts I was struggling with, specifically when I changed the nested if statements into a switch case and exporting and importing the god data from the data file.

- All inspiration for this project was taken from my personal interest into ancient civilizations and their respective mythologies and religions.

- Fonts for the site were found using **[Google Fonts](https://fonts.google.com/)**.

### Media

- All images including those used as backgrounds have been created using the DALL-E AI image creator through **[ChatGPT](https://chatgpt.com/?oai-dm=1)** by OpenAI.

- Favicon was created using **[Red Ketchup](https://redketchup.io/favicon-generator)**.
 
### Tools and Libraries

- **[Gitpod](https://www.gitpod.io/)** was used as the development environment.

- **[Visual Studio Code](https://code.visualstudio.com/)** was the code editor used for writing and editing the project's code within Gitpod.

- **[GitHub](https://github.com/)** was used for version control and hosting the project repository.

### Acknowledgements

- I would like to thank my family, specifically my sister Robyn for helping to playtest Guess the God  
and highlight any areas of gameplay I may have overlooked during development.

- I would also like to thank my Mentor Harry Dhillon who has been an invaluable source of encouragement.  
Always helping to guide me in the right direction during development.