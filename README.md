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
    - The game utilizes the default monospace font typically associated with terminal environments.  
    
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

![Full Flowchart](assets/images/readme/main-menu-mobile-wireframe.png)

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

Each feature of the game has been tested upon integration and also tested again upon completion of development, these tests will be outlined below.

- **Sliding Images**: The sliding images on the landing page were tested to ensure they animate correctly  
and reveal the main menu upon clicking the "Enter The Pantheon" button. The transition and timing were checked for smoothness and alignment.

- **Navigation Buttons**: All buttons present within the site have been tested to confirm they perform the correct actions:
    - The "Start Game" button begins the game.

    - The "How to Play" button displays the instructions.

    - The "Play Again" and "End Game" buttons appear at the end of the game, and they respectively restart the game or return the user to the main menu.

- **Answer Buttons**:  Each answer button was tested to ensure it registers the correct mythology when clicked. The correct feedback message is displayed based on the user's choice.
 
- **Hint Button**:  The hint button was tested to ensure it displays the correct hint and deducts points only the first time it is used for each god.  
The score is adjusted accordingly, and hintsUsed array functions properly to prevent repeated point deduction for the same hint.

- **Score Calculation**:  The scoring system was tested to ensure points are correctly awarded for correct answers and deducted for hints.  
The score properly resets when the game is restarted.

- **Alert Box**:  The custom alert box was tested to ensure it displays the correct messages for user feedback, and the close button functions as expected.  
Additionally, the answer buttons are temporarily disabled when the alert box is shown and re-enabled upon closing.

- **Responsive Design**: The layout and functionality was tested across different screen sizes and devices to ensure the game maintains its structural integrity and usability.

- **Accessibility**: All images were tested for appropriate alt text to ensure accessibility. Colour contrast was checked to meet accessibility guidelines.

### Lighthouse Testing

Along with feature testing I have also run lighthouse tests, these have come back very positive as seen below with the screen captures.

- #### Lighthouse report for desktop

![Lighthouse Report Desktop](assets/images/readme/lighthouse-report-desktop.png)

- #### Lighthouse report for mobile

![Lighthouse Report Mobile](assets/images/readme/lighthouse-report-mobile.png)

### Validator Testing

- __HTML__
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fshlackka.github.io%2Fguess-the-god%2F)
- __CSS__
    - No errors were returned when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fshlackka.github.io%2Fguess-the-god%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- __JavaScript__
    - No errors were returned when passing through **[JSHint](https://jshint.com/)** as shown in the images below.

    ![script.js Testing](assets/images/readme/script-testing.png)
    ![data.js Testing](assets/images/readme/data-testing.png)

### Unfixed Bugs

To the best of my knowledge after testing all aspects of the site I have been unable to find any unfixed bugs.

## Deployment

The site has been deployed to GitHub pages, in order to do this the following steps were completed.

- From within the guess-the-god repo I navigated to the settings tab

- In settings navigate to the Pages section under "Code and automation"

- Once in Pages, I chose to deploy from a branch as the source and then chose the Main branch before clicking save

- The deployed site can be found at **https://shlackka.github.io/guess-the-god/**

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