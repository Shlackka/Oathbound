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

- #### Game Zone

![Game Zone Wireframe](assets/images/readme/game-zone-wireframe.png)

## Features

Below I will go into a brief explanation of the features I have encorporated into the game.

### Existing Features

- __Landing Page (Desktop)__

    - Shown upon loading the site on desktop, an attractive image used to introduce the site with minimal wording. 
    - A central button offering an intriguing message of "Enter the Pantheon" inviting users to click and continue onto the main title screen.
    - The sliding effect of the main image on the desktop landing page offers a feeling of grandeur as the main title page is unveiled.

![Landing Page Desktop](assets/images/readme/landing-page-desktop.png)

- __Main Menu (Desktop)__

    - An intuitive and simple to use main menu with 2 buttons, "Start Game" and "How to Play".
    - Attractive imagery that supports getting the player into the right mindset for the game.

![Main Menu Desktop](assets/images/readme/main-menu-desktop.png)

- __Landing Page/Title Page (Mobile)__

    - The mobile landing page, although missing the sliding feature image of the desktop version still offers the same asthetic with a identical title page.
    - A simple to use title page main menu offering the options of "Start Game" and "How to Play" with an attractive hero image to give a distinct feel to the game.

![Landing Page/Title Page Mobile](assets/images/readme/landing-page-mobile.png)

- __Instructions__

    - When the "How to Play" button is clicked a message window will open to give all the relevant instrutions the player will need.
    - The instructions window includes it's own "Start Game" button to avoid needing to return to the main menu.

![Instructions](assets/images/readme/instructions.png)

- __Game Zone__

    - A stylised image of a god will appear central to the game zone.
    - A question will display below the god image "To which mythology does this god/goddess belong?".
    - The answer buttons are displayed clearly below the question each in the same style as the main site.
    - A hint button is displayed below the answer buttons, clearly stating the repercussion for using a hint.

![Game Zone](assets/images/readme/game-zone.png)

- __Score__

    - A score keeping area is displayed below the buttons.

![Score](assets/images/readme/score.png)

- __Alert Box (Answer)__

    - For each action the player performs a message box will appear central to the screen.
    - Uses an "x" in the top right corner as a close button.
    - Will give the player feedback on their chosen answer whether it was right or wrong.

![Alert Box Answer](assets/images/readme/alert-box-answer.png)

- __Alert Box (Hint)__

    - Will give the player a hint dependant on the current god/goddess displayed.
    - The hint can be displayed as many times as the player would like for each god/goddess.

![Alert Box Hint](assets/images/readme/alert-box-hint.png)

- __Alert Box (End Game)__

    - The message box will contain 2 buttons upon reaching an end game state "End Game" and "Play Again".
    - The "x" in the top right will not appear for this message so as not to present an unwanted loop in game.

![Alert Box End Game](assets/images/readme/alert-box-end.png)

### Features Not Yet Implemented

- __Difficulty__

    - If I was to continue adding features at this stage then next would be a difficulty selector  
    giving the player a limited amount of time or guesses to reach the required score to win.

- __More Pantheons__

    - Another feature I may implement is further Pantheons to guess from such as Roman or Hinduism.

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